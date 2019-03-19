# Setting up the angular application
FROM node:8.11.2-alpine as node
RUN mkdir -p /code/src/webapp/

# Setting the configuration
ARG configuration=production

# Set working directory
WORKDIR /code/src/webapp/

COPY package*.json /code/src/webapp/
RUN npm install
COPY . /code/src/webapp/

# Building the angular application 
RUN npm run build -- --output-path=./dist/out --configuration $configuration

# Setting the nginx
FROM nginx:1.13.12-alpine
COPY --from=node /code/src/webapp/dist/out/ /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
COPY server_conf/nginx.conf /etc/nginx/conf.d
