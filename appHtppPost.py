from flask import Flask, render_template, request, redirect, url_for

app = Flask (__name__)

@app.route('/', methods=['GET','POST'])
def home():
    submitted = None
    if request.method == 'POST':
        submitted=request.form['test_input']
    return render_template('testPostPost.html', display_value=submitted) 

if __name__ == '__main__':
    app.run(debug=True)