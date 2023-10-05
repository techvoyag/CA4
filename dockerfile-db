# Use an official Node.js runtime as the base image
FROM node:18.13.0

# Set the working directory in the container
WORKDIR /

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port your application will run on
EXPOSE 9002

# Define the command to start your application
CMD ["node", "index.js"]
