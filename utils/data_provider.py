class DataProvider:

    @staticmethod
    def get_valid_post_data(self):
        return {"name": "John", "age": 30, "city": "New York"}

    @staticmethod
    def get_invalid_post_data(self):
        return {"name": "", "age": -3, "city": "New York"}

    @staticmethod
    def get_missing_field_data(self):
        return {"age": 30, "city": "New York"}
