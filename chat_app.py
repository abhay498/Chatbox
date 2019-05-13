from flask import Flask
from flask import render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)

app.config['SECRET_KEY'] = 'asbui'
socketio = SocketIO(app)

@app.route('/')
def hello():
   return render_template('./ChatApp.html')
   
def messageRecived():
  print( 'Message was received' )
  
@socketio.on('my event')
def handle_my_custom_event(input_str):
    print('received something ' + str(input_str))
    socketio.emit( 'my response', input_str, callback=messageRecived )
    
if __name__ == '__main__':
   socketio.run(app, debug = True)

