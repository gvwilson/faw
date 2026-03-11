.PHONY: docs
all: commands

## commands: show available commands
commands:
	@grep -h -E '^##' ${MAKEFILE_LIST} \
	| sed -e 's/## //g' \
	| column -t -s ':'

## build: build package
build:
	@cd js && npm run build
	@python -m build

## check: check Python code issues
check:
	@ruff check .

## clean: clean up
clean:
	@rm -rf ./dist ./src/faw/static
	@find . -path './.venv' -prune -o -type d -name '__pycache__' -exec rm -rf {} +
	@find . -path './.venv' -prune -o -type f -name '*~' -exec rm {} +

## fix: fix formatting and code issues
fix:
	@ruff format .
	@ruff check --fix .

## test: run Python tests
test:
	@pytest tests
