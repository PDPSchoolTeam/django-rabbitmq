celery:
	celery -A root worker --loglevel=info

flower:
	celery -A root flower --port=5001

run:
	python manage.py runserver
