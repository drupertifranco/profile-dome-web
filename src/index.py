from flask import Flask, render_template # llamamos Flask

app = Flask(__name__) # Objetos

@app.route('/') # Creacion Route 

def home():
    return render_template('home.html')

@app.route('/about')

def about():
    return render_template('about.html')

@app.route('/english')

def english():
    return render_template('homeEnglish.html')


if __name__ == '__main__':
    app.run(debug= True)

