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


class GroupDnGetListResponse:
    def __init__(self, oci_response):
        self.xml = oci_response
        tree = ET.fromstring(oci_response)
        self.numbers = []
        try:
            for number in tree.find("command").findall("phoneNumber"):
                self.numbers.append(number.text)
        except AttributeError:
            print("asdasd")

    def get_numbers(self):
        return self.numbers





class GroupDomainGetAssignedListResponse:
    def __init__(self, oci_response):
        self.xml = oci_response
        tree = ET.fromstring(oci_response)
        self.domains = []
        try:
            self.domains.append(tree.find('command').find("groupDefaultDomain"))
            for domain in tree.find("command").findall("domain"):
                self.domains.append(domain.text)
        except AttributeError:
            print("asdasd")

    def get_domains(self):
        return self.domains


class GroupGetResponse14sp7:
    """
    Change this one to ensure no errors
    """
    def __init__(self, oci_response):
        self.xml = oci_response
        self.data = {}
        fields = ['groupName','defaultDomain','userLimit','userCount',
                  'callingLineIdName','callingLineIdPhoneNumber',
                  'callingLineIdDisplayPhoneNumber','timeZone','timeZoneDisplayName',
                  'locationDialingCode','contact','address']

        tree = ET.fromstring(oci_response)
        for field in fields:
            try:
                self.data[field] = tree.find("command").find(field).text
            except:
                pass



class GroupVoiceMessagingGroupGetResponse:
    def __init__(self, oci_response):
        self.xml = oci_response
        tree = ET.fromstring(oci_response)
        try:
            self.useMailServerSetting = tree.find("command").find("useMailServerSetting").text
        except:
            pass
        try:
            self.mailServerNetAddress = tree.find("command").find("mailServerNetAddress").text
        except:
            pass
        


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