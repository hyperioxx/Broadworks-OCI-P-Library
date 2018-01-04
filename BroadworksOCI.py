import sys
import os
import re
import hashlib 
import HTMLParser
import httplib2
import random
import cgi
from lxml import etree 
import xml.etree.ElementTree as ET
import time 

class Broadworks_OCI:
    def __init__(self,userId,password,url):
 
        self.serviceProviderId = ''
        self.userId = userId
        self.sessionId = ''
        self.password = password
        self.signedPassword = ''
        self.body = ''
        self.header= ''
        self.cookie = ''
        self.serviceProvider = ''
        self.current_session = ''
        self.group = ''
        self.bwuserId = ''
        self.activeSession = False
        self.responce = ''
        self.url  = url
        self.xml_header = """<?xml version="1.0" encoding="UTF-8"?> \
                       <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" >\
                       <soapenv:Body>\
                       <processOCIMessage soapenv:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">\
                       <arg0 xsi:type="soapenc:string" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/">"""

        self.xml = '<BroadsoftDocument protocol="OCI" xmlns="C" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'

        self.xml_footer = """</arg0>\
                        </processOCIMessage>\
                        </soapenv:Body>\
                        </soapenv:Envelope>"""

    def OCI(self,msgType,sessionID='',signedPassword=0,cookie=0,serviceProvider='Null',group='Null',bwuserId='Null'):
        self.serviceProvider = serviceProvider
        self.group = group
        self.bwuserId = bwuserId
        if signedPassword != 0:
            requestType = self.messageType(msgType,signedPassword)
        else:
            requestType = self.messageType(msgType)
        if cookie == 1:
            self.activeSession = True
        xml = self.xml + '<sessionId xmlns="">'+sessionID+'</sessionId>'
        xml =  xml + '<command xsi:type="%s" xmlns="">'% requestType['Name']
        for key,value in requestType['Elements'].iteritems(): 
             xml =  xml + "<%s>%s</%s>" %(key, value, key)
        xml =  xml + '</command>'
        xml = xml + '</BroadsoftDocument>'
        xml = cgi.escape(xml, quote=False)
        xml = xml.replace("&amp;","&amp;amp;")
        xml = self.xml_header + xml + self.xml_footer
        xml = xml.replace("\n","")
        responce = self.send(xml,self.url)
        #Check for nonce for authentication
        nonce = self.checkAuthenticate(responce)
        if nonce == 'No':
            return responce
        else:
            if self.header['set-cookie']:
                self.cookie = self.header['set-cookie']
                return responce, nonce
            else:
                return responce, nonce
        
        

    def messageType(self,msgType,signedPassword=0):
        if msgType == 'auth':
           return self.authRequest()
        if msgType == 'SP_servicepacks':
           return self.SP_servicePacks()
        if msgType == 'loginRequest':
           return self.loginRequest(signedPassword)
        if msgType == 'Get_all_SP':
           return self.Get_all_SPs()
        if msgType == 'Get_Groups':
           return self.Get_Group()
        if msgType == 'Get_User':
           return self.Get_User()
        if msgType == 'Get_user_services':
            return self.User_Services()
        if msgType == 'Get_Group_services':
            return self.Group_Services()
        if msgType == 'user_pass':
            return self.Get_user_pass()
        if msgType == 'HuntGroup':
            return self.return_Hunt_groups()
        if msgType == 'CallCenter':
            return self.return_Call_Center()
        if msgType == 'CallPickup':
            return self.return_CallPickup()
        if msgType == 'AutoAttendant':
            return  self.return_Auto_Attendant()
        if msgType == 'RoutePoint':
            return self.return_routePoint()
        if msgType == 'TrunkGroup':
            return self.return_trunkGroup()
        if msgType == 'FlexibleSeatingHost':
            return self.return_flexHost()
        if msgType == 'VoiceXML':
            return self.return_voiceXML()
        if msgType == 'GroupPage':
            return self.return_GroupPage()
        if msgType == 'MeetMe':
            return self.return_MeetMe()
        if msgType == 'GroupDN':
            return self.return_GroupDN()
        if msgType == 'bw-anywhere':
            return self.return_bwAnywhere()
        if msgType == 'get_user_detail':
            return self.Get_user_Detail()
        if msgType == 'Logout':
            return self.Logout()
        else:
           sys.exit()
           
        
    def checkAuthenticate(self,responce):
        nonce = re.search("<nonce>(.*?)</nonce>", responce)
        if nonce:
            paswd = self.Login(nonce.group(1))
            return paswd
        else:
           return 'No'
       

    def Login(self,nonce):
            pw = hashlib.sha1()
            pw.update(self.password)
            sha1pw = pw.hexdigest()
            spw = hashlib.md5()
            spw.update("%s:%s" % (nonce, sha1pw))
            return spw.hexdigest()
            
      
    def getHeaders(self):
        headers = {
            'Content-Type': 'text/xml; charset=utf-8',
            'Accept': 'application/soap+xml, application/dime, multipart/related, text/*',
            'User-Agent': 'Axis/1.3',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            'SOAPAction': '',
            'Connection': '',
            'Accept-Encoding': '',}
        try:
            if self.activeSession == True:
                headers['Cookie'] = self.cookie
            if self.header and self.header['set-cookie']:
                self.cookie = self.header['set-cookie']
                headers['Cookie'] = self.cookie
            return headers
        except KeyError:
            return headers
        

    def send(self,xml,url):
        http_agent = httplib2.Http(cache=None, timeout=20, disable_ssl_certificate_validation=True)
        Headers = self.getHeaders()
        try:
          self.header, self.body = http_agent.request(url, method="POST", body=xml, headers=self.getHeaders())
        except Exception as e:
             self.header,self.body = http_agent.request(url, method="POST", body=xml, headers=self.getHeaders())
             print  e ,xml 
             print "Retry"
        if self.header['status'] == '200':
            pass   
        else:   
            print self.header
            print xml
            print self.body
        return HTMLParser.HTMLParser().unescape(self.body)

    #> template {'Name':'','Elements':{}}
    def authRequest(self):
        return {'Name': 'AuthenticationRequest','Elements': {'userId': self.userId}}

    #TESTING METHOD 
    def SP_servicePacks(self):
        return {'Name':'ServiceProviderServicePackGetListRequest','Elements':{'serviceProviderId':self.serviceProvider}}

    def loginRequest(self,signedPassword=''):
        return {'Name': 'LoginRequest14sp4','Elements': {'userId': self.userId,'signedPassword': signedPassword}}

    def Get_all_SPs(self):
       return {'Name':'ServiceProviderGetListRequest','Elements':{}}#<<< DON'T EDIT 

    def Get_Group(self):
        return {'Name':'GroupGetListInServiceProviderRequest','Elements':{'serviceProviderId':self.serviceProvider}}

    def Get_User(self):
        return {'Name':'UserGetListInGroupRequest','Elements':{ 'serviceProviderId': self.serviceProvider ,'GroupId':self.group}}

    def User_Services(self):
        return {'Name':'UserServiceGetAssignmentListRequest','Elements':{'userId':self.bwuserId}}

    def Group_Services(self):
        return {'Name':'GroupServiceGetAuthorizationListRequest','Elements':{'serviceProviderId':self.serviceProvider,'groupId':self.group}}

    def Get_user_pass(self):
        return {'Name':'UserPasswordInfoGetRequest','Elements':{'userId':self.bwuserId}}

    def return_Auto_Attendant(self):
        return {'Name':'GroupAutoAttendantGetInstanceListRequest','Elements':{'serviceProviderId':self.serviceProvider,'groupId':self.group}}
 
    def return_Hunt_groups(self):
        return {'Name':'GroupHuntGroupGetInstanceListRequest','Elements':{'serviceProviderId':self.serviceProvider,'groupId':self.group}}

    def return_Call_Center(self):
        return {'Name':'GroupCallCenterGetInstanceListRequest','Elements':{'serviceProviderId':self.serviceProvider,'groupId':self.group}}

    def return_routePoint(self):
        return {'Name':'GroupRoutePointGetInstanceListRequest','Elements':{'serviceProviderId':self.serviceProvider,'groupId':self.group}}

    def return_trunkGroup(self):
        return {'Name':'GroupTrunkGroupGetInstanceListRequest14','Elements':{'serviceProviderId':self.serviceProvider,'groupId':self.group}}

    def return_flexHost(self):
        return {'Name':'GroupFlexibleSeatingHostGetInstanceListRequest','Elements':{'serviceProviderId':self.serviceProvider,'groupId':self.group}}

    def return_voiceXML(self):
        return {'Name':'GroupVoiceXmlGetInstanceListRequest','Elements':{'serviceProviderId':self.serviceProvider,'groupId':self.group}}
  
    def return_GroupPage(self):
        return {'Name':'GroupGroupPagingGetInstanceListRequest','Elements':{'serviceProviderId':self.serviceProvider,'groupId':self.group}}
   
    def return_MeetMe(self):
        return {'Name':'GroupMeetMeConferencingGetInstanceListRequest','Elements':{'serviceProviderId':self.serviceProvider,'groupId':self.group}}
    
    def return_CallPickup(self):
        return {'Name':'GroupCallPickupGetInstanceListRequest','Elements':{'serviceProviderId':self.serviceProvider,'groupId':self.group}}

    def return_bwAnywhere(self):
        return {'Name':'GroupBroadWorksAnywhereGetInstanceListRequest','Elements':{'serviceProviderId':self.serviceProvider,'groupId':self.group}}
 
    def return_GroupDN(self):
        return {'Name':'GroupDnGetListRequest','Elements':{'serviceProviderId':self.serviceProvider,'groupId':self.group}}

    def Get_user_Detail(self):
        return {'Name':'UserGetRequest20','Elements':{'userId':self.bwuserId}}

    def Logout(self):
        return {'Name':'LogoutRequest','Elements':{'userId':self.userId,'reason':'Client Logout'}}
       

    def Get_SP_ServicePacks(self,active_sessionID = ''):
         sessionID = self.current_session
         servicePack = []
         service_packs = self.OCI('SP_servicepacks',sessionID=sessionID,cookie=1)
         matches  = re.findall('<servicePackName>(.*?)</servicePackName>', service_packs, re.DOTALL)
         tmplist = []
         for i in matches:
           group_service =  re.findall('<col>(.*?)</col>', i, re.DOTALL)
           tmplist.append(group_service)
         return service_packs


    def Get_Group_ServicePacks(self,SP,group):
         sessionID = self.current_session
         servicePack = []
         service_packs = self.OCI('Get_Group_services',sessionID=sessionID,cookie=1,serviceProvider=SP,group=group)
         groupTable = re.findall('<groupServicesAuthorizationTable>(.*?)</groupServicesAuthorizationTable>', service_packs, re.DOTALL)
         matches = re.findall('<row>(.*?)</row>',groupTable[0], re.DOTALL)
         tmplist = []
         for i in matches:
           group_service = re.findall('<col>(.*?)</col>', i, re.DOTALL)
           tmplist.append(group_service)
         return tmplist

    def Get_all_SP(self):
        sessionID = self.current_session
        allServiceproviders = self.OCI('Get_all_SP',sessionID=sessionID,cookie=1)
        allServiceproviders = allServiceproviders.replace('&amp;','&')
        match = []
        matches =re.findall('<row>(.*?)</row>', allServiceproviders, re.DOTALL)
        for i in matches:
            strip = re.findall('<col>(.*?)</col>', i, re.DOTALL)
            match.append(strip)
        return match


    def Get_Groups(self,SP):
        sessionID = self.current_session
        groups = self.OCI('Get_Groups',sessionID=sessionID,cookie=1,serviceProvider=SP)
        groups = groups.replace('&amp;','&')
        matches = re.findall('<row>(.*?)</row>', groups, re.DOTALL)
        tmplist = []
        for i in matches:
              group = re.findall('<col>(.*?)</col>', i, re.DOTALL)
              tmplist.append(group[0])
        return tmplist

    def Get_Users(self,SP,group):
        sessionID = self.current_session
        users = self.OCI('Get_User',sessionID=sessionID,cookie=1,serviceProvider=SP,group=group)
        matches = re.findall('<row>(.*?)</row>', users, re.DOTALL)
        tmplist = []
        for i in matches:
           user = re.findall('<col>(.*?)</col>', i, re.DOTALL)
           tmplist.append(user[0])
        return tmplist

    def Get_User_Services(self,bwuserId,active_sessionID = ''):
        sessionID = self.current_session
        userService = self.OCI('Get_user_services',sessionID=sessionID,cookie=1,bwuserId=bwuserId)
        matches = re.findall('<col>(.*?)</col>', userService, re.DOTALL)
        services = []
        services_true = []
        for i in range(0, len(matches), 2):
          services.append(matches[i:i + 2])
        for x in services:
            if 'false' in x:
                pass
            if 'true' in x:
              services_true.append(x[0])#< remove element to return true or false 
        return services_true 

    def Get_User_Pass(self,bwuserId):
        sessionID = self.current_session
        userPass = self.OCI('user_pass',sessionID=sessionID,cookie=1,bwuserId=bwuserId)
        print userPass
    
    def GroupAutoAttendantGetInstanceListRequest(self,SP,group):
        sessionID = self.current_session
        AutoAttendant = self.OCI('AutoAttendant',sessionID=sessionID,cookie=1,serviceProvider=SP,group=group)
        AutoAttendant =  AutoAttendant.replace('&amp;','&')
        matches = re.findall('<row>(.*?)</row>', AutoAttendant, re.DOTALL)
        tmplist = []
        for i in matches:
              group = re.findall('<col>(.*?)</col>', i, re.DOTALL)
              tmplist.append(group)
        return tmplist


    def GroupHuntGroupGetInstanceListRequest(self,SP,group):
        sessionID = self.current_session
        HuntGroups = self.OCI('HuntGroup',sessionID=sessionID,cookie=1,serviceProvider=SP,group=group)
        HuntGroups =  HuntGroups.replace('&amp;','&')
        matches = re.findall('<row>(.*?)</row>', HuntGroups, re.DOTALL)
        tmplist = []
        for i in matches:
              group = re.findall('<col>(.*?)</col>', i, re.DOTALL)
              tmplist.append(group[0])
        return tmplist


    def GroupCallCenterGetInstanceListRequest(self,SP,group):
        sessionID = self.current_session
        CallCenters = self.OCI('CallCenter',sessionID=sessionID,cookie=1,serviceProvider=SP,group=group)
        CallCenters =  CallCenters.replace('&amp;','&')
        matches = re.findall('<row>(.*?)</row>', CallCenters, re.DOTALL)
        tmplist = []
        for i in matches:
              element = re.findall('<col>(.*?)</col>', i, re.DOTALL)
              tmplist.append(element)
        return tmplist
 
    def GroupRoutePointGetInstanceListRequest(self,SP,group):
        sessionID = self.current_session
        RoutePoint = self.OCI('RoutePoint',sessionID=sessionID,cookie=1,serviceProvider=SP,group=group)
        RoutePoint =  RoutePoint.replace('&amp;','&')
        matches = re.findall('<row>(.*?)</row>', RoutePoint, re.DOTALL)
        tmplist = []
        for i in matches:
              element = re.findall('<col>(.*?)</col>', i, re.DOTALL)
              tmplist.append(element[0])
        return tmplist


    def GroupTrunkGroupGetInstanceListRequest(self,SP,group):
        sessionID = self.current_session
        HuntGroups = self.OCI('TrunkGroup',sessionID=sessionID,cookie=1,serviceProvider=SP,group=group)
        HuntGroups = HuntGroups.replace('&amp;','&')
        matches = re.findall('<command echo="" xsi:type="GroupTrunkGroupGetInstanceListResponse14" xmlns="">(.*?)</command>', HuntGroups, re.DOTALL)
        tmplist1 = [] 
        try:
           tree = etree.fromstring(matches[0])
           No_of_elements = 6
           iterations = 0
           tmplist1 = []
           tmplist = []
           for i in tree.iter('col'):
               tmplist.append(i.text)
           lol2 = len(tmplist)
           for i in range(0,lol2,No_of_elements):
                 tmplist1.append(tmplist[i:i+No_of_elements])
        except:
            return tmplist1
        return tmplist1

    
    def GroupFlexibleSeatingHostGetInstanceListRequest(self,SP,group):
        sessionID = self.current_session
        FlexibleSeatingHost = self.OCI('FlexibleSeatingHost',sessionID=sessionID,cookie=1,serviceProvider=SP,group=group)
        FlexibleSeatingHost = FlexibleSeatingHost.replace('&amp;','&')
        matches = re.findall('<row>(.*?)</row>', FlexibleSeatingHost, re.DOTALL)
        tmplist = []
        for i in matches:
              group = re.findall('<col>(.*?)</col>', i, re.DOTALL)
              tmplist.append(group)
        return tmplist
 
    def GroupVoiceXmlGetInstanceListRequest(self,SP,group):
        sessionID = self.current_session
        VoiceXML = self.OCI('VoiceXML',sessionID=sessionID,cookie=1,serviceProvider=SP,group=group)
        VoiceXML = VoiceXML.replace('&amp;','&')
        matches = re.findall('<row>(.*?)</row>', VoiceXML, re.DOTALL)
        tmplist = []
        for i in matches:
              group = re.findall('<col>(.*?)</col>', i, re.DOTALL)
              tmplist.append(group)
        return tmplist


    def GroupGroupPagingGetInstanceListRequest(self,SP,group):
        sessionID = self.current_session
        GroupPage = self.OCI('GroupPage',sessionID=sessionID,cookie=1,serviceProvider=SP,group=group)
        GroupPage = GroupPage.replace('&amp;','&')
        matches = re.findall('<row>(.*?)</row>', GroupPage, re.DOTALL)
        tmplist = []
        for i in matches:
              group = re.findall('<col>(.*?)</col>', i, re.DOTALL)
              tmplist.append(group)
        return tmplist

    def GroupMeetMeConferencingGetInstanceListRequest(self,SP,group):
        sessionID = self.current_session
        MeetMe = self.OCI('MeetMe',sessionID=sessionID,cookie=1,serviceProvider=SP,group=group)
        MeetMe = MeetMe.replace('&amp;','&')
        matches = re.findall('<row>(.*?)</row>', MeetMe, re.DOTALL)
        tmplist = []
        for i in matches:
              group = re.findall('<col>(.*?)</col>', i, re.DOTALL)
              tmplist.append(group)
        return tmplist

    #FOR ADRIAN
    def GroupHuntGroupGetInstanceRequest20():
        sessionID = self.current_session
        huntGroupInfo = self.OCI('huntGroupInfo',sessionID=sessionID,cookie=1,bwuserId=bwuserId)
        matches = re.findall('<col>(.*?)</col>',huntGroupInfo,re.DOTALL)
        print matches 

     
    def GroupCallPickupGetInstanceListRequest(self,SP,group):
        sessionID = self.current_session
        CallPickup = self.OCI('CallPickup',sessionID=sessionID,cookie=1,serviceProvider=SP,group=group)
        CallPickup = CallPickup.replace('&amp;','&')
        matches = re.findall('<name>(.*?)</name>', CallPickup, re.DOTALL)
        return matches


    def GroupBroadWorksAnywhereGetInstanceListRequest(self,SP,group):
        sessionID = self.current_session
        BWanywhere = self.OCI('bw-anywhere',sessionID=sessionID,cookie=1,serviceProvider=SP,group=group)
        BWanywhere = BWanywhere.replace('&amp;','&')
        matches = re.findall('<col>(.*?)</col>', BWanywhere, re.DOTALL)
        return matches


    def GroupDnGetListRequest(self,SP,group):
        sessionID = self.current_session
        GroupDN = self.OCI('GroupDN',sessionID=sessionID,cookie=1,serviceProvider=SP,group=group)
        matches = re.findall('<phoneNumber>(.*?)</phoneNumber>', GroupDN, re.DOTALL)
        return matches
     
    def _login(self):
        sessionID = sessionId.sessionId()
        responce ,signedPassword = self.OCI('auth',sessionID=sessionID)
        self.OCI('loginRequest',sessionID=sessionID,signedPassword=signedPassword)
        self.current_session = sessionID
 
    def logout(self):
        sessionID = self.current_session
        RoutePoint = self.OCI('Logout',sessionID=sessionID,cookie=1)
        
        
class sessionId:
     @staticmethod
     def sessionId():
        sessionID = random.randint(0,100000000000000)
        return str(sessionID)



   
