from dotenv import load_dotenv
import os

load_dotenv('env')

test: str = os.getenv('TEST')
print(test)
