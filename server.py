from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/<string:reqname>')
def hello2(reqname):
    return render_template(reqname)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        email = data['email']
        subject = data['subject']
        message = data['message']
        with open('./database.csv', mode='a', newline='\n') as database:
            writer = csv.writer(database, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([email, subject, message])

        return render_template('thankyou.html', name=data['email'].split('@')[0])
    else:
        return 'something went wrong.'
