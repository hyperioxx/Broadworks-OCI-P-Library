import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import cgi
import lib.session.session_id


from xml.etree.ElementTree import Element, SubElement, tostring
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
                                     "GroupGetListInServiceProviderRequest":{'serviceProviderId':None,"order":["serviceProviderId"]},
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
                                     "UserModifyRequest17sp4":{"userId":None,"timeZone":None,"language":None,"callingLineIdPhoneNumber":None,"order":["userId","timeZone","language","callingLineIdPhoneNumber"]},
                                     "UserCallRecordingModifyRequest":{"userId":None,"recordingOption":None,"order":["userId","recordingOption"]},
                                     "UserHotelingGuestModifyRequest":{"userId":None,"isActive":None,"enableAssociationLimit":None,
                                                                       "associationLimitHours":None,"order":["userId","isActive","enableAssociationLimit","associationLimitHours"]},
                                     "UserHotelingHostModifyRequest":{"userId":None,"isActive":None,
                                                                      "enforceAssociationLimit":None,
                                                                      "associationLimitHours":None,"accessLevel":None,
                                                                      "removeGuestAssociation":None,"order":["serviceProviderId","groupId"]},
                                     "UserIntegratedIMPModifyRequest":{"userId":None,"isActive":None,"order":["serviceProviderId","groupId"]},
                                     "UserGetListInGroupRequest":{"serviceProviderId":None,"GroupId":None,"order":["serviceProviderId","GroupId"]},
                                     "UserIntegratedIMPGeneratePasswordRequest":{"userId":None,"order":["serviceProviderId","groupId"]},
                                     "UserPortalPasscodeModifyRequest":{"userId":None,"newPasscode":None,"order":["userId","newPasscode"]},
                                     "SystemRoutingGetRequest":{"order":[]},
                                     "SystemSoftwareVersionGetRequest":{"order":[]},
                                     "SystemSIPGetContentTypeListRequest":{"order":[]},
                                     "SystemSIPDeviceTypeGetListRequest":{"order":[]},
                                     "SystemSIPDeviceTypeFileModifyRequest16sp1":{"deviceType":None,"fileFormat":None,
                                                                                  "fileCustomization":None,"fileUpload":{"sourceFileName":None,
                                                                                  "fileContent":None},"order":["deviceType","fileFormat","fileCustomization","fileUpload"]},
                                     "SystemCarrierGetListRequest":{"order":[]},
                                     "SystemSIPDeviceTypeFileGetListRequest14sp8":{"deviceType":None,"order":["deviceType"]},
                                     "SystemRoutingProfileGetListRequest":{"order":[]},
                                     "SystemRoutingGetTranslationListRequest":{"order":[]},
                                     "SystemRoutingGetRouteListRequest":{"order":[]},
                                     "SystemRoutingGetRouteDeviceListRequest":{"routeName":None,"order":["routeName"]},
                                     "SystemRedundancyParametersGetRequest16sp2":{"order":[]},
                                     "SystemPortalPasscodeRulesGetRequest19":{"order":[]},
                                     "SystemPortalAPIGetACLListRequest":{"order":[]},
                                     "SystemPolicyGetDefaultRequest20":{"order":[]},
                                     "SystemPasswordRulesGetRequest16":{"order":[]},
                                     "SystemNetworkSynchingServerGetListRequest":{"order":[]},
                                     "SystemSIPDeviceTypeFileGetRequest20":{"deviceType":None,"fileFormat":None,"order":["deviceType","fileFormat"]},
                                     "UserAuthenticationModifyRequest":{"userId":None,"newPassword":None,"order":["userId","newPassword"]},
                                     "UserCallForwardingNotReachableModifyRequest":{"userId":None,"isActive":None,"forwardToPhoneNumber":None,"order":["userId","isActive","forwardToPhoneNumber"]},
                                     "GroupModifyRequest":{"serviceProviderId":None,"groupId":None,
                                                           "defaultDomain":None,"userLimit":None,"groupName":None,
                                                           "callingLineIdName":None,"callingLineIdPhoneNumber":None,
                                                           "timeZone":None,"locationDialingCode":None,"contact":None,
                                                           "address":{},"order":["serviceProviderId","groupId","defaultDomain","userLimit","groupName","callingLineIdName","callingLineIdPhoneNumber","timeZone","locationDialingCode","contact","address"]},
                                     "GroupDnGetAvailableListRequest":{"serviceProviderId":None,"groupId":None,"order":["serviceProviderId","groupId"]},
                                     "GroupCallProcessingGetPolicyRequest19sp1":{"serviceProviderId":None,"groupId":None,"order":["serviceProviderId","groupId"]},
                                     "GroupCallProcessingModifyPolicyRequest15sp2":{"serviceProviderId":None,"groupId":None,"clidPolicy":None,"emergencyClidPolicy":None,"order":["serviceProviderId","groupId","clidPolicy","emergencyClidPolicy"]},
                                     "UserVoiceMessagingUserModifyVoicePortalRequest20":{"userId":None,"usePersonalizedName":None,"voicePortalAutoLogin":None,"personalizedNameAudioFile": None,"order":["userId","usePersonalizedName","voicePortalAutoLogin","personalizedNameAudioFile"]},
                                     "UserVoiceMessagingUserModifyAdvancedVoiceManagementRequest":{"userId":None,"groupMailServerEmailAddress":None,"groupMailServerUserId":None,"groupMailServerPassword":None,"order":["userId","groupMailServerEmailAddress","groupMailServerUserId"]},
                                     "UserVoiceMessagingUserGetAdvancedVoiceManagementRequest14sp3":{"userId":None,"order":['userId']}}


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
        xml_buffer = xml_buffer + self. _new_create_xml(api_call,**kwargs)
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
                if type(self._supported_api_calls[api_call][sub_element]).__name__ == "dict":
                    for sub_sub_element in options_dict:
                        self._supported_api_calls[api_call][sub_element][sub_sub_element] = options_dict[sub_sub_element]
                else:
                    self._supported_api_calls[api_call][sub_element] = options_dict[sub_element]
            except KeyError as e:
                raise BroadworksOCIP_Xml_Tag()


    def return_sub_xml_tags(self,api_call):
        pass


    def _new_create_xml(self,api_call,**kwargs):
        message = self._supported_api_calls
        top = Element('command', attrib={"xsi:type": api_call, "xmlns": ""})
        for y in message[api_call]["order"]:
                if type(message[api_call][y]).__name__ == "dict":
                    l = SubElement(top, y)
                    for i in message[api_call][y]:
                        t = SubElement(l, i)
                        for m in message[api_call][y]:
                            t.text = m
                else:
                    if message[api_call][y] != None:
                        l = SubElement(top, y)
                        l.text = message[api_call][y]
                    else:
                        pass
        return tostring(top)



