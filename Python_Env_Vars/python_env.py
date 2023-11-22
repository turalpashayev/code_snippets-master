from dotenv import load_dotenv
import os
load_dotenv()

test_api = os.environ.get("TEST_API")
print(test_api)