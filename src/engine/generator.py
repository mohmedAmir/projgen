import os
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import shutil

# List of optional modules
OPTIONAL_MODULES = ["auth", "docker", "ci", "logging"]


class ProjectGenerator:
    def __init__(self, project_name, output_dir=".", template_type="backend", options=None):
        self.project_name = project_name
        self.output_dir = os.path.join(output_dir, project_name)


        # template_dir points to project root -> templates/template_type
        self.template_dir = os.path.join(
            Path(__file__).resolve().parents[2],  # projgen root
            "templates",
            template_type
        )
        self.options = options or []

        if not os.path.exists(self.template_dir):
            raise FileNotFoundError(
                f"Template '{template_type}' does not exist at {self.template_dir}!"
            )

        # Initialize Jinja2 environment
        self.env = Environment(
            loader=FileSystemLoader(self.template_dir),
            keep_trailing_newline=True
        )

    # Copy and render template files
    def copy_and_render(self):
        if os.path.exists(self.output_dir):
            raise FileExistsError(f"Directory {self.output_dir} already exists!")

        for root, dirs, files in os.walk(self.template_dir):
            rel_path = os.path.relpath(root, self.template_dir)

            # Skip optional modules not selected
            if rel_path.startswith("optional"):
                parts = rel_path.split(os.sep)
                module_name = parts[1] if len(parts) > 1 else None
                if module_name not in self.options:
                    continue

            # Replace {{ project_name }} in directories
            target_dir = os.path.join(self.output_dir, rel_path.replace("{{ project_name }}", self.project_name))
            os.makedirs(target_dir, exist_ok=True)

            for file_name in files:
                src_file = os.path.join(root, file_name)
                dest_file = os.path.join(target_dir, file_name.replace(".j2", ""))

                # Render Jinja2 templates
                if file_name.endswith(".j2"):
                    template_path = file_name if rel_path == "." else str(Path(rel_path) / file_name).replace("\\", "/")
                    template = self.env.get_template(template_path)
                    content = template.render(project_name=self.project_name)
                    with open(dest_file, "w", encoding="utf-8") as f:
                        f.write(content)
                    print(f"[TEMPLATE] {dest_file}")
                else:
                    shutil.copy2(src_file, dest_file)
                    print(f"[COPY] {dest_file}")

    # Generate the project
    def generate(self):
        print(f"Generating project '{self.project_name}'...")
        self.copy_and_render()
        print(f"Project '{self.project_name}' created successfully at {self.output_dir}")
