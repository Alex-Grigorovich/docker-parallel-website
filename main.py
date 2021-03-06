from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_url_path='/static',
            static_folder='static/')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/roadmap')
def roadmap():
    return render_template('roadmap.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/ourMission')
def ourMission():
    return render_template('ourMission.html')



if __name__ == "__main__":
    app.run(debug=True)
