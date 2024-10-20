# Use the specified Python version from runtime.txt
FROM python:3.9.1

# Set the working directory
WORKDIR /app

# Copy the requirements.txt and runtime.txt to the container
COPY requirements.txt /app/
COPY runtime.txt /app/

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files to the container
COPY . /app

# Expose the default port (adjust if necessary)
EXPOSE 5000

# Command to run your application (modify based on your app structure)
CMD ["gunicorn", "-b", "0.0.0.0:5000", "main:app"]
