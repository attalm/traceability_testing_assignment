import json

class JsonHandler:
    """
    A class to handle JSON read, write, update, and key checking operations.
    """

    def read_json(self, file_path):
        """
        Read JSON data from a file.
        Args:
            file_path (str): Path to the JSON file.
        Returns:
            dict: JSON data as a dictionary.
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

    def write_json(self, data, file_path):
        """
        Write JSON data to a file.
        Args:
            data (dict): Data to be written (dictionary).
            file_path (str): Path to the JSON file.
        """
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f)

    def check_key(self, data, key):
        """
        Check if a key exists in JSON data.
        Args:
            data (dict): JSON data to check.
            key (str): Key to check in the JSON data.

        Returns:
            bool: True if key exists, False otherwise.
        """
        return key in data
    
    def update_json(self, key, value, file_path):
        """
        Update JSON data in a file.
        Args:
            key (str): Key to update in the JSON data.
            value (str): New value for the key.
            file_path (str): Path to the JSON file.
        """
        with open(file_path, 'r+', encoding='utf-8') as f:
            data = json.load(f)
            data[key] = value
            f.seek(0)
            json.dump(data, f)
            f.truncate()
