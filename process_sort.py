def sort_process_table(process_table, sorting_parameter):
    if sorting_parameter == 1:  # Sort by P_ID
        return sorted(process_table, key=lambda x: x[0])
    elif sorting_parameter == 2:  # Sort by Start Time
        return sorted(process_table, key=lambda x: x[2])
    elif sorting_parameter == 3:  # Sort by Priority
        priority_order = {"Low": 1, "MID": 2, "High": 3}
        return sorted(process_table, key=lambda x: priority_order[x[3]])

if __name__ == "__main__":
    process_table = [
        ("P1", "VSCode", 100, "MID"),
        ("P23", "Eclipse", 234, "MID"),
        ("P93", "Chrome", 189, "High"),
        ("P42", "JDK", 9, "High"),
        ("P9", "CMD", 7, "High"),
        ("P87", "NotePad", 23, "Low"),
    ]

    print("Sorting Options:")
    print("1. Sort by P_ID")
    print("2. Sort by Start Time")
    print("3. Sort by Priority")

    sorting_option = int(input("Enter sorting option: "))

    sorted_process_table = sort_process_table(process_table, sorting_option)
    print("\nSorted Process Table:")
    print("P_ID  Process   Start Time (ms)  Priority")
    print("-" * 40)
    for row in sorted_process_table:
        print(f"{row[0]:<5} {row[1]:<9} {row[2]:<16} {row[3]}")
