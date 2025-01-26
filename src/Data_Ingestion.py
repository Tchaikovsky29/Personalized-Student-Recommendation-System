import requests
import json
from log import logger
import warnings
import os

warnings.filterwarnings("ignore")

#create logger
logger = logger("Data_Ingestion")

#create data directory
os.makedirs("./data/raw", exist_ok=True)

#save quiz data
url = "https://jsonkeeper.com/b/LLQT"

try:
    response = requests.get(url, verify=False)
    response.raise_for_status()
    data = response.json()

    logger.debug("Obtained quiz data")

    output_file = "./data/raw/quiz_data.json"
    with open(output_file, "w") as file:
        json.dump(data, file, indent=4)
    
    logger.debug(f"Data written to {output_file}")

except requests.exceptions.RequestException as e:
    logger.error(f"Error fetching data: {e}")

#save submission data
url = "https://api.jsonserve.com/rJvd7g"

try:
    response = requests.get(url, verify=False)
    response.raise_for_status()
    data = response.json()
    
    logger.debug("Obtained submission data")

    output_file = "./data/raw/quiz_submission_data.json"
    with open(output_file, "w") as file:
        json.dump(data, file, indent=4)
    
    logger.debug(f"Data written to {output_file}")
except requests.exceptions.RequestException as e:
    logger.error(f"Error fetching data: {e}")

#save historical data
url = "https://api.jsonserve.com/XgAgFJ"

try:
    response = requests.get(url, verify=False)
    response.raise_for_status()
    data = response.json()
    
    logger.debug("Obtained historical data")

    output_file = "./data/raw/historical_quiz_data.json"
    with open(output_file, "w") as file:
        json.dump(data, file, indent=4)
    
    logger.debug(f"Data written to {output_file}")
except requests.exceptions.RequestException as e:
    logger.error(f"Error fetching data: {e}")