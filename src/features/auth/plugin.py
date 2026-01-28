# features/auth/plugin.py
from pathlib import Path
from src.engine.plugin import FeaturePlugin

class AuthPlugin(FeaturePlugin):
    name = "auth"

    def register(self, context):
        print(f"[REGISTER] AuthPlugin for {context.project_name}")

    def apply(self, context):
        print(f"[APPLY] AuthPlugin for {context.project_name}")
        context.require_template(["backend", "fullstack"], self.name)
        
        features_root = Path(__file__).resolve().parents[2]
        context.render_feature_files(self.name, context.template, features_root)

    def after(self, context):
        print(f"[AFTER] AuthPlugin for {context.project_name}")
