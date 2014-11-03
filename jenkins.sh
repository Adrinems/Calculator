#! /bin/sh

pip install -r requirements.txt
autopep8 -ir .
flake8 --max-complexity=3 --exclude=*.txt,*.md --max-line-length=200 .

lettuce AcceptanceTest
cd UnitTest
python TestCalculator.py -v
coverage run --branch TestCalculator.py
coverage report -m
coverage html --title="Coverage about Figures"
