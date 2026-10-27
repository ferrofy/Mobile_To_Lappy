# Contributing

Contributions and suggestions are welcome. For significant changes, open an
issue first to discuss the proposed approach.

## Before You Start

- Read the [Code of Conduct](CODE_OF_CONDUCT.md).
- For security vulnerabilities, follow [SECURITY.md](SECURITY.md) instead of
  opening a public issue.

## Development Setup

1. Fork and clone the repository.
2. From the project directory, create and activate a virtual environment:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   On macOS or Linux, use `python3 -m venv .venv` and
   `source .venv/bin/activate`.
3. Install dependencies with `python -m pip install -r requirements.txt`.
4. Run the app with `python Run.py`.

## Changes and Verification

- Keep changes focused and follow the existing Python, HTML, CSS, and
  JavaScript conventions.
- Test the app locally: confirm the page loads, **Test Upload** sends text to
  the server terminal, and **Write Text** types into the intended focused
  application.
- There is no automated test suite configured at this time. Mention the
  checks you performed in your pull request.
- Update relevant documentation when behavior or setup instructions change.

## Pull Requests

Use a clear title and explain what the change does, why it is needed, and how
you verified it. Link related issues and include screenshots for visible UI
changes when useful.