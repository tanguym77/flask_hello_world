from flask import Flask
from flask import render_template
from flask import json
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/test')
def hello_world():
    return render_template('hello.html')
                                                                                          
if __name__ == "__main__":
  app.run(debug=True)
