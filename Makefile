all: dest/index.html dest/kumar_small.jpg dest/nptel_course.html

dest/nptel_course.html: nptel_course.html
	mkdir -p dest
	cp $< $@

dest/index.html: index_base.html publications_conference.html publications_journal.html
	mkdir -p dest
	python3 render_publications.py | sed 's/vol. 0, no. 0/to appear/g;s/Murali./Murali/g' > dest/index.html

dest/kumar_small.jpg: kumar_small.jpg
	mkdir -p dest
	cp kumar_small.jpg dest/kumar_small.jpg

publications_conference.html: publications_conference.bib
	jabref -n -o publications_conference_temp.csv,oocsv publications_conference.bib && \
	xsv sort -s Identifier -R publications_conference_temp.csv > publications_conference_sorted.csv
	python3 pubcsv2list.py conference publications_conference_sorted.csv "K. Appaiah" > publications_conference.html
	$(RM) publications_conference_temp.csv publications_conference_sorted.csv

publications_journal.html: publications_journal.bib
	jabref -n -o publications_journal_temp.csv,oocsv publications_journal.bib && \
	xsv sort -s Identifier -R publications_journal_temp.csv > publications_journal_sorted.csv
	python3 pubcsv2list.py journal publications_journal_sorted.csv "K. Appaiah" > publications_journal.html
	$(RM) publications_journal_temp.csv publications_journal_sorted.csv

.PHONY: clean
clean:
	$(RM) test.csv publications_journal.html publications_conference.html index.html dest/*
