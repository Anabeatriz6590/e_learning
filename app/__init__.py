from flask import Flask

def create_app():
    app = Flask(__name__)

    #Configurando a Aplicação
    app.config.from_object("config.Config")

    from app.routes import course_routes, user_routes
    app.register_blueprint(course_routes.bp)
    app.register_blueprint(user_routes.bp)

    return app
