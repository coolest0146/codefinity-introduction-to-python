# Intial lists
junior_school_students = ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack', 'Kelly']
middle_school_students = ['Liam', 'Mona', 'Nina', 'Oscar', 'Paul', 'Quinn', 'Rachel', 'Sam', 'Tina', 'Ursula', 'Vera']
high_school_students = ['William', 'Xander', 'Yara', 'Zane', 'Amos', 'Bella', 'Chris', 'Diana', 'Ethan', 'Fiona', 'George']
junior_middle = []
all_students = []

# Write your code here
junior_middle=junior_school_students + middle_school_students
result=junior_middle+high_school_students
all_students.extend(result)
# Testing
print(f"All students list: {result}")
