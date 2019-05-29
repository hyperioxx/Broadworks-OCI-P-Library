import io
import random
from BroadworksOCIP.utils.broadworks.schema.OCISchemaAS import AuthenticationRequest as AuthReq
from BroadworksOCIP.utils.broadworks.schema.OCISchemaAS import BroadsoftDocument


class AuthenticationRequest:

    def __init__(self, userId):
        self.userId = userId
        self.broadsoft_doc = BroadsoftDocument()
        self.command = AuthReq()
        self.command.original_tagname_ = "command"
        self.broadsoft_doc.protocol = "OCI"
        self.broadsoft_doc.sessionId = AuthenticationRequest._generate_session_id()
        self.command.userId = self.userId
        self.broadsoft_doc.add_command_with_type(self.command)
        self.inmemfile = io.StringIO()

    def __repr__(self):
        self.broadsoft_doc.export(self.inmemfile, 0)
        return str(self.inmemfile.getvalue())

    def __str__(self):
        self.broadsoft_doc.export(self.inmemfile, 0)
        return str(self.inmemfile.getvalue())

    @staticmethod
    def _generate_session_id():
        return random.randint(10000000,99999999)








