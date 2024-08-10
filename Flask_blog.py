from flask import Flask  
  
app = Flask(__name__) #creating the Flask class object   
 
@app.route('/') #decorator drfines the   
def home():  
    return "<h1>hello, this is our first flask personal website</h1>";  
  
if __name__ =='__main__':  
    app.run(debug = True)  