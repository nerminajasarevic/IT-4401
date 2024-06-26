import csv

#load data into dict for reading
def load_data(file_path):
    
    data = []
    
    with open(file_path, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
            
    return data

#1
def list_dates(data):
    
    formatted_dates = {row['week'][:10] for row in data}
    
    dates = sorted(formatted_dates)
    
    #removes duplicates and prints
    print("\n".join(dates))

#2
def print_modality_by_date(data):

    #get state & date
    print("Enter the two-digit state code (e.g., CA, MO, IL, TX) or 'all' for all states.")
    state = input("State (two-digit code or 'all'): ")
    date = input("Date (MM/DD/YYYY): ")
    
    #find state data at date
    filtered_data = [row for row in data if (state.lower() == 'all' or row['state'].lower() == state.lower()) and row['week'][:10] == date]

    if filtered_data:
        
        #sum num schools & students
        schools = sum(int(row['operational_schools']) for row in filtered_data)
        students = sum(int(row['student_count']) for row in filtered_data)

        #sum students per modality
        modality_count = {'In Person': 0, 'Hybrid': 0, 'Remote': 0}
        for row in filtered_data:
            modality_count[row['learning_modality']] += int(row['operational_schools'])

        print("--------------------------------------")
        print(f"\nDate: {date}")
        print(f"Description: {state.upper() if state.lower() != 'all' else 'All States'}")
        print(f"{schools} schools")
        print(f"{students} students")
        print("Schools per modality:")
        
        #print count and percentage of school modality
        for modality, count in modality_count.items():
            percentage = (count / schools) * 100 if schools != 0 else 0
            print(f" * {count} ({percentage:.1f}%) {modality}")

        #print count and percentage of student modality
        print(f"Students per modality:")
        for modality, count in modality_count.items():
            student_count = sum(int(row['student_count']) for row in filtered_data if row['learning_modality'] == modality)
            student_percentage = (student_count / students) * 100 if students != 0 else 0
            print(f" * {student_count} ({student_percentage:.1f}%) {modality}")
        print("--------------------------------------")

        #loop
        choice = input("\nEnter another state and date? (y/n): ")
        if choice.lower() == 'y':
            print_modality_by_date(data)
    else:
        print("No results found.")

#3
def print_modality_change(data):

    #get state
    print("Enter the two-digit state code (e.g., CA, MO, IL, TX): ")
    state = input("State (two-digit code): ")

    state_data = {}

    #add data to state_data
    for row in data:
        if row['state'].lower() == state.lower():
            date = row['week'][:10]
            if date not in state_data:
                state_data[date] = {'schools': 0, 'students': 0, 'modalities': {'In Person': 0, 'Hybrid': 0, 'Remote': 0}}
            state_data[date]['schools'] += int(row['operational_schools'])
            state_data[date]['students'] += int(row['student_count'])
            state_data[date]['modalities'][row['learning_modality']] += int(row['operational_schools'])

    #print data
    if state_data:
        print("--------------------------------------")
        print(f"Learning Modality Trends for {state.upper()}")

        first_date = '09/06/2020'
        last_date = '05/30/2021'

        first_values = state_data.get(first_date, {'schools': 0, 'students': 0, 'modalities': {'In Person': 0, 'Hybrid': 0, 'Remote': 0}})
        last_values = state_data.get(last_date, {'schools': 0, 'students': 0, 'modalities': {'In Person': 0, 'Hybrid': 0, 'Remote': 0}})

        #print data from state from first recorded instance
        print("\nData as of 09/06/2020")
        print(f"{first_values['schools']} schools")
        print(f"{first_values['students']} students")
        print("Schools per modality:")
        for modality, count in first_values['modalities'].items():
            percentage = (count / first_values['schools']) * 100 if first_values['schools'] != 0 else 0
            print(f" * {count} ({percentage:.1f}%) {modality}")

        #print data from state from last recorded instance
        print("\nData as of 05/30/2021")
        print(f"{last_values['schools']} schools")
        print(f"{last_values['students']} students")
        print("Schools per modality:")
        for modality, count in last_values['modalities'].items():
            percentage = (count / last_values['schools']) * 100 if last_values['schools'] != 0 else 0
            print(f" * {count} ({percentage:.1f}%) {modality}")

        print("--------------------------------------")

        #loop
        choice = input("\nEnter another state? (y/n): ")
        if choice.lower() == 'y':
            print_modality_change(data)
    else:
        print("No results found.")

#main function
def main():
    print("Learning Modalities Analyzer\n")

    #enter file path
    file_path = input("Data file path: ")
    data = load_data(file_path)

    #print menu
    while True:
        print("\nData analysis options:")
        print("1. List dates")
        print("2. Learning modality by state on date")
        print("3. Learning modality by state across time")
        print("4. Exit")

        #get choice
        choice = input("Enter the number of the option (1, 2, 3, or 4): ")

        if choice == '1':
            list_dates(data)
        elif choice == '2':
            print_modality_by_date(data)
        elif choice == '3':
            print_modality_change(data)
        elif choice == '4':
            break
        else:
            print("Please enter (1, 2, 3, or 4): ")

main()
