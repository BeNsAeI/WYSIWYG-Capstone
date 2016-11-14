filename=BehnamSaeedi_technology_Review.tex

pdf: ps
	ps2pdf ${filename}.ps

pdf-print: ps
	ps2pdf -dColorConversionStrategy=/LeaveColorUnchanged -dPDFSETTINGS=/printer ${filename}.ps

text: html
	html2text -width 100 -style pretty ${filename}/${filename}.html | sed -n '/./,$$p' | head -n-2 >${filename}.txt

html:
	@#latex2html -split +0 -info "" -no_navigation ${filename}
	htlatex ${filename}

ps:	dvi
	dvips -t letter ${filename}.dvi

dvi:
	latex ${filename}
	bibtex ${filename}||true
	latex ${filename}
	latex ${filename}

read:
	evince ${filename}.pdf &

aread:
	acroread ${filename}.pdf

clean:
	rm -f ${filename}.{ps,pdf,log,aux,out,dvi,bbl,blg}
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
back-up:
	cp Assignment1.tex backup/Assignment1.tex
	cp Makefile backup/Makefile
view:
	xdvi Assignment1.dvi &

update:
	git pull

clean:
	rm -f *.pdf *.ps *.dvi *.out *.log *.aux *.bbl *.blg *.pyg *.toc

.PHONY: all show clean ps pdf showps

