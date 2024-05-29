from flask import *
import pymysql
import re






app = Flask(__name__)
app.secret_key = 'RadheKrishna'

from main import *


# app.register_blueprint(auth_bp)


@app.route('/')
def openlogin():

    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get form data
        v_email = str(request.form['email'])
        v_password = str(request.form['password'])
        
        # Building connection with the database
        con = pymysql.connect(host="127.0.0.1", user="root", password="Ajay@2002")
        cur = con.cursor()
        cur.execute("USE labour")
        x = "SELECT id FROM users WHERE email='%s' AND password='%s'"
        cur.execute(x% (v_email, v_password))
        global a
        a = cur.fetchone()
        if a:
            # flash('Login Successful')
            return redirect(url_for("home"))  # Redirect to the same URL after form submission
        else:
            useremail = "SELECT id FROM users WHERE email='%s'"
            cur.execute(useremail%(v_email))
            email=cur.fetchone()
            if email:
                flash('Incorrect Password..!')
                return redirect(url_for('login'))
            else:
                flash(f'No account created with this {v_email}')
                return redirect(url_for('login'))
            
    return render_template('login.htm')

@app.route('/signup', methods=['GET', 'POST'])
# main_bp.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        # Get form data
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm-password']
        re_pattern=r'[a-z]'
        re_pattern1=r'[A-Z]'
        re_pattern2=r'[0-9]'
        re_pattern3 = r'[^0-9a-zA-Z\s]'
        pattern=re.search(re_pattern,password)
        pattern1=re.search(re_pattern1,password)
        pattern2=re.search(re_pattern2,password)
        pattern3=re.search(re_pattern3,password)
        all_pattern=[pattern,pattern1,pattern2,pattern3]

        if (len(password)<8) or (all(all_pattern)==False) or (' ' in password):
            flash('Password must be atleast 8characters')
            flash('password must contain a-z,A-Z,0-9 and special characters')
            return redirect(url_for('signup'))
        else:
            try:
                # building connection with database
                if password == confirm_password:
                    con = pymysql.connect(host="127.0.0.1",
                                  user="root",
                                  password="Ajay@2002")
                    cur=con.cursor()
                    cur.execute("use labour")
                    q = 'insert into users(username,email,password) values ("%s","%s","%s")'
                    cur.execute(q % (username,email,password))
                    con.commit()

                    flash('Signup Successful')
                    return redirect(url_for('signup')) 
                else:
                        flash('Both passwords should be same')
                        return redirect(url_for('signup'))  # Redirect to the same URL after form submission
            except :#pymysql.IntegrityError
                    flash('Email or username already in use')
                    return redirect(url_for('signup'))  # Redirect to the same URL after form submission

    return render_template('signup.htm')

if __name__=="__main__":
 app.run(debug=True)

