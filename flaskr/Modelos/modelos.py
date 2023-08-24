from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Cancion(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(128))
    minutos = db.Column(db.Integer)
    segundos = db.Column(db.Integer)
    interprete = db.Column(db.String(128))

    def __repr__(self):
        return "{}-{}-{}-{}".format(self.titulo, self.minutos, self.segundos, self.interprete)
class Medio(db.Model):
    disco = db.Column(db.String(128))
    casete = db.Column(db.String(128))
    cd = db.Column(db.String(128))

    def __repr__(self):
        return "{}-{}-{}".format(self.disco, self.casete, self.cd)
class Album(db.Model, Medio):
    tablename_ = db.Column(db.Stringer(128))
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.Stringer(128))
    year = db.Column(db.Integer)
    descripcion = db.Column(db.Stringer(128))
    medio = db.Column(db.Medio)

    def __repr__(self):
        return "{}-{}-{}-{}-{}".format(self.tablename_, self.titulo, self.year, self.descripcion, self.medio)

class Usuario(db.Model):
    tablename_u = db.Column(db.String(100))
    id = db.Column(db.Integer)
    nombre_usuario = db.Column(db.String)
    contraseña = db.Column(db.String)

    def __repr__(self):
        return "{}-{}".format(self.tablename_u, self.nombre_usuario)