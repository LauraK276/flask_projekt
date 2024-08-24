# Dazzling Coffee & Cake Shop Web Application

## Opis Aplikacije

Dazzling Coffee & Cake Shop je web aplikacija osmišljena za kafić specijaliziran za domaće kolače i kavu. Aplikacija omogućuje korisnicima pregled ponude, rezervaciju stolova, pregled dnevnih ponuda te uvid u galeriju slika.


## Tehnička Specifikacija

### Tehnologije
- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, Bootstrap
- **Baza Podataka**: SQLite
- **Form Validation**: Flask-WTF


### Funkcionalnosti
1. **Početna stranica**: Pregled osnovnih informacija o kafiću i galerije slika.
2. **O Nama**: Informacije o povijesti i misiji kafića.
3. **Meni**: Detaljan pregled ponude toplih i hladnih napitaka, kolača i dnevnih ponuda.
4. **Rezervacije**: Korisnici mogu napraviti rezervaciju stola putem forme koja validira podatke.
5. **Galerija**: Prikaz slika interijera, napitaka i kolača.
6. **Contact**: Mogućnost ostavljanja poruke preko web stranice i pregled kontakt informacija







### Instalacija

Da biste postavili aplikaciju na lokalnom sustavu, slijedite ove korake:

1. Klonirajte repozitorij:
   ```bash
   git clone <URL_REPOZITORIJA>
   cd dazzling_coffee_shop
   ```
Stvorite i aktivirajte virtualnu okolinu:

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Instalirajte potrebne pakete:

```bash
pip install -r requirements.txt
```
Postavite okolišne varijable (na primjer, za razvojni način rada):


```bash
export FLASK_APP=app.py
export FLASK_ENV=development
```
Pokrenite aplikaciju:


```bash
flask run
```
Aplikacija će biti dostupna na http://127.0.0.1:5000/.

Struktura Projekta
app.py - Glavna datoteka aplikacije koja pokreće Flask server.
dazzling/ - Glavni direktorij aplikacije s poddirektorijima za rute, modele, forme i statičke datoteke.
templates/ - HTML predlošci.
static/ - Statičke datoteke (CSS, slike).


