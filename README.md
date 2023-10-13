
![main workflow](https://github.com/makstetoro3/lyceum/actions/workflows/python-package.yml/badge.svg)

### Создание и активация виртуального окружения
```commandline
python3 -m venv venv
source venv\bin\activate
```

### Установка зависимостей
```commandline
pip3 install -r requirements/prod.txt
```

### Установка зависимостей для разработки
```commandline
pip3 install -r requirements/dev.txt
```

### Установка зависимостей для тестирования
```commandline
pip3 install -r requirements/test.txt
```
### Настройка переменных окружения
Скопируйте файл "config.env" в ".env", если нужно, отредактируйте значение переменных
```commandline
cp confing.env .env
```

### Запуск
```commandline
python3 manage.py runserver
```