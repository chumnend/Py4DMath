all: install-deps

.PHONY: init
init:
	@python -m virtualenv venv
	@source venv/bin/activate
	@pip install -r requirements.txt
	@pre-commit install

.PHONY: install-deps
install-deps:
	@pip install -r requirements.txt

.PHONY: save-deps
save-deps:
	@pip freeze > requirements.txt
	@echo "Dependencies saved."

.PHONY: build
build: clean
	@python setup.py sdist
	@python setup.py bdist_wheel

.PHONY: upload
upload: build
	@twine upload dist/*

.PHONY: test
test:
	@python setup.py pytest

.PHONY: test-cov
test-cov:
	@pytest --cov

.PHONY: clean
clean:
	@rm -rf build dist

.PHONY: lint
lint:
	@python -m black Py4DMath
