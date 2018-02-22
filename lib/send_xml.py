import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import urllib2
import xml.etree.ElementTree as ET
from lib.session import jsession
from lib.soap_responce import Soap_obj

#custom traceback errors for broadworks
from lib.errors.broadworks_errors import BroadworksOCIP_5404_Unauthorized_Transaction
from lib.errors.broadworks_errors import BroadworksOCIP_5202_Account_Disabled
from lib.errors.broadworks_errors import BroadworksOCIP_4962_Invalid_Password



class Send_xml():
    '''
       Send_xml object:
           A http connector which is a wrapper around urlib2
           methods:
               send():
                  send an OCIP request takes in 2 arguments (soap envelope,url)

               _map_to_soap_obj():
                   parses xml responce from an XSP(Extended Services Platform) Server and creates a python object
                   from the responce


    '''

    def __init__(self):
        self.headers = {
            'Content-Type': 'text/xml; charset=utf-8',
            'Accept': 'application/soap+xml, application/dime, multipart/related, text/*',
            'User-Agent': 'Axis/1.3',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            'SOAPAction': '',
            'Connection': '',
            'Accept-Encoding': ''}

        self._responce = None
        self.cookie = None

    def send(self, xml, url):
        try:
            req = urllib2.Request(url,data=xml,headers=self.headers)
            response = urllib2.urlopen(req)
            try:
                self.cookie = jsession.Jsession(response.info()["Set-Cookie"])
                self.headers["Cookie"] = self.cookie.get_current_jsession_id()
                return self._map_to_soap_obj(response.read())
            except KeyError:
                mes = self._map_to_soap_obj(response.read())
                try:
                    if mes['summary'] == "[Error 5404] Unauthorized transaction.":
                        raise BroadworksOCIP_5404_Unauthorized_Transaction()
                    elif mes['summary'] == "[Error 5202] Account is disabled.":
                        raise BroadworksOCIP_5202_Account_Disabled()
                    elif mes['summary'] == "[Error 4962] Invalid password":
                        raise BroadworksOCIP_4962_Invalid_Password()
                    else:
                        return mes
                except:
                     return mes

        except urllib2.HTTPError, error:
              err = self._map_to_soap_obj(error.read())



    def _map_to_soap_obj(self,responce):
        new_soap_reply = Soap_obj()
        tree = ET.fromstring(responce)
        responce_dict = {}
        for x in tree.iter():
            if x.tag == "{urn:com:broadsoft:webservice}processOCIMessageReturn":
                new_tree =  ET.fromstring(x.text)
                for i in new_tree.iter():
                    if i.tag == "command":
                        new_soap_reply.input_data({"responcecode":i.attrib['{http://www.w3.org/2001/XMLSchema-instance}type']})
                    else:
                        new_soap_reply.input_data({i.tag:i.text})
                        responce_dict[i.tag] = i.text

        return new_soap_reply.get_values()