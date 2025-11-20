# 📘 Assignment: REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using the FastAPI framework. Students will learn to create endpoints, validate request and response models with Pydantic, and run the app locally with `uvicorn`.

## 📝 Tasks

### 🛠️ Create a Basic API

#### Description
Create an API with endpoints to list, create, update, and delete a resource (for example, "items" or "notes"). Use Pydantic models for request validation and response serialization.

#### Requirements
Completed program should:

- Define at least GET, POST, PUT (or PATCH), and DELETE endpoints for a single resource.
- Use `pydantic` models to validate request bodies (e.g., ItemCreate, ItemUpdate).
- Return correct HTTP status codes (201 for created, 404 for not found, etc.).
- Keep all data in memory (a dictionary or list is fine for this exercise).

### 🛠️ Add Validation and Documentation

#### Description
Add data validation rules and use FastAPI's automatic OpenAPI docs to expose the API.

#### Requirements
Completed program should:

- Validate fields (required fields, max length, data types) in Pydantic models.
- Use path and query parameters (e.g., `GET /items/{id}` and `GET /items?limit=10`).
- Document example payloads by using `example` in Pydantic model `Field` definitions.
- The project's API must be accessible with interactive docs at `/docs` when the app is running.


---

## ✅ Optional Enhancements

- Add pagination, filtering, or search to the list endpoint.
- Add authentication (e.g., simple API key) to protect certain endpoints.
- Add basic unit tests for endpoints using `requests` or `httpx` and `pytest`.
- Containerize the app with Docker.

## 📎 Attachments

- Starter code is included: `starter-code.py` (a minimal FastAPI app skeleton).

## 💡 Run locally

Install dependencies and run the app with `uvicorn`:

```bash
python3 -m pip install fastapi uvicorn
uvicorn starter-code:app --reload
```

Open http://localhost:8000/docs to view interactive API docs.
