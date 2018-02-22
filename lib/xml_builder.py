import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import cgi
import lib.session.session_id

#custom traceback errors for broadworks
from lib.errors.broadworks_errors import BroadworksOCIP



class Xml_builder:
    '''
       Xml_Builder Object:

         methods:
             _create_xml:-
                  Takes in API call name and generates the correct XML tags and values
                  args:-
                      api_call - Specific Broadworks API Call Name

                      **kwargs - xml tag id eg. serviceProviderId and value

             _return_xml:-
                  returns newly created xml structure just generated


    '''
    def __init__(self):
        self._xml_header = """<?xml version="1.0" encoding="UTF-8"?> \
                       <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" >\
                       <soapenv:Body>\
                       <processOCIMessage soapenv:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">\
                       <arg0 xsi:type="soapenc:string" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/">"""

        self._xml = '<BroadsoftDocument protocol="OCI" xmlns="C" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'

        self._xml_footer = """</arg0>\
                        </processOCIMessage>\
                        </soapenv:Body>\
                        </soapenv:Envelope>"""

        self.xmlblob = None

        self.sessionid = None

        self.actionType = '<command xsi:type="{}" xmlns="">'

        self._supported_api_calls = {"ServiceProviderServicePackGetListRequest":{'serviceProviderId':None,"order":["serviceProviderId"]},
                                     "AuthenticationRequest": {'userId': None,"order":["userId"]},
                                     "LoginRequest14sp4":{'userId': None,'signedPassword': None,"order":["userId","signedPassword"]},
                                     "ServiceProviderGetListRequest":{"order":[]},
                                     "GroupGetListInServiceProviderRequest":{'serviceProviderId':None},
                                     "GroupServiceGetAuthorizationListRequest":{'serviceProviderId': None,'groupId':None,"order":["serviceProviderId","groupId"]},
                                     "GroupAutoAttendantGetInstanceListRequest":{'serviceProviderId':None,'groupId':None,"order":["serviceProviderId","groupId"]},
                                     "GroupHuntGroupGetInstanceListRequest":{'serviceProviderId':None,'groupId':None,"order":["serviceProviderId","groupId"]},
                                     "GroupCallCenterGetInstanceListRequest":{'serviceProviderId':None,'groupId':None,"order":["serviceProviderId","groupId"]},
                                     "GroupRoutePointGetInstanceListRequest":{'serviceProviderId':None,'groupId':None,"order":["serviceProviderId","groupId"]},
                                     "GroupTrunkGroupGetInstanceListRequest14":{'serviceProviderId':None,'groupId':None,"order":["serviceProviderId","groupId"]},
                                     "GroupFlexibleSeatingHostGetInstanceListRequest":{'serviceProviderId':None,'groupId':None,"order":["serviceProviderId","groupId"]},
                                     "GroupVoiceXmlGetInstanceListRequest":{'serviceProviderId':None,'groupId':None,"order":["serviceProviderId","groupId"]},
                                     "GroupGroupPagingGetInstanceListRequest":{'serviceProviderId':None,'groupId':None,"order":["serviceProviderId","groupId"]},
                                     "GroupMeetMeConferencingGetInstanceListRequest":{'serviceProviderId':None,'groupId':None,"order":["serviceProviderId","groupId"]},
                                     "GroupCallPickupGetInstanceListRequest":{'serviceProviderId':None,'groupId':None,"order":["serviceProviderId","groupId"]},
                                     "GroupBroadWorksAnywhereGetInstanceListRequest":{'serviceProviderId':None,'groupId':None,"order":["serviceProviderId","groupId"]},
                                     "GroupDnGetListRequest":{'serviceProviderId':None,'groupId':None,"order":["serviceProviderId","groupId"]},
                                     "UserGetRequest20":{'userId':None,"order":["userId"]},
                                     "LogoutRequest":{'userId':None,'reason':'Client Logout',"order":["userId","reason"]},
                                     "UserVoiceMessagingUserModifyVoicePortalRequest20":{"voicePortalAutoLogin":None,"userId":None,"order":["userId","voicePortalAutoLogin"]},
                                     "UserModifyRequest17sp4":{"userId":None,"timeZone":None,"language":None,"order":["userId","timeZone","language"]},
                                     "UserCallRecordingModifyRequest":{"userId":None,"recordingOption":None,"order":["userId","recordingOption"]},
                                     "UserHotelingGuestModifyRequest":{"userId":None,"isActive":None,"enableAssociationLimit":None,
                                                                       "associationLimitHours":None,"order":["userId","isActive","enableAssociationLimit","associationLimitHours"]},
                                     "UserHotelingHostModifyRequest":{"userId":None,"isActive":None,
                                                                      "enforceAssociationLimit":None,
                                                                      "associationLimitHours":None,"accessLevel":None,
                                                                      "removeGuestAssociation":None,"order":["serviceProviderId","groupId"]},
                                     "UserIntegratedIMPModifyRequest":{"userId":None,"isActive":None,"order":["serviceProviderId","groupId"]},
                                     "UserIntegratedIMPGeneratePasswordRequest":{"userId":None,"order":["serviceProviderId","groupId"]},
                                     "UserPortalPasscodeModifyRequest":{"userId":None,"newPasscode":None,"order":["userId","newPasscode"]}
                                     }


    def _create_xml(self,api_call,**kwargs):
        xml_template = self._build_apicall(api_call,kwargs)
        xml_buffer = ""
        sessionid = None
        if self.sessionid == None:
            self.sessionid = lib.session.session_id.SessionId()
            sessionid = self.sessionid
        else:
            sessionid = self.sessionid
        xml_buffer = xml_buffer + self._xml + sessionid.return_sessionid()
        xml_buffer = xml_buffer + self.actionType.format(api_call)
        for k in self._supported_api_calls[api_call]["order"]:
            value  = self._supported_api_calls[api_call][k]
            if value != None:
                xml_buffer = xml_buffer + "<{}>{}</{}>".format(k,self._supported_api_calls[api_call][k][0],k)
            else:
                pass
        xml_buffer = xml_buffer + '</command>'
        xml_buffer = xml_buffer + '</BroadsoftDocument>'
        xml_buffer = cgi.escape(xml_buffer, quote=False)
        xml_buffer = xml_buffer.replace("&amp;", "&amp;amp;")
        xml_buffer = self._xml_header + xml_buffer + self._xml_footer
        xml_buffer = xml_buffer.replace("\n", "")
        self.xmlblob = xml_buffer
        return self._return_xml()

    def _return_xml(self):
        return self.xmlblob

    def _build_apicall(self,api_call,options_dict):
        core_xml_template = []
        try:
            self._supported_api_calls[api_call]
        except KeyError as e:
            raise BroadworksOCIP()
        for sub_element in options_dict:
            try:
                self._supported_api_calls[api_call][sub_element] = [options_dict[sub_element]]
            except KeyError as e:
                raise BroadworksOCIP_Xml_Tag()


    def return_sub_xml_tags(self,api_call):
        pass



