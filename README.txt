1/ Создание БД в cmd:   	createdb -U postgres importphones
				пароль: postgres

2/ Миграция в cmd: 		python manage.py migrate

3/ Создание админки:    	python manage.py createsuperuser
				username:  admin
				email adress: -
				password: admin

4/ Подкл. библиотек в cmd: 	pip install -r requirements.txt

5/ Загрузка базы данных: 	python manage.py import_phones

6/ Запуск программы:		python manage.py runserver
