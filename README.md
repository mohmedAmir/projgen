# projgen

**projgen** is a Python CLI tool to quickly generate Python project templates with a predefined structure.  
It helps you bootstrap new projects in **one command** instead of manually creating folders and files every time.

---

## Features

- Generate Python project templates with a single command.
- Supports multiple template types: `backend`, `frontend`, `fullstack`, `library`.
- Automatically creates proper package structure with `__init__.py` in your source folders.
- Includes example `main.py`, `tests/`, `requirements.txt`, and `README.md`.
- Supports **optional modules/features** like `auth`, `docker`, `ci`, and `logging`.
- Features are **modular plugins**; you can add your own or extend existing ones.
- Templates and features are rendered with Jinja2 and respect folder structure.

---

---

## Installation

 Clone the repo
```bash
git clone https://github.com/yourusername/projgen.git
cd projgen
```

### Optional: create virtual environment:

```bash
python -m venv venv

source venv/bin/activate  # Linux/Mac

venv\Scripts\activate     # Windows
```
### Install projgen locally (editable)
```bash
pip install -e .
```


## Usage

### Generate a new project from any template
```
projgen new <project_name> --template <template_type> [--features auth,docker,ci,logging] [--path "/path/to/projects"]


```
### Example
```bash
 projgen new myapp --template backend --features auth --path "/path/to/projects"

```

## Arguments


**template_type**
Type of project template to use (e.g., backend, frontend, fullstack, library).

**project_name**
Name of the project to generate.

**--template**
Template type to use (backend, frontend, fullstack, library). Default: backend.

-**--path (optional)**
Directory where the project will be created. Default: current directory.

**--features (optional)**
Comma-separated list of optional features/modules to include: auth, docker, ci, logging.

## Notes

- Available templates are in the templates/ directory.

- Features are inside features/ and automatically integrated into your project.

- Jinja2 templates automatically replace {{ project_name }} in files and folders.

- The generator preserves folder structures from templates and features; it will not create unnecessary nested folders.
## Generated Structure Example
For a backend template:

```
my_backend_project/
├── files/
│   └── src/
│       └── backend/
│           ├── auth/          # if auth feature included
│           │   ├── jwt.py
│           │   └── routes.py
│           ├── __init__.py
│           ├── main.py
│           ├── api/
│           ├── core/
│           ├── models/
│           ├── schemas/
│           ├── services/
│           └── db/
├── tests/
│   └── test_health.py
├── configs/
│   ├── settings.dev.yaml
│   └── settings.prod.yaml
├── requirements.txt
├── pyproject.toml
└── README.md

```

## Requirements
```
Python 3.10+

Jinja2 >= 3.1

FastAPI >= 0.100 (for backend template)

Uvicorn[standard] >= 0.22 (for backend template)

Pytest >= 7.0 (for tests)
```
## License

This project is licensed under the MIT License.

