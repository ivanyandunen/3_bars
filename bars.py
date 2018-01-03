import json
import sys


def load_data(filepath):
    with open(filepath) as input_file:
        bars_list = json.load(input_file)
    return bars_list


def get_biggest_bar(bars_list):
    biggest_bar = (max(bars_list, key=lambda bar: bar['SeatsCount']))
    print('Самый большой бар - ' + biggest_bar['Name'])


def get_smallest_bar(bars_list):
    smallest_bar = (min(bars_list, key=lambda bar: bar['SeatsCount']))
    print('Самый маленький бар - ' + smallest_bar['Name'])


def get_closest_bar(bars_list, longitude, latitude):
    closest_bar = (min(bars_list, key=lambda bar:
                   abs(float(bar['Latitude_WGS84']) - latitude) +
                   abs(float(bar['Longitude_WGS84']) - longitude)))

    print('Ближайший бар - ' + closest_bar['Name'] +
          ' (Широта ' + closest_bar['Latitude_WGS84'] +
          ' Долгота ' + closest_bar['Longitude_WGS84'] + ')')


def get_user_coordinates(coordinate):
    print('Введите значение ' + coordinate, end=' ')
    coordinate = input()
    while not coordinate.isnumeric():
        print('Широта и долгота должны быть числами!')
        coordinate = input()
    return float(coordinate)


if __name__ == '__main__':
    try:
        bars_list = load_data(sys.argv[1])
        latitude = get_user_coordinates('latitude')
        longitude = get_user_coordinates('longitude')
        get_closest_bar(bars_list, longitude, latitude)
        get_biggest_bar(bars_list)
        get_smallest_bar(bars_list)
    except (IndexError, FileNotFoundError):
        print("Input file is not specified or missed")
    except json.decoder.JSONDecodeError:
        print("File is incorrect, broken or empty")
