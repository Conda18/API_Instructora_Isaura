from flask_restful import Resource
from ..modelos.modelos import db, Cancion, CancionSchema
from flask import request

cancion_schema = CancionSchema()

from flask import request
from flask_restful import Resource
from ..modelos import db, Cancion, AlbumSchema

cancion_schema = AlbumSchema()

class VistaCanciones(Resource):
    def get(self):
        canciones = Cancion.query.all()
        return [cancion_schema.dump(cancion) for cancion in canciones]

    def post(self):
        nueva_cancion = Cancion(
            titulo=request.json['titulo'],
            minutos=request.json['minutos'],
            segundos=request.json['segundos'],
            interprete=request.json['interprete']
        )
        db.session.add(nueva_cancion)
        db.session.commit()
        return cancion_schema.dump(nueva_cancion), 201

    def delete(self, id_cancion):
        cancion = Cancion.query.get_or_404(id_cancion)
        db.session.delete(cancion)
        db.session.commit()
        return 'operacion exitosa', 204
