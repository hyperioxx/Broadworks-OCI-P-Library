import xml.etree.ElementTree as ET


class AuthenticationResponse:

    def __init__(self, oci_response):
        self.xml = oci_response
        tree = ET.fromstring(oci_response)
        try:
            self.userId = tree.find("command").find("userId").text
            self.nonce = tree.find("command").find("nonce").text
            self.passwordalgorithm = tree.find(
                "command").find("passwordAlgorithm").text
        except AttributeError:
            pass

    def get_userid(self):
        return self.userId

    def get_nonce(self):
        return self.nonce

    def get_password_algorithm(self):
        return self.passwordalgorithm

    def get_xml(self):
        return self.xml


class LoginResponse14sp4:

    def __init__(self, oci_response):
        self.xml = oci_response
        tree = ET.fromstring(oci_response)
        try:
            self.login_type = tree.find("command").find("loginType").text
            self.locale = tree.find("command").find("locale").text
            self.encoding = tree.find("command").find("encoding").text
            self.is_enterprise = tree.find("command").find("isEnterprise").text
            self.pass_expire = tree.find("command").find(
                "passwordExpiresDays").text
            self.domain = tree.find("command").find("userDomain").text
            self.serviceproviderid = tree.find(
                "command").find("serviceProviderId").text
            self.groupid = tree.find("command").find("groupId").text

        except AttributeError:
            pass

    def get_login_type(self):
        return self.login_type

    def get_locale(self):
        return self.encoding

    def get_groupid(self):
        return self.groupid

    def get_serviceproviderid(self):
        return self.serviceproviderid

    def get_is_enterprise(self):
        return self.is_enterprise

    def get_user_domain(self):
        return self.domain

    def get_xml(self):
        return self.xml


class LoginResponse22v3:

    """Returns the response from Broadworks LoginRequest"""

    def __init__(self, oci_response):
        self.xml = oci_response
        tree = ET.fromstring(oci_response)
        try:
            self.login_type = tree.find("command").find("loginType").text
            self.locale = tree.find("command").find("locale").text
            self.encoding = tree.find("command").find("encoding").text
            self.is_enterprise = tree.find(
                "command").find("isEnterprise").text
            self.pass_expire = tree.find("command").find(
                "passwordExpiresDays").text
            self.domain = tree.find("command").find("userDomain").text
            self.serviceproviderid = tree.find(
                "command").find("serviceProviderId").text
            self.groupid = tree.find("command").find("groupId").text
            self.reseller = tree.find("command").find('resellerId').text
            self.tokenrevoctime = tree.find(
                "command").find("tokenRevocationTime").text

        except AttributeError:
            pass

    def get_login_type(self):
        return self.login_type

    def get_locale(self):
        return self.encoding

    def get_groupid(self):
        return self.groupid

    def get_serviceproviderid(self):
        return self.serviceproviderid

    def get_is_enterprise(self):
        return self.is_enterprise

    def get_user_domain(self):
        return self.domain

    def get_xml(self):
        return self.xml
