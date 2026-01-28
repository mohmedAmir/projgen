# projgen/engine/loader.py
import importlib.util
from pathlib import Path
from src.engine.plugin import FeaturePlugin

def load_plugins(features_root: Path, selected: list[str]):
    plugins = []
    for name in selected:
        plugin_path = features_root / name / "plugin.py"
        
        if not plugin_path.exists():
            raise FileNotFoundError(f"Plugin not found at {plugin_path}. Features root: {features_root}")
        
        spec = importlib.util.spec_from_file_location(name, plugin_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        plugin_class = None
        for obj in vars(module).values():
            if isinstance(obj, type) and issubclass(obj, FeaturePlugin) and obj is not FeaturePlugin:
                plugin_class = obj
                break

        if not plugin_class:
            raise RuntimeError(f"No FeaturePlugin subclass found in {plugin_path}")

        plugins.append(plugin_class())
    return plugins
