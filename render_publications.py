import jinja2, time

loader = jinja2.FileSystemLoader(searchpath=".")
env = jinja2.Environment(loader=loader)

TEMPLATE_FILE = "./index_base.html"
template = env.get_template( TEMPLATE_FILE )
with open("publications_conference.html") as f:
    conf_pubs = f.read()
with open("publications_journal.html") as f:
    journal_pubs = f.read()

templateVars = { "conference" : conf_pubs,
		 "journal" : journal_pubs,
		 "last_updated_on" : time.strftime("Last updated on %d/%m/%Y at %H:%M %Z", time.localtime())}

print(template.render(templateVars))
