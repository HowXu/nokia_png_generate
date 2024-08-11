FROM node:current-alpine3.13
WORKDIR /app
COPY package*.json ./
RUN npm config set registry=http://registry.npmmirror.com
RUN npm install
COPY . .