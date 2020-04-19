# Приложение отвечает по указанному адресу.
# TODO Сервер отдаёт HTTP 200 OK по пути /
# TODO Сервер отдаёт json с сгенерированным сообщением по пути /api/generate в соответствии с таблицей генерации.
# TODO Сервер отдаёт json с X сгенерированными сообщениями по пути /api/generate/X, где X — случайное число от 1 до 20.
"""
проверить свой код с терминала:
http https://blooming-shore-52769.herokuapp.com/
Пример ответа от сервера по запросу /api/generate/:

HTTP/1.0 200 OK
Content-Length: 849
Content-Type: application/json
Date: Thu, 8 Oct 2019 07:49:54 GMT
Server: WSGIServer/0.2 CPython/3.7.4

{
    "message": "С другой стороны, совокупность сквозных технологий  выдвигает новые требования  бюджетного финансированиясинергетического эффекта цифровых следов граждан."
}
Пример ответа от сервера по запросу /api/generate/5:

HTTP/1.0 200 OK
Content-Length: 3205
Content-Type: application/json
Date: Thu, 10 Oct 2019 04:51:33 GMT
Server: WSGIServer/0.2 CPython/3.7.4

{
    "messages": [
        "Вместе с тем, ускорение блокчейн-транзакций  заставляет искать варианты дальнейшего углубления внезапных открытий.",
        "Коллеги, парадигма цифровой экономики открывает новые возможности для нормативного регулирования знаний и компетенций.",
        "Следовательно, парадигма цифровой экономики повышает вероятность дальнейшего углубления волатильных активов.",
        "Вместе с тем, ускорение блокчейн-транзакций  заставляет искать варианты универсальной коммодизации государственно-частных партнёрств.",
        "Однако, парадигма цифровой экономики не оставляет шанса для универсальной коммодизации нежелательных последствий."
    ]
}
"""

import json
import os
import random
from bottle import route, run, redirect, response
import sayings as s


def generate_message(count=1):
    msg = []
    if count > 1:
        for i in range(count):
            msg.append(random.choice(s.beginnings) + ' ' + random.choice(s.subjects) + ' ' + random.choice(
                s.verbs) + ' ' + random.choice(s.actions))

    else:
        msg.append(random.choice(s.beginnings) + ' ' + random.choice(s.subjects) + ' ' + random.choice(
            s.verbs) + ' ' + random.choice(s.actions))

    return msg
    # return json.dumps(msg)


@route("/")
def index():
    # response.set_header('Content-Type', 'application/json')
    html = """
<!doctype html>
<html lang="en">
  <head>
    <title>Генератор утверждений</title>
  </head>
  <body>
    <div class="container">
      <h1>Коллеги, добрый день!</h1>
      <p>{}</p>
      <p class="small">Перейдите  по ссылке  <a href="/api/generate">"/api/generate/"</a>
      "или <a href="/api/generate/3">"/api/generate/&lt;num:int&gt;"</a> "
      </p>
    </div>
  </body>
</html>
""".format(
        generate_message())
         # json.loads(generate_message()))
    return html


@route("/api/generate/")
def api_response_generate():
    # response_generate =  json.loads(generate_message())
    response_generate = generate_message()
    return {"message": response_generate}


@route("/api/generate/<x:int>")
def api_response_generate_number(x):
    response_generate = generate_message(x)
    return {"message": response_generate}
    # return {"requested_id": x, "random_number": random.randrange(x)}


# @route('/wrong/url')
# def wrong():
#     redirect("/right/url")
#

if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    run(host="localhost", port=8080, debug=True)
