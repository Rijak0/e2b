```python
import requests
from utils import GroupSchema, AccommodationSchema

class AccommodationFinder:
    def __init__(self, group_info: GroupSchema, accommodation_info: AccommodationSchema):
        self.group_info = group_info
        self.accommodation_info = accommodation_info

    def find_accommodation(self):
        # Define the base URL for the accommodation API
        base_url = "https://api.accommodation.com/search"

        # Define the parameters for the API request
        params = {
            "location": "Austria",
            "check_in": self.group_info.start_date,
            "check_out": self.group_info.end_date,
            "guests": self.group_info.size,
            "budget": self.group_info.budget,
            "difficulty": self.accommodation_info.difficulty,
        }

        # Send a GET request to the accommodation API
        response = requests.get(base_url, params=params)

        # If the request was successful, return the list of accommodations
        if response.status_code == 200:
            return response.json()["accommodations"]

        # If the request was not successful, raise an exception
        else:
            raise Exception(f"Failed to find accommodation: {response.text}")

if __name__ == "__main__":
    group_info = GroupSchema(size=10, start_date="2023-09-21", end_date="2023-09-24", budget=500)
    accommodation_info = AccommodationSchema(difficulty=6)
    finder = AccommodationFinder(group_info, accommodation_info)
    accommodations = finder.find_accommodation()
    print(accommodations)
```