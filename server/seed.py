from server.app import app, db
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance

with app.app_context():
    db.drop_all()
    db.create_all()

    g1 = Guest(name="Tom Hanks", occupation="Actor")
    g2 = Guest(name="Bill Gates", occupation="Entrepreneur")

    e1 = Episode(date="2024-01-01", number=1)
    e2 = Episode(date="2024-01-02", number=2)

    a1 = Appearance(rating=4, guest=g1, episode=e1)
    a2 = Appearance(rating=5, guest=g2, episode=e1)

    db.session.add_all([g1, g2, e1, e2, a1, a2])
    db.session.commit()