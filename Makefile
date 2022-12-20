.SHELL := bash
.SHELLFLAGS := -eu -c
.DELETE_ON_ERROR:
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules
MAKEFLAGS += -j 8

watch:
	uvicorn main:app --reload

clean:
	rm -rf __pycache__
.PHONY: clean
