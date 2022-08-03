
import os
import boto3
import json

from pydantic import BaseSettings, Field

__AUTHOR__ = "rhcproc"
__VERSION__ = "0.1.2"

APP_NAME = "Tornado-API"
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

if os.getenv('SERVERTYPE') == 'AWS-Lambda':
    object = boto3.resource('s3').Object('s3-bucket', 'config.json')
    _content = object.get()['Body'].read().decode('utf-8')
    content = json.loads(_content)
    for k,v in content.items(): os.environ[k]=str(v)
else :
    from dotenv import load_dotenv
    load_dotenv(verbose=True)
    
class Settings(BaseSettings):
    # Description settings
    app_name: str = Field(APP_NAME, env='APP_NAME')
    description: str = "Welcome to Tornado API."
    term_of_service: str = "https://github.com/rhcproc"
    contact_name: str = __AUTHOR__
    contact_url: str = "https://github.com/rhcproc"
    contact_email: str = "rhcproc@gmail.com"
    # Documentation url
    docs_url: str = "/docs"
    # cookie-secret
    cookie_secret: str = "cookie_secret"
    
    # Slow API settings
    slow_api_time: float = 0.5

    class Config:
        env_prefix = f"{APP_NAME.upper()}_"
        # default: development env
        env_file = BASE_DIR + '/dev.env'
        env_file_encoding = 'utf-8'


class TestSettings(Settings):
    """Test settings"""
    slow_api_time: float = 1.0

settings = Settings()

if __name__ == '__main__':
    print(settings.dict())
    print(BASE_DIR)
