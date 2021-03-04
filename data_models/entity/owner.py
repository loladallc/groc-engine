from sqlalchemy import Column, Integer, String, ForeignKey
from data_models.db import Base
from werkzeug.security import generate_password_hash, check_password_hash


class Owner(Base):
    __tablename__ = 'owner'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(80), nullable=False)
    last_name = Column(String(255), nullable=True)
    username = Column(String(80), nullable=False)
    email = Column(Integer, nullable=False)
    password = Column(String)
    phone = Column(String)
    prev_password = Column(String)
    store_id = Column(Integer, ForeignKey('store.id'))
    otp = Column(String)

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_location(self):
        return self.name

    def set_location(self, name):
        self.name = name

    def set_password(self, plain_text_password):
        self.password = generate_password_hash(plain_text_password)

    def check_password(self, plain_text_password):
        return check_password_hash(self.password, plain_text_password)
        
    def get_owner_details(self):
        owner_details = {"id": self.id,
                         "first_name": self.first_name,
                         "last_name": self.last_name,
                         "email": self.email,
                         "phone": self.phone}
        return owner_details
