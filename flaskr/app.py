from flaskr import create_app
from .Modelos import db, cancion, usuario, album, medio


app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

with app.app_context():
    u = usuario(nombre_usuario='pepe', contraseña='12345')
    a = album(titulo='Tego-Calderon', year=2004, descripcion=' Para que lo goces ', Medio=medio.cd)
    c = cancion(tituo='mi cancion', minutos=1, segundos=15, interprete='Feid')
    u.albumes.apped(a)
    db.session.add(u)
    db.session.commit()
    print(usuario.query.all())
    print(usuario.query.all()[0].albumes)
    db.session.delete(u)
    print(usuario.query.all())
    print(album.query.all())
