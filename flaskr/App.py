from flaskr import create_app
from flask_restful import Api
from .Vistas.vistas import VistaCanciones
from . import create_app


app = create_app('default')
api = Api(app)
api.add_resource(VistaCanciones, '/canciones')

if __name__ == '__main__':
    app.run()