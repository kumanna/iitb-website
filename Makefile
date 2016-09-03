all: index.html

index.html: index_base.html publications_conference.html publications_journal.html
	python3 render_publications.py > index.html

publications_conference.html: publications_conference.bib
	jabref -n -o test.csv,oocsv publications_conference.bib && \
	python3 pubcsv2list.py conference test.csv "K. Appaiah" > publications_conference.html
	$(RM) test.csv

publications_journal.html: publications_journal.bib
	jabref -n -o test.csv,oocsv publications_journal.bib && \
	python3 pubcsv2list.py journal test.csv "K. Appaiah" > publications_journal.html
	$(RM) test.csv

.PHONY: clean
clean:
	$(RM) test.csv publications_journal.html publications_conference.html index.html
