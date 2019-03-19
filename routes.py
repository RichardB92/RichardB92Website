from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['es', 'en'])
	#return 'es'
	
@app.route("/")
def index():
	if get_locale() is "en":
		return render_template("index_en.html")
	else:
		return render_template("index_es.html")
	

if __name__=="__main__":
	app.run(debug=True)