HOWTO unite a repositories

@ Create a dir
@ Adding remote repositories (git remote add ..)
	"""
	git remote add repo1 ...
	git remote add repo2 ...
	"""
@ Pulling remotes
	"""
	git pull repo1 <branch>
	git pull repo2 <branch>
	"""
@ Pushing into remotes
	"""
	git push repo1 <branch>
	git push repo2 <branch>
	"""
@ Excellent! We united 2 repositories into 1 repository!


HOWTO update a repository

@ We getting an notice via webhook github (for example repo1)
@ Pulling an repo1
	"""
	git pull repo1 <branch>
	"""
@ Pushing into other repos
	"""
	git push repo2 <branch>
	"""
@ Excellent! We updated an repository!



Скрипт запускает простой сервер,
 который будет обрабатывать запросы с github-webhook
 и синхронизировать между собой репозитории


to run:
	$ python __main__.py --host <host> --port <port> --localrepo <path to localrepo> --replist <path to replist.txt>

	- localrepo - папка, которая будет создана для связывания всех репозиториев в единое целое,
					с помощью 'git pull' мы получим локальный репозиторий со общими данными с репозиториев
	- replist - файл, в котором будет храниться информация о репозиториях в формате, похожем на csv:
		| <url> <branch> <name> |
		
		- url, путь к репозиторию
		- branch, отслеживаемая ветка
		- name, название этого удалённого репозитория в localrepo (git remote add <name> <url>)
	
	- host - хост, на котором будет работать скрипт
	
	- port - порт, на котором будет работать скрипт 




