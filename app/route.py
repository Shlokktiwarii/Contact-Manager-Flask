from flask import Blueprint,render_template,redirect, request , url_for
from .extensions import db
from .models import Contact

bp = Blueprint("main", __name__)


@bp.get("/")
def home():
    contacts = Contact.query.order_by(Contact.name.asc()).all()
    return render_template("index2.html",contacts=contacts)

@bp.route("/contacts/new", methods=["GET","POST"])
def new_contact():
    if request.method=="GET":
      return render_template("new.html")
    elif request.method=="POST":
        name = (request.form.get("name") or "").strip()
        email = (request.form.get("email") or "").strip().lower()
        phone = (request.form.get("phone") or "").strip() or None

        if not name or not email:
          return "Name and email are required",400
    
        c = Contact(name=name ,email=email, phone=phone)
        db.session.add(c)

        try:
          db.session.commit()
        except Exception:
          db.session.rollback()
          return "Email must be unique",400
        return redirect(url_for("main.home"))

@bp.get("/contacts/<int:contact_id>/edit")
def edit_contact(contact_id: int):
   contact = Contact.query.get_or_404(contact_id)

   return render_template("edit.html",contact=contact)

@bp.post("/contacts/<int:contact_id>/edit")
def update_contact(contact_id:int):
  contact = Contact.query.get_or_404(contact_id)
   
  contact.name = (request.form.get("name") or "").strip()
  contact.email = (request.form.get("email") or "").strip().lower()
  contact.phone = (request.form.get("phone") or "").strip() or None

  if not contact.name or not contact.email:
      return "Name and email are required",400

  try:
     db.session.commit()
  except Exception:
     db.session.rollback()
     return "Email must be unique",400
  return redirect(url_for("main.home"))

@bp.post("/contacts/<int:contact_id>/delete")
def delete_contact(contact_id:int):
  contact = Contact.query.get_or_404(contact_id)
  db.session.delete(contact)
  db.session.commit()
  return redirect(url_for('main.home'))  
   
   

@bp.get("/dev/seed")
def dev_seed():
    c = [
         ("Stuti", "stuti@gmail.com" , "200-20-20000")
        ]
    for name ,email ,phone in c:
        db.session.add(Contact(name=name ,email=email ,phone=phone))
    db.session.commit()
    return f"Inserted contact id={c}"