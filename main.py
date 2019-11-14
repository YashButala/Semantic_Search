from flask import Flask, request
import requests
from query import do_query

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def adder_page():
    errors = ""
    if request.method == "POST":
        question = None
        try:
            question = request.get_data()
            question=str(question[6:-3])
            question=question.replace("+"," ")

        except:
            errors += "<p>{!r} is not a query_string.</p>\n"

        if question is not None :
       # 	ques = question.decode('utf-8')
        	print(question[2:-1])
        	result = do_query(question[2:-1])
        	print(result)
        	return '''
		    	<html>
		    		<body>
		                <p>The result is {result}</p>
		                <p><a href="/">Click here to calculate again</a>
		            </body>
		        </html>
		    '''.format(result=result)

    return '''
        <html>
            <body>
                {errors}
                <p>Enter your query:</p>
                <form method="post" action=".">
                    <p><input name="Query" /></p>
                    <p><input type="submit" value="Search" /></p>
                </form>
            </body>
        </html>
    '''.format(errors=errors)
if __name__ == "__main__":
#    app.secret_key = 'super secret key'
#    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)
