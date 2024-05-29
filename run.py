from app._init_ import create_app

app = create_app()

if __name__ == "__main__":
    app = create_app()
    port = int(os.environ.get("PORT", 5000))  # Default to port 5000 if PORT is not set
    app.run(host="0.0.0.0", port=port)
