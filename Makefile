.PHONY: run, clean

run:
	@python src/main.py

clean:
	@echo "cleaning up..."
	@find . \( -name '__pycache__' -o -name '*.pyc' -o -name '*.pyo' \) -delete
