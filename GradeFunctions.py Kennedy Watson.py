# Kennedy Watson
# SCIS 111-113
# Function practice
# Program meant to compute avg and letter grade with five tests
# Lowest score
# Functions needed for get_grade, Do_avg, Lowest, and Letter_ Grade


def get_grade():
    grade = float(input("Enter a grade between 0 and 100: "))
    while grade < 0 or grade > 100:
        print("This number is out of range, please try again.")
        grade = float(input("Enter a grade between 0 and 100: "))
    return grade

def Lowest(T1, T2, T3, T4, T5):
    lowNum = T1
    if T2 < lowNum:
        lowNum = T2
    if T3 < lowNum:
        lowNum = T3
    if T4 < lowNum:
        lowNum = T4
    if T5 < lowNum:
        lowNum = T5
    return lowNum

def Do_Average(T1, T2, T3, T4, T5):
    total = T1 + T2 + T3 + T4 + T5
    lowTest = Lowest(T1, T2, T3, T4, T5)
    total -= lowTest  # Subtract the lowest test score
    average = total / 4  # Divide by 4 since one score is dropped
    return average

def letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def main():
    # Get grades from the user
    Test1 = get_grade()
    Test2 = get_grade()
    Test3 = get_grade()
    Test4 = get_grade()
    Test5 = get_grade()

    # Calculate average and letter grade
    Average = Do_Average(Test1, Test2, Test3, Test4, Test5)
    Letter = letter_grade(Average)

    # Output results
    print(f"You have an average of {Average:.2f} and a letter grade of {Letter}.")

# Call the main function to execute the program
if __name__ == "__main__":
    main()


    

    






