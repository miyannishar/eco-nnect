from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={
    r"/*": {
        "origins": [
            "http://localhost:3000",
            "http://192.168.x.x:3000"  # Replace with your local IP
        ]
    }
})

# If using Flask
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

# If using FastAPI with uvicorn
# Run with: uvicorn main:app --host 0.0.0.0 --port 5000 