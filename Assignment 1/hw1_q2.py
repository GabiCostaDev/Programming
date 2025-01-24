"""
Author: Gabi Costa
Assignment / Part: HW1 - Q2
Date due: 2023-02-09, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

year = int(input('Please enter a year greater than 2023:'))

current_population = 330109174
addition = current_population + 1
removal = current_population - 1

sec_in_min = 60
min_in_hour = 60
hour_in_day = 24
day_in_year = 365
sec_in_year = day_in_year * hour_in_day * min_in_hour * sec_in_min

births_in_year = sec_in_year/7
deaths_in_year = sec_in_year/15
immigrants_in_year = sec_in_year/42
emigrants_in_year = sec_in_year/(1.25*60)

number_of_additional_years = year - 2023

final_population = current_population + (number_of_additional_years * births_in_year) - (number_of_additional_years * deaths_in_year) + (number_of_additional_years * immigrants_in_year) - (number_of_additional_years * emigrants_in_year)

print('The population in year', year, 'will be', final_population)