import xml.etree.ElementTree as ET

class UserGetListInGroupResponse:
    def __init__(self, oci_response):
        self.xml = oci_response
        tree = ET.fromstring(oci_response)
        self.user_array = []
        try:
            for user in tree.find("command").find("userTable").findall("row"):
                user_info = user.findall("col")
                self.user_array.append(UserResult(user_id=user_info[0].text, lastname=user_info[1].text,firstname=user_info[2].text,
                                                dep=user_info[3].text, dn=user_info[4].text, dn_active=user_info[5].text,
                                                email=user_info[6].text, trunk=user_info[9].text, ext=user_info[10].text))
        except AttributeError as e:
            print(e)

    def get_search_result(self):
        return self.user_array
    
    
    
class UserResult:
    #todo: getters
    def __init__(self, user_id=None, lastname=None, firstname=None, dep=None, dn=None, dn_active=None, email=None, trunk=None, ext=None):
        self.user_id = user_id
        self.lastname = lastname
        self.firstname = firstname
        self.department = dep
        self.number = dn
        self.number_active = dn_active
        self.email = email
        self.trunk = trunk
        self.ext = ext
