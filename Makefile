style:
	flake8 .

sqlite:
	python test_sqlite.py

sqlite_orm:
	python test_sqlite_orm.py

imports:
	isort . --diff

check:
	make imports
	make style
