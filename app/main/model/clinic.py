from .. import db


class Clinic(db.Model):
    """ Clinic Model for storing clinics details """
    __tablename__ = "clinic"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    phone_number = db.Column(db.String(20))
    id_number = db.Column(db.String(50))
    address = db.Column(db.String(255))

    def __repr__(self):
        return "<Clinic '{}'>".format(self.name)
