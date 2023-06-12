
from datetime import datetime
from src import db
import uuid


class Product(db.Model):
    product_id = db.Column(db.Text, primary_key=True,default=lambda: str(uuid.uuid4()))
    product_name = db.Column(db.String(50), nullable=False)
    movements = db.relationship('ProductMovement', backref='product')

    def __repr__(self):
        return f"Product(`{self.product_name}`)"


class Location(db.Model):
    location_id = db.Column(db.Text, primary_key=True, default=lambda: str(uuid.uuid4()))
    location_name = db.Column(db.String(50), nullable=False)
    movements_from = db.relationship('ProductMovement', foreign_keys='ProductMovement.from_location_id', backref='from_location')
    movements_to = db.relationship('ProductMovement', foreign_keys='ProductMovement.to_location_id', backref='to_location')

    def __repr__(self):
        return f"Location(`{self.location_name}`)"


class ProductMovement(db.Model):
    movement_id = db.Column(db.Text, primary_key=True, default=lambda: str(uuid.uuid4()))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    from_location_id = db.Column(db.Text, db.ForeignKey('location.location_id'))
    to_location_id = db.Column(db.Text, db.ForeignKey('location.location_id'))
    qty = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Text, db.ForeignKey('product.product_id'), nullable=False)

    def __repr__(self):
        return f"Movement(`{self.timestamp}`, `{self.movement_id}`,`{self.qty}`)"
