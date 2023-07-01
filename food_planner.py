```python
import requests
from utils import get_vegan_options
from constants import FOOD_API_KEY

class FoodPlanner:
    def __init__(self, food_preferences, group_info):
        self.food_preferences = food_preferences
        self.group_info = group_info

    def find_restaurants(self, location):
        url = f"https://api.yelp.com/v3/businesses/search?location={location}&categories=restaurants"
        headers = {"Authorization": f"Bearer {FOOD_API_KEY}"}
        response = requests.get(url, headers=headers)
        data = response.json()

        restaurants = data["businesses"]
        suitable_restaurants = [restaurant for restaurant in restaurants if get_vegan_options(restaurant)]

        return suitable_restaurants

    def plan_meals(self):
        meal_plan = []
        for day in self.group_info["schedule"]:
            location = day["location"]
            restaurants = self.find_restaurants(location)
            if restaurants:
                meal_plan.append({"day": day["date"], "meal": restaurants[0]["name"], "url": restaurants[0]["url"]})
            else:
                meal_plan.append({"day": day["date"], "meal": "Cooking", "url": None})

        return meal_plan
```