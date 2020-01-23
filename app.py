# import
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# instantiate
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/flask_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# model class
class TestTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    string_field = db.Column(db.String(80))
    string_field_2 = db.Column(db.String(80))

if __name__ == '__main__':
    app.run(debug=True)