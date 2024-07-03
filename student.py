def main():
    # Taking marks input
    marks = []
    num_students = int(input("Enter the number of students: "))
    
    for i in range(num_students):
        mark = float(input(f"Enter marks for student {i+1}: "))
        marks.append(mark)
    
    # Calculating average marks
    average_marks = sum(marks) / num_students
    print(f"Average marks: {average_marks}")
    
    # Sorting marks in descending order
    marks_sorted = sorted(marks, reverse=True)
    
    # Comparing marks
    max_mark = max(marks)
    min_mark = min(marks)
    
    print("\nMarks in descending order:")
    for mark in marks_sorted:
        print(mark)
    
    print(f"\nMaximum marks: {max_mark}")
    print(f"Minimum marks: {min_mark}")
    
if _name_ == "_main_":
    main()
