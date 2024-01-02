from build import marks
from log import logging
def append_to_file(file_path, data):
    logging.info("DataHandling to the File")
    try:
        with open(file_path, 'a') as file:
            logging.info("File Created")
            file.write(data + '\n')
            logging.info("Data Append to the file")
        print(f"Data appended to {file_path} successfully.")
    except Exception as e:
        print(f"Error appending data to {file_path}: {e}")
        logging.info('FileHandling Process Completed')
