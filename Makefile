all: install-deps

.PHONY: init
init:
	@python -m virtualenv venv
	@source venv/bin/activate
	@pip install --upgrade pip setuptools wheel twine pytest pytest-runner

.PHONY: install-deps
install-deps:
	@pip install -r requirements.txt

.PHONY: save-deps
save-deps:
	@pip freeze > requirements.txt
	@echo "Dependencies saved."

.PHONY: build
build:
	@python setup.py sdist
	@python setup.py bdist_wheel

.PHONY: upload
upload: build
	@twine upload dist/*

.PHONY: test
test:
	@python setup.py pytest
