PYTHON = python3
PIP = pip

run:
	@$(PYTHON) ./src/Main.py

setup:
	@$(PIP) install -r requirements.txt

clean:
	@rm -rf ./src/__pycache__
