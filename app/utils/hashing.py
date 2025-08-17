from passlib.context import CryptContext

pwd_cxt=CryptContext(schemes=["bcrypt"], deprecated = "auto")


class Hash():
    def bcrypt(password: str):
        return pwd_cxt.hash(password)

    def verify(hash_pwd: str, user_pwd:str):
        return pwd_cxt.verify(hash_pwd,user_pwd)