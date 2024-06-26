#prints list
def display_list(label, items):
    print(label)
    for item in items:
        print(item)

def main():

    #create list
    foods = ["pizza", "salad", "hamburger", "steak", "apple", "orange"]
    display_list("foods in original order:", foods)

    #sorted ascending
    foods.sort()
    display_list("foods in ascending alphabetical order:", foods)

    #sorted decending
    foods.sort(reverse=True)
    display_list("foods in descending alphabetical order:", foods) 

    #copy list sort acending
    foods2 = foods.copy()
    foods2.sort()
    display_list("foods2 in ascending alphabetical order:", foods2)

    #foods list stays the same
    display_list("foods still in descending alphabetical order:", foods)

    #reverse
    foods.reverse()
    display_list("foods in ascending alphabetical order:", foods)

    #add to end of list
    foods.append("carrots")
    foods.append("milk")
    display_list("sorted foods with carrots and milk appended to the end:", foods)

    #sort with carrots and milk added
    foods.sort()
    display_list("foods in ascending alphabetical order:", foods)

    #check index
    pizza_index = foods.index("pizza")
    print("Pizza is at", pizza_index)

    #add fries and check index
    foods.insert(pizza_index, "fries")
    pizza_index = foods.index("pizza")
    print("Pizza is now at", pizza_index)

main()
