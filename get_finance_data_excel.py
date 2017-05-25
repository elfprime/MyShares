import tushare as ts
from pandas import ExcelWriter

def get_finance_data(date):
    """
    date[0] - year, int
    date[1] - date(1,2,3,4), int
    """
    fileName = 'stock_finance_' + str(date[0]) + '_' + str(date[1]) + '.xlsx'
    try:
        df1 = ts.get_report_data(date[0], date[1]).drop_duplicates()
        df2 = ts.get_profit_data(date[0], date[1]).drop_duplicates()
        df3 = ts.get_growth_data(date[0], date[1]).drop_duplicates()
    except Exception as e:
        print e
        print date
    else:
        file = ExcelWriter(fileName)
        df1.to_excel(file, 'main')
        df2.to_excel(file, 'profit')
        df3.to_excel(file, 'growth')

def main():
    start = [2017, 1]
    end = [2017, 1]
    for year in range(start[0], end[0] + 1):
        for quater in range(1, 5):
            if year == start[0] and quater < start[1]:
                continue
            if year == end[0] and quater > end[1]:
                break
            get_finance_data([year, quater])

if __name__ == '__main__':
    main()


