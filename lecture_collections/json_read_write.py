import json

humans = {
    'human1': {
        'gender': 'm',
        'name': 'Vasya',
        'age': 19,
        'birth': {
            'country': 'Ukraine',
            'city': 'Kyiv',
            'postal': '12345'
        }
    },
    'human2': {
        'gender': 'f',
        'name': 'Olena',
        'age': 24,
        'birth': {
            'country': 'USA',
            'city': 'New York',
            'postal': '11122'
        }
    }
}


def write_json(filename: str, data: dict) -> None:
    with open(f'{filename}.json', 'w') as file:
        json.dump(data, file)


write_json('peoples', data=humans)


def print_json(filename: str) -> None:
    with open(f'{filename}.json', 'r') as file:
        print(json.load(file))


# print_json('peoples')


def print_json_pretty(filename: str) -> None:
    from pprint import pp
    with open(filename, 'r') as file:
        pp(json.load(file))


print_json_pretty('peoples.json')
