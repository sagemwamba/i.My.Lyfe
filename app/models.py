from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Region(db.Model):
    __tablename__ = 'regions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.String(255), nullable=True)
    districts = db.relationship('District', backref='region', lazy=True)

    def __repr__(self):
        return f'<Region {self.name}>'

class District(db.Model):
    __tablename__ = 'districts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    region_id = db.Column(db.Integer, db.ForeignKey('regions.id'), nullable=False)
    description = db.Column(db.Text, nullable=True)
    cost_of_living = db.Column(db.Text, nullable=True)
    economic_activities = db.Column(db.Text, nullable=True)
    weather_conditions = db.Column(db.Text, nullable=True)
    image_url1 = db.Column(db.String(255), nullable=True)
    image_url2 = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f'<District {self.name}>'
