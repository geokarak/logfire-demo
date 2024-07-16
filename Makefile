.ONESHELL:

.PHONY: venv
venv: pyproject.toml
	rm -rf ./.venv
	python -m venv .venv
	./.venv/bin/pip install --upgrade pip
	./.venv/bin/pip install uv
	./.venv/bin/python -m uv pip install -e .