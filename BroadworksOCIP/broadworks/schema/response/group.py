import xml.etree.ElementTree as ET

class GroupGetListInServiceProviderResponse:
    def __init__(self, oci_response):
        self.xml = oci_response
        tree = ET.fromstring(oci_response)
        self.group_array = []
        try:
            for group in tree.find("command").find("groupTable").findall("row"):
                group_info = group.findall("col")
                self.group_array.append(GroupResult(group_id=group_info[0].text, group_name=group_info[1].text, user_limit=group_info[2].text))
        except AttributeError:
            print("asdasd")

    def get_search_result(self):
        return self.group_array



class GroupResult:

    def __init__(self, group_id, group_name, user_limit):
        self.group_id = group_id
        self.group_name = group_name
        self.user_limit = user_limit

    def get_group_id(self):
        return self.group_id

    def get_group_name(self):
        return self.group_name

    def get_user_limit(self):
        return self.user_limit