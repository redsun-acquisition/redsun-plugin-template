.DEFAULT_GOAL := help

.PHONY: clean
clean: clean-nox clean-build clean-pyc ## Remove all file artifacts

.PHONY: clean-nox
clean-nox: ## Remove nox testing artifacts
	@echo "+ $@"
	@rm -rf .nox/

.PHONY: clean-build
clean-build: ## Remove build artifacts
	@echo "+ $@"
	@rm -fr build/
	@rm -fr dist/
	@rm -fr *.egg-info

.PHONY: clean-pyc
clean-pyc: ## Remove Python file artifacts
	@echo "+ $@"
	@find . -type f -name "*.py[co]" -delete
	@find . -type d -name "__pycache__" -delete
	@find . -name '*~' -delete

.PHONY: test
test: ## Run tests quickly with the default Python
	@echo "+ $@"
	@nox -e py

.PHONY: test-all
test-all: ## Run tests on every Python version with nox
	@echo "+ $@"
	@nox

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}'
