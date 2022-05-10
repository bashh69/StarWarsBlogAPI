from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Characters(db.Model):
            __tablename__= 'Characters'
            id = db.Column(db.Integer, primary_key=True)
            name = db.Column(db.String(120), unique=True, nullable=False)
            height = db.Column(db.String(120), unique=True, nullable=False)
            mass = db.Column(db.String(120), unique=True, nullable=False)
            hair_color = db.Column(db.String(120), unique=True, nullable=False)
            skin_color = db.Column(db.String(120), unique=True, nullable=False)
            eye_color = db.Column(db.String(120), unique=True, nullable=False)
            gender = db.Column(db.String(120), unique=True, nullable=False)

            def serialize(self):
                return{
                    "id": self.id,
                    "name": self.name,
                    "height": self.height,
                    "mass": self.mass,
                    "hair_color": self.hair_color,
                    "skin_color": self.skin_color,
                    "eye_color": self.eye_color,
                    "gender": self.gender,
                }
            
class Stars(db.Model):
            __tablename__= 'Stars'
            id = db.Column(db.Integer, primary_key=True)
            name = db.Column(db.String(120), unique=True, nullable=False)
            galaxy = db.Column(db.String(120), unique=True, nullable=False)
            mass = db.Column(db.String(120), unique=True, nullable=False)
            shine_color = db.Column(db.String(120), unique=True, nullable=False)
            distance_from_sun = db.Column(db.String(120), unique=True, nullable=False)
            
            def serialize(self):
                return{
                    "id": self.id,
                    "name": self.name,
                    "galaxy": self.galaxy,
                    "mass": self.mass,
                    "distance_from-sun": self.distance_from_sun,                    }

class Ships(db.Model):
            __tablename__ = "Ships"
            id = db.Column(db.Integer, primary_key=True)
            name = db.Column(db.String(120), unique=True, nullable=False)
            speed = db.Column(db.String(120), unique=False, nullable=False)
            weapons = db.Column(db.String(120), unique=False, nullable=False)
            def serialize(self):

                return{
                    "id": self.id,
                    "name": self.name,
                    "speed": self.speed,
                    "weapon": self.weapons,
                }

