## Перед началом работы
Открыть блокнот stable_diffusion_webui_colab.ipynb в Google Colab. Дождаться получения ссылки. Проверить, есть ли в url/docs эндпоинт /sdapi/v1/txt2img. Если нет, то добавить вниз блокнота строку 
**!python launch.py --listen --xformers --enable-insecure-extension-access --theme dark --gradio-queue --multiple --api**

##Разворачивание стенда
После загрузки блокнота, копируем ссылку в переменные окружения **.env**. Пишем в терминале **pip install -r requirements.txt**, после чего запускаем **app.py**.
Приложение крутится на **5000** порту, порт можно сменить. В форму вводим промпт, ждем. Спустя ~5-10 секунд, в папке с проектом будет изображение **output.png**
