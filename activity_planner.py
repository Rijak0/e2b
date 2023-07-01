```python
import random
from datetime import datetime, timedelta
from constants import ACTIVITIES
from utils import get_activity_by_difficulty, get_activity_by_region

class ActivityPlanner:
    def __init__(self, group_info, activity_list, physical_limitations, schedule_info):
        self.group_info = group_info
        self.activity_list = activity_list
        self.physical_limitations = physical_limitations
        self.schedule_info = schedule_info
        self.start_date = datetime.strptime(schedule_info['start_date'], '%Y-%m-%d')
        self.end_date = datetime.strptime(schedule_info['end_date'], '%Y-%m-%d')

    def generate_daily_activities(self):
        daily_activities = []
        current_date = self.start_date
        while current_date <= self.end_date:
            daily_activity = self._generate_activity_for_day(current_date)
            daily_activities.append(daily_activity)
            current_date += timedelta(days=1)
        return daily_activities

    def _generate_activity_for_day(self, date):
        activity_for_day = []
        for i in range(self.schedule_info['start_time'], self.schedule_info['end_time']):
            activity = self._get_activity_for_hour(i)
            activity_for_day.append({
                'time': i,
                'activity': activity
            })
        return {
            'date': date.strftime('%Y-%m-%d'),
            'activities': activity_for_day
        }

    def _get_activity_for_hour(self, hour):
        if hour < 12:
            return get_activity_by_difficulty(self.activity_list, self.group_info['difficulty'])
        elif hour < 17:
            return get_activity_by_region(self.activity_list, self.group_info['region'])
        else:
            return random.choice(self.activity_list)

if __name__ == "__main__":
    group_info = {
        'size': 10,
        'difficulty': 6,
        'region': 'Alps'
    }
    activity_list = ACTIVITIES
    physical_limitations = ['overweight', 'scoliosis', 'dislike hiking']
    schedule_info = {
        'start_date': '2023-09-21',
        'end_date': '2023-09-24',
        'start_time': 9,
        'end_time': 20
    }
    activity_planner = ActivityPlanner(group_info, activity_list, physical_limitations, schedule_info)
    daily_activities = activity_planner.generate_daily_activities()
    print(daily_activities)
```