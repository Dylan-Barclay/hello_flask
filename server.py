from flask import Flask  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/')          # The "@" decorator associates this route with the function immediately following

def hello_world():return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def dojo():
  return "Dojo!"

@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hi(name):
  return "Hi, " + str(name)

@app.route('/repeat/<num>/<word>')
def number_and_words(num, word):
  return (word * int(num))



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
  app.run(debug=True)    # Run the app in debug mode.