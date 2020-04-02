import random
import socket 
import BroadworksOCIP.broadworks.errors
from requests import Session
from zeep import Transport
from zeep import Client as _Client
from BroadworksOCIP.broadworks.schema.response import ResponseFactory
from BroadworksOCIP.broadworks.utils import Authentication
from BroadworksOCIP.broadworks.schema.base import BroadsoftDocument
from BroadworksOCIP.broadworks.schema.request.login import AuthenticationRequest, LoginRequest14sp4, LoginRequest22v3
from BroadworksOCIP.broadworks.schema.response.login import AuthenticationResponse, LoginResponse14sp4, LoginResponse22v3

class _Client:

    def login(self):
        if self.isRelease22 == False:
            response = self.send(AuthenticationRequest(userId=self.username))
            signed_pass = Authentication.signed_password(
                self.password, response.get_nonce())
            response = self.send(LoginRequest14sp4(
                userId=self.username, signedpassword=signed_pass))
            self.login_type = response.get_login_type()
            try:
                self.groupid = response.groupid
                self.serviceproviderid = response.serviceproviderid
            except:
                pass
        elif self.isRelease22 == True:
            response = self.send(LoginRequest22v3(
                userId=self.username, password=self.password))
        else:
            raise IndexError

        



class Client(_Client):

    # Added isRelease22 parameter to change the login request function format
    def __init__(self, address=None, username=None, password=None, jsession=None, bwsession=None, isRelease22=False):
        self.address = address + "?wsdl"
        self.username = username
        self.password = password
        self.protocol = "OCI"
        self.jsession = jsession
        self.bw_session = bwsession
        self.session = Session()
        if jsession:
            self.session.cookies['JSESSIONID'] = jsession
        self.client = _Client(
            self.address, transport=Transport(session=self.session))
        self.log = None
        self.login_type = None
        self.isRelease22 = isRelease22

    # Change login function to accept both loginRequest14sp4 and LoginRequest22v3
    
        
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
        bw_doc = BroadsoftDocument(
            protocol=self.protocol, sessionId=self.bw_session)
        bw_doc.add_command(request)
        return ResponseFactory.main(self.client.service.processOCIMessage(bw_doc))

    def _generate_session(self):
        self.bw_session = str(random.randint(0000000000000, 9999999999999))




class TCPClient(_Client):
    def __init__(self, address=None, port=None, username=None, password=None, bwsession=None, isRelease22=False):
        self.address = address 
        self.username = username
        self.password = password    
        self.protocol = "OCI"
        self.bw_session = bwsession
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((address, int(port)))
        self.log = None
        self.login_type = None
        self.isRelease22 = isRelease22
        
    def send(self, message):
        if not self.bw_session:
            self._generate_session()
        bw_doc = BroadsoftDocument(protocol=self.protocol, sessionId=self.bw_session)
        bw_doc.add_command(message)
        msg = bw_doc._export().decode()
        msg = """<?xml version="1.0" encoding="ISO-8859-1"?>""" + msg + "\n" 
        self.client.send(msg.encode())

        return ResponseFactory.main(self.client.recv(2000).decode())


    def _generate_session(self):
        self.bw_session = str(random.randint(0000000000000, 9999999999999))








