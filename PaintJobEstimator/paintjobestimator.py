import math

def roundUp(number):
    return math.ceil(number)

def calculateCost(squareFeet, pricePerGallon):

    squareFeetPerGallon = 350
    laborRate = 62.25

    if squareFeet <= 0 or pricePerGallon <= 0:
        print("Error: Enter a positive value.")
        return

    paintGallons = roundUp(squareFeet / squareFeetPerGallon)

    hoursLabor = squareFeet / squareFeetPerGallon * 6

    paintCost = paintGallons * pricePerGallon

    laborCharges = hoursLabor * laborRate

    total = paintCost + laborCharges

    print(f"\nPaint Job Estimator:")
    print(f"Gallons of Paint: {paintGallons}")
    print(f"Hours of Labor: {hoursLabor:.1f} hours")
    print(f"Cost of Paint: ${paintCost:.2f}")
    print(f"Labor Charges: ${laborCharges:.2f}")
    print(f"Total Cost: ${total:.2f}")

while True:
    
    try:
        squareFeet = float(input("Enter the square footage of wall space: "))
        pricePerGallon = float(input("Enter the price per gallon of paint: "))
        
    except ValueError:
        print("Error: Please enter a valid value.")
        continue

    calculateCost(squareFeet, pricePerGallon)

    anotherEstimate = input("\nWould you like to do another estimate? (y/n)").lower()
    if anotherEstimate != 'y':
        exit();
