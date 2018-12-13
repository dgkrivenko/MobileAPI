from flask import Flask, request
import auth
import reg
import recommendations
import json
import add_genre


app = Flask(__name__)


@app.route('/auth', methods=['POST'])
def auth_handler():
    request_data = request.get_json()
    login = request_data['login']
    password = request_data['password']
    query_result = auth.get_data_by_login(login)
    code = auth.auth(login, password, query_result)
    res = {}
    res['code'] = str(code)
    if code == 0:
        res['name'] = query_result[3]
    res = json.dumps(res)
    return res


@app.route('/reg', methods=['POST'])
def reg_handler():
    request_data = request.get_json()
    login = request_data['login']
    password = request_data['password']
    user_name = request_data['username']
    code = reg.registration(login, password, user_name)
    res = {
        'code': str(code)
    }
    res = json.dumps(res)
    return res


@app.route('/genre', methods=['POST', 'GET'])
def add_handler():
    request_data = request.get_json()
    login = request_data['login']
    genre = request_data['genre']
    code = add_genre.add_genre(login, genre)
    response = {
        'code': code
    }
    response = json.dumps(response)
    return response


@app.route('/choose', methods=['POST'])
def choose_handler():
    request_data = request.get_json()
    flight = request_data['flight']
    login = request_data['login']
    genre = recommendations.get_genre_by_login(login)
    response = recommendations.recomend_by_genre(genre, flight)
    response = json.dumps(response)
    return response


if __name__ == '__main__':
    app.run()
