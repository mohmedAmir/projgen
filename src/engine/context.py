from pathlib import Path
import shutil


class Context:
    def __init__(
        self,
        project_name: str,
        template: str,
        output_dir: Path,
        features: list[str],
    ):
        self.project_name = project_name
        self.template = template
        self.output_dir = output_dir
        self.features = features

    # ---------- filesystem helpers ----------

    def copy_tree(self, src: Path, dest: Path):
        if not src.exists():
            return
        shutil.copytree(src, dest, dirs_exist_ok=True)

    def render_feature_files(self, feature: str, adapter: str, features_root: Path):
        src = (
            features_root
            / feature
            / "adapters"
            / adapter
            / "files"
        )
        dest = self.output_dir / "src" / self.project_name
        self.copy_tree(src, dest)

    # ---------- validation helpers ----------

    def require_template(self, allowed: list[str], feature: str):
        if self.template not in allowed:
            raise RuntimeError(
                f"Feature '{feature}' not supported for template '{self.template}'"
            )
