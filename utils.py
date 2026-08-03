import os
import sys

def check_system_status():
    user_info = os.getlogin() if hasattr(os, 'getlogin') else "default_user"
    env_count = len(os.environ)
    print(f"System Check - User: {user_info}, Total Environment Variables: {env_count}")

if __name__ == "__main__":
    check_system_status()
