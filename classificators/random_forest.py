import pandas as pd
import warnings
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from analytical_and_get_df import get_df
warnings.simplefilter("ignore")

pd.set_option('display.max_rows', 10000)
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 300)


def random_forest(interval, get_number_intervals, directory_train, directory_test, method, show):
    """
            Функция для обучения и предсказания данных по классификатору random forest

            Args:
                interval             (int) : количество значений в одном промежутке.
                get_number_intervals (int) : количество максимально лучших интервалов.
                directory_train      (str) : путь до директории, содержащей тренировочные данные.
                directory_test       (str) : путь до директории, содержащей тестовые данные.
                method               (str) : акустический признак по которому будут вычисляться данные.
                show                 (int) : переменная отображения промежуточных данных.

    """
    df_train = pd.DataFrame()
    df_test = pd.DataFrame()

    # запись тренировочных данных в dataframe
    print("Идет подсчёт тренировочной выборки...")
    df_train = get_df(directory_train, interval, get_number_intervals, method)
    print("Готово")

    if show:
        print(df_train)

    X = df_train.drop(['actor'], axis=1)
    y = df_train.actor

    # Для закрытой задачи
    # df_test = get_df(directory_test, interval, get_number_intervals)

    # запись тестовых данных в dataframe
    print("Идет подсчёт тестовой выборки...")
    df_test = get_df(directory_test, interval, get_number_intervals, method)
    print("Готово")

    if show:
        print(df_test)

    x_pred = df_test.drop(['actor'], axis=1)
    x_res = list(df_test.actor)

    # разбиение тренировочной выборки на тестовую и тренировочную для обучения
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

    # определение классификатора и подбор параметров для ег обучения
    param_rf = {'n_estimators': range(5, 66, 5), 'max_depth': range(1, 40, 3),
                'min_samples_split': range(2, 15, 3), 'min_samples_leaf': range(2, 15, 3)}
    clf_rf = RandomForestClassifier()
    grid_search_cv_clf = GridSearchCV(clf_rf, param_rf, cv=5)

    print("Обучение классификатора...")
    grid_search_cv_clf.fit(X_train, y_train)
    best_clf = grid_search_cv_clf.best_estimator_

    # print(grid_search_cv_clf.best_params_)
    # print(best_clf.score(X_test, y_test))

    res = best_clf.predict(x_pred)
    res = list(res)

    cnt = 0
    right = 0
    for el in res:
        if x_res[cnt] == el:
            right += 1
        cnt += 1

    # подсчёт результата
    result_acc = (100 * right) / len(res)
    print(f"Итог: {result_acc}")
