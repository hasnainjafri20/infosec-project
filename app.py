from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    success_message = None  # Variable to hold success message
    submitted_message = None # Variable to hold submitted message
    error = None            # Variable to hold error message

    if request.method == 'POST':
        user_message = request.form.get('message')

        if user_message:
            # Success! Prepare messages for the index template
            success_message = "Message submitted successfully!"
            submitted_message = user_message
            # Render index.html again, but with success info
            return render_template('index.html',
                                   success_message=success_message,
                                   submitted_message=submitted_message,
                                   error=None) # Clear any previous error
        else:
            # Handle case where message is empty
            error = "Message cannot be empty."
            # Render index.html with the error
            return render_template('index.html',
                                   success_message=None,
                                   submitted_message=None,
                                   error=error)

    # If it's a GET request, just show the form without success/error messages initially
    return render_template('index.html',
                           success_message=None,
                           submitted_message=None,
                           error=None)

if __name__ == '__main__':
    app.run(debug=True)