# Contributing

Contributions are very welcome.
Please file issues or submit pull requests in our [GitHub repository][repo].
All contributors will be acknowledged,
but must abide by our Code of Conduct.

## Setup

-   `uv venv` to create a virtual environment
-   `source .venv/bin/activate` to activate it
-   `make setup` to complete installation
-   `make` on its own for a list of available commands

## Organization

-   JavaScript source and CSS is in `js/src`
-   Python source is in `src/faw`
-   `src/faw/static` holds built version of JavaScript that is included in Python package
-   Markdown documentation pages are in `pages`, and Python documentation is built to `docs` using `mkdocs`

## Learn More

-   [AnyWidget documentation][anywidget]
-   [Marimo documentation][marimo]

[anywidget]: https://anywidget.dev/
[marimo]: https://marimo.io/
[repo]: https://github.com/gvwilson/faw
