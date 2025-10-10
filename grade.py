student_name= input('Enrer your name')
GPA= float(input("Enter your GPA (0-4.0): "))
credit_hours=int (input("Enter your total credit hours: "))
dean_list = GPA >= 3.5 and credit_hours >= 12

student_information= (f"{student_name},{GPA},{credit_hours}")
print(bool(dean_list))
print(student_information)
print(f"Deans list: {"True" if dean_list else "False"}  ")
print(f"How many gpa needs:{"no need" if GPA>=3.5 else 3.5-GPA }")
print(f"How many more credits needed: {"no need"if credit_hours >=12 else 12-credit_hours}")
