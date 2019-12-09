import xml.etree.ElementTree as ET

class SystemRoutingGetResponse:
    def __init__(self, oci_response):
        self.xml = oci_response
        tree = ET.fromstring(oci_response)
        self.is_route_rr = None
        self.route_timer_seconds = None
        self.dns = None
        self.statefulexpiration = None
        self.maxaddresseshost = None
        self.maxaddressessetup = None

        try:
            self.is_route_rr = tree.find("command").find("isRouteRoundRobin").text
            self.route_timer_seconds = tree.find("command").find("routeTimerSeconds").text
            self.dns = tree.find("command").find("dnsResolvedAddressSelectionPolicy").text
            self.statefulexpiration = tree.find("command").find("statefulExpirationMinutes").text
            self.maxaddresseshost = tree.find("command").find("maxAddressesPerHostname").text
            self.maxaddressessetup = tree.find("command").find("maxAddressesDuringSetup").text
        except AttributeError:
            pass
    def __repr__(self):
        return self.xml

    def is_route_round_robin(self):
        if self.is_route_rr == "false":
            return False
        return True

    def get_route_timer_seconds(self):
        return self.route_timer_seconds

    def get_dns_policy(self):
        return self.dns

    def get_statefulexpiration(self):
        return self.statefulexpiration

    def get_maxaddresseshost(self):
        return self.maxaddresseshost

    def get_maxaddressessetup(self):
        return self.maxaddressessetup



class SystemSoftwareVersionGetResponse:

    def __init__(self, oci_response):
        self.xml = oci_response
        tree = ET.fromstring(oci_response)
        self.version = tree.find("command").find("version").text

    def get_version(self):
        return self.version


class SystemCodecGetListResponse:
    def __init__(self, oci_response):
        self.xml = oci_response
        tree = ET.fromstring(oci_response)
        self.codec = [codec.text for codec in tree.find("command").findall("codec")]

    def get_codec(self):
        return self.codec

