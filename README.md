# JUT Marketplace API

A simple marketplace API built with Python, Flask, and Docker. This project demonstrates basic API development and containerization.

## Features

- View a list of available professionals.
- Retrieve a professional by ID.
- Return a 404 error when a professional is not found.
- Run the application inside a Docker container.

## Technologies Used

- Python
- Flask
- Docker
- Git and GitHub
- Linux (Ubuntu on WSL)

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check if the API is running |
| GET | `/professionals` | Get all professionals |
| GET | `/professionals/1` | Get a professional by ID |

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Diligentcreations/Practical-marketplace-api.git
cd Practical-marketplace-api
```

### 2. Build the Docker image

```bash
docker build -t jut-marketplace-api .
```

### 3. Run the container

```bash
docker run -d --name jut-api -p 5000:5000 jut-marketplace-api
```

### 4. Test the API

Open these URLs in your browser:

- `http://127.0.0.1:5000/`
- `http://127.0.0.1:5000/professionals`
- `http://127.0.0.1:5000/professionals/1`

## Docker Commands

View running containers:

```bash
docker ps
```

View application logs:

```bash
docker logs jut-api
```

Stop the container:

```bash
docker stop jut-api
```

Start it again:

```bash
docker start jut-api
```

## Objectives

This project was built as a practical exercise to learn API development, Docker image creation, container management, and Git-based version control.

## Future Improvements

- Connect the API to a database.
- Add automated tests.
- Implement CI/CD with GitHub Actions.
- Deploy the application to a cloud platform.
