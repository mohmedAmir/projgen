from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import shutil
import os


class Renderer:
    """
    Renderer for project templates and feature adapters.
    Uses Jinja2 to render files and copies non-template files.
    Works with Context and FeaturePlugin system.
    """

    def __init__(self, template_dir: Path, output_dir: Path, project_name: str):
        self.template_dir = template_dir
        self.output_dir = output_dir
        self.project_name = project_name

        self.env = Environment(
            loader=FileSystemLoader(template_dir),
            keep_trailing_newline=True
        )

    # ---------- render base template ----------
    def render_template_dir(self, template_name: str):
        if self.output_dir.exists():
            raise FileExistsError(f"Directory {self.output_dir} already exists")

        for root, dirs, files in os.walk(self.template_dir):
            rel_path = Path(root).relative_to(self.template_dir)
            # replace {{ project_name }} in path
            target_dir = self.output_dir / str(rel_path).replace("{{ project_name }}", template_name)
            target_dir.mkdir(parents=True, exist_ok=True)

            for f in files:
                src_file = Path(root) / f
                # replace {{ project_name }} in filename
                dest_file = target_dir / f.replace(".j2", "").replace("{{ project_name }}", template_name)

                if f.endswith(".j2"):
                    template_path = str(rel_path / f).replace("\\", "/")
                    template = self.env.get_template(template_path)
                    # standard rendering with project_name
                    content = template.render(project_name=self.project_name)
                    with open(dest_file, "w", encoding="utf-8") as out:
                        out.write(content)
                    print(f"[TEMPLATE] {dest_file}")
                else:
                    shutil.copy2(src_file, dest_file)
                    print(f"[COPY] {dest_file}")


    # ---------- render a feature adapter ----------
    def render_feature_adapter(self, feature_name: str, adapter_dir: Path):
        
        # Copy and render all files from a feature adapter into the output_dir.
        # adapter_dir = features/<feature>/adapters/<template>/files
        
        if not adapter_dir.exists():
            print(f"[SKIP] Adapter for feature '{feature_name}' does not exist at {adapter_dir}")
            return

        # Feature files should go into src/project_name directory (same as base template)
        project_dir = self.output_dir / "src" / self.project_name

        for root, dirs, files in os.walk(adapter_dir):
            rel_path = Path(root).relative_to(adapter_dir)
            target_dir = project_dir / rel_path
            target_dir.mkdir(parents=True, exist_ok=True)

            for f in files:
                src_file = Path(root) / f
                dest_file = target_dir / f.replace(".j2", "")

                if f.endswith(".j2"):
                    # render with jinja2
                    env = Environment(
                        loader=FileSystemLoader(adapter_dir),
                        keep_trailing_newline=True
                    )
                    template_path = str(rel_path / f).replace("\\", "/")
                    template = env.get_template(template_path)
                    content = template.render(project_name=self.project_name)
                    with open(dest_file, "w", encoding="utf-8") as out:
                        out.write(content)
                    print(f"[FEATURE TEMPLATE] {feature_name}: {dest_file}")
                else:
                    shutil.copy2(src_file, dest_file)
                    print(f"[FEATURE COPY] {feature_name}: {dest_file}")
