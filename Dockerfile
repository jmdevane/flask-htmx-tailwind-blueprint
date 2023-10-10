FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Expose port for the Flask app
EXPOSE 8000

# Specify the command to run on container start
CMD ["./run.sh"]