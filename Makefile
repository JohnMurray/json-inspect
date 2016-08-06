default: doctoc

setup:
	npm install -g doctoc

doctoc:
	doctoc readme.md --github --notitle
	cp readme.md README
	doctoc README --github --notitle
