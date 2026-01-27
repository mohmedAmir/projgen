from jinja2 import Environment, FileSystemLoader

class TemplateRenderer:
    def __init__(self, template_dir: str):
        self.env = Environment(
            loader=FileSystemLoader(template_dir),
            keep_trailing_newline=True,
        )

    def render_file(self, src_path, dest_path, context: dict):
        template = self.env.get_template(src_path)
        content = template.render(**context)

        with open(dest_path, "w", encoding="utf-8") as f:
            f.write(content)
