init:
	python setup.py bdist_wheel
test:
	python -m unittest discover tests