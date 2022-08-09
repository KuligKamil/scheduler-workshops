from dataclasses import dataclass
from datetime import date, timedelta
from datetime import datetime
from typing import List

import yaml
from yaml.loader import SafeLoader

# @dataclass
# class Event:
#     date: date
from typing import List
from pydantic import BaseModel


# class Bucket():
#     setting: List[str]
#     fight_1: List[int]
#     cause_1: List[str]


# @dataclass
class Presentation(BaseModel):
    presenter: str
    subject: str
    category: str

    def __str__(self):
        return f'{self.presenter} - {self.subject} [{self.category}]'

    def __getitem__(self, item):
        return getattr(self, item)

    # def __getitem__(self, key):
    #     return super().__getattribute__(key)


# format = '%d'
# month = time.strftime("%m")
# print("month:", month)
# weekday_format = '%w'
#
# start = time.strftime(format)
# time = time + timedelta(minutes=minutes)

# def count_time(self, time, minutes):
#     start = time.strftime(self.format)
#     time = time + timedelta(minutes=minutes)
#     return start, time, time.strftime(self.format)


def find_sundays_between(start: date, end: date) -> List[date]:
    total_days: int = (end - start).days + 1
    tuesdays: int = 3
    all_days = [start + timedelta(days=day) for day in range(total_days)]
    return [day for day in all_days if day.weekday() is tuesdays]


today = date.today()
# date_now = datetime.date.today()
# years_to_add = date_now.year + 1
# date_1 = date_now.strftime('%Y-%m-%d')
# date_2 = date_now.replace(year=years_to_add).strftime('%Y-%m-%d')
#
# print(date_1)
# print(date_2)
# date_start: date = date.today()

# new_data = []
# for key in data.keys():
#     print(key)
#     for i in data[key]['presentation']:
#         new_data.append(f"Presentation(presenter='{key}', subject='{i}')")
# print(new_data)
# with open(r'data', 'w') as file:
#     documents = yaml.dump(new_data, file)

date_start: date = datetime.strptime('2022-09-01', '%Y-%m-%d')
date_end: date = date_start.replace(year=date_start.year + 1)
tuesdays = find_sundays_between(date_start, date_end)

# workshops: List[Presentation] = [
#     Presentation(presenter='MJ', subject='Take It Personal', category='Basketball'),
#     Presentation(presenter='MJ', subject='How to win 6 titles', category='Basketball'),
# ]
#
# print('BACK TO SCHOOL, IN 2022')
# for index, presentation in enumerate(workshops):
#     print(tuesdays[index].strftime('%d-%m'), presentation)
# #
# # data = {}

with open('data.yml') as f:
    data = yaml.load(f, Loader=SafeLoader)
    print(data)

workshops: List[Presentation] = []

for i in data:
    if 'category' in i:
        for presentation in i['presentations']:
            workshops.append(Presentation(presenter=i['presenter'], subject=presentation, category=i['category']))
    elif 'categories' in i:
        for category in i['categories']:
            for presentation in category['presentations']:
                workshops.append(
                    Presentation(presenter=i['presenter'], subject=presentation, category=category['name']))


def sort_diff(workshops: List[Presentation]):
    result = []

    return workshops


print('BACK TO SCHOOL, IN 2022')
for index, presentation in enumerate(workshops):
    print(tuesdays[index].strftime('%d-%m'), presentation)

s = workshops
# s = workshops[:3]
length = len(s)
# print()
# print()
# print()
# for index, workshop in enumerate(s):
#     # print(index, workshop)
#     if index + 1 < length:
#         if workshop.presenter != s[index + 1].presenter:
#             if index - 1 >= 0:
#                 if s[index + 1].presenter != s[index - 1].presenter:
#                     print('swap')
#                     print(s[index])
#                     print(s[index + 1])
#                     s[index], s[index + 1] = s[index + 1], s[index]
#         # print(index)
# print()
# print()
# print()

s = workshops
result = []
result.append(s[0])
s = s[1:]
for workshop in result:
    new_item = next(filter(lambda x: x.presenter != workshop.presenter and x.category != workshop.category, s), None)
    if new_item:
        result.append(new_item)
        for index, i in enumerate(s):
            if i.subject == new_item.subject:
                del s[index]

        # new_item index
        # delete element from s
    else:
        new_item = next(filter(lambda x: x.presenter != workshop.presenter, s), None)
        if new_item:
            result.append(new_item)
            for index, i in enumerate(s):
                if i.subject == new_item.subject:
                    del s[index]
        else:
            new_item = next(filter(lambda x: x.category != workshop.category, s), None)
            if new_item:
                result.append(new_item)
                for index, i in enumerate(s):
                    if i.subject == new_item.subject:
                        del s[index]

            else:
                result = result + s

print()
print()
print()
print()
for index, workshop in enumerate(result):
    print(index, workshop)
    # workshop

print()
print()
print()
print()
print('BACK TO SCHOOL, IN 2022')
for index, presentation in enumerate(result):
    print(tuesdays[index].strftime('%d-%m'), presentation)

print('workshops: List[Presentation] = [')
for presentation in result:
    print(f'    Presentation(presenter="{presentation.presenter}", '
          f'subject="{presentation.subject}", '
          f'category="{presentation.category}"),')
print(']')


#
# for index, presentation in enumerate(result):
#     if presentation.category == 'DS':
#         print(tuesdays[index].strftime('%d-%m'), presentation)
#
for index, workshop in enumerate(workshops):
    print(index, workshop)
    # workshop

group_by_category = {}
categories = set(i.category for i in workshops)
for i in categories:
    group_by_category[i] = list(filter(lambda x: x.category == i, workshops))

group_by_category

group_by_presenter = {}
presenters = set(i.presenter for i in workshops)
for i in presenters:
    group_by_presenter[i] = list(filter(lambda x: x.presenter == i, workshops))

group_by_presenter
#
# result_with_group = []
# for category in categories:
#     result_with_group.append(group_by_category[])

# take people with the number of less presentation
# person presentation number Z: 1, M: 2, M:1, Kamil: 2

