"""
Write a function called get_list_of_grades() that will:
- Accept a single parameter, grades_filepath ( str ): The address of the CSV file containing the grades data.
- Return a list of lists, where each nested list corresponds to a question the exam,
and itself contains the grade each student got on that question.

"""


def get_list_of_grades():



"""
Write a second function, generate_statistics_report() that will:
- Accept two parameters:
    * grades_filepath ( str ): The address of the CSV file containing the grades data.
    * stats_filepath ( str ): The address of a file to be created containing the statistics of the exam.
    This parameter should default to score_stats.csv if the user does not specify a path.
- Use get_list_of_grades() to get a list of grades of each question from the grades_filepath file.
- Use this list of lists to calculate the mean, standard deviation, and median of each of the questions on the
exam ( Q1_a to Q6 ). To make this easier, import the statistics Python module, which contains functions to
calculate the mean, standard deviation, and median of a list of numbers.
- Print these statistics onto a file ( stats_filepath ).

"""

def generate_statistics_report():


def main():

    grades = get_list_of_grades("Midterm1_scores.csv")
    print(grades)

    generate_statistics_report("Midterm1_scores.csv", "stats.csv")


main()