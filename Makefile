default: release

setup:
	npm install -g doctoc
	pip install pyandoc

release:
	doctoc readme.md --github --notitle
	python setup.py sdist upload
