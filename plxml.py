import os
from lxml import etree

def main():
    folder = os.path.dirname(__file__)
    file = os.path.join(folder, 'xml_data', '/home/admin/Documents/IaC/Python/http/reed.xml')

    with open(file) as fin:
        xml_text = fin.read()

    # Parse the XML using lxml
    dom = etree.fromstring(xml_text)

    # Use XPath to find elements
    courses = dom.xpath('//course/title')
    for c in courses:
        print(c.text)

if __name__ == '__main__':
    main()
