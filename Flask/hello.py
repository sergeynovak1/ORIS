# необходимые импорты
import json
from flask import Flask, render_template, request

# инициализируем приложение
# из документации:
#     The flask object implements a WSGI application and acts as the central
#     object.  It is passed the name of the module or package of the
#     application.  Once it is created it will act as a central registry for
#     the view functions, the URL rules, template configuration and much more.
app = Flask(__name__)

# дальше реализуем методы, которые мы можем выполнить из браузера,
# благодаря указанным относительным путям


# метод, который возвращает список фильмов по относительному адресу /films
@app.route("/films")
def films_list():
    # читаем файл с фильмами
    with open("films.json", 'r') as f:
        films = json.load(f)

    # получаем GET-параметр country (Russia/USA/French
    country = request.args.get("country")
    rating = request.args.get("rating")

    if rating:
        films = filter(lambda x: x["rating"] >= float(rating), films)

    # формируем контекст, который мы будем передавать для генерации шаблона
    context = {
        'films': films,
        'title': "FILMS",
        'country': country
    }

    # возвращаем сгенерированный шаблон с нужным нам контекстом
    return render_template("films.html", **context)


@app.route("/film/<int:film_id>")
def get_film(film_id):
    with open("films.json", 'r') as f:
        films = json.load(f)

    for film in films:
        if film['id'] == film_id:
            return render_template("film.html", title=film['name'], film=film)

    return render_template("error.html", error="Такого фильма не существует в системе")


@app.route('/new_film', methods=['GET'])
def my_form():
    return render_template('new_film.html')


@app.route('/new_film', methods=['POST'])
def new_film():
    id = request.form['id']
    name = request.form['name']
    rating = request.form.get('rating')
    country = request.form['country']
    context = {
        'id': id,
        'name': name,
        'rating': rating,
        'country': country,
    }
    with open("films.json", 'r', encoding='utf-8') as f:
        films = json.load(f)
        films.append(context)
    with open("films.json", 'w', encoding='utf-8') as f:
        json.dump(films, f)
    return render_template("new_film.html")



if __name__ == "__main__":
    app.run(debug=True)
