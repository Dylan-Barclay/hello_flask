from flask import Flask, render_template  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return "Hello World!"
@app.route('/dojo')
def dojo():
  return "Dojo!"

@app.route('/hello/<string:name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hi(name):
  return "Hi, " + str(name)

@app.route('/repeat/<int:num>/<string:word>')
def number_and_words(num, word):
  stuff = ''
  for x in range(0, int(num)):
    stuff += str(word) + ' '
  return stuff

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return 'Sorry! No response. Try again.'



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
  app.run(debug=True)    # Run the app in debug mode.