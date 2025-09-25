# fastapi_cicd

**FastAPI project** with **pytest unit tests** and **GitHub Actions CI/CD**.  
This simple project was demonstrated in the **Software Engineering Laboratory (SEL)** course during **Spring '25 Semester** at **Premier University**.


---

## Project summary

A small FastAPI application whose entry point is `src/main.py`. Unit tests live in the `test/` folder and the project is validated and deployed using GitHub Actions.

---

## Table of Contents

- [Repo structure](#repo-structure)
- [Prerequisites](#prerequisites)
- [Quickstart / Install](#quickstart--install)
- [Run locally](#run-locally)
- [Run tests](#run-tests)
---

## Repo structure

```
fastapi_cicd/
├── src/
│   └── main.py           # FastAPI app (driver)
├── test/
│   └── test_main.py      # pytest unit tests for main.py
├── requirements.txt      # (optional) project dependencies
├── README.md
└── .github/
    └── workflows/
        └── ci.yml        # GitHub Actions workflow (CI)
```
---

## Quickstart / Install

1. Clone the repo

```bash
git clone https://github.com/sazid51/fastapi_cicd.git
cd fastapi_cicd
```

2. Create and activate a virtual environment:

```bash
# Unix / macOS
python -m venv venv
source venv/bin/activate

# Windows (cmd)
python -m venv venv
venv\Scripts\activate

# Windows (PowerShell)
python -m venv venv
venv\Scripts\Activate.ps1
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run locally

Start the FastAPI server (from the repository root):

```bash
# run with uvicorn, using the module path to the app
uvicorn src.main:api --reload --host 127.0.0.1 --port 8000
```

Open `http://127.0.0.1:8000/docs` for Swagger UI

---

## Run tests

Run all tests with pytest from the repo root:

```bash
pytest
```

