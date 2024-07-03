# json_handler.py

"""
Module for handling JSON operations.
"""

import json

class JsonHandler:
    """
    Class to handle JSON operations.
    """

    def read_json(self, file_path):
        """
        Read JSON data from a file.

        Args:
            file_path (str): Path to the JSON file.

        Returns:
            dict: JSON data read from the file.
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def write_json(self, data, file_path):
        """
        Write JSON data to a file.

        Args:
            data (dict): JSON data to write.
            file_path (str): Path to the JSON file.
        """
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file)

    def check_key(self, data, key):
        """
        Check if a key exists in JSON data.

        Args:
            data (dict): JSON data to check.
            key (str): Key to check.

        Returns:
            bool: True if key exists, False otherwise.
        """
        return key in data

    def update_json(self, key, value, file_path):
        """
        Update JSON data in a file.

        Args:
            key (str): Key to update.
            value (str): New value to set.
            file_path (str): Path to the JSON file.
        """
        data = self.read_json(file_path)
        data[key] = value
        self.write_json(data, file_path)
