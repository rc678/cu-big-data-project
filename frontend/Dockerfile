# Use Node.js LTS version as the base image
FROM node:14

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json (or yarn.lock) to the container
# This allows Docker to cache the npm install step if the dependencies haven't changed
# COPY . /app/

COPY package*.json ./


# Install dependencies
RUN npm install

# Copy the rest of your frontend source code to the container
COPY . .

RUN npm run build

EXPOSE 8001

# Start the development server
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
# CMD ["npm", "run", "dev", "--host", "0.0.0.0", "--port", "5173"]
CMD ["npm", "run", "dev"]
