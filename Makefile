LATEX	= latex -shell-escape
#BIBTEX	= bibtex
DVIPS	= dvips
DVIPDF  = dvipdft
XDVI	= xdvi -gamma 4
GH		= gv

EXAMPLES = $(wildcard *.c)
SRC	:= $(shell egrep -l '^[^%]*\\begin\{document\}' *.tex)
TRG	= $(SRC:%.tex=%.dvi)
PSF	= $(SRC:%.tex=%.ps)
PDF	= $(SRC:%.tex=%.pdf)

pdf: $(PDF)

ps: $(PSF)

$(TRG): %.dvi: %.tex

	$(LATEX) $<
#	$(BIBTEX) $(<:%.tex=%)
	$(LATEX) $<
	$(LATEX) $<


$(PSF):%.ps: %.dvi
	$(DVIPS) -R -Poutline -t letter $< -o $@

$(PDF): %.pdf: %.ps
	ps2pdf $<
	xdvi Assignment1.dvi &

show: $(TRG)
	@for i in $(TRG) ; do $(XDVI) $$i & done

showps: $(PSF)
	@for i in $(PSF) ; do $(GH) $$i & done

all: pdf
gitall:
	make clean
	git pull
	git add -A
	git commit -m "General update: many files are updated please go through details"
	git push
gittex:
	make clean
	git pull
	git add -A
	git commit -m "Updating the tex file"
	git push
gitmake:
	make clean
	git pull
	git add -A
	git commit -m "Updating makefile"
	git push
gitreadme:
	make clean
	git pull
	git add -A
	git commit -m "updating the readme file: README.md"
	git push
clean:
	rm -f *.pdf *.ps *.dvi *.out *.log *.aux *.bbl *.blg *.pyg

.PHONY: all show clean ps pdf showps

