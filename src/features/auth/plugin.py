from pathlib import Path
from src.engine.plugin import FeaturePlugin

class AuthPlugin(FeaturePlugin):
    name = "auth"

    def apply(self, ctx):
        features_root = Path(__file__).resolve().parents[2]

        #try to find adapter files for the current template
        adapter_path = features_root / self.name / "adapters" / ctx.template / "files"

        # use adapter files if they exist, otherwise use generic files
        if adapter_path.exists():
            src = adapter_path
        else:
            src = features_root / self.name / "files"

        dest = ctx.output_dir / "src" / ctx.project_name
        ctx.copy_tree(src, dest)
