# Проект по тестированию формы регистрации учетной записи

> <a target="_blank" href="https://demoqa.com/">demoqa.com</a>

[//]: # (## Проект реализован с использованием)

[//]: # ()
[//]: # (<img src="/images/icons/python-original.svg" width="40" height="40" title="Python" alt=""> <img src="/images/icons/pytest.png" width="40" height="40" title="Pytest" alt=""> <img src="/images/icons/intellij_pycharm.png" width="40" height="40" title="PyCharm" alt=""> <img src="/images/icons/selenium.png" width="40" height="40" title="Selenium" alt=""> <img src="/images/icons/selene.png" width="40" height="40" title="Selene" alt=""> <img src="/images/icons/selenoid.png" width="40" height="40" title="Selenoid" alt=""> <img src="/images/icons/jenkins.png" width="40" height="40" title="Jenkins" alt=""> <img src="/images/icons/allure_report.png" width="40" height="40" title="Allure Report" alt=""> <img src="/images/icons/allure_testops.png" width="40" height="40" title="Allure TestOps" alt=""> <img src="/images/icons/telegram.png" width="40" height="40" title="Telegram" alt=""> <img src="/images/icons/jira-original.svg" width="40" height="40" title="Jira" alt=""> )


[//]: # (![This is an image]&#40;/images/icons/python-original.svg&#41;![This is an image]&#40;/images/icons/pytest.png&#41;![This is an image]&#40;/images/icons/intellij_pycharm.png&#41;![This is an image]&#40;/images/icons/selenium.png&#41;![This is an image]&#40;/images/icons/selene.png&#41;![This is an image]&#40;/images/icons/selenoid.png&#41;![This is an image]&#40;/images/icons/jenkins.png&#41;![This is an image]&#40;/images/icons/allure_report.png&#41;![This is an image]&#40;/images/icons/allure_testops.png&#41;![This is an image]&#40;/images/icons/telegram.png&#41;![This is an image]&#40;/images/icons/jira-original.svg&#41;)


![This is an image](/images/examples/test_page.png)

#### Список проверок, реализованных в авто-тестах

- [x] Заполнение всех полей формы с последующей верификацией введенных значений
- [x] Заполнение обязательных полей формы с последующей верификацией введенных значений
- [x] Отправление не заполненной формы
- [x] Заполнение вариативных полей формы с последующей верификацией введенных значений
- [x] Обработка входа на склад книг не зарегистрированным пользователем
- [x] Вход на склад книг зарегистрированным пользователем
- [x] Обработка попытки регистрации без заполнения обязательных полей

#### Список проверок ручного тестирования

- [x] Визуальная характеристика главной страницы сайта, соответствие единому корпоративному стилю
- [x] Адаптивность вёрстки
- [x] Соответствие вёрстки сайта общепринятым стандартам

## Запуск авто-тестов в Jenkins

#### Параметры сборки

* `ENVIRONMENT` - параметр определяет окружение для запуска тестов, по умолчанию STAGE
* `COMMENT` - комментарий к сборке
* `BROWSER_VERSION` - желаемая версия браузера Google Chrome, по умолчанию 100


#### 1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/qa_g_diplome/">проект</a>

![This is an image](/images/examples/jenkins_project_main.png)

#### 2. Выбрать пункт **Build with Parameters**

#### 3. Внести изменения в конфигурации сборки, при необходимости

#### 4. Нажать **Build**

#### 5. Результат запуска сборки можно посмотреть как в классическом формате Allure Results

![This is an image](/images/examples/allure_example.png)

#### 6. Так и в интегрированном с Jira и Allure TestOps

![This is an image](/images/examples/testops_example.png)

#### 7. Информация о завершении сборки так же будет опубликована в telegram на канале

![This is an image](/images/examples/notiffication_example.png)

#### 8. Запуск авто-тестов

Пример командной строки:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -vv -s . --browser-version=$BROWSER_VERSION --context="remote_selenoid"
```
где:<br/> 
* '--browser-version' не обязательный параметр имеющий значение по умолчанию 100.0<br/>
* '--context' не обязательный параметр имеющий значение по умолчанию<br/> 
"remote_selenoid". Для локального запуска тестов должен иметь значение "local"

Создание локального отчета:

```bash
allure serve allure-results
```

## Пример выполнения удаленного теста

![This is an video](/images/videos/demo_test_execution.gif)

#### 9. Так же результаты выполнения будут транслированы в Jira

![This is an image](/images/examples/jira_integration.png)