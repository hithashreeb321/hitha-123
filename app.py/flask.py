
from flask_socketio import SocketIO
import random, time

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

# Emit vitals every few seconds
def generate_vitals():
    while True:
        data = {
            "heart_rate": random.randint(60, 100),
            "blood_pressure": f"{random.randint(110,130)}/{random.randint(70,85)}",
            "oxygen_level": random.randint(95,100)
        }
        socketio.emit("vitals_update", data)
        time.sleep(3)

if __name__ == "__main__":
    socketio.start_background_task(generate_vitals)
    socketio.run(app, debug=True)