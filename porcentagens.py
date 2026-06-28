import pandas as pd

data = {
    '2019-07-27': {'Fila corrida': 12, 'Olympikus corrida': 14, 'Mizuno corrida': 29, 'Asics corrida': 60},
    '2019-08-03': {'Fila corrida': 13, 'Olympikus corrida': 18, 'Mizuno corrida': 28, 'Asics corrida': 46},
    '2019-08-10': {'Fila corrida': 10, 'Olympikus corrida': 14, 'Mizuno corrida': 26, 'Asics corrida': 54},
    '2019-08-17': {'Fila corrida': 7, 'Olympikus corrida': 15, 'Mizuno corrida': 23, 'Asics corrida': 33},
    '2019-08-24': {'Fila corrida': 11, 'Olympikus corrida': 14, 'Mizuno corrida': 23, 'Asics corrida': 42},
    '2019-08-31': {'Fila corrida': 7, 'Olympikus corrida': 18, 'Mizuno corrida': 32, 'Asics corrida': 40},
    '2019-09-07': {'Fila corrida': 7, 'Olympikus corrida': 17, 'Mizuno corrida': 25, 'Asics corrida': 38},
    '2019-09-14': {'Fila corrida': 13, 'Olympikus corrida': 14, 'Mizuno corrida': 22, 'Asics corrida': 40},
    '2019-09-21': {'Fila corrida': 8, 'Olympikus corrida': 16, 'Mizuno corrida': 24, 'Asics corrida': 31},
    '2019-09-28': {'Fila corrida': 0, 'Olympikus corrida': 14, 'Mizuno corrida': 24, 'Asics corrida': 33},
    '2019-10-05': {'Fila corrida': 8, 'Olympikus corrida': 9, 'Mizuno corrida': 16, 'Asics corrida': 32},
    '2019-10-12': {'Fila corrida': 8, 'Olympikus corrida': 16, 'Mizuno corrida': 23, 'Asics corrida': 45},
    '2019-10-19': {'Fila corrida': 0, 'Olympikus corrida': 19, 'Mizuno corrida': 20, 'Asics corrida': 36},
    '2019-10-26': {'Fila corrida': 12, 'Olympikus corrida': 15, 'Mizuno corrida': 24, 'Asics corrida': 32},
    '2019-11-02': {'Fila corrida': 6, 'Olympikus corrida': 23, 'Mizuno corrida': 19, 'Asics corrida': 37},
    '2019-11-09': {'Fila corrida': 9, 'Olympikus corrida': 23, 'Mizuno corrida': 23, 'Asics corrida': 41},
    '2019-11-16': {'Fila corrida': 7, 'Olympikus corrida': 17, 'Mizuno corrida': 21, 'Asics corrida': 39},
    '2019-11-23': {'Fila corrida': 10, 'Olympikus corrida': 24, 'Mizuno corrida': 31, 'Asics corrida': 57},
    '2019-11-30': {'Fila corrida': 9, 'Olympikus corrida': 20, 'Mizuno corrida': 26, 'Asics corrida': 43},
    '2019-12-07': {'Fila corrida': 9, 'Olympikus corrida': 15, 'Mizuno corrida': 19, 'Asics corrida': 41},
    '2019-12-14': {'Fila corrida': 7, 'Olympikus corrida': 18, 'Mizuno corrida': 16, 'Asics corrida': 34},
    '2019-12-21': {'Fila corrida': 9, 'Olympikus corrida': 14, 'Mizuno corrida': 22, 'Asics corrida': 36},
    '2019-12-28': {'Fila corrida': 8, 'Olympikus corrida': 15, 'Mizuno corrida': 23, 'Asics corrida': 41},
    '2020-01-04': {'Fila corrida': 13, 'Olympikus corrida': 19, 'Mizuno corrida': 23, 'Asics corrida': 42},
    '2020-01-11': {'Fila corrida': 7, 'Olympikus corrida': 22, 'Mizuno corrida': 29, 'Asics corrida': 53},
    '2020-01-18': {'Fila corrida': 9, 'Olympikus corrida': 17, 'Mizuno corrida': 27, 'Asics corrida': 49},
    '2020-01-25': {'Fila corrida': 11, 'Olympikus corrida': 18, 'Mizuno corrida': 30, 'Asics corrida': 39},
    '2020-02-01': {'Fila corrida': 11, 'Olympikus corrida': 19, 'Mizuno corrida': 29, 'Asics corrida': 50},
    '2020-02-08': {'Fila corrida': 0, 'Olympikus corrida': 13, 'Mizuno corrida': 28, 'Asics corrida': 42},
    '2020-02-15': {'Fila corrida': 0, 'Olympikus corrida': 9, 'Mizuno corrida': 19, 'Asics corrida': 39},
    '2020-02-22': {'Fila corrida': 9, 'Olympikus corrida': 17, 'Mizuno corrida': 17, 'Asics corrida': 34},
    '2020-02-29': {'Fila corrida': 8, 'Olympikus corrida': 14, 'Mizuno corrida': 20, 'Asics corrida': 33},
    '2020-03-07': {'Fila corrida': 0, 'Olympikus corrida': 18, 'Mizuno corrida': 25, 'Asics corrida': 31},
    '2020-03-14': {'Fila corrida': 0, 'Olympikus corrida': 9, 'Mizuno corrida': 17, 'Asics corrida': 23},
    '2020-03-21': {'Fila corrida': 0, 'Olympikus corrida': 8, 'Mizuno corrida': 12, 'Asics corrida': 11},
    '2020-03-28': {'Fila corrida': 9, 'Olympikus corrida': 9, 'Mizuno corrida': 20, 'Asics corrida': 24},
    '2020-04-04': {'Fila corrida': 6, 'Olympikus corrida': 10, 'Mizuno corrida': 18, 'Asics corrida': 23},
    '2020-04-11': {'Fila corrida': 6, 'Olympikus corrida': 17, 'Mizuno corrida': 14, 'Asics corrida': 27},
    '2020-04-18': {'Fila corrida': 10, 'Olympikus corrida': 13, 'Mizuno corrida': 23, 'Asics corrida': 29},
    '2020-04-25': {'Fila corrida': 7, 'Olympikus corrida': 18, 'Mizuno corrida': 22, 'Asics corrida': 36},
    '2020-05-02': {'Fila corrida': 8, 'Olympikus corrida': 11, 'Mizuno corrida': 19, 'Asics corrida': 40},
    '2020-05-09': {'Fila corrida': 9, 'Olympikus corrida': 21, 'Mizuno corrida': 21, 'Asics corrida': 38},
    '2020-05-16': {'Fila corrida': 6, 'Olympikus corrida': 19, 'Mizuno corrida': 28, 'Asics corrida': 35},
    '2020-05-23': {'Fila corrida': 11, 'Olympikus corrida': 16, 'Mizuno corrida': 27, 'Asics corrida': 44},
    '2020-05-30': {'Fila corrida': 10, 'Olympikus corrida': 21, 'Mizuno corrida': 35, 'Asics corrida': 41},
    '2020-06-06': {'Fila corrida': 8, 'Olympikus corrida': 22, 'Mizuno corrida': 25, 'Asics corrida': 43},
    '2020-06-13': {'Fila corrida': 12, 'Olympikus corrida': 18, 'Mizuno corrida': 26, 'Asics corrida': 45},
    '2020-06-20': {'Fila corrida': 10, 'Olympikus corrida': 19, 'Mizuno corrida': 29, 'Asics corrida': 39},
    '2020-06-27': {'Fila corrida': 8, 'Olympikus corrida': 21, 'Mizuno corrida': 26, 'Asics corrida': 44},
    '2020-07-04': {'Fila corrida': 10, 'Olympikus corrida': 24, 'Mizuno corrida': 28, 'Asics corrida': 39},
    '2020-07-11': {'Fila corrida': 10, 'Olympikus corrida': 29, 'Mizuno corrida': 37, 'Asics corrida': 38},
    '2020-07-18': {'Fila corrida': 10, 'Olympikus corrida': 29, 'Mizuno corrida': 38, 'Asics corrida': 52},
    '2020-07-25': {'Fila corrida': 10, 'Olympikus corrida': 29, 'Mizuno corrida': 36, 'Asics corrida': 54},
    '2020-08-01': {'Fila corrida': 16, 'Olympikus corrida': 26, 'Mizuno corrida': 23, 'Asics corrida': 54},
    '2020-08-08': {'Fila corrida': 10, 'Olympikus corrida': 25, 'Mizuno corrida': 30, 'Asics corrida': 54},
    '2020-08-15': {'Fila corrida': 12, 'Olympikus corrida': 22, 'Mizuno corrida': 20, 'Asics corrida': 49},
    '2020-08-22': {'Fila corrida': 11, 'Olympikus corrida': 28, 'Mizuno corrida': 30, 'Asics corrida': 38},
    '2020-08-29': {'Fila corrida': 8, 'Olympikus corrida': 15, 'Mizuno corrida': 26, 'Asics corrida': 32},
    '2020-09-05': {'Fila corrida': 13, 'Olympikus corrida': 24, 'Mizuno corrida': 25, 'Asics corrida': 40},
    '2020-09-12': {'Fila corrida': 15, 'Olympikus corrida': 20, 'Mizuno corrida': 19, 'Asics corrida': 37},
    '2020-09-19': {'Fila corrida': 9, 'Olympikus corrida': 12, 'Mizuno corrida': 20, 'Asics corrida': 35},
    '2020-09-26': {'Fila corrida': 9, 'Olympikus corrida': 22, 'Mizuno corrida': 22, 'Asics corrida': 35},
    '2020-10-03': {'Fila corrida': 10, 'Olympikus corrida': 13, 'Mizuno corrida': 23, 'Asics corrida': 38},
    '2020-10-10': {'Fila corrida': 10, 'Olympikus corrida': 24, 'Mizuno corrida': 18, 'Asics corrida': 34},
    '2020-10-17': {'Fila corrida': 7, 'Olympikus corrida': 20, 'Mizuno corrida': 21, 'Asics corrida': 34},
    '2020-10-24': {'Fila corrida': 7, 'Olympikus corrida': 15, 'Mizuno corrida': 21, 'Asics corrida': 37},
    '2020-10-31': {'Fila corrida': 10, 'Olympikus corrida': 17, 'Mizuno corrida': 20, 'Asics corrida': 35},
    '2020-11-07': {'Fila corrida': 9, 'Olympikus corrida': 18, 'Mizuno corrida': 23, 'Asics corrida': 40},
    '2020-11-14': {'Fila corrida': 9, 'Olympikus corrida': 14, 'Mizuno corrida': 15, 'Asics corrida': 46},
    '2020-11-21': {'Fila corrida': 14, 'Olympikus corrida': 28, 'Mizuno corrida': 34, 'Asics corrida': 68},
    '2020-11-28': {'Fila corrida': 11, 'Olympikus corrida': 23, 'Mizuno corrida': 24, 'Asics corrida': 42},
    '2020-12-05': {'Fila corrida': 12, 'Olympikus corrida': 19, 'Mizuno corrida': 21, 'Asics corrida': 33},
    '2020-12-12': {'Fila corrida': 9, 'Olympikus corrida': 17, 'Mizuno corrida': 24, 'Asics corrida': 34},
    '2020-12-19': {'Fila corrida': 13, 'Olympikus corrida': 17, 'Mizuno corrida': 23, 'Asics corrida': 38},
    '2020-12-26': {'Fila corrida': 8, 'Olympikus corrida': 19, 'Mizuno corrida': 23, 'Asics corrida': 27},
    '2021-01-02': {'Fila corrida': 10, 'Olympikus corrida': 25, 'Mizuno corrida': 30, 'Asics corrida': 52},
    '2021-01-09': {'Fila corrida': 12, 'Olympikus corrida': 21, 'Mizuno corrida': 20, 'Asics corrida': 42},
    '2021-01-16': {'Fila corrida': 10, 'Olympikus corrida': 16, 'Mizuno corrida': 27, 'Asics corrida': 43},
    '2021-01-23': {'Fila corrida': 11, 'Olympikus corrida': 22, 'Mizuno corrida': 22, 'Asics corrida': 32},
    '2021-01-30': {'Fila corrida': 0, 'Olympikus corrida': 18, 'Mizuno corrida': 15, 'Asics corrida': 35},
    '2021-02-06': {'Fila corrida': 11, 'Olympikus corrida': 19, 'Mizuno corrida': 25, 'Asics corrida': 34},
    '2021-02-13': {'Fila corrida': 10, 'Olympikus corrida': 25, 'Mizuno corrida': 25, 'Asics corrida': 48},
    '2021-02-20': {'Fila corrida': 8, 'Olympikus corrida': 24, 'Mizuno corrida': 18, 'Asics corrida': 36},
    '2021-02-27': {'Fila corrida': 15, 'Olympikus corrida': 22, 'Mizuno corrida': 24, 'Asics corrida': 39},
    '2021-03-06': {'Fila corrida': 13, 'Olympikus corrida': 17, 'Mizuno corrida': 26, 'Asics corrida': 37},
    '2021-03-13': {'Fila corrida': 9, 'Olympikus corrida': 21, 'Mizuno corrida': 22, 'Asics corrida': 39},
    '2021-03-20': {'Fila corrida': 9, 'Olympikus corrida': 20, 'Mizuno corrida': 22, 'Asics corrida': 34},
    '2021-03-27': {'Fila corrida': 11, 'Olympikus corrida': 19, 'Mizuno corrida': 27, 'Asics corrida': 34},
    '2021-04-03': {'Fila corrida': 7, 'Olympikus corrida': 26, 'Mizuno corrida': 29, 'Asics corrida': 46},
    '2021-04-10': {'Fila corrida': 14, 'Olympikus corrida': 22, 'Mizuno corrida': 25, 'Asics corrida': 43},
    '2021-04-17': {'Fila corrida': 12, 'Olympikus corrida': 21, 'Mizuno corrida': 32, 'Asics corrida': 46},
    '2021-04-24': {'Fila corrida': 12, 'Olympikus corrida': 25, 'Mizuno corrida': 36, 'Asics corrida': 46},
    '2021-05-01': {'Fila corrida': 8, 'Olympikus corrida': 23, 'Mizuno corrida': 27, 'Asics corrida': 42},
    '2021-05-08': {'Fila corrida': 16, 'Olympikus corrida': 25, 'Mizuno corrida': 25, 'Asics corrida': 45},
    '2021-05-15': {'Fila corrida': 16, 'Olympikus corrida': 20, 'Mizuno corrida': 26, 'Asics corrida': 49},
    '2021-05-22': {'Fila corrida': 17, 'Olympikus corrida': 18, 'Mizuno corrida': 24, 'Asics corrida': 46},
    '2021-05-29': {'Fila corrida': 15, 'Olympikus corrida': 23, 'Mizuno corrida': 28, 'Asics corrida': 40},
    '2021-06-05': {'Fila corrida': 20, 'Olympikus corrida': 24, 'Mizuno corrida': 24, 'Asics corrida': 39},
    '2021-06-12': {'Fila corrida': 15, 'Olympikus corrida': 24, 'Mizuno corrida': 32, 'Asics corrida': 38},
    '2021-06-19': {'Fila corrida': 15, 'Olympikus corrida': 13, 'Mizuno corrida': 30, 'Asics corrida': 40},
    '2021-06-26': {'Fila corrida': 17, 'Olympikus corrida': 20, 'Mizuno corrida': 20, 'Asics corrida': 40},
    '2021-07-03': {'Fila corrida': 13, 'Olympikus corrida': 18, 'Mizuno corrida': 27, 'Asics corrida': 39},
    '2021-07-10': {'Fila corrida': 15, 'Olympikus corrida': 22, 'Mizuno corrida': 26, 'Asics corrida': 40},
    '2021-07-17': {'Fila corrida': 17, 'Olympikus corrida': 21, 'Mizuno corrida': 23, 'Asics corrida': 31},
    '2021-07-24': {'Fila corrida': 13, 'Olympikus corrida': 27, 'Mizuno corrida': 21, 'Asics corrida': 45},
    '2021-07-31': {'Fila corrida': 16, 'Olympikus corrida': 23, 'Mizuno corrida': 27, 'Asics corrida': 47},
    '2021-08-07': {'Fila corrida': 21, 'Olympikus corrida': 20, 'Mizuno corrida': 24, 'Asics corrida': 47},
    '2021-08-14': {'Fila corrida': 14, 'Olympikus corrida': 22, 'Mizuno corrida': 25, 'Asics corrida': 40},
    '2021-08-21': {'Fila corrida': 15, 'Olympikus corrida': 17, 'Mizuno corrida': 18, 'Asics corrida': 41},
    '2021-08-28': {'Fila corrida': 16, 'Olympikus corrida': 20, 'Mizuno corrida': 22, 'Asics corrida': 36},
    '2021-09-04': {'Fila corrida': 16, 'Olympikus corrida': 24, 'Mizuno corrida': 18, 'Asics corrida': 36},
    '2021-09-11': {'Fila corrida': 11, 'Olympikus corrida': 16, 'Mizuno corrida': 20, 'Asics corrida': 38},
    '2021-09-18': {'Fila corrida': 16, 'Olympikus corrida': 14, 'Mizuno corrida': 16, 'Asics corrida': 35},
    '2021-09-25': {'Fila corrida': 9, 'Olympikus corrida': 15, 'Mizuno corrida': 18, 'Asics corrida': 31},
    '2021-10-02': {'Fila corrida': 9, 'Olympikus corrida': 16, 'Mizuno corrida': 22, 'Asics corrida': 33},
    '2021-10-09': {'Fila corrida': 19, 'Olympikus corrida': 24, 'Mizuno corrida': 24, 'Asics corrida': 32},
    '2021-10-16': {'Fila corrida': 11, 'Olympikus corrida': 24, 'Mizuno corrida': 17, 'Asics corrida': 31},
    '2021-10-23': {'Fila corrida': 14, 'Olympikus corrida': 22, 'Mizuno corrida': 28, 'Asics corrida': 25},
    '2021-10-30': {'Fila corrida': 9, 'Olympikus corrida': 16, 'Mizuno corrida': 22, 'Asics corrida': 39},
    '2021-11-06': {'Fila corrida': 19, 'Olympikus corrida': 16, 'Mizuno corrida': 23, 'Asics corrida': 36},
    '2021-11-13': {'Fila corrida': 17, 'Olympikus corrida': 21, 'Mizuno corrida': 28, 'Asics corrida': 36},
    '2021-11-20': {'Fila corrida': 19, 'Olympikus corrida': 24, 'Mizuno corrida': 39, 'Asics corrida': 62},
    '2021-11-27': {'Fila corrida': 13, 'Olympikus corrida': 21, 'Mizuno corrida': 24, 'Asics corrida': 41},
    '2021-12-04': {'Fila corrida': 16, 'Olympikus corrida': 14, 'Mizuno corrida': 18, 'Asics corrida': 32},
    '2021-12-11': {'Fila corrida': 13, 'Olympikus corrida': 16, 'Mizuno corrida': 15, 'Asics corrida': 38},
    '2021-12-18': {'Fila corrida': 17, 'Olympikus corrida': 19, 'Mizuno corrida': 27, 'Asics corrida': 33},
    '2021-12-25': {'Fila corrida': 19, 'Olympikus corrida': 18, 'Mizuno corrida': 18, 'Asics corrida': 32},
    '2022-01-01': {'Fila corrida': 19, 'Olympikus corrida': 26, 'Mizuno corrida': 30, 'Asics corrida': 53},
    '2022-01-08': {'Fila corrida': 17, 'Olympikus corrida': 19, 'Mizuno corrida': 36, 'Asics corrida': 42},
    '2022-01-15': {'Fila corrida': 19, 'Olympikus corrida': 21, 'Mizuno corrida': 21, 'Asics corrida': 53},
    '2022-01-22': {'Fila corrida': 16, 'Olympikus corrida': 27, 'Mizuno corrida': 29, 'Asics corrida': 43},
    '2022-01-29': {'Fila corrida': 20, 'Olympikus corrida': 29, 'Mizuno corrida': 28, 'Asics corrida': 58},
    '2022-02-05': {'Fila corrida': 15, 'Olympikus corrida': 23, 'Mizuno corrida': 40, 'Asics corrida': 38},
    '2022-02-12': {'Fila corrida': 22, 'Olympikus corrida': 30, 'Mizuno corrida': 34, 'Asics corrida': 50},
    '2022-02-19': {'Fila corrida': 20, 'Olympikus corrida': 27, 'Mizuno corrida': 31, 'Asics corrida': 44},
    '2022-02-26': {'Fila corrida': 24, 'Olympikus corrida': 30, 'Mizuno corrida': 29, 'Asics corrida': 47},
    '2022-03-05': {'Fila corrida': 21, 'Olympikus corrida': 26, 'Mizuno corrida': 33, 'Asics corrida': 49},
    '2022-03-12': {'Fila corrida': 22, 'Olympikus corrida': 29, 'Mizuno corrida': 39, 'Asics corrida': 51},
    '2022-03-19': {'Fila corrida': 20, 'Olympikus corrida': 29, 'Mizuno corrida': 29, 'Asics corrida': 49},
    '2022-03-26': {'Fila corrida': 21, 'Olympikus corrida': 24, 'Mizuno corrida': 31, 'Asics corrida': 48},
    '2022-04-02': {'Fila corrida': 17, 'Olympikus corrida': 27, 'Mizuno corrida': 33, 'Asics corrida': 43},
    '2022-04-09': {'Fila corrida': 25, 'Olympikus corrida': 35, 'Mizuno corrida': 33, 'Asics corrida': 56},
    '2022-04-16': {'Fila corrida': 22, 'Olympikus corrida': 29, 'Mizuno corrida': 29, 'Asics corrida': 52},
    '2022-04-23': {'Fila corrida': 24, 'Olympikus corrida': 26, 'Mizuno corrida': 26, 'Asics corrida': 54},
    '2022-04-30': {'Fila corrida': 21, 'Olympikus corrida': 29, 'Mizuno corrida': 35, 'Asics corrida': 52},
    '2022-05-07': {'Fila corrida': 22, 'Olympikus corrida': 31, 'Mizuno corrida': 33, 'Asics corrida': 57},
    '2022-05-14': {'Fila corrida': 23, 'Olympikus corrida': 16, 'Mizuno corrida': 28, 'Asics corrida': 58},
    '2022-05-21': {'Fila corrida': 23, 'Olympikus corrida': 23, 'Mizuno corrida': 23, 'Asics corrida': 45},
    '2022-05-28': {'Fila corrida': 20, 'Olympikus corrida': 21, 'Mizuno corrida': 27, 'Asics corrida': 43},
    '2022-06-04': {'Fila corrida': 21, 'Olympikus corrida': 29, 'Mizuno corrida': 34, 'Asics corrida': 48},
    '2022-06-11': {'Fila corrida': 23, 'Olympikus corrida': 27, 'Mizuno corrida': 31, 'Asics corrida': 43},
    '2022-06-18': {'Fila corrida': 21, 'Olympikus corrida': 25, 'Mizuno corrida': 26, 'Asics corrida': 46},
    '2022-06-25': {'Fila corrida': 19, 'Olympikus corrida': 28, 'Mizuno corrida': 27, 'Asics corrida': 40},
    '2022-07-02': {'Fila corrida': 27, 'Olympikus corrida': 30, 'Mizuno corrida': 32, 'Asics corrida': 53},
    '2022-07-09': {'Fila corrida': 31, 'Olympikus corrida': 39, 'Mizuno corrida': 31, 'Asics corrida': 55},
    '2022-07-16': {'Fila corrida': 24, 'Olympikus corrida': 34, 'Mizuno corrida': 30, 'Asics corrida': 46},
    '2022-07-23': {'Fila corrida': 25, 'Olympikus corrida': 29, 'Mizuno corrida': 32, 'Asics corrida': 47},
    '2022-07-30': {'Fila corrida': 29, 'Olympikus corrida': 36, 'Mizuno corrida': 44, 'Asics corrida': 52},
    '2022-08-06': {'Fila corrida': 25, 'Olympikus corrida': 39, 'Mizuno corrida': 42, 'Asics corrida': 55},
    '2022-08-13': {'Fila corrida': 23, 'Olympikus corrida': 30, 'Mizuno corrida': 42, 'Asics corrida': 46},
    '2022-08-20': {'Fila corrida': 26, 'Olympikus corrida': 34, 'Mizuno corrida': 40, 'Asics corrida': 43},
    '2022-08-27': {'Fila corrida': 23, 'Olympikus corrida': 28, 'Mizuno corrida': 33, 'Asics corrida': 41},
    '2022-09-03': {'Fila corrida': 25, 'Olympikus corrida': 32, 'Mizuno corrida': 39, 'Asics corrida': 36},
    '2022-09-10': {'Fila corrida': 25, 'Olympikus corrida': 34, 'Mizuno corrida': 38, 'Asics corrida': 38},
    '2022-09-17': {'Fila corrida': 24, 'Olympikus corrida': 31, 'Mizuno corrida': 38, 'Asics corrida': 46},
    '2022-09-24': {'Fila corrida': 23, 'Olympikus corrida': 28, 'Mizuno corrida': 34, 'Asics corrida': 43},
    '2022-10-01': {'Fila corrida': 22, 'Olympikus corrida': 23, 'Mizuno corrida': 27, 'Asics corrida': 38},
    '2022-10-08': {'Fila corrida': 22, 'Olympikus corrida': 30, 'Mizuno corrida': 32, 'Asics corrida': 40},
    '2022-10-15': {'Fila corrida': 25, 'Olympikus corrida': 28, 'Mizuno corrida': 30, 'Asics corrida': 40},
    '2022-10-22': {'Fila corrida': 22, 'Olympikus corrida': 30, 'Mizuno corrida': 37, 'Asics corrida': 39},
    '2022-10-29': {'Fila corrida': 27, 'Olympikus corrida': 27, 'Mizuno corrida': 27, 'Asics corrida': 37},
    '2022-11-05': {'Fila corrida': 32, 'Olympikus corrida': 34, 'Mizuno corrida': 39, 'Asics corrida': 43},
    '2022-11-12': {'Fila corrida': 33, 'Olympikus corrida': 40, 'Mizuno corrida': 44, 'Asics corrida': 62},
    '2022-11-19': {'Fila corrida': 39, 'Olympikus corrida': 43, 'Mizuno corrida': 51, 'Asics corrida': 75},
    '2022-11-26': {'Fila corrida': 34, 'Olympikus corrida': 35, 'Mizuno corrida': 44, 'Asics corrida': 49},
    '2022-12-03': {'Fila corrida': 27, 'Olympikus corrida': 35, 'Mizuno corrida': 36, 'Asics corrida': 49},
    '2022-12-10': {'Fila corrida': 25, 'Olympikus corrida': 32, 'Mizuno corrida': 29, 'Asics corrida': 42},
    '2022-12-17': {'Fila corrida': 38, 'Olympikus corrida': 33, 'Mizuno corrida': 28, 'Asics corrida': 43},
    '2022-12-24': {'Fila corrida': 31, 'Olympikus corrida': 40, 'Mizuno corrida': 43, 'Asics corrida': 51},
    '2022-12-31': {'Fila corrida': 38, 'Olympikus corrida': 41, 'Mizuno corrida': 49, 'Asics corrida': 55},
    '2023-01-07': {'Fila corrida': 43, 'Olympikus corrida': 52, 'Mizuno corrida': 46, 'Asics corrida': 57},
    '2023-01-14': {'Fila corrida': 35, 'Olympikus corrida': 36, 'Mizuno corrida': 45, 'Asics corrida': 62},
    '2023-01-21': {'Fila corrida': 38, 'Olympikus corrida': 41, 'Mizuno corrida': 41, 'Asics corrida': 56},
    '2023-01-28': {'Fila corrida': 35, 'Olympikus corrida': 39, 'Mizuno corrida': 42, 'Asics corrida': 54},
    '2023-02-04': {'Fila corrida': 30, 'Olympikus corrida': 47, 'Mizuno corrida': 41, 'Asics corrida': 62},
    '2023-02-11': {'Fila corrida': 33, 'Olympikus corrida': 42, 'Mizuno corrida': 46, 'Asics corrida': 52},
    '2023-02-18': {'Fila corrida': 31, 'Olympikus corrida': 42, 'Mizuno corrida': 39, 'Asics corrida': 50},
    '2023-02-25': {'Fila corrida': 32, 'Olympikus corrida': 44, 'Mizuno corrida': 43, 'Asics corrida': 56},
    '2023-03-04': {'Fila corrida': 35, 'Olympikus corrida': 42, 'Mizuno corrida': 53, 'Asics corrida': 60},
    '2023-03-11': {'Fila corrida': 41, 'Olympikus corrida': 42, 'Mizuno corrida': 48, 'Asics corrida': 64},
    '2023-03-18': {'Fila corrida': 34, 'Olympikus corrida': 44, 'Mizuno corrida': 43, 'Asics corrida': 50},
    '2023-03-25': {'Fila corrida': 35, 'Olympikus corrida': 46, 'Mizuno corrida': 41, 'Asics corrida': 51},
    '2023-04-01': {'Fila corrida': 36, 'Olympikus corrida': 45, 'Mizuno corrida': 37, 'Asics corrida': 54},
    '2023-04-08': {'Fila corrida': 34, 'Olympikus corrida': 41, 'Mizuno corrida': 47, 'Asics corrida': 48},
    '2023-04-15': {'Fila corrida': 35, 'Olympikus corrida': 43, 'Mizuno corrida': 41, 'Asics corrida': 52},
    '2023-04-22': {'Fila corrida': 40, 'Olympikus corrida': 36, 'Mizuno corrida': 41, 'Asics corrida': 47},
    '2023-04-29': {'Fila corrida': 45, 'Olympikus corrida': 46, 'Mizuno corrida': 55, 'Asics corrida': 63},
    '2023-05-06': {'Fila corrida': 38, 'Olympikus corrida': 45, 'Mizuno corrida': 53, 'Asics corrida': 67},
    '2023-05-13': {'Fila corrida': 31, 'Olympikus corrida': 44, 'Mizuno corrida': 49, 'Asics corrida': 56},
    '2023-05-20': {'Fila corrida': 38, 'Olympikus corrida': 43, 'Mizuno corrida': 36, 'Asics corrida': 63},
    '2023-05-27': {'Fila corrida': 43, 'Olympikus corrida': 44, 'Mizuno corrida': 37, 'Asics corrida': 54},
    '2023-06-03': {'Fila corrida': 43, 'Olympikus corrida': 45, 'Mizuno corrida': 47, 'Asics corrida': 56},
    '2023-06-10': {'Fila corrida': 38, 'Olympikus corrida': 43, 'Mizuno corrida': 44, 'Asics corrida': 58},
    '2023-06-17': {'Fila corrida': 28, 'Olympikus corrida': 37, 'Mizuno corrida': 39, 'Asics corrida': 46},
    '2023-06-24': {'Fila corrida': 43, 'Olympikus corrida': 47, 'Mizuno corrida': 40, 'Asics corrida': 59},
    '2023-07-01': {'Fila corrida': 39, 'Olympikus corrida': 47, 'Mizuno corrida': 39, 'Asics corrida': 67},
    '2023-07-08': {'Fila corrida': 48, 'Olympikus corrida': 46, 'Mizuno corrida': 40, 'Asics corrida': 54},
    '2023-07-15': {'Fila corrida': 40, 'Olympikus corrida': 49, 'Mizuno corrida': 44, 'Asics corrida': 45},
    '2023-07-22': {'Fila corrida': 37, 'Olympikus corrida': 50, 'Mizuno corrida': 46, 'Asics corrida': 52},
    '2023-07-29': {'Fila corrida': 45, 'Olympikus corrida': 48, 'Mizuno corrida': 50, 'Asics corrida': 64},
    '2023-08-05': {'Fila corrida': 48, 'Olympikus corrida': 48, 'Mizuno corrida': 66, 'Asics corrida': 55},
    '2023-08-12': {'Fila corrida': 43, 'Olympikus corrida': 54, 'Mizuno corrida': 55, 'Asics corrida': 57},
    '2023-08-19': {'Fila corrida': 45, 'Olympikus corrida': 47, 'Mizuno corrida': 43, 'Asics corrida': 60},
    '2023-08-26': {'Fila corrida': 50, 'Olympikus corrida': 57, 'Mizuno corrida': 58, 'Asics corrida': 59},
    '2023-09-02': {'Fila corrida': 50, 'Olympikus corrida': 52, 'Mizuno corrida': 44, 'Asics corrida': 53},
    '2023-09-09': {'Fila corrida': 39, 'Olympikus corrida': 61, 'Mizuno corrida': 43, 'Asics corrida': 53},
    '2023-09-16': {'Fila corrida': 43, 'Olympikus corrida': 49, 'Mizuno corrida': 42, 'Asics corrida': 51},
    '2023-09-23': {'Fila corrida': 39, 'Olympikus corrida': 46, 'Mizuno corrida': 41, 'Asics corrida': 49},
    '2023-09-30': {'Fila corrida': 54, 'Olympikus corrida': 49, 'Mizuno corrida': 48, 'Asics corrida': 52},
    '2023-10-07': {'Fila corrida': 48, 'Olympikus corrida': 54, 'Mizuno corrida': 42, 'Asics corrida': 50},
    '2023-10-14': {'Fila corrida': 41, 'Olympikus corrida': 54, 'Mizuno corrida': 47, 'Asics corrida': 52},
    '2023-10-21': {'Fila corrida': 49, 'Olympikus corrida': 53, 'Mizuno corrida': 58, 'Asics corrida': 57},
    '2023-10-28': {'Fila corrida': 56, 'Olympikus corrida': 50, 'Mizuno corrida': 68, 'Asics corrida': 65},
    '2023-11-04': {'Fila corrida': 56, 'Olympikus corrida': 64, 'Mizuno corrida': 74, 'Asics corrida': 55},
    '2023-11-11': {'Fila corrida': 51, 'Olympikus corrida': 59, 'Mizuno corrida': 66, 'Asics corrida': 57},
    '2023-11-18': {'Fila corrida': 68, 'Olympikus corrida': 78, 'Mizuno corrida': 100, 'Asics corrida': 81},
    '2023-11-25': {'Fila corrida': 50, 'Olympikus corrida': 55, 'Mizuno corrida': 70, 'Asics corrida': 62},
    '2023-12-02': {'Fila corrida': 54, 'Olympikus corrida': 51, 'Mizuno corrida': 62, 'Asics corrida': 60},
    '2023-12-09': {'Fila corrida': 52, 'Olympikus corrida': 55, 'Mizuno corrida': 75, 'Asics corrida': 64},
    '2023-12-16': {'Fila corrida': 47, 'Olympikus corrida': 56, 'Mizuno corrida': 65, 'Asics corrida': 58},
    '2023-12-23': {'Fila corrida': 57, 'Olympikus corrida': 61, 'Mizuno corrida': 64, 'Asics corrida': 70},
    '2023-12-30': {'Fila corrida': 59, 'Olympikus corrida': 84, 'Mizuno corrida': 77, 'Asics corrida': 82},
    '2024-01-06': {'Fila corrida': 73, 'Olympikus corrida': 91, 'Mizuno corrida': 77, 'Asics corrida': 87},
    '2024-01-13': {'Fila corrida': 67, 'Olympikus corrida': 84, 'Mizuno corrida': 54, 'Asics corrida': 85},
    '2024-01-20': {'Fila corrida': 63, 'Olympikus corrida': 79, 'Mizuno corrida': 57, 'Asics corrida': 88},
    '2024-01-27': {'Fila corrida': 73, 'Olympikus corrida': 70, 'Mizuno corrida': 67, 'Asics corrida': 80},
    '2024-02-03': {'Fila corrida': 57, 'Olympikus corrida': 71, 'Mizuno corrida': 60, 'Asics corrida': 77},
    '2024-02-10': {'Fila corrida': 56, 'Olympikus corrida': 68, 'Mizuno corrida': 60, 'Asics corrida': 76},
    '2024-02-17': {'Fila corrida': 56, 'Olympikus corrida': 64, 'Mizuno corrida': 53, 'Asics corrida': 70},
    '2024-02-24': {'Fila corrida': 57, 'Olympikus corrida': 60, 'Mizuno corrida': 60, 'Asics corrida': 77},
    '2024-03-02': {'Fila corrida': 64, 'Olympikus corrida': 80, 'Mizuno corrida': 60, 'Asics corrida': 77},
    '2024-03-09': {'Fila corrida': 68, 'Olympikus corrida': 83, 'Mizuno corrida': 67, 'Asics corrida': 77},
    '2024-03-16': {'Fila corrida': 61, 'Olympikus corrida': 74, 'Mizuno corrida': 63, 'Asics corrida': 82},
    '2024-03-23': {'Fila corrida': 61, 'Olympikus corrida': 64, 'Mizuno corrida': 68, 'Asics corrida': 84},
    '2024-03-30': {'Fila corrida': 77, 'Olympikus corrida': 83, 'Mizuno corrida': 68, 'Asics corrida': 84},
    '2024-04-06': {'Fila corrida': 62, 'Olympikus corrida': 87, 'Mizuno corrida': 61, 'Asics corrida': 89},
    '2024-04-13': {'Fila corrida': 77, 'Olympikus corrida': 76, 'Mizuno corrida': 56, 'Asics corrida': 82},
    '2024-04-20': {'Fila corrida': 65, 'Olympikus corrida': 90, 'Mizuno corrida': 56, 'Asics corrida': 93},
    '2024-04-27': {'Fila corrida': 72, 'Olympikus corrida': 96, 'Mizuno corrida': 63, 'Asics corrida': 94},
    '2024-05-04': {'Fila corrida': 72, 'Olympikus corrida': 82, 'Mizuno corrida': 57, 'Asics corrida': 86},
    '2024-05-11': {'Fila corrida': 72, 'Olympikus corrida': 82, 'Mizuno corrida': 59, 'Asics corrida': 67},
    '2024-05-18': {'Fila corrida': 68, 'Olympikus corrida': 78, 'Mizuno corrida': 62, 'Asics corrida': 98},
    '2024-05-25': {'Fila corrida': 72, 'Olympikus corrida': 78, 'Mizuno corrida': 54, 'Asics corrida': 94},
    '2024-06-01': {'Fila corrida': 79, 'Olympikus corrida': 71, 'Mizuno corrida': 63, 'Asics corrida': 91},
    '2024-06-08': {'Fila corrida': 94, 'Olympikus corrida': 94, 'Mizuno corrida': 69, 'Asics corrida': 92},
    '2024-06-15': {'Fila corrida': 62, 'Olympikus corrida': 71, 'Mizuno corrida': 59, 'Asics corrida': 78},
    '2024-06-22': {'Fila corrida': 71, 'Olympikus corrida': 80, 'Mizuno corrida': 61, 'Asics corrida': 75},
    '2024-06-29': {'Fila corrida': 65, 'Olympikus corrida': 81, 'Mizuno corrida': 61, 'Asics corrida': 85},
    '2024-07-06': {'Fila corrida': 60, 'Olympikus corrida': 74, 'Mizuno corrida': 55, 'Asics corrida': 88},
    '2024-07-13': {'Fila corrida': 71, 'Olympikus corrida': 98, 'Mizuno corrida': 68, 'Asics corrida': 93},
    '2024-07-20': {'Fila corrida': 73, 'Olympikus corrida': 91, 'Mizuno corrida': 65, 'Asics corrida': 92},
    '2024-07-27': {'Fila corrida': 79, 'Olympikus corrida': 90, 'Mizuno corrida': 65, 'Asics corrida': 99}
}

