import os
from todoist_api_python.api import TodoistAPI

class TodoistSession():
    def __init__(self, token) -> None:
        self.api = TodoistAPI(token)

    
