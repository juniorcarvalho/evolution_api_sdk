# AGENTS.md

Operational guide for coding agents working in `evolution_api_sdk`.

## 1) Project Snapshot
- Language: Python (`>=3.9`)
- Packaging: `pyproject.toml` + `hatchling`
- Dependency/venv workflow: `uv`
- Main package path: `evolution_api_sdk/`
- Tests path: `tests/`
- Lint + format: `ruff`
- Type checking: `mypy`

## 2) Cursor/Copilot Rule Files

Checked locations:
- `.cursorrules`
- `.cursor/rules/`
- `.github/copilot-instructions.md`

Current result:
- No Cursor rules found.
- No Copilot instruction file found.

If these files are added later, treat them as higher-priority repository policy and update this document.

## 3) Setup and Environment

Preferred setup:
```bash
uv sync --dev
```

If shell activation is needed:
```bash
source .venv/bin/activate
```

## 4) Build/Lint/Test Commands

Build artifacts (wheel + sdist):
```bash
uv build
```

Lint:
```bash
uv run ruff check .
```

Format:
```bash
uv run ruff format .
```

Type-check (repo is not `src/` layout):
```bash
uv run mypy evolution_api_sdk
```

Run all tests:
```bash
uv run pytest
```

Run a single test file:
```bash
uv run pytest tests/test_client.py
```

Run a single test function (node id):
```bash
uv run pytest tests/test_client.py::test_get_success
```

Run tests by expression:
```bash
uv run pytest -k "get_success"
```

Run with coverage:
```bash
uv run pytest --cov=evolution_api_sdk --cov-report=term-missing
```

Recommended pre-PR validation:
```bash
uv run ruff format . && uv run ruff check . && uv run mypy evolution_api_sdk && uv run pytest
```

## 5) Test Suite Notes

- Unit tests: `tests/test_client.py`, `tests/test_service_instance.py`, `tests/test_model_instance.py`.
- Integration/manual test: `tests/test_create_instance_api.py`.
- Integration file uses `EVOLUTION_API_URL` and `EVOLUTION_API_KEY`; values are empty by default.
- Do not include integration test in automated CI unless credentials/environment are configured.

## 6) Code Style Guidelines

Rules come from `pyproject.toml` and current code patterns.

### Imports
- Respect Ruff isort rules (`I`).
- Import order: stdlib -> third-party -> local package.
- Prefer explicit symbol imports; avoid wildcard imports.
- Keep imports grouped logically and sorted.

### Formatting
- Line length is `120`.
- Use `uv run ruff format .` as formatter of record.
- Quote style is single quotes where formatter applies it.
- Keep files free of trailing whitespace and inconsistent spacing.

### Types
- All functions/methods should be typed (`disallow_untyped_defs = true`).
- Always include return annotations.
- Use specific types over broad ones when practical.
- When evolving APIs, preserve public signatures unless change is intentional and tested.

### Naming
- Functions, methods, locals: `snake_case`.
- Classes/exceptions/enums: `PascalCase`.
- Constants: `UPPER_SNAKE_CASE`.
- Preserve external Evolution API keys in payloads (`instanceName`, `byEvents`, etc.).
- Do not normalize external payload keys to snake_case unless a translation layer is explicit.

### Error Handling
- Raise SDK domain exceptions from `evolution_api_sdk.exception` for API-level failures.
- Include useful context in error messages (status code and response detail when possible).
- Catch specific exception types where possible; avoid bare `except` in new code.
- In tests, assert exception type and relevant message content for behavioral checks.

### API and Service Conventions
- Keep endpoint path construction centralized in client/service methods.
- Keep service methods thin: shape inputs, delegate transport to `EvolutionClient`.
- Convert payload models via `to_dict()` before transport.
- Omit `None` fields in payload objects where sparse payloads are expected.
- Avoid side effects in model constructors beyond normal field assignment/normalization.

## 7) Test Authoring Guidelines

- Use `pytest` fixtures for shared setup.
- Use `unittest.mock.patch`/`Mock` for HTTP isolation.
- Keep tests deterministic and offline by default.
- Name tests as `test_<behavior>`.
- Assert both returned values and mocked client call contracts.

## 8) Change Management for Agents

- Keep diffs focused and minimal.
- Do not silently change behavior without corresponding tests.
- If request/response logic changes, update/add tests in related test modules.
- If adding new public models/services, export them via package `__init__` where appropriate.
- Run format, lint, type-check, and tests before handing off work.
