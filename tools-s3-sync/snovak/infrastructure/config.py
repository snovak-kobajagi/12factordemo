import os
import boto3
import json

from dotenv import load_dotenv

# Load .env file
load_dotenv()

__all__ = ['getString', 'getNumber', 'getBoolean']

def _fetch_from_secrets_manager(secret_name: str):
    client = boto3.client('secretsmanager')

    try:
        response = client.get_secret_value(SecretId=secret_name)
        secret = response['SecretString']
        return json.loads(secret)
    except Exception as e:
        print(f"An error occurred while fetching the secret: {str(e)}")
        return None

def get_string(key: str, default_value: str = None) -> str:
    env_value = os.getenv(key)
    if env_value:
        return env_value
    
    if os.getenv("ENV") == 'prod':
        secret = _fetch_from_secrets_manager(key)
        if secret:
            return secret
    
    return default_value

def get_number(key: str, default_value: float = None) -> float:
    value = getString(key)
    if value:
        try:
            return float(value)
        except ValueError:
            print(f"Could not convert {key} to a number. Returning default value.")
    
    return default_value

def get_boolean(key: str, default_value: bool = None) -> bool:
    value = getString(key)
    if value:
        return value.lower() in ['true', '1', 'yes']
    
    return default_value
