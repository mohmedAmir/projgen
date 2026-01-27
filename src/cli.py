import argparse
import sys
from src.engine.generator import ProjectGenerator, OPTIONAL_MODULES

def main():
    parser = argparse.ArgumentParser(description="projgen: Generate a Python project template")
    parser.add_argument("template_type", type=str, help="Type of template (e.g., backend)")
    parser.add_argument("project_name", type=str, help="The name of the project to generate")
    parser.add_argument("--path", type=str, default=".", help="Directory where the project will be created")

    # Optional modules flags
    parser.add_argument("--auth", action="store_true", help="Include auth module")
    parser.add_argument("--docker", action="store_true", help="Include docker module")
    parser.add_argument("--ci", action="store_true", help="Include CI/CD module")
    parser.add_argument("--logging", action="store_true", help="Include logging module")

    args = parser.parse_args()

    options = [mod for mod in OPTIONAL_MODULES if getattr(args, mod)]

    try:
        generator = ProjectGenerator(
            project_name=args.project_name,
            output_dir=args.path,
            template_type=args.template_type,
            options=options
        )
        generator.generate()

    # Handle errors gracefully
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except FileExistsError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
