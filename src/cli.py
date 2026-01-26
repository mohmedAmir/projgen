import argparse
from src.generator import ProjectGenerator
import sys

def main():
    parser = argparse.ArgumentParser(
        description="projgen: Generate a Python project template"
    )

    # Define command-line arguments
    parser.add_argument(
        "template_type",
        type=str,
        help="Type of template (e.g., backend, frontend)"
    )

    # Project name argument
    parser.add_argument(
        "project_name",
        type=str,
        help="The name of the project to generate"
    )

    # Optional path argument
    parser.add_argument(
        "--path",
        type=str,
        default=".",
        help="Directory where the project will be created"
    )

    args = parser.parse_args()

    try:
        generator = ProjectGenerator(
            project_name=args.project_name,
            output_dir=args.path,
            template_type=args.template_type
        )
        generator.generate()
    except FileNotFoundError as e:
        # Template type does not exist
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except FileExistsError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
