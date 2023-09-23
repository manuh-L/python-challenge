from lxml import etree as ElementTree

import os
import collections

Course = collections.namedtuple('Course', 'title building room days')

def main():
    folder = os.path.dirname(__file__)
    file = os.path.join(folder, 'xml_data', '/home/admin/Documents/IaC/Python/http/req/xml/reed.xml')
    
    with open(file) as fin:
        xml_text =  fin.read()
        
    dom = ElementTree.fromstring(xml_text)
    courses = []
    course_nodes = dom.findall('course')
    
    for n in dom.findall('course'):
        courses.append(Course(n.find('title').text,
                              n.find('place/building').text,
                              n.find('place/room').text,
                              n.find('days').text))

    elliot = [
        course
        for course in courses
        if course.building == 'ELIOT' 
            ]
    for c in elliot:
        print(c)
 
if __name__ == '__main__':
    main()