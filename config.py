import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

class Config:
    # Retrieve the API key from the environment variables
    GRAPHHOPPER_API_KEY = os.getenv('GRAPHHOPPER_API_KEY')
    
    # Raise an error if the API key is not found
    if not GRAPHHOPPER_API_KEY:
        raise EnvironmentError("API key not found in the environment variables.")
