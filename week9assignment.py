
#Variant A
def format_roster(names):
    cleaned_list=[]
    for name in names:
        cleaned = name.strip()
        if cleaned=="":
            continue
        cleaned=cleaned.upper()
        cleaned_list.append(cleaned)

    return cleaned_list
student_list = [
    "  john doe ",
    "JANE SMITH",
    "   ",
    "alice wonderland",
    "bOb rOsS  "
]

print(format_roster(student_list))