all:
	pyflakes3  model_*.py
	python3 freecad_eval.py model_toy_volvo_spoler.py
