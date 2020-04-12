init:
	pipenv install --python 3
update-from-requirements:
	pipenv install -r ./molecule/requirements-dev.txt
