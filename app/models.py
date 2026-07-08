from app.extensions import db

class Contact(db.Model):
    __tablename__ = "contact"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(120),nullable = False)
    email = db.Column(db.String(120),nullable = False , unique =True)
    phone = db.Column(db.String(50),nullable = False , unique =True)

    def __repr__(self) -> str:
        return f"<Contact{self.id}{self.name}>"