from flaskr import create_app
from .Modelos import db, Cancion, Album

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

with app.app_context():
    c = Cancion(titulo='prueba ', minutos=2, segundos=25, interprete=' Marlon ')
    db.session.add(c)
    db.session.commit()
    print(Cancion.query.all())

with app.app_context():
    a = Album(tablename='Snoop-Dog', titulo='MI Cancion', year=2004, descripcion=' Para que lo goces ', Medio='medio')
    db.session.add(a)
    db.session.commit()
    print(Album.query.all())


