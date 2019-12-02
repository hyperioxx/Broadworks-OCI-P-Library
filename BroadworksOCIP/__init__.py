import random
import BroadworksOCIP.broadworks.errors
from requests import Session
from zeep import Transport
from zeep import Client as _Client
from BroadworksOCIP.broadworks.schema.response import ResponseFactory
from BroadworksOCIP.broadworks.utils import Authentication
from BroadworksOCIP.broadworks.schema.base import BroadsoftDocument
from BroadworksOCIP.broadworks.schema.request.login import AuthenticationRequest, LoginRequest14sp4
from BroadworksOCIP.broadworks.schema.response.login import AuthenticationResponse, LoginResponse14sp4



class Client:

    def __init__(self, address=None, username=None, password=None):
        self.address = address + "?wsdl"
        self.username = username
        self.password = password
        self.protocol = "OCI"
        self.session = Session()
        self.client = _Client(self.address , transport=Transport(session=self.session))
        self.jsession = None
        self.bw_session = None
        self.log = None
        self.login_type = None

    def login(self):
        response = self.send(AuthenticationRequest(userId=self.username))
        signed_pass = Authentication.signed_password(self.password, response.get_nonce())
        response = self.send(LoginRequest14sp4(userId=self.username, signedpassword=signed_pass))
        self.login_type = response.get_login_type()



    def get_login_type(self):
        return self.login_type

    def get_bw_session(self):
        return self.bw_session

    def get_jsession(self):
        return self.session.cookies.get_dict()['JSESSIONID']

    def set_jsession(self, jsession):
        self.session.cookies.get_dict()['JSESSIONID'] = jsession

    def set_bw_session(self, bw_session):
        self.bw_session = bw_session

    def send(self, request):
        if not self.bw_session:
            self._generate_session()
        bw_doc = BroadsoftDocument(protocol=self.protocol, sessionId=self.bw_session)
        bw_doc.add_command(request)
        return ResponseFactory.main(self.client.service.processOCIMessage(bw_doc))


    def _generate_session(self):
        self.bw_session = str(random.randint(0000000000000, 9999999999999))






