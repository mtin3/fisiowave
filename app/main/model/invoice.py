from .. import db


class Invoice(db.Model):
    """ Patient Model for storing patients details """
    __tablename__ = "invoice"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    invoice_number = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey("patient.id"))
    clinic_id = db.Column(db.Integer, db.ForeignKey("clinic.id"))
    appointments = db.relationship('Appointment', backref='appointment', lazy=True)
    subtotal = db.Column(db.Integer, nullable=False)
    VAT = db.Column(db.Decimal, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)


    def __repr__(self):
        return "<Invoice '{}'>".format(self.name)