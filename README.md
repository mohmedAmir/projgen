# projgen

**projgen** is a Python CLI tool to quickly generate project templates with a predefined structure.  
It helps you bootstrap new projects in **one command** instead of manually creating folders and files every time.

---

## Features

- Generate Python project templates with a single command.
- Templates can be easily extended or customized.
- Supports multiple template types (e.g., `backend`, `frontend`, `fullstack`, `library`).
- Automatically creates proper package structure with `__init__.py`.
- Includes example `main.py`, `tests/`, `requirements.txt`, and `README.md`.
- Supports **optional modules** like `auth`, `docker`, `ci`, and `logging`.
- Templates can be easily extended or customized.


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
projgen <template_type> <project_name> [--path "/path/to/projects"] [--with auth,docker,logging]

```
### Example
```bash
projgen backend my_backend_project --path "/path/to/projects" --with auth,logging

```

## Arguments


**template_type**
Type of project template to use (e.g., backend, frontend, fullstack, library).


**project_name**
Name of the project to be generated.

**--path (optional)**
Directory where the project will be created.
Default: current directory.

**--with (optional)**
Comma-separated list of optional modules to include:
auth, docker, ci, logging.

## Notes

- Available templates are defined inside the templates/ directory.

- You can add your own templates by creating a new folder under templates/.

- The generator automatically renders Jinja2 templates and replaces {{ project_name }} in files and folders.

## Generated Structure Example
For a backend template:

```
my_backend_project/
├── src/
│   └── {{ project_name }}/
│       ├── __init__.py
│       ├── main.py
│       ├── api/
│       ├── core/
│       ├── models/
│       ├── schemas/
│       ├── services/
│       └── db/
├── tests/
│   └── test_health.py
├── configs/
│   ├── settings.dev.yaml
│   └── settings.prod.yaml
├── optional/
│   ├── auth/
│   ├── docker/
│   ├── logging/
│   └── ci/
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

