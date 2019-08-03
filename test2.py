# coding=utf-8
import csv
import matplotlib.pyplot as plt


class GetAvgFromCsv():

    def __init__(self, filename, key, values):
        self.filename = filename
        self.key = key
        self.values = values
        self.data = {}

    def _get_dict_data_form_file(self, value):
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
    data = GetAvgFromCsv('pollution.csv', 'year', ['pm2.5', 'TEMP', 'PRES', 'Iws']).get_data()
    print(data)
    data_dict = {}
    for key, data in data.items():
        data_dict[key] = []
        for value in data.values():
            data_dict[key].append(value)
            print(data_dict)
    # 使用subplot
    x = ([2010, 2011, 2012, 2013, 2014])
    y1 = data_dict['pm2.5']
    plt.subplot(2, 2, 1)  # 两行两列，第一个图
    plt.plot(x, y1, 'r')
    plt.xticks([2010, 2011, 2012, 2013, 2014])
    plt.xlabel('year', fontsize='10')
    plt.ylabel('颗粒大小', fontsize='10')
    plt.title('2010-2014年度PM2.5变化情况', fontsize='11')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False


# 两行两列的第二个图
    x = ([2010, 2011, 2012, 2013, 2014])
    y2 = data_dict['TEMP']
    plt.subplot(2, 2, 2)
    plt.plot(x, y2, 'g')
    plt.xticks([2010, 2011, 2012, 2013, 2014])
    plt.xlabel('year', fontsize='10')
    plt.ylabel('温度', fontsize='10')
    plt.title('2010-2014年度气温变化情况', fontsize='11')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    # 两行两列的第三个图
    x = ([2010, 2011, 2012, 2013, 2014])
    y3 = data_dict['PRES']
    plt.subplot(2, 2, 3)
    plt.plot(x, y3, '#87CEFA')
    plt.xticks([2010, 2011, 2012, 2013, 2014])
    plt.xlabel('year', fontsize='10')
    plt.ylabel('PA', fontsize='10')
    plt.title('2010-2014年度气压变化情况', fontsize='11')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    # 两行两列的第四个图
    x = ([2010, 2011, 2012, 2013, 2014])
    y4 = data_dict['Iws']
    plt.subplot(2, 2, 4)
    plt.plot(x, y4, 'b')
    plt.xticks([2010, 2011, 2012, 2013, 2014])
    plt.xlabel('year', fontsize='10')
    plt.ylabel('单位/mm', fontsize='10')
    plt.title('2010-2014年度降雨量变化情况', fontsize='11')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

plt.subplots_adjust(wspace=0.5, hspace=0.5)

plt.show()
