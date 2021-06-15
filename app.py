from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    covid_world_data = requests.get('https://api.covid19api.com/summary')
    #print(covid_world_data.status_code)
    data = json.loads(covid_world_data.content)
    
    return render_template('index.html', data = data)



if __name__ == '__main__':
    app.run(debug=True)