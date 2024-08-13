from flask import Flask, render_template, redirect, url_for


app = Flask(__name__) #creating the Flask class object   
 
@app.route('/') #decorator drfines the   
def home():  
    return render_template("home.html")

@app.route('/about') #decorator drfines the   
def about():  
    return render_template("about.html")  

#@app.route('/admin') #decorator drfines the   
#def admin():  
   # return redirect(url_for('home'))

@app.route('/about') #decorator drfines the   
def admin():  
    return redirect(url_for('about.html'))
  
if __name__ =='__main__':  
    app.run(debug = True) 