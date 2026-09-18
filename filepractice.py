students = [
    {
        "Student_ID": 101,
        "Name": "Rohit",
        "Age": 20,
        "Gender": "Male",
        "Class": "BCA",
        "City": "Pune",
        "Marks": 85
    },
    {
        "Student_ID": 101,
        "Name": "Amit",
        "Age": 21,
        "Gender": "Male",
        "Class": "BCA",
        "City": "Mumbai",
        "Marks": 78
    },
    {
        "Student_ID": 103,
        "Name": "Priya",
        "Age": 20,
        "Gender": "Female",
        "Class": "BCA",
        "City": "Nashik",
        "Marks": 92
    },
    {
        "Student_ID": 104,
        "Name": "Sneha",
        "Age": 19,
        "Gender": "Female",
        "Class": "BCA",
        "City": "Nagpur",
        "Marks": 88
    },
    {
        "Student_ID": 105,
        "Name": "Rahul",
        "Age": 21,
        "Gender": "Male",
        "Class": "BCA",
        "City": "Pune",
        "Marks": 74
    },
    {
        "Student_ID": 106,
        "Name": "Neha",
        "Age": 20,
        "Gender": "Female",
        "Class": "BCA",
        "City": "Kolhapur",
        "Marks": 95
    }
]
def sort_value():

    # Sort students by Marks
    sort = sorted(
        students,
        key=lambda val: val["Marks"]
    )

    print("-" * 90)

    # Table Header
    print(
        f"{'Student_ID':<12}"
        f"{'Name':<10}"
        f"{'Age':<8}"
        f"{'Gender':<10}"
        f"{'Class':<10}"
        f"{'City':<12}"
        f"{'Marks':<8}"
        f"{'Grade':<10}"
    )

    print("-" * 90)

    # Print sorted data
    for val in sort:

        # Calculate Grade
        if val["Marks"] >= 90:
            grade = "A"
        elif val["Marks"] >= 80:
            grade = "B"
        elif val["Marks"] >= 60:
            grade = "C"
        elif val["Marks"] >= 45:
            grade = "D"
        else:
            grade = "Fail"

        # Display data
        print(
            f"{val['Student_ID']:<12}"
            f"{val['Name']:<10}"
            f"{val['Age']:<8}"
            f"{val['Gender']:<10}"
            f"{val['Class']:<10}"
            f"{val['City']:<12}"
            f"{val['Marks']:<8}"
            f"{grade:<10}"
        )

    print("-" * 90)


sort_value()


print("============================================STUDENT SUMMARY======================================================")
def total_marks():
    count=0
    for student in students:
        count+=student["Marks"]
    print("1.Total student:",count)
total_marks()

def total_average():
    count=0
    for val in students:
        count=count+val["Marks"]
        average =count/len(students)
    print("2.average the marks of all student:",average)
total_average()

def highest_marks():
    highest=students[0]
    for val in students:
        if val["Marks"]>highest["Marks"]:
            highest=val
    print("3.highest marks:",highest["Marks"])
    print("4.highest marks of student:",highest["Name"])
highest_marks()

def filter_pune():
    for val in students:
        if val["City"]=="Pune":
            print("5.inside the Pune:",val["Name"])
filter_pune()


def lowest_marks():
    lowest=students[0]
    for val in students:
        if val["Marks"]<lowest["Marks"]:
            lowest=val
    print("6.lowest marks:",lowest["Marks"])
    print("7.lowset marks of student:",lowest["Name"])
lowest_marks()
print("=================================================THE END=============================================================")
print("_______________________________Data are arrange to lowest to highest Marks___________________________________________ ")
def sort_data():
    sort=sorted(
        students,
        key=lambda val:val["Marks"]

    )
    for val in sort:
        print(val)
sort_data()
print("_____________________________________________________________________________________________________________________")
print("_____________________________________________duplicate remove________________________________________________________ ")
def duplicate_data():
    unique_val=[]
    duplicate_val=set()
    for val in students:
        if val["Student_ID"] not in duplicate_val:
            unique_val.append(val)
            duplicate_val.add(val["Student_ID"])
    for val in unique_val:
        print(val)
duplicate_data()

print("==================================================THE AND========================================================")


