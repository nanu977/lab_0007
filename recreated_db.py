# recreate_db.py
import os
from app import create_app, db

app = create_app()

with app.app_context():
    if os.path.exists('site.db'):
        os.remove('site.db')
    db.create_all()

