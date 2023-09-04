from flask import Flask
from src.logger import logging
from src.exception import CustomException
import sys,os

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    try:
        raise Exception("We are testing Exception file")
    except Exception as e:
        ml = CustomException(e,sys)
        logging.info(ml.error_message)
        logging.info('We are testing logger file')

        return "welcome"

if __name__ =='__main__':
    app.run(debug=True)