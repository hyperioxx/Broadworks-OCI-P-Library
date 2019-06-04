import hashlib

class Authentication:

    @staticmethod
    def signed_password(password, nonce):
        sha1_password = hashlib.sha1(password.encode("ascii")).hexdigest()
        signed_pass = hashlib.md5()
        signed_pass.update("{}:{}".format(nonce, sha1_password).encode("ascii"))
        return signed_pass.hexdigest()


