import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
class Jsession:
    '''
        JSession Object:
            Object that handles j-session cookies
    '''

    def __init__(self,jsession_id):
        self._jsession_id = jsession_id

    def get_current_jsession_id(self):
        return self._jsession_id

    def update_jsession_id(self,jsession_id):
        self._jsession_id = jsession_id

