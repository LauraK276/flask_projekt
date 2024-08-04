from flask import Flask

def create_app():
    app = Flask(__name__)

    # Konfiguracija aplikacije
    app.config['SECRET_KEY'] = 'your_secret_key_here'  # Obavezno promijenite ovo na stvarnu tajnu vrijednost

    # Registracija ruta
    from .routes import main
    app.register_blueprint(main)

    return app

