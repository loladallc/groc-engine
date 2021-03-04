from data_models.entity.owner import Owner
from data_models.db import db_session
from werkzeug.security import generate_password_hash

class OwnerRegistration(object):

    def register_owner(self, new_owner_information):
        new_owner = Owner(
            email=new_owner_information["email"],
            phone=new_owner_information["phone"],
            username=new_owner_information["username"],
            password=generate_password_hash(new_owner_information["password"]),
            first_name=None if "first_name" not in new_owner_information else new_owner_information[
                "first_name"],
            last_name=None if "first_name" not in new_owner_information else new_owner_information[
                "first_name"],
        )
        db_session.add(new_owner)
        db_session.commit()
        db_session.close()

    def retreive_owner_details(self, username):
        existing_owner_details = Owner.query.filter_by(
            username=username).first().get_owner_details()
        return existing_owner_details

    def check_if_owner_registered(self, phone):
        owner = self.get_registered_user(phone)
        if owner is None:
            return False
        else:
            return True

    def get_registered_user(self, phone):
        return Owner.query.filter_by(phone=phone).first()
