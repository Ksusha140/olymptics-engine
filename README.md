# olymptics-engine

Скрипт для теста большого массива решений задач.

## Принцип работы

* `argv` принимает путь до папки с файлами юнит-тестов и решениями задач
* Поиск происходит по всем подпапкам, поэтому внутренняя структура хранения задач и тестов не важна
* Ожидается, что файлы тестов названы по след. принципу: `test_[название задачи].py`
* Для каждого найденного файла тестов происходит поиск соответствующих ему задач, которые названы по принципу: `[имя исполнителя]_[название задачи].py`
* После нахождения всех файлов запускаются тесты для каждого найденного решения
* Результаты прохождения тестов сохраняются (вывод результатов в отдельный файл пока не реализован)
