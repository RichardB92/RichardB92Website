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
	return render_template("index_"+ get_locale() +".html")
	# if get_locale() is "en":
		# return render_template("index_en.html")
	# else:
		# return render_template("index_es.html")

@app.route("/contact")
def contact():
	return render_template("contact_"+ get_locale() +".html")		

if __name__=="__main__":
	app.run(debug=True)