from datetime import date
from project import db
from project.models import Task, User

db.create_all()

#db.session.add(User("admin", "ad@min.com", "admin", "admin"))
#db.session.add(Task("Finish this tutorial", date(2017, 10, 15), 10, date(2017, 8, 29), 1, 1))
#db.session.add(Task("Finish Real Python", date(2017, 11, 15), 10, date(2017, 8, 29),1, 1))
db.session.commit()

