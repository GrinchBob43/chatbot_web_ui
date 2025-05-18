from flask import Flask, render_template, request


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html', response='')
@app.route('/chat', methods=['POST'])
def chat():
    prompt = request.form.get('prompt', '')
    # code for chatting with the model
    response = "function to get response from the model"
    return render_template('index.html', response=response)
    
if __name__ == '__main__':
    app.run(debug=True)