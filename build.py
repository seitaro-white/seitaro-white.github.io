"""Render the static homepage from content.yaml and the Jinja template."""

from pathlib import Path

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined
from markupsafe import Markup

ROOT = Path(__file__).resolve().parent


def render_markdown(text: str) -> Markup:
    # Only use with repository-authored content: Markdown permits raw HTML.
    return Markup(markdown.markdown(text))


def main() -> None:
    content = yaml.safe_load((ROOT / "content.yaml").read_text(encoding="utf-8"))
    environment = Environment(
        loader=FileSystemLoader(ROOT / "templates"),
        autoescape=True,
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
    )
    environment.filters["markdown"] = render_markdown
    html = environment.get_template("index.html.jinja").render(content)
    (ROOT / "index.html").write_text(html, encoding="utf-8")
    print("Built index.html")


if __name__ == "__main__":
    main()
