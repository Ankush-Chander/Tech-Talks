# Graphs — ACM Summer School 2026

## Self-hosting with MkDocs

### Prerequisites

- Python 3.8+
- pip

### Quick start

You can download just this `graphs/` folder without cloning the full repository:

**Option A — Download as ZIP (recommended)**

1. Go to the [`graphs/` directory on GitHub](https://github.com/Ankush-Chander/Tech-Talks/tree/master/graphs)
2. Click **Code → Download Folder** (or use a tool like [GitZip](http://gitzip.org/) to grab only this subtree)
3. Extract the ZIP

**Option B — Sparse checkout**

```bash
git clone --filter=blob:none --sparse https://github.com/Ankush-Chander/Tech-Talks.git
cd Tech-Talks
git sparse-checkout set graphs
mv graphs/* . && rm -rf graphs
```

Then continue with:

```bash
# Install dependencies
pip install -r requirements.txt

# Start the dev server
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