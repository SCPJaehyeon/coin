init:
	python3 setup.py bdist_wheel
test:
	python3 -m unittest discover tests
