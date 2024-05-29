from flask import *
import pymysql


app = Flask(__name__)
app.secret_key = 'RadheKrishna'

# @app.route('/', methods=['GET', 'POST'])
# def open():
#    return redirect(url_for('labourReg'))

@app.route('/labreg', methods=['GET', 'POST'])
def labourReg():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        phone_no = str(request.form['phone'])
        age = int(request.form['age'])
        gender = request.form['gender']
        skills =",".join(request.form.getlist('skills'))
        location = request.form['location']


        # print(name,phone_no,age,gender,skills,location)
        
            # building connection with database
    
        con = pymysql.connect(host="127.0.0.1",
                        user="root",
                        password="Ajay@2002")
        cur=con.cursor()
        cur.execute("use labour")
        
        q = 'insert into labourdetails(name,phone_no,age,gender,skills,location) values ("%s","%s",%d,"%s","%s","%s")'
        cur.execute(q % (name,phone_no,age,gender,skills,location))
        con.commit()
        # value="harvesting"
        # cur.execute(f"select * from labourdetails where skills like '%{value}%'")
        # a=cur.fetchall()    
        # print(a)       
                 

    return render_template('labourRegister.htm')




if __name__=='__main__':
 app.run(debug=True)
        