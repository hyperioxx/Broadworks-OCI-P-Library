import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import random

class SessionId:
    '''
      SessionId Object:
          An object which handles OCIP sessions

          methods:
              _generate_sessionid:
                  as the name states it generates a sessionid
    '''
    def __init__(self):
        self.current_session = None
        self.session_xml = '<sessionId xmlns="">{}</sessionId>'
        self._generate_sessionid()

    def _generate_sessionid(self):
        sessionID = random.randint(0,100000000000000)
        self.current_session = str(sessionID)

    def return_sessionid(self):
        return self.session_xml.format(self.current_session)
