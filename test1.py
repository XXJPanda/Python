# coding=utf-8
import csv
import matplotlib.pyplot as plt
import numpy as np


class GetAvgFromCsv():
    def __init__(self, filename, key, values):
        self.filename = filename
        self.key = key
        self.values = values
        self.data = {}

    def _get_dict_data_form_file(self, value):
        # { 'year':{'sum':0,'counter':0} }
        dict_data = {}

        with open(self.filename, 'r') as fp:
            lines = csv.DictReader(fp)
            for line in lines:
                key = line[self.key]
                try:
                    pm2_5 = int(line[value])
                except Exception as e:
                    continue

                if key not in dict_data:
                    dict_data[key] = {'sum': 0, 'counter': 0}

                dict_value = dict_data[key]
                dict_value['sum'] += pm2_5
                dict_value['counter'] += 1

        return dict_data

    def _get_avg_data(self):
        if isinstance(self.values, list):
            for v in self.values:
                temp_data = {}
                dict_data = self._get_dict_data_form_file(v)
                for key, value in dict_data.items():
                    avg = value['sum'] / value['counter']
                    temp_data[key] = avg

                self.data[v] = temp_data
        else:
            temp_data = {}
            dict_data = self._get_dict_data_form_file(self.values)
            for key, value in dict_data.items():
                avg = value['sum'] / value['counter']
                temp_data[key] = avg

            self.data[self.values] = temp_data

        return self.data

    def get_data(self):
        return self._get_avg_data()


if __name__ == '__main__':
    data = GetAvgFromCsv('pollution.csv', 'year', ['pm2.5', 'TEMP']).get_data()
    print(data)

    data_dict = {}
    for key, data in data.items():
        data_dict[key] = []
        for value in data.values():
            data_dict[key].append(value)

    x = np.arange(5)
    y1 = data_dict['TEMP']
    y2 = data_dict['pm2.5']
    width = 0.5
    ax1 = plt.subplot(2, 2, 1)
    ax2 = plt.subplot(2, 2, 4)
    ax1.bar(x, y1, width, color='#87CEFA')
    ax2.bar(x + width, y2, width, color='g')
    ax1.set_xticks(x + width)
    ax1.set_xticklabels(['2010', '2011', '2012', '2013', '2014'])
    ax2.set_xticks(x + width)
    ax2.set_xticklabels(['2010', '2011', '2012', '2013', '2014'])
    ax1.set_title('日平均温度')
    ax2.set_title('日平均pm2.5')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    # 设置横轴标签
    ax1.set_xlabel('Years')
    # 设置纵轴标签
    ax1.set_ylabel('Sheshidu')
    ax2.set_xlabel('Years')
    ax2.set_ylabel('Large')
    plt.show()