# features/logging/plugin.py
from pathlib import Path
from src.engine.plugin import FeaturePlugin

class LoggingPlugin(FeaturePlugin):
    name = "logging"

    def register(self, context):
        print(f"[REGISTER] LoggingPlugin for {context.project_name}")

    def apply(self, context):
        print(f"[APPLY] LoggingPlugin for {context.project_name}")
        context.require_template(["fastapi", "fullstack"], self.name)
        
        features_root = Path(__file__).resolve().parents[2]
        context.render_feature_files(self.name, features_root)

    def after(self, context):
        print(f"[AFTER] LoggingPlugin for {context.project_name}")
