import time

import markdown
from pygments.formatters.html import HtmlFormatter

import tempfile
import webbrowser
from pathlib import Path

from agents import function_tool

@function_tool
def render_markdown_to_html_file(md_text: str) -> str:
    """When provided with Markdown text this function converts it to html and renders it onto the browser"""
    html_body = markdown.markdown(md_text, extensions=["fenced_code", "codehilite", "tables", "toc"])
    pygments_css = HtmlFormatter().get_style_defs('.codehilite')

    full_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Markdown Preview</title>
    <style>
        body {{
            max-width: 800px;
            margin: 2em auto;
            padding: 2em;
            background-color: #f5f5f5;
            font-family: Arial, sans-serif;
        }}
        .markdown-body {{
            background: white;
            padding: 2em;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }}
        {pygments_css}
    </style>
</head>
<body>
    <article class="markdown-body">
        {html_body}
    </article>
</body>
</html>"""

    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".html")
    output_path = tmp_file.name

    # Create the file
    Path(output_path).write_text(full_html, encoding="utf-8")
    webbrowser.open(f"file://{output_path}")
    time.sleep(5)
    # Delete the file afterward
    Path(output_path).unlink()
    return output_path