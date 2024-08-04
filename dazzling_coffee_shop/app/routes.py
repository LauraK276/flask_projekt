from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/ponuda-dana')
def daily_offer():
    return render_template('daily_offer.html')

@main.route('/o-nama')
def about():
    return render_template('about.html')

@main.route('/meni')
def menu():
    return render_template('menu.html')

@main.route('/ostale-usluge')
def services():
    return render_template('services.html')

@main.route('/slike')
def gallery():
    return render_template('gallery.html')

@main.route('/rezervacija', methods=['GET', 'POST'])
def reservation():
    return render_template('reservation.html')

@main.route('/recenzije', methods=['GET', 'POST'])
def reviews():
    return render_template('reviews.html')
