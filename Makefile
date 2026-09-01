MAIN := main

.PHONY: all pdf clean distclean check-refs

all: pdf

pdf:
	latexmk -pdf -interaction=nonstopmode -halt-on-error $(MAIN).tex

check-refs:
	python3 scripts/check_refs.py

clean:
	latexmk -c $(MAIN).tex

distclean:
	latexmk -C $(MAIN).tex
