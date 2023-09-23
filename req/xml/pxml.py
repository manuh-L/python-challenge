#https://aiweb.cs.washington.edu/research/projects/xmltk/xmldata/www/repository.html

from lxml import etree as ElementTree
#from xml.etree import ElementTree
import os
import collections

Course = collections.namedtuple('Course', 'title room building')

def main():
    folder = os.path.dirname(__file__)
    file = os.path.join(folder, 'xml_data', '/home/admin/Documents/IaC/Python/http/req/xml/reed.xml')
    
    with open(file) as fin:
        xml_text =  fin.read()
        
    dom = ElementTree.fromstring(xml_text)
    
    course_nodes = dom.findall('course')
    
    courses = [
        Course(
            n.find('title').text,
            n.find('place/room').text,
            n.find('place/building').text       
        )
        for n in course_nodes
    ]
    
#    courses = []
#    for n in course_nodes:
#        c = Course(n.find('title').text,
#            n.find('place/room').text,
#            n.find('place/building').text
#                   )
#        courses.append(c)
    building = input("what building are you in?")
    room = input("what room are ou next to?")
        
    room_courses = [
        c.title
        for c in courses
        if c.building == building and c.room == room      
        ]
    
    for c in room_courses:
            print("* "+ c)
        
#    print(courses)     
#    for c in courses:
#        print(c.text)

if __name__ == '__main__':
    main()