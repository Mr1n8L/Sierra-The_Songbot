# Chatbot Project

This project is a Python-based chatbot that uses various dependencies, including some that may require Rust for building. This README provides step-by-step instructions on how to set up the project, build the Docker image, and run the application.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Project Structure](#project-structure)
3. [Docker Setup](#docker-setup)
   - [Dockerfile](#dockerfile)
   - [Building the Docker Image](#building-the-docker-image)
   - [Running the Docker Container](#running-the-docker-container)
4. [Handling Rust Dependency](#handling-rust-dependency)
5. [Running the Application](#running-the-application)
6. [Troubleshooting](#troubleshooting)
7. [License](#license)

## Prerequisites

Before you begin, ensure you have the following installed on your local machine:

- [Docker](https://www.docker.com/get-started)
- [Git](https://git-scm.com/)

## Project Structure

The project structure should look something like this:

```plaintext
├── Dockerfile
├── requirements.txt
├── chatbot_training.py
├── chat.py
└── README.md
```

## Docker Setup

### Dockerfile

The Dockerfile is used to create a Docker image for the chatbot application. It installs all necessary dependencies, including Rust and Cargo, which are required for some Python packages.

```Dockerfile
# Use an official Python runtime as a base image
FROM python:3.10-slim

# Install Rust and Cargo
RUN apt-get update && apt-get install -y curl \
    && curl https://sh.rustup.rs -sSf | sh -s -- -y \
    && source $HOME/.cargo/env

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the application port
EXPOSE 8000

# Define the command to run your application
CMD ["python", "chatbot_training.py"]
```

### Building the Docker Image

To build the Docker image, navigate to the project directory in your terminal and run the following command:

```bash
docker build -t chatbot:latest .
```

### Running the Docker Container

After building the image, you can run the Docker container using:

```bash
docker run -p 8000:8000 chatbot:latest
```

This command will start the application and map port 8000 from the container to port 8000 on your host machine.

## Handling Rust Dependency

Some Python packages in this project require Rust and Cargo to compile. The Dockerfile includes steps to install Rust and Cargo to handle these dependencies. If you encounter errors related to Rust during the build process, ensure that Rust is properly installed and available in the PATH.

## Running the Application

The application can be run in two separate terminals:

1. **Terminal 1**: Run the chatbot training script.

   ```bash
   python chatbot_training.py
   ```

   This script preprocesses the data, trains the model, and saves the necessary objects.

2. **Terminal 2**: Run the chat interface.

   ```bash
   python chat.py
   ```

   This script starts the chat interface where you can interact with the trained chatbot.

## Troubleshooting

### Rust and Cargo Issues

If you encounter issues related to Rust or Cargo not being installed:

- Ensure that Rust is installed on your system or in your Docker environment.
- Rebuild the Docker image after making sure Rust is available.

### Dependency Version Conflicts

If you experience dependency version conflicts, consider updating your `requirements.txt` to compatible versions or consult the documentation for the specific package.

### Updating pip

If you see notices about an outdated version of `pip`, you can update it by adding this line to your Dockerfile before the `pip install` command:

```Dockerfile
RUN python -m pip install --upgrade pip
