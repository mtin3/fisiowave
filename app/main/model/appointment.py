from .. import db


class Appointment(db.Model):
    """ Appointment Model for storing appointments details """
    __tablename__ = "appointment"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    patient_id = db.Column(db.Integer, db.ForeignKey("patient.id"), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    clinic_id = db.Column(db.Integer, db.ForeignKey("clinic.id"))
    address = db.Column(db.String(255))
    price = db.Column(db.Float, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    invoice_id = db.Column(db.Integer, db.ForeignKey("invoice.id"))

    def __repr__(self):
        return "<Appointment '{}'>".format(self.id)