'''

# Converte o dicionário em um DataFrame
df = pd.DataFrame(list(data.items()), columns=['Date', 'Searches'])
df['Date'] = pd.to_datetime(df['Date'])

# Calcula a média de buscas por ano
df['Year'] = df['Date'].dt.year
yearly_avg = df.groupby('Year')['Searches'].mean()

# Calcula o crescimento percentual entre os anos
yearly_growth = yearly_avg.pct_change() * 100

# Exibe os resultados
print("Média de buscas por ano:")
print(yearly_avg)
print("\nCrescimento percentual anual:")
print(yearly_growth)

# Para calcular o crescimento percentual entre a data inicial e a data final
start_date = df['Date'].min()
end_date = df['Date'].max()
start_value = df.loc[df['Date'] == start_date, 'Searches'].values[0]
end_value = df.loc[df['Date'] == end_date, 'Searches'].values[0]

growth_overall = ((end_value - start_value) / start_value) * 100

print(f"\nCrescimento percentual de {start_date.date()} até {end_date.date()}: {growth_overall:.2f}%")
'''

# Converte o dicionário em um DataFrame
df = pd.DataFrame.from_dict(data, orient='index')
df.index = pd.to_datetime(df.index)
df['Year'] = df.index.year

# Calcula a média de buscas por ano para cada marca
yearly_avg = df.groupby('Year').mean()

# Calcula o crescimento percentual entre os anos para cada marca
yearly_growth = yearly_avg.pct_change() * 100

# Exibe os resultados
print("Média de buscas por ano:")
print(yearly_avg)
print("\nCrescimento percentual anual:")
print(yearly_growth)

# Para calcular o crescimento percentual entre a data inicial e a data final para cada marca
start_date = df.index.min()
end_date = df.index.max()
growth_overall = {}

for column in df.columns[:-1]:  # Exclui a coluna 'Year' da iteração
    start_value = df.loc[start_date, column]
    end_value = df.loc[end_date, column]
    growth_overall[column] = ((end_value - start_value) / start_value) * 100

print(f"\nCrescimento percentual de {start_date.date()} até {end_date.date()}:")
for brand, growth in growth_overall.items():
    print(f"{brand}: {growth:.2f}%")