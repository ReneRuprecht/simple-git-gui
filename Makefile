.PHONY: fmt run

fmt:
	@black --line-length 79 .

run: fmt
	@python main.py
