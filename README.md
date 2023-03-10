# VDSControlBot

[![Python Version](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge)](https://www.python.org/) [![GitHub Stars](https://img.shields.io/github/stars/ilyhalight/VdsControlBot?logo=FemisioStars&style=for-the-badge)](https://github.com/ilyhalight/VdsControlBot/stargazers) [![GitHub Issues](https://img.shields.io/github/issues/ilyhalight/VdsControlBot?style=for-the-badge)](https://github.com/ilyhalight/VdsControlBot/issues) [![Current Version](https://img.shields.io/github/v/release/ilyhalight/VdsControlBot?style=for-the-badge)](https://github.com/ilyhalight/VdsControlBot) [![GitHub License](https://img.shields.io/github/license/ilyhalight/VdsControlBot?style=for-the-badge)](https://github.com/ilyhalight/VdsControlBot/blob/master/LICENSE)

⭐ Поставьте звездочку на GitHub — это очень мотивирует!

**VdsControlBot** - это телеграм бот для удобного мониторинга и управления вашими виртуальными серверами по SSH. Бот написан на Python с использованием библиотеки [aiogram v2](https://aiogram.dev/) и [asyncssh](https://asyncssh.readthedocs.io/en/latest/).

![VdsControlBot Preview](https://i.imgur.com/uJOB94B.png)

---

## 📜 Команды
1. `/start` - запуск бота и отображение клавиатуры
2. `/cancel` - сброс текущего действия
3. `/info` - отображение информации о сервере
4. `/add` - добавление нового сервера
5. `/remove` - удаление сервера 
6. `/list` - отображение списка серверов

---

## 📦 Установка
1. Загрузите репозиторий с GitHub
2. Зайдите в загруженную папку и пропишите `pip install -r requirements.txt` для установки зависимостей
3. Зайдите в папку `config` и отредактируйте файл `settings.cfg` установив свой chat_id
4. Запустите бота командой `python main.py`

---

## 📝 Лицензия
>Вы можете ознакомиться с полной лицензией [здесь](https://github.com/ilyhalight/VdsControlBot/blob/master/LICENSE)

Этот проект находится под лицензией MIT. Вы можете использовать его в любых целях.