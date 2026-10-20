# Personal website

A static GitHub Pages site, rendered locally with Jinja. No Python or JavaScript
is required on the hosting server.

## Where to edit

- **`content.yaml`** — name, bio, social links, and ordered list of projects.
  Bio, project descriptions, responsibilities, and other-work text support Markdown
  (e.g. `[link text](https://example.com)` and `**bold**`).
- **`templates/index.html.jinja`** — HTML layout and project loop.
- **`style.css`** — styling, unchanged by the build.
- **`index.html`** — generated output; don't edit directly.

Markdown is trusted, repository-authored content and may include raw HTML. Other
values are HTML-escaped by Jinja; missing required template values fail the build.

## Setup and build

Requires Python 3.10+.

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python build.py
```

After editing content or the template, run `python build.py` again. Commit the
source changes **and the regenerated `index.html`**. The existing GitHub Pages
branch-based deployment can keep serving the root directory without a new build
workflow or hosting configuration.

To add a project, copy an existing entry under `projects` in `content.yaml`.
Projects appear in file order. `responsibilities` and `tech` can be omitted;
`responsibilities_label` optionally overrides “Responsible for:”. Quote YAML
strings containing a colon followed by a space, and use `|` for multi-paragraph
Markdown or `>-` for a paragraph wrapped across multiple source lines.

## Preview

```sh
python -m http.server 8000
```

Open <http://localhost:8000> and refresh after rebuilding. This development server
serves the repository, including source files; it is not a production server.
