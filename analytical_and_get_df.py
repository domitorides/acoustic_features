import numpy as np
import pandas as pd
import os
import librosa
import librosa.display
from rasta import rastaplp
from spafe.features.lfcc import lfcc
from librosa.feature import spectral_centroid


def analytical_detector(interval, get_number_intervals, y):
    """
        Функция вычисляет по заданному интервалу наилучшие промежутки (сумма модулей значений) и выбирает столько,
        сколько задал пользователь

        Args:
            interval             (int) : количество значений в одном промежутке.
            get_number_intervals (int) : количество максимально лучших интервалов


        Returns:
            (list) : лучшие интервалы
    """

    # Отсекаем конец, если не делится на выбранные интервалы
    while len(y) % interval != 0:
        y = y[:-1]

    # Приводим массив к целым числам
    y_abs = list(np.abs(y))

    # Находим сумму по интервалам и записываем в словарь
    dict_sum_intervals = {}
    number_interval = 0
    for i in range(0, len(y_abs), interval):
        sum_interval = sum(y_abs[i:interval+i])
        dict_sum_intervals[number_interval] = sum_interval
        number_interval += 1

    # Сортируем словарь по убыванию значений
    sorted_dict_sum_intervals = {}
    sorted_keys = sorted(dict_sum_intervals, key=dict_sum_intervals.get, reverse=True)
    for key in sorted_keys:
        sorted_dict_sum_intervals[key] = dict_sum_intervals[key]

    # Выпишем номера максимальных интервалов в list
    cnt = 0
    list_max_values = []
    for intervals in sorted_dict_sum_intervals:
        if cnt >= get_number_intervals:
            break
        list_max_values.append(intervals)
        cnt += 1
    list_max_values = sorted(list_max_values)

    # Запишем максимальные  интервалы в массив и вернём его
    result_y = []
    for number_interval in list_max_values:
        ind = number_interval * interval
        result_y += y[ind:interval+ind]

    return result_y


def get_df(directory, interval, get_number_intervals, method):
    """
            Функция вычисляет акустические признаки и записывает их в датафрейм

            Args:
                directory             (str) : путь до директории с данными.
                interval              (int) : количество значений в одном промежутке.
                get_number_intervals  (int) : количество максимально лучших интервалов
                method                (str) : акустический признак по которому будут вычисляться данные.


            Returns:
                (pandas dataframe) : полученные данные после преобразования по признаку
    """

    df = pd.DataFrame()
    cnt_row = 0

    # проход по речевому аудиосигналу и запись его в dataframe
    for dirpath, dirnames, filenames in os.walk(directory):

        # перебираем файлы
        for filename in filenames:
            if "DS" in filename:
                pass
            else:

                path = os.path.join(dirpath, filename)

                # считывание звуковой дорожки
                ar, sr = librosa.load(path)

                # выбор лучших промежутков по энергии
                ar = analytical_detector(interval, get_number_intervals, list(ar))
                ar = np.array(ar)

                # применение выбранного признака
                if method == "mfcc":
                    result = librosa.feature.mfcc(y=ar, sr=sr, hop_length=512, n_mfcc=16)
                elif method == "plp":
                    result = rastaplp(x=ar, modelorder=13)
                elif method == "lfcc":
                    ar = np.asanyarray(ar)
                    result = lfcc(sig=ar, fs=sr, win_len=0.04, win_hop=0.02)
                elif method == "spec_cent":
                    result = spectral_centroid(y=ar, sr=sr)

                # запись результата в list
                res = []
                for data in result:
                    list_data = list(data)
                    res += list_data

                # запись данных в dataframe
                cnt_col = 1
                for data in res:

                    df.loc[cnt_row, f"data{cnt_col}"] = data
                    if cnt_col == len(res):
                        actor_number = int(filename[18:20])
                        if actor_number == 1:
                            df.loc[cnt_row, "actor"] = 1
                        else:
                            df.loc[cnt_row, "actor"] = 0
                    cnt_col += 1
                cnt_row += 1

    return df
