# Read integer numbers from a file and determine the
# sum, count, average, maximum, minimum, and range.
# Each number is an a separate line in the file.

# This solution uses the data structures list and dictionary.

# This can throw an exception.
# An error could occur opening or reading the file or converting a line to an int
def get_numbers_from_file(file_name):
    numbers = []
    # with open(file_name) as file: automatically closes the file when leaving the block
    with open(file_name, 'r') as file:
        # Read the file's contents as a list of strings.
        unconverted_numbers = file.readlines()
         # Convert the strings to integers and store them in numbers list
        for number in unconverted_numbers:
                numbers.append(int(number))
    return numbers

def calculate_median(numbers):
    #put in order and count
    numbers.sort()
    count = len(numbers)

    #when it is odd
    if count % 2 == 1:
        median = numbers[count // 2]
    #when it is even
    else:
        firstHalf = numbers[count // 2 - 1]
        secondHalf = numbers[count // 2]
        median = (firstHalf + secondHalf) / 2

    return median

def calculate_mode(numbers):
    number_counts = {}
    
    for number in numbers:
        if number in number_counts:
            number_counts[number] += 1
        else:
            number_counts[number] = 1

    #finds highest frequency
    highest_frequency = max(number_counts.values())
    mode = [number for number, frequency in number_counts.items() if frequency == highest_frequency]

    return mode

def calculate_summary_statistics(numbers):
    # results is a dictionary that holds the sum, count, maximum, minimum, average and range
    results = {}
    results["sum"] = sum(numbers)
    results["count"] = len(numbers)
    results["maximum"] = max(numbers)
    results["minimum"] = min(numbers)
    results["average"] = results["sum"] / results["count"]
    results["range"] = results["maximum"] - results["minimum"]
    results["median"] = calculate_median(numbers)
    results["mode"] = calculate_mode(numbers)
    return results

def display_summary_statistics(file_name, results):
    print("File name:", file_name)
    print("Sum:", results["sum"])
    print("Count:", results["count"])
    print("Average:", results["average"])
    print("Maximum:", results["maximum"])
    print("Minimum:", results["minimum"])
    print("Range:", results["range"])
    print("Median:", results["median"])
    print("Mode:", results["mode"])

def main():
    while (True):
        file_name = input("Enter the path of the file you would like to process: ")
        try:
            numbers = get_numbers_from_file(file_name)
            results = calculate_summary_statistics(numbers)
            display_summary_statistics(file_name, results)
        except Exception as e:
            print("An error occurred:", e)
        
        calculate_again = input("Would you like to evaluate another file? (y/n) ")
        if (calculate_again != "y"):
            break  
        else:
            print('') # separator between inputs

main()
