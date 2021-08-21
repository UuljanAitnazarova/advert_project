Для запуска проекта установите python версии 3.7 и выше, pip и virualenv

После клонирования перейдите в склонированную папку и вывполните следующие команды:

Создайте виртуальное окружение командой
```bash
python3 -m virtualenv -p python3 venv
```

Активируйте виртуальное окружение командой
```bash
source venv/bin/activate
```

Перейдите в папку server
```bash
cd server
```

Установите зависимости командой

```bash
pip install -r requirements.txt
```

Примените миграции командой
```bash
./manage.py migrate
```

Установите фикстуры командой 
```bash
./manage.py loaddata
```


Для доступа в панель администратора перейдите по ссылке {url_проекта}/admin

Пользователи

username: jenny
password: jenny12345

username: admin
password: admin
