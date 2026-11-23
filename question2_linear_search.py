def linear_search_registration(records, target_reg_no):
    """
    Searches for a student's registration number in a list of student records.
    Returns the index of the matching record if found, otherwise -1.
    """
    for index, student in enumerate(records):
        if student.get("reg_no") == target_reg_no:
            return index
    return -1


# Example usage with student records
student_records = [
    {"reg_no": "REG/2026/014", "name": "Amina Wanjiku", "course": "Data Analytics"},
    {"reg_no": "REG/2026/003", "name": "Brian Otieno", "course": "Software Engineering"},
    {"reg_no": "REG/2026/029", "name": "Faith Kamau", "course": "Automotive Engineering"},
    {"reg_no": "REG/2026/011", "name": "David Kiprop", "course": "Electrical Engineering"},
]

target = "REG/2026/029"
position = linear_search_registration(student_records, target)

if position != -1:
    print(f"Found {target} at index {position}: {student_records[position]['name']}")
else:
    print(f"Registration number {target} not found.")
