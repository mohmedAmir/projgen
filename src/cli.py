import argparse
from pathlib import Path
from src.engine.context import Context
from src.engine.loader import load_plugins
from src.engine.renderer import Renderer

def main():
    parser = argparse.ArgumentParser(description="ProjGen CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    new_parser = subparsers.add_parser("new", help="Create new project")
    new_parser.add_argument("project_name", type=str)
    new_parser.add_argument("--template", type=str, default="backend")
    new_parser.add_argument("--features", type=str, nargs="+", default=[])
    new_parser.add_argument("--path", type=str, default=".")

    args = parser.parse_args()
    if args.command == "new":
        output_dir = Path(args.path) / args.project_name
        context = Context(args.project_name, args.template, output_dir, args.features)

        # Load plugins
        features_root = Path(__file__).resolve().parent / "features"
        plugins = load_plugins(features_root, args.features)
        for p in plugins:
            p.register(context)

        # Render base template
        template_root = Path(__file__).resolve().parents[1] / "templates" / args.template
        renderer = Renderer(template_root, output_dir, args.project_name)
        renderer.render_template_dir(template_name=args.template)

        # Render feature adapters
        for p in plugins:
            adapter_dir = features_root / p.name / "adapters" / args.template / "files"
            renderer.render_feature_adapter(p.name, adapter_dir)

        # Apply plugin logic
        for p in plugins:
            p.apply(context)
        for p in plugins:
            p.after(context)

        print(f"Project '{args.project_name}' generated successfully at {output_dir}")

if __name__ == "__main__":
    main()
