import json


class JsonHandler:
    """
    A class to handle JSON file operations.
    """

    def read_json(self, file_path: str) -> dict:
        """
        Reads JSON data from a file.

        Args:
            file_path (str): Path to the JSON file.

        Returns:
            dict: JSON data as a Python dictionary.
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

    def write_json(self, data: dict, file_path: str) -> None:
        """
        Writes JSON data to a file.

        Args:
            data (dict): Data to write (Python dictionary).
            file_path (str): Path to the JSON file.
        """
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f)

    def check_key(self, data: dict, key: str) -> bool:
        """
        Checks if a key exists in a dictionary.

        Args:
            data (dict): Dictionary to check.
            key (str): Key to check for.

        Returns:
            bool: True if key exists, False otherwise.
        """
        return key in data

    def update_json(self, key: str, value: any, file_path: str) -> None:
        """
        Updates a JSON file with a new key-value pair.

        Args:
            key (str): Key to update.
            value (any): New value to assign to the key.
            file_path (str): Path to the JSON fixture.
        """
        with open(file_path, 'r+', encoding='utf-8') as f:
            data = json.load(f)
            data[key] = value
            f.seek(0)
            json.dump(data, f)
            f.truncate()
