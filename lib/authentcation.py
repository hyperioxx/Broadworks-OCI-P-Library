import hashlib

class Authentication:

    @staticmethod
    def signed_password(password,nonce):
        sha1_password = hashlib.sha1(password).hexdigest()
        spw = hashlib.md5()
        spw.update("%s:%s" % (nonce, sha1_password))
        return spw.hexdigest()



