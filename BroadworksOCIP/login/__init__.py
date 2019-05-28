import io
from BroadworksOCIP.utils.broadworks.schema.OCISchemaAS import \
    AuthenticationRequest as AuthReq
from BroadworksOCIP.utils.broadworks.schema.OCISchemaAS import BroadsoftDocument


class AuthenticationRequest:

    def __init__(self, userId):
        self.userId = userId
        self.broadsoft_doc = BroadsoftDocument()
        self.command = AuthReq()
        self.broadsoft_doc.protocol = "OCI"
        self.command.userId = self.userId
        self.broadsoft_doc.add_command(self.command)
        self.inmemfile = io.StringIO()



    def get_raw_xml(self):
        self.broadsoft_doc.export(self.inmemfile,0)
        print(self.inmemfile.getvalue())



    def get_bw_session(self):
        pass







