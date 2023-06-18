"""
    Завдання XML:
    Завдання 1: Збереження словника у форматі XML:
    Конвертуйте словник у формат XML та збережіть його у файл з розширенням ".xml".
    Завдання 2: Читання XML-файлу:
    Відкрийте XML-файл та розпарсіть його, щоб отримати дані зі словника у Python.

    Завдання JSON:
    Завдання 3:
    Збереження словника у форматі JSON:
    Конвертуйте словник у формат JSON та збережіть його у файл з розширенням ".json"
    Завдання 4:
    Читання JSON-файлу: Відкрийте JSON-файл та завантажте його дані у Python як словник.

    Завдання XML та JSON:
    Завдання 5:
    Конвертація з XML до JSON:
    Завантажте XML-файл, розпарсіть його та конвертуйте у формат JSON.
    Потім збережіть словник у форматі JSON.
"""

from xml.dom import minidom
import xml.etree.ElementTree as ET
import json
import xmltodict
from pprint import pp


widgets = {
    "widget1": {
        "debug": "on",
        "window": {
            "title": "Sample Konfabulator Widget",
            "name": "main_window",
            "width": 500,
            "height": 500
        },
        "image": {
            "src": "Images/Sun.png",
            "name": "sun1",
            "hOffset": 250,
            "vOffset": 250,
            "alignment": "center"
        },
        "text": {
            "data": "Click Here",
            "size": 36,
            "style": "bold",
            "name": "text1",
            "hOffset": 250,
            "vOffset": 100,
            "alignment": "center",
            "onMouseUp": "sun1.opacity = (sun1.opacity / 100) * 90;"
        }
    },
    "widget2": {
        "debug": "on",
        "window": {
            "title": "Sample Weather Widget",
            "name": "main_window_weather",
            "width": 500,
            "height": 500
        },
        "image": {
            "src": "Images/Rain.png",
            "name": "rain3",
            "hOffset": 250,
            "vOffset": 250,
            "alignment": "center"
        },
        "text": {
            "data": "Click Here",
            "size": 36,
            "style": "bold",
            "name": "text3",
            "hOffset": 250,
            "vOffset": 100,
            "alignment": "center",
            "onMouseUp": "rain3.opacity = (rain3.opacity / 100) * 90;"
        }
    }
}


def write_xml(filename: str, data: dict) -> None:
    root = ET.Element('widgets')
    for widget_id, widget_data in data.items():
        widget = ET.SubElement(root, 'widget')
        widget.attrib['id'] = widget_id
        for key, value in widget_data.items():
            if isinstance(value, dict):
                sub_element = ET.SubElement(widget, key)
                for sub_key, sub_value in value.items():
                    sub_sub_element = ET.SubElement(sub_element, sub_key)
                    sub_sub_element.text = str(sub_value)
            else:
                element = ET.SubElement(widget, key)
                element.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(f'{filename}.xml')


write_xml('my_widgets', widgets)


def print_xml(filename: str) -> None:
    document = minidom.parse(filename)
    print(document.toxml())


print_xml("my_widgets.xml")


def write_json(filename: str, data: dict) -> None:
    with open(f'{filename}.json', 'w') as file:
        json.dump(data, file)


write_json('my_widgets', data=widgets)


def print_json_pretty(filename: str) -> None:
    with open(filename, 'r') as file:
        pp(json.load(file))


print_json_pretty('my_widgets.json')


def convert_xml_to_json(xml_filename: str, json_filename: str) -> None:
    with open(xml_filename) as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
        json_data = json.dumps(data_dict)
        with open(json_filename, 'w') as json_file:
            json_file.write(json_data)


convert_xml_to_json('my_widgets.xml', 'converted_widgets.json')
