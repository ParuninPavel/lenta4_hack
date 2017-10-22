from flask import Flask
from flask import request
app = Flask(__name__)
import dl_module
predictor = dl_module.NN_Predictor()

@app.route('/')
def hello_world():
    img = request.args.get('img', None)
    txt = request.args.get('txt', None)
    print(type(txt))
    print(txt)
    
    return predictor.predict(txt = txt, img = img)
