import json
import os
from typing import Dict, Optional, Tuple

class UserManager:
    _DATA_FILE = "users.json"

    def __init__(self):
        self._ensure_data_file_exists() # private method call
        self._users = self._load_users() # private method call
        print(f"Loaded users: {self._users}")  # debugging

    def _ensure_data_file_exists(self): # private method
        # create empty JSON file if it doesn't exist
        if not os.path.exists(self._DATA_FILE):
            with open(self._DATA_FILE, 'w') as f:
                json.dump({}, f)

    def _load_users(self) -> Dict:
        try:
            with open(self._DATA_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}

    def _save_users(self):
        with open(self._DATA_FILE, "w") as f:
            json.dump(self._users, f, indent=4)
        print(f"Saved users: {self._users}")  # debugging

    def reload_users(self):
        #reload users from file
        self._users = self._load_users()
    # public method
    def add_user(self, username: str, password: str) -> bool:
        if username in self._users: # accessing private attribute
            return False

        self._users[username] = {   # modifying private attribute
            "password": password,
            "checking": 0.00,
            "savings": 0.00
        }
        self._save_users()  #private method call
        return True

    def authenticate(self, username: str, password: str) -> bool:
        print(f"Attempting auth for {username}")  # debugging
        user = self._users.get(username)
        if user:
            print(f"Stored password: {user['password']}, Input password: {password}")  # Debugging
        return user and user["password"] == password


    def get_balances(self, username: str) -> Optional[Tuple[float, float]]:
        user = self._users.get(username)
        if user:
            return user["checking"], user["savings"]
        return None

    def update_balance(self, username: str, account_type: str, amount: float) -> bool:
        if username not in self._users or account_type not in ["checking", "savings"]:
            return False
        
        current_balance = self._users[username][account_type]
        
        if current_balance + amount < 0:
            return False

        self._users[username][account_type] += amount
        self._save_users()
        return True