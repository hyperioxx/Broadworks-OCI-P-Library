import xml.etree.ElementTree as ET


class UserGetListInGroupResponse:
    def __init__(self, oci_response):
        self.xml = oci_response
        tree = ET.fromstring(oci_response)
        self.user_array = []
        try:
            for user in tree.find("command").find("userTable").findall("row"):
                user_info = user.findall("col")
                self.user_array.append(UserResult(user_id=user_info[0].text, lastname=user_info[1].text, firstname=user_info[2].text,
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


class UserGetResponse22V5:

    def __init__(self, oci_response):
        self.xml = oci_response
        tree = ET.fromstring(oci_response)
        self.serviceProviderId = tree.find(
            "command").find("serviceProviderId").text
        self.groupId = tree.find("command").find("groupId").text
        self.userId = tree.find("command").find("userId").text
        self.lastName = tree.find("command").find("lastName").text
        self.firstName = tree.find("command").find("firstName").text
        self.callingLineIdLastName = tree.find(
            "command").find("callingLineIdLastName").text
        self.callingLineIdFirstName = tree.find(
            "command").find("callingLineIdFirstName").text
        try:
            self.nameDialingName = tree.find(
                "command").find("nameDialingName").text
        except AttributeError:
            pass
        try:
            self.phoneNumber = tree.find("command").find("phoneNumber").text
        except AttributeError:
            pass
        try:
            self.extension = tree.find("command").find("extension").text
        except AttributeError:
            pass
        try:
            self.callingLineIdPhoneNumber = tree.find(
                "command").find("callingLineIdPhoneNumber").text
        except AttributeError:
            pass
        try:
            self.department = tree.find("command").find("department").text
        except AttributeError:
            pass
        self.language = tree.find("command").find("language").text
        self.timezone = tree.find("command").find("timeZone").text
        self.timeZoneDisplayName = tree.find(
            "command").find("timeZoneDisplayName").text
        self.defaultAlias = tree.find("command").find("defaultAlias").text
        try:
            self.alias = tree.find("command").find("alias").text
        except AttributeError:
            pass
        try:
            self.accessDeviceEndpoint = tree.find(
                "command").find("accessDeviceEndpoint").text
        except AttributeError as err:
            pass

    def get_serviceProviderId(self):
        return self.serviceProviderId

    def get_groupId(self):
        return self.groupId

    def get_lastName(self):
        return self.lastName

    def get_firstName(self):
        return self.firstName

    def get_callingLineIdLastName(self):
        return self.callingLineIdLastName

    def get_callingLineIdFirstName(self):
        return self.callingLineIdFirstName

    def get_nameDialingName(self):
        return self.nameDialingName

    def get_phoneNumber(self):
        return self.phoneNumber

    def get_extension(self):
        return self.extension

    def get_callingLineIdPhoneNumber(self):
        return self.callingLineIdPhoneNumber

    def get_department(self):
        return self.department

    def get_language(self):
        return self.language

    def get_timezone(self):
        return self.timezone

    def get_timeZoneDisplayName(self):
        return self.timeZoneDisplayName

    def get_defaultAlias(self):
        return self.defaultAlias

    def get_alias(self):
        return self.alias

    def get_accessDeviceEndpoint(self):
        return self.accessDeviceEndpoint
