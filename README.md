# Fast-API-Login

## Clone the repository
```sh
git clone https://github.com/dikshadutt08/fast-api-login.git
```

## Create virtual environment
```sh
python -m venv fast-api-venv
```

## Activate the virtual environment
```sh
cd fast-api-venv
Scripts\activate
```

## Installation of Requirements
```sh
cd fast-api-login
pip install -r requirements.txt
```

## Database Connectivity
It has been done using SQLite

## Run the server for the app locally
```sh
uvicorn main:app --reload
```

## Swagger UI
Put '/docs' after your localhost url.

## Docker Containerization
```sh
docker compose-up
```
