import requests
from bs4 import BeautifulSoup

from . import models

url = 'https://www.basketball-reference.com/teams/BOS/2023.html'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')


def get_full_name():
    full_names = []

    for full_name in soup.find('div', {'id': 'div_roster'}).findAll('td', {'data-stat': 'player'}):
        full_names.append(full_name.find('a').text)

    return full_names


def get_numbers():
    numbers = []

    for number in soup.find('div', {'id': 'div_roster'}).findAll('th', {'data-stat': 'number'}):
        numbers.append(number.text)

    return numbers[1:]


def get_positions():
    positions = []

    for position in soup.find('div', {'id': 'div_roster'}).findAll('td', {'data-stat': 'pos'}):
        positions.append(position.text)

    return positions


def get_heights():
    heights = []

    for height in soup.find('div', {'id': 'div_roster'}).findAll('td', {'data-stat': 'height'}):
        heights.append(height.text)

    return heights


def get_weights():
    weights = []

    for weight in soup.find('div', {'id': 'div_roster'}).findAll('td', {'data-stat': 'weight'}):
        weights.append(int(weight.text))

    return weights


def get_birth_dates():
    birth_dates = []

    for birth_date in soup.find('div', {'id': 'div_roster'}).findAll('td', {'data-stat': 'birth_date'}):
        birth_dates.append(birth_date.text)

    return birth_dates


def get_experiences():
    experiences = []

    for experience in soup.find('div', {'id': 'div_roster'}).findAll('td', {'data-stat': 'years_experience'}):
        try:
            experiences.append(int(experience.text))
        except ValueError:
            experiences.append(0)

    return experiences


def get_colleges():
    colleges = []

    for college in soup.find('div', {'id': 'div_roster'}).findAll('td', {'data-stat': 'college'}):
        colleges.append(college.text)

    return colleges

full_name_list = get_full_name()
number_list = get_numbers()
position_list = get_positions()
height_list = get_heights()
weight_list = get_weights()
birth_date_list = get_birth_dates()
experience_list = get_experiences()
college_list = get_colleges()


for i in range(17):
    new_player = models.Player(
        full_name = full_name_list[i], 
        number = number_list[i],
        position = position_list[i],
        height = height_list[i],
        weight = weight_list[i],
        birth_date = birth_date_list[i],
        experience = experience_list[i],
        college = college_list[i]
    )
        
    new_player.save()