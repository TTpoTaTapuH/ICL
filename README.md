## Contributing
#### Installation
#### Устанавливаем python 3.7.3
#### Копируем этот репозиторий (перед этим надо установить git) `git clone https://github.com/TTpoTaTapuH/ICL.git` или просто скачиваем zip файл и распаковываем.
#### Устанавливаем базу данных PostgreSQL (Linux - `sudo apt-get install postgresql postgresql-client postgresql-common`), запускам командную строку этой БД через командную строку `sudo -u postgres psql` и выполняем следующие команды `CREATE DATABASE icl_test;` 
`CREATE USER "iclUser" WITH PASSWORD 'icl_user';` 
`GRANT ALL PRIVILEGES ON DATABASE  icl_test TO "iclUser";` 
`\q` 
#### Переходим в папку ICL через командную строку и вводим команды `pipenv shell`, потом `pip3 install -r requirements.txt`
#### Переходим в папку, где хранится manage.py, т.е. в api_server и вводим команды `python manage.py makemigrations` и `python manage.py migrate`
#### Создаем пользователя для админки: `make createsuperuser` логин и пароль вводим, он понадобится, чтобы заходить на сайт

#### Endpoints
- Admin page: http://localhost:8060/admin/
- get script http://localhost:8060/api/tasks/

#### Переходим на сайт Admin page и вводим свои данные для входа, которые указали при создании пользователя для админки. Кликаем по полю Tasks и добавляем новый объект. Сохраняем текст скрипта powershell. Например: Write-Host 444. Сохраняем объект.
#### Переходим в папку ICL, вводим команду `make run-server`. Сервер запускается, остается запустить только клиента.
#### Открываем файл client.py и указываем там в поле `p = subprocess.Popen(["pwsh","data.ps1"],stdout=sys.stdout)` вместо переменной `"pwsh"` расположение файла для запуска powershell, например "C://system/powershell.exe" и сохраняем файл.
#### Переходим в папку где находится client.py через командную строку, вводим в командную строку команду `python client.py`. Клиент заработал, скрипт выполнился!
