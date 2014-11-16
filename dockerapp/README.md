# Run app in container

    docker build -t hellopython .
    docker run hellopython /app/hello.py

# Run interactive bash shell

    docker run -i -t hellopython sh

