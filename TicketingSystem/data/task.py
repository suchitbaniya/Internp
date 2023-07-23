from .services import fetch_data_from_api,check_data

from celery import shared_task


import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a file handler for logging
file_handler = logging.FileHandler('api_task.log')
file_handler.setLevel(logging.INFO)

# Create a formatter and add it to the file handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)

@shared_task
def call_api():
    fetch_data_from_api()
    check_data()
    
    logger.info("API call complete")

    print("Calling API...")


