from basic import db,puppy
db.create_all()
sam=puppy('sammy',3)
frank=puppy('frankie',4)
#none
#none
print(sam.id)
print(frank.id)
db.session.add_all([sam,frank])
db.session.commit()
print(sam.id)
print(frank.id)
