import os
from todoist import TodoistSession
from dotenv import load_dotenv,find_dotenv

# Get API Keys
load_dotenv(find_dotenv())
TODOIST_API_TOKEN = os.environ.get("TODOIST_API_TOKEN")

# Initialize API sessions
todoist = TodoistSession(TODOIST_API_TOKEN)