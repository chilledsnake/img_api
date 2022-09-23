# url_shortener

This api allows you to resize and store your common formats images.

## Installation requirements
Docker, docker-compose

## Installation
Just
```bash
docker-compose up
```

## Usage

allowed hosts: localhost, 0.0.0.0, 127.0.0.1

api documentation on localhost:8000 (swagger)

## Stack
- Python
- Django
- DRF
- Postgres
- Gunicorn
- Swagger
- Docker
- docker-compose
- poetry
- Pillow

## Contributing
Feel free to comment

## Notes
I've removed .env file from .gitignore deliberately so You can fire up the project without any inconveniences :) 
If You'd like to use AWS S3 then you need to fill .env fields:
USE_AWS_S3=1
AWS_ACCESS_KEY_ID=<your aws key>
AWS_SECRET_ACCESS_KEY=<your aws secret key>
AWS_STORAGE_BUCKET_NAME=<your aws bucket name>
