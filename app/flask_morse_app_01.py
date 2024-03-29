### flask_morse_app_01.py
from flask import Flask, request, render_template
from string_to_morse_function_01 import etmf2
from datetime import datetime

dateTimeObj = datetime.now()

app = Flask(__name__)

@app.route('/morse/<value_to_convert>')
def morse(value_to_convert):
    etmf2(value_to_convert)

    b = etmf2.code
    converted_value = value_to_convert + ' ' + b
    with open('./log.txt', 'a') as f:
        print(str(dateTimeObj) + ' ' + converted_value, file=f)

    translating_message = 'Translating "{}" to Morse code: {}'.format(value_to_convert, b)
    return render_template('template.html', translating_message=translating_message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
