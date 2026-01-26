import os
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import shutil


# Project Generator Class

class ProjectGenerator:
    # Initialize with project name and template directory
    def __init__(self, project_name, output_dir=".", template_type="backend"):
        self.project_name = project_name
        self.output_dir = os.path.join(output_dir, project_name)
        self.template_dir = os.path.join(
            os.path.dirname(__file__), f"../templates/{template_type}"
        )

        # Check if template directory exists
        if not os.path.exists(self.template_dir):
            raise FileNotFoundError(f"Template '{template_type}' does not exist at {self.template_dir}!")

        # Setup Jinja2 environment
        self.env = Environment(
            loader=FileSystemLoader(self.template_dir),
            keep_trailing_newline=True
        )

    # Copy and render templates
    def copy_and_render(self):
        if os.path.exists(self.output_dir):
            raise FileExistsError(f"Directory {self.output_dir} already exists!")

        # copy template files and render .j2
        for root, dirs, files in os.walk(self.template_dir):
            rel_path = os.path.relpath(root, self.template_dir)
            target_dir = os.path.join(self.output_dir, rel_path)
            os.makedirs(target_dir, exist_ok=True)

            for file_name in files:
                if file_name.endswith('.j2'):
                    # render Jinja2 template
                    template_path = file_name if rel_path == "." else str(Path(rel_path) / file_name).replace("\\", "/")
                    template = self.env.get_template(template_path)
                    output_content = template.render(project_name=self.project_name)
                    output_file_name = file_name[:-3]  # remove .j2
                    with open(os.path.join(target_dir, output_file_name), 'w', encoding='utf-8') as f:
                        f.write(output_content)
                else:
                    # copy other files as they are
                    shutil.copy2(os.path.join(root, file_name), os.path.join(target_dir, file_name))

    # Generate the project
    def generate(self):
        print(f"Generating project '{self.project_name}'...")
        self.copy_and_render()
        print(f"Project '{self.project_name}' created successfully at {self.output_dir}")
