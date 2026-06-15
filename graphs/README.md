# Graphs — ACM Summer School 2026

## Self-hosting with MkDocs

### Prerequisites

- Python 3.8+
- pip

### Quick start

```bash
# 1. Clone the repository
git clone <repo-url>
cd graphs

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start the dev server
mkdocs serve
```

The site will be available at `http://localhost:8000`.

### Building for production

```bash
mkdocs build
```

This creates a static `_site/` directory you can serve with any HTTP server (nginx, caddy, etc.).

### Dockerised deployment

Build the image and run:

```bash
docker build -t tech-talks-graphs .
docker run -d -p 8000:8000 tech-talks-graphs
```

### Configuration

See `mkdocs.yml` for navigation structure, theme settings, and plugin options.

### Stack

| Component          | Purpose                    |
|--------------------|----------------------------|
| MkDocs             | Static site generator      |
| mkdocs-material    | Material theme             |
| mkdocs-jupyter     | Render Jupyter notebooks   |
| mkdocs-slides      | Slides support             |
| mkdocs-to-pdf      | PDF export                 |