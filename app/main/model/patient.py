from .. import db


class Patient(db.Model):
    """ Patient Model for storing patients details """
    __tablename__ = "patient"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    surname = db.Column(db.String(255), nullable=False)
    alias = db.Column(db.String(255))
    registered_on = db.Column(db.DateTime, nullable=False)
    email = db.Column(db.String(255))
    phone_number = db.Column(db.String(20))
    id_number = db.Column(db.String(50))
    address = db.Column(db.String(255))

    def __repr__(self):
        return "<Patient '{}'>".format(self.name)
