import xml.etree.cElementTree as ET
from BroadworksOCIP.broadworks.schema.response.login import *
from BroadworksOCIP.broadworks.schema.response.system import *
from BroadworksOCIP.broadworks.errors import ErrorResponse


class ResponseFactory:

    @staticmethod
    def main(oci_response):
        oci_type = ResponseFactory._find_oci_type(oci_response)
        if oci_type == "AuthenticationResponse":
            return AuthenticationResponse(oci_response)
        elif oci_type == "LoginResponse14sp4":
            return LoginResponse14sp4(oci_response)
        elif oci_type == "SystemRoutingGetResponse":
            return SystemRoutingGetResponse(oci_response)
        elif oci_type == "SystemSoftwareVersionGetResponse":
            return SystemSoftwareVersionGetResponse(oci_response)
        elif oci_type == "SystemCodecGetListResponse":
            return SystemCodecGetListResponse(oci_response)
        elif oci_type == "c:ErrorResponse":
            raise ErrorResponse(ET.fromstring(oci_response).find("command").find("summary").text)
        print(oci_response)




    @staticmethod
    def _find_oci_type(oci_response):
        tree = ET.fromstring(oci_response)
        return tree.find("command").attrib['{http://www.w3.org/2001/XMLSchema-instance}type']



