# from app import create_app

# app = create_app()

# if __name__ == "__main__":
#     app.run(debug=True)
# from app import create_app

# app = create_app()

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5000)
from app import app  # Import the Flask app object from the app module

if __name__ == "__main__":
    app.run()

