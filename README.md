# Blog API

## Description
This is a RESTful API for a blog application. The API provides endpoints to manage articles, comments, categories, and user authentication. It is my first venture into REST API's, will make improvements in subsequent projects as I learn more.

### Features
- **User Authentication**
    - Register an admin or a regular user
    - Email verification on signup
    - Login and logout functionality
    - Forgot password and change password features
- **Articles**
    - Create, read, update, and delete blog articles
    - Search functionality to find articles by keywords or categories
- **Comments**
    - Add comments to articles
- **Categories**
    - List available categories
- **API Interaction**
    - Token-based authentication for API access
    - Permissions to ensure article and comment ownership
    - Browse articles with search and filter options

## Installation
### To use this API locally:
- Clone this repository to a specified directory on your local machine.
- Ensure Python is installed on your local machine.
- Create a Python environment:
    ```bash
    python -m venv .venv
    ```
    and activate it:
    - On Windows:
      ```bash
      .venv\Scripts\activate
      ```
    - On Unix or MacOS:
      ```bash
      source .venv/bin/activate
      ```
- Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
- Set up the database:
    ```bash
    python manage.py migrate
    ```
- Start the development server:
    ```bash
    python manage.py runserver
    ```
- The API will be accessible at `http://localhost:8000/api/v1/article/`.

## Usage
- Register for a new account or log in if you already have one.
- Use token-based authentication for API access.
- Explore and interact with the available endpoints using tools like `curl`, `Postman`, or other API clients.
- Refer to the API documentation at thiis link `http://127.0.0.1:8000/api/schema/swagger-ui/#/` or OpenAPI schema for detailed information on available endpoints, request/response formats, and authentication methods.
