from pathlib import Path

dist = Path("dist")
dist.mkdir(exist_ok=True)

html = """<!doctype html>
<html lang="ko">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>DevOps CI/CD Assignment</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 720px;
            margin: 80px auto;
            padding: 0 20px;
            line-height: 1.7;
        }
        h1 { margin-bottom: 12px; }
        .ok { font-weight: bold; }
        code {
            background: #f3f3f3;
            padding: 2px 6px;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <h1>DevOps CI/CD Assignment</h1>
    <p class="ok">CI/CD pipeline deployed successfully.</p>
    <p>
        GitHub Actions automatically runs tests, builds this page,
        and deploys it to GitHub Pages.
    </p>
    <p><code>CI → Build → Deploy</code></p>
</body>
</html>
"""

(dist / "index.html").write_text(html, encoding="utf-8")
print("Build complete: dist/index.html")
