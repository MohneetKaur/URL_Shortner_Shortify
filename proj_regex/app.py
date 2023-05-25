from flask import Flask,request,render_template
import re 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search',methods=['POST'])
def search_fun():
    text = request.form.get('text')
    regex = request.form.get('regex')
    matches = re.findall(regex,text)
    return render_template('results.html',matches=matches)

if __name__ =='__main__':
    app.run(debug=True)