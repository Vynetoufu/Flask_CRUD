from flask import Flask, render_template, request, redirect, url_for

app = Flask (__name__)

@app.route('/', methods=['GET','POST'])
def home():
    #Initialization of Variables
    submitted = None
    hidden_text = None

    #Form Post Request
    if request.method == 'POST':
        submitted=request.form['test_input']
        hidden_text = request.form['hidden_id']
    return render_template('testPostAdvance.html', display_value=submitted, student_to_edit=hidden_text) 

if __name__ == '__main__':
    app.run(debug=True)