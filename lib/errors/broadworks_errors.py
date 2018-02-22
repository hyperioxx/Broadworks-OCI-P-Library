class BroadworksOCIP(Exception):
    def __init__(self):
        Exception.__init__(self, "the api call you specified does not exist")

class BroadworksOCIP_Xml_Tag(Exception):
    def __init__(self):
        Exception.__init__(self, "one of the xml tags specified does not exist for this api call")

class BroadworksOCIP_5404_Unauthorized_Transaction(Exception):
    def __init__(self):
        Exception.__init__(self, "[Error 5404] Unauthorized transaction.")

class BroadworksOCIP_4962_Invalid_Password(Exception):
    def __init__(self):
        Exception.__init__(self, "[Error 4962] Invalid password")

class BroadworksOCIP_5202_Account_Disabled(Exception):
    def __init__(self):
        Exception.__init__(self, "[Error 5202] Account is disabled.")