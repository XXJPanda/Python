import csv
import matplotlib.pyplot as plt

class GetHeightMonthData():
    def __init__(self, key, filename='pollution.csv', month=5):
        self.key = key
        self.month = month
        self.filename = filename

    def _get_dict_data_from_file(self):
        dict_data = {}

        with open(self.filename, 'r') as fp:
            lines = csv.DictReader(fp)

            for line in lines:
                year = line['year']
                month = line['month']

                try:
                    value = int(line[self.key])
                except ValueError:
                    continue

                if year not in dict_data:
                    dict_data[year] = {}

                month_dicts = dict_data[year]

                if month not in month_dicts:
                    month_dicts[month] = {'sum': 0, 'counter': 0}

                month_dict = month_dicts[month]
                month_dict['sum'] += value
                month_dict['counter'] += 1

        return dict_data

    def _get_every_month_avg_data(self, dict_data):
        every_month_avg_data = {}
        for year, values in dict_data.items():
            every_month_avg_data[year] = []
            for month, month_dict in values.items():
                avg = month_dict['sum'] / month_dict['counter']
                every_month_avg_data[year].append((month, avg))

        return every_month_avg_data

    def _get_height_month_data(self, data_avg_dict):
        result_data_avg_dict = {}
        for year, value_list in data_avg_dict.items():
            result_list = sorted(value_list, key=lambda value: value[1])
            result_list.reverse()
            result_list = result_list[:self.month]
            result_data_avg_dict[year] = result_list

        return result_data_avg_dict

    def _get_every_day_data_from_year_and_month(self, year, month):
        result_data = []
        with open(self.filename, 'r') as fp:
            lines = csv.DictReader(fp)

            for line in lines:
                if line['year'] == year and line['month'] == month:
                    result_data.append(line['pm2.5'])

        return result_data

    def get_result(self):
        result = {}
        dict_data = self._get_dict_data_from_file()
        data_avg_dict = self._get_every_month_avg_data(dict_data)
        data_avg_dict = self._get_height_month_data(data_avg_dict)

        for year, value_list in data_avg_dict.items():
            result[year] = {}
            for month, avg in value_list:
                every_day_data = self._get_every_day_data_from_year_and_month(year, month)
                result[year][month] = every_day_data

        return result


if __name__ == '__main__':
    data = GetHeightMonthData('pm2.5').get_result()
    # print(data)
    data_dict = {}
    for key, data in data.items():
        data_dict[key] = []
        for value in data.values():
            data_dict[key].extend(value)
    print(data_dict)

    fig = plt.subplots(1)
    y0 = data_dict['2010']
    y1 = data_dict['2011']
    y2 = data_dict['2012']
    y3 = data_dict['2013']
    y4 = data_dict['2014']
    plt.plot(y0, 'g', label='2010')
    plt.plot(y1, 'r', label='2011')
    plt.plot(y2, 'b', label='2012')
    plt.plot(y3, 'y', label='2013')
    plt.plot(y4, 'c', label='2014')
    plt.xticks([0, 3600])
    plt.yticks([0, 550])
    plt.xlabel('hour', fontsize='10')
    plt.ylabel('PM2.5', fontsize='10')
    plt.title('2010-2014年度平均PM2.5最高的五个月', fontsize='13')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.legend(loc='best')
    plt.legend()
    plt.show()