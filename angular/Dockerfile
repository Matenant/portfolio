FROM node:latest
WORKDIR /var/www/html/portfolio

COPY . .

RUN npm install -g @angular/cli && npm install

CMD ["ng", "serve", "--host", "0.0.0.0", "--poll", "500"]
