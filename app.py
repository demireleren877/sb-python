from flask import Flask, render_template, request
import firebase
import get_person

app = Flask(__name__)


def ses():
    while True:
        print("Waiting for face")

@app.route('/',methods=['GET','POST'])
def index():
        
        print(request.method)
        id =  get_person.getPerson()
        return render_template('index.html', coffees=firebase.getUsersCoffees(id),name=firebase.getProfile(id))

if __name__ == '__main__':
    app.run(debug=True)



