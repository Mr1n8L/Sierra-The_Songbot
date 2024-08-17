# Use an official Python runtime as a base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set environment variables if needed (example)
# ENV SOME_ENV_VAR=value

# Expose port 8000 (or the port your application uses)
EXPOSE 8000

# Define the command to run your application
CMD ["python", "chatbot_training.py"]
