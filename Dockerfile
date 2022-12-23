FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the required packages
RUN pip install -r requirements.txt

# Copy the rest of the app's source code to the working directory
COPY . .

# Expose port 80
EXPOSE 80

# Set the default command to run the app
CMD ["python", "doomsday_game.py"]
