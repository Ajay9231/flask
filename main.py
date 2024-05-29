from flask import *



app = Flask(__name__)
# auth_bp = Blueprint('auth', __name__)
app.secret_key = 'RadheKrishna'

from labourRegister import *


@app.route('/home')
# @auth_bp.route('/home')

def home():
   return render_template('index.html')

@app.route('/about')
# @auth_bp.route('/about')

def about():
   return render_template('about.html')

@app.route('/wages')
# @auth_bp.route('/wages')

def wages():
   return render_template('wages.html')

@app.route('/contact')
# @auth_bp.route('/wages')

def contact():
   return render_template('contact.html')


    
        
# if __name__=='__main__':
#     app.run(debug=True)