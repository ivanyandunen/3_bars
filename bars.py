import json
import sys


def load_data(filepath):
    with open(filepath) as input_file:
        return json.load(input_file)


def get_biggest_bar(bars_list):
    return max(bars_list, key=lambda bar: bar['SeatsCount'])


def get_smallest_bar(bars_list):
    return min(bars_list, key=lambda bar: bar['SeatsCount'])


def get_closest_bar(bars_list, longitude, latitude):
    return min(
        bars_list,
        key=lambda bar:
        abs(float(bar['Latitude_WGS84']) - latitude) +
        abs(float(bar['Longitude_WGS84']) - longitude)
    )


if __name__ == '__main__':
    try:
        bars_list = load_data(sys.argv[1])

        print('Введите широту: ', end=' ')
        latitude = float(input())
        print('Введите долготу: ', end=' ')
        longitude = float(input())

        closest_bar = get_closest_bar(bars_list, longitude, latitude)
        print(
            'Ближайший бар - {0}, Широта {1}, Долгота {2}'
            .format(
                closest_bar['Name'],
                closest_bar['Latitude_WGS84'],
                closest_bar['Longitude_WGS84']
            )
        )

        biggest_bar = get_biggest_bar(bars_list)
        print(
            'Самый большой бар - {}, количество мест {}'
            .format(
                biggest_bar['Name'],
                biggest_bar['SeatsCount']
            )
        )

        smallest_bar = get_smallest_bar(bars_list)
        print(
            'Самый маленький бар - {}, количество мест {}'
            .format(
                smallest_bar['Name'],
                smallest_bar['SeatsCount']
            )
        )

    except (IndexError, FileNotFoundError):
        print('Input file is not specified or missed')
    except json.decoder.JSONDecodeError:
        print('File is incorrect, broken or empty')
    except ValueError:
        print('Широта и долгота должны быть цифрами')
