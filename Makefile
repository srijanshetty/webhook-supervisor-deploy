.SHELL := bash
.SHELLFLAGS := -eu -c
.DELETE_ON_ERROR:
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules
MAKEFLAGS += -j 8

watch:
	uvicorn main:app --reload --port=8001

clean:
	rm -rf __pycache__
.PHONY: clean
