# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./ /app

# RUN pip install psycopg3
# RUN pip install psycopg2-binary

# Install the FastAPI dependencies
# RUN pip install -r requirements.txt 

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose the FastAPI port
EXPOSE 8000

# Define the command to run your FastAPI server using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
