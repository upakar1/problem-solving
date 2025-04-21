numbers_list = [10, 20, 30, 40, 50]
fruits_list = ["apple", "mango"]

# Adding to numbers_list
numbers_list.append(60)                          # Adds 60 at the end
numbers_list.extend([70, 80, 90])                # Adds multiple items
numbers_list.insert(0, 0)                        # Inserts 0 at index 0

# Adding to fruits_list
fruits_list.append("orange")                     # Adds "orange" at the end
fruits_list.extend(["watermelon", "pineapple"])  # Adds multiple fruits
fruits_list.insert(0, "litchi")                  # Inserts "litchi" at beginning

print("Numbers List:", numbers_list)
print("Fruits List:", fruits_list)
