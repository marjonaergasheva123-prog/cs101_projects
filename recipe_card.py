#A simple kitchen creations program

# --- 1. Input Data ---
recipe_name = input('Enter recipe name')
cuisine_type = input('Enter cuisine type')
chef_name = input('Enter chef name')
main_ingredient=input('Enter name of the main ingredient')
prep_time=input('Enter preparation time')

#---2.Constants for borders---
HEADER_BORDER= '+' * 36
SEPARATOR= '-' * 36

#---3. Signature dish---
signature_dish = "Signature Dish: " + chef_name + "'s Famous" + cuisine_type +"  "+ recipe_name

# --- 4. Print the Formatted Profile Card ---

# Header Block
print(HEADER_BORDER)
#center
print("KITCHEN CREATIONS".center(36))
print(HEADER_BORDER)


print()


# Main Info Block 
print("RECIPE: "+ recipe_name)      # 6 chars + 7 spaces = 13
print("CUISINE:"+ cuisine_type)      # 7 chars + 6 spaces = 13
print("CHEF:" + chef_name)      # 4 chars + 9 spaces = 13

print()


print("Signature Dish: " + signature_dish) # 7 chars + 6 spaces =13

print(SEPARATOR)

print("Main Ingredient:" +main_ingredient) # 7chars + 6 spaces = 13

print("Prep Time: " +prep_time)   #7chars + 6 spaces = 13
 
print(SEPARATOR)