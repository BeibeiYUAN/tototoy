from app import create_app

# Note: It is very unlikely that you need to
# touch this file at all.

my_app = create_app()

if __name__ == "__main__":
    my_app.run(debug=False, port=8080)