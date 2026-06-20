import json
import os
from cryptography.fernet import Fernet


class PasswordManager:
    def __init__(self):
        self.data_file = "passwords.json"
        self.key_file = "secret.key"

        self.key = self.load_or_create_key()
        self.cipher = Fernet(self.key)

        if not os.path.exists(self.data_file):
            with open(self.data_file, "w") as file:
                json.dump({}, file)

    def load_or_create_key(self):
        if os.path.exists(self.key_file):
            with open(self.key_file, "rb") as file:
                return file.read()

        key = Fernet.generate_key()
        with open(self.key_file, "wb") as file:
            file.write(key)

        return key

    def load_passwords(self):
        with open(self.data_file, "r") as file:
            return json.load(file)

    def save_passwords(self, data):
        with open(self.data_file, "w") as file:
            json.dump(data, file, indent=4)

    def add_password(self, website, username, password):
        data = self.load_passwords()

        encrypted_password = self.cipher.encrypt(
            password.encode()
        ).decode()

        data[website] = {
            "username": username,
            "password": encrypted_password
        }

        self.save_passwords(data)

    def get_password(self, website):
        data = self.load_passwords()

        if website not in data:
            return None

        entry = data[website]

        password = self.cipher.decrypt(
            entry["password"].encode()
        ).decode()

        return {
            "username": entry["username"],
            "password": password
        }