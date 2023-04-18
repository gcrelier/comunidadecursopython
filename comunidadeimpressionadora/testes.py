from main import app
from comunidadeimpressionadora import database
from comunidadeimpressionadora.models import Usuario

# with app.app_context():
#     database.create_all()

# with app.app_context():
#     usuario = Usuario(username="Lira", email="gscrelier@gmail.com",senha="123456")
#     usuario2 = Usuario(username="Joao", email="piece_br@yahoo.com.br",senha="123456")
#     database.session.add(usuario)
#     database.session.add(usuario2)
#     database.session.commit()
#
with app.app_context():
    meus_usuarios = Usuario.query.all()
    print(meus_usuarios)
    usuario_teste = Usuario.query.filter_by(id=4).first()
    print(usuario_teste)
    print(usuario_teste.email)
#
# # with app.app_context():
# #     meu_post = Post(id_usuario=1, titulo="Primeiro post do lira", corpo="lira voando")
# #     database.session.add(meu_post)
# #     database.session.commit()
#
# # with app.app_context():
# #     post = Post.query.first()
# #     print(post)
# #     print(post.autor.email)
#
# with app.app_context():
#     database.drop_all()
