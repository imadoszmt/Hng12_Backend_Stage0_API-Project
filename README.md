# Hng12_Backend_Stage0_API-Project

This project is a simple FastAPI application that serves a public API to retrieve basic information as specified in the task requirements.

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/Hng12_Backend_Stage0_API-Project.git
   cd Hng12_Backend_Stage0_API-Project
   ```

2. Create a virtual environment:
   ```
   python3 -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```
   pip3 install -r requirements.txt
   ```

5. Run the application:
   ```
   uvicorn app.main:app --reload
   ```

## API Documentation

### Endpoint

- **GET** `/`

### Response Format

```json
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/repo"
}
```

### Example Usage

You can test the API using a tool like Postman or curl:

```bash
curl http://localhost:8000/
```

## Deployment

This API is deployed on Railway and can be accessed at:
https://hng12backendstage0api-project-production.up.railway.app

## Head up to HNG Talents pool to meet a lot of skilled developers.

- [Python Developers](https://hng.tech/hire/python-developers)
- [C# Developers](https://hng.tech/hire/csharp-developers)
- [Go Developers](https://hng.tech/hire/golang-developers)
- [PHP Developers](https://hng.tech/hire/php-developers)
- [Java Developers](https://hng.tech/hire/java-developers)
- [Node.js Developers](https://hng.tech/hire/nodejs-developers)