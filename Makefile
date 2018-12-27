.DEFAULT_GOAL := all

.PHONY: lint
lint:
	flake8

.PHONY: test
test:
	pytest --cov=bottender/

.PHONY: all
all: test lint

.PHONY: clean
clean:
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '*~' `
	rm -f `find . -type f -name '.*~' `
	rm -rf .cache
	rm -rf htmlcov
	rm -rf *.egg-info
	rm -f .coverage
	rm -f .coverage.*
	rm -rf build
	python setup.py clean

.PHONY: distribute
distribute:
	make clean
	python setup.py sdist bdist_wheel
