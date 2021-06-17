all:
	pyflakes3  generic_box*.py
	python3 freecad_eval.py generic_box.py
