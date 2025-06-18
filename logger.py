# logger.py
import logging

# Configure logger
logging.basicConfig(
    filename='calculator.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger()
