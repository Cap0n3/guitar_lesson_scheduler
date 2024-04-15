TARGET = src/main

.PHONY: run
run:
	@echo "Running the program..."
	poetry run python $(TARGET).py

.PHONY: test-all
test-all:
	@echo "Running all tests..."
	poetry run python tests/test_yearcal.py
	