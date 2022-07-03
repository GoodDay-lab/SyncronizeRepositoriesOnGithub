# Description
- Скрипт запускает простой сервер,
 который будет обрабатывать запросы с github-webhook
 и синхронизировать между собой репозитории.

- Названия веток, репозиториев и почтовых адресов - условны, вы можете заменить их.

# HOW IT WORKS

### HOWTO unite a repositories

- Create a dir
- Adding remote repositories (git remote add ..)
	
	$ git remote add repo1 https://github.com/path/to/your/repo
	
	$ git remote add repo2 https://github.com/path/to/your/repo

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

Всё происходит в соответствии с статьёй (src),
  под объединением репозиториев я понимаю процесс, когда их основные ветки объединяются в один коммит.


### HOWTO update a repository

- We getting an notice via webhook github (for example repo1)
- Pulling an repo1
	
	$ git pull repo1 development
	
- Pushing into other repos
	
	$ git push repo2 development
	
- Excellent! We updated an repository!

Здесь мы merge-им историю repo1/development с локальный веткой development
  и обновляем repo2/development

# Installing

### ngrok
Для теста можно использовать ngrok.

	$ ngrok http 9999

### Adding webhook
Перед началом надо подключить webhook:
	- Заходите в репозиторий -> settings -> webhook -> add a webhook -> "в поле url ставите url от ngrok"

### Install git and python packages
Утилита git должна быть в системной переменной PATH

Так же необходимо обеспечить автоаутенфикацию аккаунта в github-е при push:
	
	$ git config credential.helper store
	
	$ echo "https://(yourgithubaccount):(yourauthkey)@github.com/path/to/your/repository" >> ~/.git-credentials

Обязательно установить пакеты для python

	$ python -m pip install -r requirements.txt	

# Usage

### to run:
	$ python main.py --host (host) --port (port) --localrepo (path to localrepo) --replist (path to config file)

	- --localrepo (localrepo) - аргумент (localrepo) - это путь к папке, которая будет создана для связывания всех репозиториев в единое целое. После окончания работы скрипта должна автоматически удалиться, если указывает на существующую папку, то сначала удаляет её, даже, если она не пустая, будьте аккуратны (WARNING!!!)

	- --replist (configfile) - аргумент (configfile) - это путь к файлу, в котором будет храниться информация о репозиториях в формате, похожем на csv.
	
	- --host (host) - аргумент (host) - это хост на котором будет работать скрипт. Доменное имя или IP адрес, например, "localhost". 

	- --port (port) - порт, на котором будет работать скрипт. Должно быть числом от 2^0 до 2^16 (65355, включительно) 


### Configure configfile:
	Текстовый файл, данные храняться в формате:
	
	- (url) - url к удалённому репозиторию
	
	- (branch) - ветка, которую надо отслеживать, должна быть главной. Для примера главными ветками часто бывают (master, development, stable)

	- (email) - электронный адрес, к которому привязан аккаунт github-а. Email адрес автора коммита будет автоматически заменяться на этот адрес, для каждого репозитория индивидуально.


### Examples

	- Пример configfile:

		https://github.com/youaccount/path/to/repo1 master example1@gmail.com
		https://github.com/youaccount/path/to/repo2 master example2@gmail.com

	- Пример запуска программы:

		$ python main.py --localrepo ~/localrepo --replist replist.txt


