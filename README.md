# CI/CD Flask Demo

This project demonstrates a Continuous Integration and Continuous Deployment (CI/CD) pipeline for a Flask application, utilizing GitHub, Jenkins, and Docker.

## Project Structure

- **app/**: Contains the main Flask application code.
- **tests/**: Contains unit tests for the Flask app.
- **Dockerfile**: Used to build the Docker image for the Flask app.
- **Jenkinsfile**: Defines the CI/CD pipeline steps.
- **requirements.txt**: Lists the Python dependencies for the Flask app.

## Requirements

To run and test this project, ensure you have the following installed:

- Docker
- Jenkins (with Docker integration)
- Python 3.x
- Git

## CI/CD Pipeline

The pipeline follows these steps:

1. **Build**: Builds a Docker image for the Flask app based on the `Dockerfile`.
2. **Test**: Runs unit tests using the `unittest` framework to verify the integrity of the application.
3. **Deploy**: Pushes the Docker image to Docker Hub and deploys it to a production environment.

### Pipeline Setup with Jenkins

The `Jenkinsfile` outlines the stages:

1. **Clone Repository**: Jenkins pulls the latest code from GitHub.
2. **Build Docker Image**: Jenkins builds the Docker image using the `Dockerfile`.
3. **Run Tests**: The pipeline executes tests defined in the `tests/` folder.
4. **Push Docker Image**: If the tests pass, the Docker image is pushed to Docker Hub.
5. **Deploy**: Deploy the application to the target environment using the latest Docker image.

## Docker

To build and run the Flask app locally using Docker:

```bash
# Build the Docker image
docker build -t flask_demo .

# Run the container
docker run -d -p 5000:5000 flask_demo
```

## API Usage
After successful deployment, the API will be available at:

```ruby
http(s)://coolscientist.tech/todo/api/v1/tasks
```
Here are the routes available in the API:

### GET `/todo/api/v1/tasks`
Returns a list of all tasks.

#### Example Response:

```json
{
  "1": {
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, Cheese, Pizza, Fruit, Tylenol",
    "done": false
  },
  "2": {
    "id": 2,
    "title": "Learn Python",
    "description": "Need to find a good Python tutorial on the web",
    "done": false
  }
}
```
### GET `/todo/api/v1/tasks/<int:task_id>`
Returns a single task by task_id.

### Example Response:

```json
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Milk, Cheese, Pizza, Fruit, Tylenol",
  "done": false
}
```
### POST `/todo/api/v1/tasks`
Creates a new task.

#### Example Request:

```json
{
  "title": "Read a book",
  "description": "Read 'Sapiens: A Brief History of Humankind'"
}
```
#### Example Response:

```json
{
  "id": 3,
  "title": "Read a book",
  "description": "Read 'Sapiens: A Brief History of Humankind'",
  "done": false
}
```
### PUT `/todo/api/v1/tasks/<int:task_id>`
Updates an existing task with the provided task_id.

#### Example Request:

```json
{
  "title": "Buy more groceries",
  "done": true
}
```
#### Example Response:

```json
{
  "Updated Task": {
    "id": 1,
    "title": "Buy more groceries",
    "description": "Milk, Cheese, Pizza, Fruit, Tylenol",
    "done": true
  }
}
```
### DELETE `/todo/api/v1/tasks/<int:task_id>`
Deletes the task with the provided task_id.

#### Example Response:

```json
{
  "result": true
}
```

## Running Tests
The application includes unit tests located in the tests/ directory. To run the tests:

```bash
python3 -m unittest discover tests
```
## License
This project is licensed under the MIT License. See the LICENSE file for details.
