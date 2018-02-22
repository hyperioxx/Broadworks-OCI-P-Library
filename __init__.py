from lib import send_xml, xml_builder
from lib.authentcation import Authentication

class Ocip_lib:
    '''
    Ocip_lib:

       ** A native python libirary to for Broadworks OCI-Provisioning API **
       methods:
           __login__():
                self defined dunder method in which provides the login function to the API

           _logedin_check():
                Checks if user is already logged into the OCIP




    '''
    def __init__(self,username,password,url):
        self.username = username
        self.password = password
        self.url = url
        self.is_loggedin = False
        self._builder_object = None
        self._send_obj = None


    def __login__(self):
        self._builder_object = xml_builder.Xml_builder()
        self._send_obj = send_xml.Send_xml()
        nonce = self._send_obj.send(self._builder_object._create_xml("AuthenticationRequest",userId=self.username),self.url)['nonce']

        self._send_obj.send(self._builder_object._create_xml("LoginRequest14sp4", userId=self.username,
                                                            signedPassword=Authentication.signed_password(self.password,nonce)), self.url)

    def _ocip_timeout(self):
        pass

    def _logedin_check(self):
        if self.is_loggedin == False:
            self.__login__()
            return
        else:
            return

    def send(self,api_call,**kwargs):
        self._logedin_check()
        return self._send_obj.send(self._builder_object._create_xml(api_call,**kwargs), self.url)

    def send_raw_xml(self,xml):
        self._logedin_check()
        return self._send_obj.send(xml,self.url)

    def supported_api_calls(self):
        pass

    def list_api_opts(self):
        pass





