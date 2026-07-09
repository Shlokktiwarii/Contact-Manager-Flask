from flask import Blueprint,render_template
from .extensions import db
from .models import Contact

bp = Blueprint("main", __name__)


@bp.get("/")
def home():
    contacts = Contact.query.order_by(Contact.name.asc()).all()
    return render_template("index2.html",contacts=contacts)

@bp.get("/contacts/new")
def new_contact():
    return render_template("new.html")

@bp.get("/dev/seed")
def dev_seed():
    c = [
         ("Stuti", "stuti@gmail.com" , "200-20-20000")
        ]
    for name ,email ,phone in c:
        db.session.add(Contact(name=name ,email=email ,phone=phone))
    db.session.commit()
    return f"Inserted contact id={c}"