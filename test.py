import random
import json
import sayings as s
import requests


def answer():
    response = requests.post('https://blooming-shore-52769.herokuapp.com/')
    return response


def generate_message():
    msg = random.choice(s.beginnings) + ' ' + random.choice(s.subjects) + ' ' + random.choice(
        s.verbs) + ' ' + random.choice(s.actions)
    return json.dumps(msg)
    # "Сегодня уже не вчера, ещё не завтра"


r = answer()
print(r)

# for key, value in enumerate(code.headers):
#     print(key, value)
#
#
# print(code.headers)
# print(code.headers['Content-Type'])
