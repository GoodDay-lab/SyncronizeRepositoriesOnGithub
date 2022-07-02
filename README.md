HOWTO unite a repositories

- Create a dir
- Adding remote repositories (git remote add ..)
	
	$ git remote add repo1 ...
	
	$ git remote add repo2 ...

- Pulling remotes
	
	$ git pull repo1 development
	
	$ git pull repo2 development
	
- Pushing into remotes
	
	$ git push repo1 development
	
	$ git push repo2 development
	
- Excellent! We united 2 repositories into 1 repository!

Имеется ввиду это:
src: https://blog.devgenius.io/how-to-merge-two-repositories-on-git-b0ed5e3b4448

Но поскольку "git pull repo1 development" в своей реализации производит, грубо говоря:

	$ git fetch repo1 && git merge repo1/development

Как следствие всё происходит в соответствии с статьёй (src),
  под объединением репозиториев я понимаю "git merge repo/master", когда их основные ветки объединяются в один коммит.


HOWTO update a repository

- We getting an notice via webhook github (for example repo1)
- Pulling an repo1
	
	$ git pull repo1 development
	
- Pushing into other repos
	
	$ git push repo2 development
	
- Excellent! We updated an repository!

Здесь мы merge-им историю repo1/development с локальный веткой development
  и обновляем repo2/development



Скрипт запускает простой сервер,
 который будет обрабатывать запросы с github-webhook
 и синхронизировать между собой репозитории.

Для теста можно использовать ngrok
Перед началом надо подключить webhook:
	- Заходите в репозиторий -> settings -> webhook -> add a webhook -> "в поле url ставите url от ngrok"

Утилита git должна быть в системной переменной PATH

Так же необходимо обеспечить автоаутенфикацию аккаунта в github-е при push:
	
	$ git config credential.helper store
	
	$ echo "https://(youremail):(yourauthkey)@github.com/path/to/your/repository >> ~/.git-credentials

Обязательно установить пакеты для python

	$ python -m pip install -r requirements.txt


to run:
	$ python __main__.py --host <host> --port <port> --localrepo <path to localrepo> --replist <path to replist.txt>

	- localrepo - папка, которая будет создана для связывания всех репозиториев в единое целое,
					с помощью 'git pull' мы получим локальный репозиторий со общими данными с репозиториев
	- replist - файл, в котором будет храниться информация о репозиториях в формате, похожем на csv:
		| <url> <branch> |
		
		- url, путь к репозиторию
		- branch, отслеживаемая ветка
	
	- host - хост, на котором будет работать скрипт
	
	- port - порт, на котором будет работать скрипт 




