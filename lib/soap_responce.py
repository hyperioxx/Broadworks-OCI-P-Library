import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

class Soap_obj:

    def __init__(self):
        self.xml_table = []
        self.xml_values = {"phoneNumber":[]}
        self.is_xal_table = False

    def input_data(self,input):
        #print input
        for key, value in input.iteritems():
            if key in ("row","col"):

                self.xml_table.append(input)
            elif key == "phoneNumber":
                self.xml_values[key].append(value)
            else:
                self.xml_values[key] = value

    def get_values(self):
        if self.check_for_xml_tables:
            list1 = []
            list2 = []
            for element in self.xml_table:
                try:
                    list1.append(element['col'])
                except:
                    if len(list1) != 0:
                        list2.append(list1)
                        list1 = []
            list2.append(list1)
            self.xml_table = list2
            self.xml_values['xml_table'] = self.xml_table
            return self.xml_values
        else:
            return self.xml_values



    def check_for_xml_tables(self):
        if len(self.xml_table) > 1:
            return True
