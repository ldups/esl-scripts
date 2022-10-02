import matplotlib.pyplot as plt
import numpy as np
from datetime import date, timedelta
from hiv_date_sort import extract_date

def get_all_date_difs(pheno_file_path):
    difference_list = []

    with open(pheno_file_path, 'r') as pheno_file:
        end_of_file = False
        while not end_of_file:
            line1 = pheno_file.readline().strip().split(',')[0]

            if line1:
                id, date1 = extract_date(line1)
                line2 = pheno_file.readline().strip().split(',')[0]
                date2 = extract_date(line2)[1]

                difference = date2 - date1
                difference_list.append(difference)

            else:
                end_of_file = True

    return difference_list

def get_dates_as_days(date_dif_list):
    day_list = []
    for date in date_dif_list:
        days = date.days
        day_list.append(days)
    return day_list

def get_dates_as_years(date_dif_list):
    year_list = []
    for date in date_dif_list:
        days = date.days
        years = days / 365
        year_list.append(years)
    return year_list

def plot_date_distribution(date_dif_list, unit):
    '''draws histogram of hiv pairs vs time difference between them'''
    num_bins = 50
    plt.hist(date_dif_list, density=False, bins=num_bins, color = '#33CEFF')
    plt.ylabel('Number of Pairs')
    plt.xlabel('Difference Between Pairs in ' + unit)
    plt.title('Pairs vs. Difference Between Sample Times')
    plt.show()

pheno_file_path = 'hiv_dates\hiv_phenos.txt'
date_dif_list = get_dates_as_years(get_all_date_difs(pheno_file_path))
plot_date_distribution(date_dif_list, 'Years')