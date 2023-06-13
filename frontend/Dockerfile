# Base image
FROM node:14-alpine

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the entire application
COPY . .

# Build the React app
RUN npm run build

# Set environment variables
ENV NODE_ENV=production
ENV PORT=4200

# Expose port
EXPOSE 4200

# Start the application
CMD [ "npm", "start" ]
