import os
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import shutil

class Renderer:
    def __init__(self, template_dir: Path, output_dir: Path, project_name: str):
        self.template_dir = template_dir
        self.output_dir = output_dir
        self.project_name = project_name
        self.env = Environment(loader=FileSystemLoader(template_dir), keep_trailing_newline=True)

    def render_template_dir(self, template_name: str):
        if self.output_dir.exists():
            raise FileExistsError(f"Directory {self.output_dir} already exists")

        for root, dirs, files in os.walk(self.template_dir):
            rel_path = Path(root).relative_to(self.template_dir)
            target_dir = self.output_dir / str(rel_path).replace("{{ project_name }}", template_name)
            target_dir.mkdir(parents=True, exist_ok=True)



            for f in files:
                src_file = Path(root) / f
                dest_file = target_dir / f.replace(".j2", "").replace("{{ project_name }}", template_name)
                if f.endswith(".j2"):
                    template_path = str(rel_path / f).replace("\\", "/")
                    template = self.env.get_template(template_path)
                    content = template.render(project_name=self.project_name)
                    with open(dest_file, "w", encoding="utf-8") as out:
                        out.write(content)
                    print(f"[TEMPLATE] {dest_file}")
                else:
                    shutil.copy2(src_file, dest_file)
                    print(f"[COPY] {dest_file}")

    # ---------- render a feature adapter ----------

    def render_feature_adapter(self, feature_name: str, adapter_dir: Path):
        adapter_dir = Path(adapter_dir)
        if not adapter_dir.exists():
            print(f"[SKIP] Adapter '{feature_name}' not found at {adapter_dir}")
            return

        # استخدام folder "files" إذا موجود
        adapter_files_dir = adapter_dir / "files" / "src" if (adapter_dir / "files" / "src").exists() else adapter_dir

        # المسار الأساسي داخل المشروع: src/<template_name>
        project_dir = self.output_dir / "files" / "src" / self.template_dir.name / feature_name  # هنا نضيف feature_name كـ folder

        for root, dirs, files in os.walk(adapter_files_dir):
            rel_path = Path(root).relative_to(adapter_files_dir)  # فقط المسار النسبي داخل adapter_files_dir
            target_dir = project_dir / rel_path
            target_dir.mkdir(parents=True, exist_ok=True)

            
            for f in files:
                src_file = Path(root) / f
                dest_file = target_dir / f.replace(".j2", "")
                if f.endswith(".j2"):
                    env = Environment(loader=FileSystemLoader(adapter_dir), keep_trailing_newline=True)
                    template_path = str(rel_path / f).replace("\\", "/")
                    template = env.get_template(template_path)
                    content = template.render(project_name=self.project_name)
                    with open(dest_file, "w", encoding="utf-8") as out:
                        out.write(content)
                    print(f"[FEATURE TEMPLATE] {feature_name}: {dest_file}")
                else:
                    shutil.copy2(src_file, dest_file)
                    print(f"[FEATURE COPY] {feature_name}: {dest_file}")

