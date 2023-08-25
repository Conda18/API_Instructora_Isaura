from flask_sqlalchemy import SQLAlchemy
import enum


db = SQLAlchemy()

class cancion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128))
    minutos = db.Column(db.Integer)
    segundos = db.Column(db.Integer)
    interprete = db.Column(db.String(128))
    #albumes = db.relationship('Album', secondary='album_cancion', back_populates='canciones')

class medio(enum.Enum):
        disco = 1
        casete = 2
        cd = 3

class usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128))
    constrasena = db.Column(db.String(128))
    albumes = db.relationship('album', cascade='all, delete, delete-orphan')
class album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128))
    anio = db.Column(db.Integer)
    descripcion = db.Column(db.String(512))
    medio = db.Column(db.Enum(medio))
    usuario = db.Column(db.Integer, db.Foreignkey("usuario.id"))
    __table__args__ = (db.UniqueConstraint('usuario', 'titulo', name='titulo_unico_almbum'),)
    #canciones = db.relationship('cancion', secondary='album_cancion', back_pupolates='albumes')
    #__table__args__ = (db.UniqueConstraint('usuario', 'titulo', name='titulo_unico_almbum'),)


#albumes_canciones =  db.Table('album_cancion',\
 #   db.Column('album_id', db.Integer, db.ForeignKey('album.id'), primary_key=True),\
  #  db.Column('cancion_id', db.Integer, db.ForeignKey('cancion.id'), primary_key=True))

