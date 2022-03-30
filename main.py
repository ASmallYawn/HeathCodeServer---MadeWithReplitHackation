import requests, json, replit, os, flask
from flask import Flask
from flask_cors import CORS
from flask_cors import cross_origin
app = Flask(__name__)
CORS(app)
Token = os.environ['Token']

#San Francisco
def updateDBSF():         
  headers = {
    "X-App Token": Token,
    "limit": "500000"
  }
  
  url = "https://data.sfgov.org/resource/pyih-qa8i.json"
  r = requests.get(url, headers=headers)
  data = r.json()
  replit.db["sf"] = json.dumps(data)

#Chicago
def updateDBCH():         
  headers = {
    "X-App Token": Token,
    "limit": "500000"
  }
  
  url = "https://data.cityofchicago.org/resource/4ijn-s7e5.json"
  r = requests.get(url, headers=headers)
  data = r.json()  
  replit.db["ch"] = json.dumps(data)

updateDBSF()
updateDBCH()



#GET Responses
#SanFrancisco
def getDBSF():
  d = replit.db["sf"]
  return(d)

@app.route('/sf')
@cross_origin()
def sf():
  return getDBSF()

#Chicago
def getDBCH():
  d = replit.db["ch"]
  return(d)

@app.route('/ch')
@cross_origin()
def ch():
  return getDBCH()

if __name__ == "__main__":
  app.run(host="0.0.0.0")  