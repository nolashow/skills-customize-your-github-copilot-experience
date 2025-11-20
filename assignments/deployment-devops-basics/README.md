# 📘 Assignment: Deployment & DevOps Basics (Docker + CI)

## 🎯 Objective

Students will learn the basics of packaging a Python FastAPI app into a Docker container and set up a continuous integration workflow using GitHub Actions to build and test the project automatically.

## 📝 Tasks

### 🛠️ Create a Dockerfile for the FastAPI app

#### Description
Write a `Dockerfile` that packages the FastAPI starter app (`assignments/fastapi-rest-apis/starter-code.py`) and starts it with `uvicorn`.

#### Requirements
Completed program should:

- Produce a small, efficient Docker image using a recent Python base image.
- Install dependencies from `requirements.txt` (or `pip install fastapi uvicorn`).
- Expose the app to port 8000 and run `uvicorn starter-code:app --host 0.0.0.0 --port 8000`.
- Be runnable locally with `docker build` and `docker run`.


### 🛠️ Add a simple GitHub Actions CI workflow

#### Description
Add a CI workflow that runs tests (if any) and builds the Docker image on each pull request or push to main.

#### Requirements
Completed program should:

- Include a `.yml` shown in the assignment (students will copy to `.github/workflows/`).
- Install dependencies and run test commands (you can stub a test command if not present, but structure the job to run it).
- Build a Docker image using `docker build` in the runner (or use `docker/build-push-action` for advanced students).


## ✅ Optional Enhancements

- Push the image to a container registry (Docker Hub or ghcr.io) using repository secrets.
- Add a deployment stage to the CI workflow to deploy to a cloud service or a VM.
- Use `docker-compose` to run multiple services if the app needs a database.


## 📎 Attachments

- `Dockerfile` (starter example)
- `docker-compose.yml` (optional helper to run)
- `sample-workflow.yml` (GitHub Actions example) 


## 💡 Run & Test Locally

1. Build the image from project root (or the assignment folder):

```bash
# from repository root
docker build -t mergington-fastapi -f assignments/fastapi-rest-apis/Dockerfile .
# Or if you added the Dockerfile here, run from this folder:
# docker build -t mergington-fastapi .

# Run the container
docker run -p 8000:8000 mergington-fastapi
```

2. Open http://localhost:8000/docs to verify the app is running.

---

This assignment pairs well with `REST APIs with FastAPI` — students can containerize the starter code and test CI on their repository.
