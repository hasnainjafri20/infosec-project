from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    success_message = None      
    submitted_message = None 
    error = None          
     
    if request.method == 'POST':
        user_message = request.form.get('message')

        if user_message:
            success_message = "Message submitted successfully!"
            submitted_message = user_message
            return render_template('index.html',
                                   success_message=success_message,
                                   submitted_message=submitted_message,
                                   error=None) 
        else:
            error = "Message cannot be empty."
            return render_template('index.html',
                                   success_message=None,
                                   submitted_message=None,
                                   error=error)

    return render_template('index.html',
                           success_message=None,
                           submitted_message=None,
                           error=None)

if __name__ == '__main__':
    app.run(debug=True)      
