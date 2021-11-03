import flask
import lipd
from flask import Flask
from flask import send_from_directory
from flask import request
from lipd import readLipd

app = Flask(__name__)
# setting the route pf the server
@app.route('/', methods = ['POST'])
def receiveLiPD():
   # setting the files from the POST request equal to a variable
   fileReceived = request.files['pond']
   # saving the file locally in order to read it
   fileReceived.save('pond.lpd')
   # reading the locally saved pond file
   readFile = lipd.readLipd("./pond.lpd")
   # returning the netCDF file from the resulting climate model
   return send_from_directory("./", "test.nc")


# setting the host and port for the server to run on
app.run(host='0.0.0.0', port=80)
