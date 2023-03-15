import string, secrets, logging
from flask import Flask, request, render_template

app = Flask(__name__)
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',filename="log_password_generator.log", level=logging.INFO,datefmt= '%d-%m-%Y %H:%M:%S')

def password_generator():
    logging.info("password_generator() called")
    pass_length = 16
    characters = string.punctuation + string.digits + string.ascii_letters
    password = ''
    logging.info("variables initialised")

    for i in range(pass_length):
        index_choice = secrets.randbelow(len(characters)-1 - 1) + 1  # random number from range [1, length of characters string)
        password = password + characters[index_choice]
        logging.info(str(i+1) + " random char(s) now in password string")
 
    logging.info("returning password...")   
    return password

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        return render_template("home.html", ButtonPressed = password_generator())
    return render_template('home.html')

if __name__ == '__main__':
    logging.info("main executed")
    app.run(debug = True) # running at http://127.0.0.1:5000/
    logging.info("end of main")
 
   