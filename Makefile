run:
	./create_dotenv.sh
	./install.sh
	flask run

style:
	flake8 .

test-sqlite:
	python test_sqlite.py

test-sqlite_orm:
	python test_sqlite_orm.py

test:
	pytest

imports:
	isort .

check:
	make imports
	make style
	make test
