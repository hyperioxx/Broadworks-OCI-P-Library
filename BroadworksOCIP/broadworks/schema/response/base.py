class Contact:
    def __init__(self, oci_response):
        self.xml = oci_response
        tree = ET.fromstring(oci_response)
        try:
            self.contact_name = tree.find("command").find("contactName")
            self.contact_number = tree.find("command").find("contactNumber")
            self.contact_email = tree.find("command").find("contactEmail")
        except AttributeError:
            pass #todo: lazy


    def get_contact_name(self):
        return self.contact_name

    def get_contact_number(self):
        return self.contact_number

    def get_contact_email(self):
        return self.contact_email


class StreetAddress:

    def __init__(self, oci_response):
        self.xml = oci_response
        tree = ET.fromstring(oci_response)
        try:
            self.address1 = tree.find("command").find("addressLine1")
            self.address2 = tree.find("command").find("addressLine2")
            self.city = tree.find("command").find("city")
            self.state_or_province = tree.find("command").find("city")
            self.state_or_province_dn = tree.find("command").find("stateOrProvinceDisplayName")
            self.zip_or_postcode = tree.find("command").find("zipOrPostalCode")
            self.country = tree.find("command").find("country")
        except AttributeError:
            pass #todo: lazy

