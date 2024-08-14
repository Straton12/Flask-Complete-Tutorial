from flask import Flask, render_template, redirect, url_for


app = Flask(__name__) #creating the Flask class object   
 
@app.route('/') #decorator drfines the   
@app.route('/home')
def home_page():  
    return render_template("home.html")

  
if __name__ =='__main__':  
    app.run(debug = True) 