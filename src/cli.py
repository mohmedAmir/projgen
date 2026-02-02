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
    new_parser.add_argument("--template", type=str, default="fastapi")
    new_parser.add_argument(
    "--features",
    type=str,
    default="",
    help="Comma-separated list of features"
)

    new_parser.add_argument("--path", type=str, default=".")

    args = parser.parse_args()
    features_list = [f.strip() for f in args.features.split(",") if f.strip()]


    if args.command == "new":
        output_dir = Path(args.path) / args.project_name
        context = Context(args.project_name, args.template, output_dir, features_list)

        # Load plugins
        features_root = Path(__file__).resolve().parent / "features"
        plugins = load_plugins(features_root, features_list)
        for p in plugins:
            p.register(context)

        # Render base template
        template_root = Path(__file__).resolve().parents[1] / "templates" / args.template
        renderer = Renderer(template_root, output_dir, args.project_name)
        renderer.render_template_dir(template_name=args.template)

        # If auth feature is included, render its adapter files
        for p in plugins:
            # path to features directory
            adapter_dir = features_root / p.name / "adapters" / args.template / "files"

            # fall back to generic files if no adapter exists
            if not adapter_dir.exists():
                adapter_dir = features_root / p.name / "files"

            renderer.render_feature_adapter(p.name, adapter_dir)

        # Apply plugin logic
        for p in plugins:
            p.apply(context)
        for p in plugins:
            p.after(context)

        print(f"Project '{args.project_name}' generated successfully at {output_dir}")

if __name__ == "__main__":
    main()
