from .. import db


class Appointment(db.Model):
    """ Appointment Model for storing appointments details """
    __tablename__ = "appointment"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    patient_id = db.Column(db.Integer, db.ForeignKey("patient.id"), nullable=False)
    date = db.Column(db.Timestamp, nullable=False)
    clinic_id = db.Column(db.Integer, db.ForeignKey("clinic.id"))
    address = db.Column(db.String(255))
    registered_on = db.Column(db.DateTime, nullable=False)
    appointment_id = db.Column(db.Integer, db.ForeignKey('appointment.id'), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<Appointment '{}'>".format(self.id)
