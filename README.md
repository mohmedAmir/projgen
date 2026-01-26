# projgen

**projgen** is a Python CLI tool to quickly generate project templates with a predefined structure.  
It helps you bootstrap new projects in **one command** instead of manually creating folders and files every time.

---

## Features

- Generate Python project templates with a single command.
- Supports multiple template types (e.g., `backend`, `frontend`, `api`).
- Automatically creates proper package structure with `__init__.py`.
- Includes example `main.py`, `tests/`, `requirements.txt`, and `README.md`.
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
projgen <template_type> <project_name> --path "/path/to/projects"
```
### Example
```bash
projgen backend my_backend_project --path "/path/to/projects"
```

### Arguments

**template_type**
Type of project template to use (e.g. backend, frontend, api, or any custom template).

**project_name**
Name of the project to be generated.

**--path (optional)**
Directory where the project will be created.
Default: current directory.

## Notes

Available templates are defined inside the templates/ directory.

You can add your own templates by creating a new folder under templates/.

## Generated Structure Example
For a backend template:

```
Copy code
my_backend_project/
├── src/
│   ├── __init__.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── README.md
└── requirements.txt
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

