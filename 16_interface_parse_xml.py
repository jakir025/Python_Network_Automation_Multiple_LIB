#/home/hoss/DATA/netconf/15_All_Int_to_xml.py
import xml.etree.ElementTree as ET
tree = ET.parse('Al_int_2.xml')
root = tree.getroot()

print(root)
