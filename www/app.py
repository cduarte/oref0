import os
import socket

from flask import Flask, render_template, url_for, json, jsonify
app = Flask(__name__)

@app.route("/")
def index():
    myopenaps_dir = "/root/myopenaps/"
    data=dict()
    data['hostname']=socket.gethostname()
    data['glucose'] = json.load(open(os.path.join(myopenaps_dir, "monitor/glucose.json")))
    iob = json.load(open(os.path.join(myopenaps_dir, "monitor/iob.json")))
    data['iob'] = iob[0]
    data['battery'] = json.load(open(os.path.join(myopenaps_dir, "monitor/battery.json")))
    data['edison_battery'] = json.load(open(os.path.join(myopenaps_dir, "monitor/edison-battery.json")))
    data['meal'] = json.load(open(os.path.join(myopenaps_dir, "monitor/meal.json")))
    

    data['suggested'] = json.load(open(os.path.join(myopenaps_dir, "enact/suggested.json")))
    data['smb_suggested'] = json.load(open(os.path.join(myopenaps_dir, "enact/smb-suggested.json")))
    

    data['enacted'] = json.load(open(os.path.join(myopenaps_dir, "enact/enacted.json")))
    data['smb_enacted'] = json.load(open(os.path.join(myopenaps_dir, "enact/smb-enacted.json")))

    data['temp_basal'] = json.load(open(os.path.join(myopenaps_dir, "monitor/temp_basal.json")))
    return render_template('index.html', data=data )

@app.route("/enacted")
def enacted():
    json_url = os.path.join("/root/myopenaps/enact/enacted.json")
    data = json.load(open(json_url))
    return jsonify(data)

@app.route("/glucose")
def glucose():
    json_url = os.path.join("/root/myopenaps/monitor/glucose.json")
    data = json.load(open(json_url))
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
