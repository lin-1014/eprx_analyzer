from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pandas import to_numeric
from .data_processing import load_eprx_data, filter_eprx_dataframe, extract_date_block_info
from .analysis_tool import analyze_and_visualize_heatmap

app = FastAPI()

origins = [
    "http://localhost:4200",
    # 若有其他本地測試網址，或之後的正式網域，也可以加進來
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],    # GET, POST, PUT, DELETE, OPTIONS...
    allow_headers=["*"],    # Authorization, Content-Type...
)

@app.get("/heatmap/")
def get_heatmap(target_tso: str = Query(...), price_threshold: float = Query(...), target_reserve_type: str = Query(...)):
    """
    get the data for heatmap.

    Args:
        target_tso (str, optional): _description_. Defaults to Query(...).
        price_threshold (float, optional): _description_. Defaults to Query(...).

    Returns:
        JSONResponse: data for heatmap
    """
    permit_reserve_type = ['1-0', '2-1', '2-2', '3-1', '3-2']
    if target_reserve_type not in permit_reserve_type:
        return JSONResponse({"error": "Invalid reserve type."}, status_code=400)

    df = load_eprx_data(reservetype=target_reserve_type, year='2024')
    wanted_columns = ['TT', '調達区分', '取引情報']
    wanted_columns.append(target_tso)

    filter_conditions = {
        '調達区分': 'システム約定結果',
        '取引情報': '最高落札価格（TSO別）[円/kW・30分]'
    }
    filtered_df = filter_eprx_dataframe(df, wanted_columns, filter_conditions)
    filtered_df = extract_date_block_info(filtered_df)

    filtered_df[target_tso] = to_numeric(filtered_df[target_tso], errors='coerce')

    count_series = analyze_and_visualize_heatmap(
        df=filtered_df,
        value_column=target_tso,
        filter_value=price_threshold,
        group_columns=['Block', 'Weekday'],
        return_data=True
    )
    return JSONResponse(count_series)  # 轉成 list

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
