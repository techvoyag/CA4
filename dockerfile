# Use an official Node.js runtime as the base image
FROM node:18.13.0

# Set the working directory within the container
WORKDIR /

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install project dependencies
RUN npm install

# Copy the entire application code to the working directory
COPY . .


# Expose the port on which your app will run (adjust as needed)
EXPOSE 3000

# Define the command to start your application
CMD ["npm", "start"]
