import jinja2

loader = jinja2.FileSystemLoader(searchpath=".")
env = jinja2.Environment(loader=loader)

TEMPLATE_FILE = "./index_base.html"
template = env.get_template( TEMPLATE_FILE )
with open("publications_conference.html") as f:
    conf_pubs = f.read()
with open("publications_journal.html") as f:
    journal_pubs = f.read()

templateVars = { "conference" : conf_pubs,
		 "journal" : journal_pubs }

print(template.render(templateVars))
