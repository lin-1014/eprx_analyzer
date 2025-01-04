import os
import logging

def setup_logging(log_dir="logs", log_file="app.log", log_level=logging.INFO):
    """
    global logging。
    
    Parameters:
    - log_dir (str): 日誌目錄。
    - log_file (str): 日誌文件名稱。
    - log_level (int): 日誌等級，例如 logging.INFO。
    """
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # set file_path
    log_file_path = os.path.join(log_dir, log_file)

    # set logging
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file_path, mode='a', encoding='utf-8'),  # into file
            # logging.StreamHandler()  # terminal
        ]
    )

    logging.info("Logging is set up. Logs will be written to: %s", log_file_path)
