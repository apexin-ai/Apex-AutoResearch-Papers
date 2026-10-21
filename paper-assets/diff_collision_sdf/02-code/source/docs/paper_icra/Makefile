TEX = pdflatex
BIB = bibtex
MAIN = main

all: $(MAIN).pdf

$(MAIN).pdf: $(MAIN).tex abstract.tex introduction.tex related_work.tex method.tex claim1.tex claim2.tex claim3.tex discussion.tex references.bib
	$(TEX) -interaction=nonstopmode $(MAIN)
	$(BIB) $(MAIN) || true
	$(TEX) -interaction=nonstopmode $(MAIN)
	$(TEX) -interaction=nonstopmode $(MAIN)

clean:
	rm -f *.aux *.bbl *.blg *.log *.out *.fls *.fdb_latexmk *.synctex.gz

distclean: clean
	rm -f $(MAIN).pdf

.PHONY: all clean distclean
