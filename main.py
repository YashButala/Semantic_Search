from flask import Flask, render_template
#from db_setup import init_db, db_session
from forms import MusicSearchForm
from flask import flash, request, redirect, url_for
import requests
from query import do_query
#from models import Album

app = Flask(__name__)

@app.route("/",methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/about",methods=["GET", "POST"])
def about():
    return render_template("about2.html")

@app.route("/result_page/<result>", methods=["GET", "POST"])
def result_page(result):
    print('Request is shit', request)
    return render_template('result.html', result=result)

@app.route("/adder_page", methods=["GET", "POST"])    
def adder_page():
    errors = ""
    result = None
    print('it')
    print('rEQUEST IS', request)
    if request.method == "POST":
        print('chala')
        print(request)
        question = None
        print(1)
        try:
            question = request.get_data()
            question=str(question[6:-3])
            print(question)
            question=question.replace("+"," ")

        except:
            errors += "<p>{!r} is not a query_string.</p>\n"
        if question is not None:
            print(question[2:-1])
            result = do_query(question[2:-1])
            print(question)
            return redirect(url_for('result_page', result=result))

    return '''
        <html>
            <body>
                {errors}
                <p>Enter your query:</p>
                <form method="post" action="""{{ url_for('result_page', result={res}) }}""">
                    <p><input name="Query" /></p>
                    <p><input type="submit" value="Search" /></p>
                </form>
            </body>
        </html>
    '''.format(errors=errors,res=result)
    



# @app.route("/salvador")    
# def salvador():
#     return "Hello, Salvador"
    
if __name__ == "__main__":
    app.run(debug=True)
