from classificators.random_forest import random_forest
from classificators.decision_tree import decision_tree

DEFAULT_DIRECTORY_TRAIN = "/Users/dmitrijelizarov/PycharmProjects/acoustic_signs/actors"
directory_test = "/Users/dmitrijelizarov/PycharmProjects/acoustic_signs/actor1_test"

if __name__ == '__main__':

    # выбор данных
    method = input("Выберите метод: \n1 - lfcc, 2- mfcc, 3 - plp, 4 - spectral centroid: ")
    classificator = input("Выберите классификатор: 1 - decision tree, 2 - random forest: ")
    interval = int(input("Введите интервал для подсчёта: "))
    get_number_intervals = int(input("Введите количество максимальных интервалов для взятия: "))
    directory = int(
        input("Использовать директории для тренировочной и тестовой выборки по умолчанию? 1 - да, 2 - нет: "))
    if directory == 2:
        directory_train = input("Введите директорию для обучения: ")
        directory_test = input("Введите директорию для тестирования: ")
    else:
        directory_train = DEFAULT_DIRECTORY_TRAIN
        directory_test = directory_test
    count_start = int(input("Введите кол-во запусков: "))
    show = int(input("Отображать получившиеся данные обучения и тестирования: 1 - да, 0 - нет: "))

    if method == "1":
        feat = "lfcc"
    elif method == "2":
        feat = "mfcc"
    elif method == "3":
        feat = "plp"
    elif method == "4":
        feat = "spec_cent"

    while count_start:

        if classificator == "1":
            decision_tree(interval=interval, get_number_intervals=get_number_intervals,
                          directory_train=directory_train, directory_test=directory_test,
                          method=feat, show=show)
        elif classificator == "2":
            random_forest(interval=interval, get_number_intervals=get_number_intervals,
                          directory_train=directory_train, directory_test=directory_test,
                          method=feat, show=show)

        count_start -= 1
