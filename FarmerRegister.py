from flask import *
import pymysql


app = Flask(__name__)
app.secret_key = 'RadheKrishna'

# @app.route('/', methods=['GET', 'POST'])
# def openfarmerreg():
#    return redirect(url_for('farmerreg'))

@app.route('/farreg', methods=['GET', 'POST'])
def farmerreg():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        phone_no = str(request.form['phone'])
        age = int(request.form['age'])
        gender = request.form['gender']
        b_type = request.form['business-type']


        # print(name,phone_no,age,gender,skills,location)
        
            # building connection with database
    
        con = pymysql.connect(host="127.0.0.1",
                        user="root",
                        password="Ajay@2002")
        cur=con.cursor()
        cur.execute("use labour")
        
        q = 'insert into farmerdetails(name,phone_no,age,gender,business_type) values ("%s","%s",%d,"%s","%s")'
        cur.execute(q % (name,phone_no,age,gender,b_type))
        con.commit()
        # value="harvesting"
        # cur.execute(f"select * from labourdetails where skills like '%{value}%'")
        # a=cur.fetchall()    
        # print(a)       
                 

    return render_template('FarmerRegister.htm')




if __name__=='__main__':
 app.run(debug=True)
        