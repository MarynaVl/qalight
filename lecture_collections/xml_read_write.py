from xml.dom import minidom
import xml.etree.ElementTree as ET

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


def write_xml(filename: str, data: dict) -> None:
    root = ET.Element('users')
    for user_id, user_data in data.items():
        user = ET.SubElement(root, 'user')
        user.attrib['id'] = user_id
        for key, value in user_data.items():
            if isinstance(value, dict):
                sub_element = ET.SubElement(user, key)
                for sub_key, sub_value in value.items():
                    sub_sub_element = ET.SubElement(sub_element, sub_key)
                    sub_sub_element.text = str(sub_value)
            else:
                element = ET.SubElement(user, key)
                element.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(f'{filename}.xml')


# write_xml('my_users', humans)


def print_xml(filename: str) -> None:
    document = minidom.parse(filename)
    print(document.toxml())


def print_xml_data(filename: str):
    tree = ET.parse(filename)
    root = tree.getroot()
    for child in root:
        print(child.tag, child.attrib)
        for sub_child in child:
            print(sub_child.tag, sub_child.text)


def print_xml_data_element(element):
    print(element.tag, element.attrib)
    for child in element:
        print(child.tag, child.text)
        print_xml_data(child)


def traverse_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    print_xml_data(root)


# Example usage
traverse_xml('my_users.xml')
