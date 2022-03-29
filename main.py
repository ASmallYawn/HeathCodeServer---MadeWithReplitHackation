import requests, json, replit, os, flask
from flask import Flask
from flask_cors import CORS
from flask_cors import cross_origin
app = Flask(__name__)
CORS(app)
sfToken = os.environ['sfToken']

def updateDB():         
  headers = {
    "X-App Token": sfToken,
    "limit": "500000"
  }
  
  url = "https://data.sfgov.org/resource/pyih-qa8i.json"
  r = requests.get(url, headers=headers)
  data = r.json()
  
  dataSorted = {}
  
  for value in data:
    id = value["business_name"] 
    if id in dataSorted:
      dataSorted[id].append(value)
    else:
      dataSorted[id] = [value]

  replit.db["data"] = json.dumps(data)

updateDB()

def getDB():
  d = replit.db["data"]
  return(d)

@app.route('/')
@cross_origin()
def e():
  return getDB()

if __name__ == "__main__":
  app.run(host="0.0.0.0")  