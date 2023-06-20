menu_item = "pizza"
guests = 11

print(menu_item)
print(guests)
menu_item = "biryani"
print("Updated menu item is: " + menu_item)

biryani_per_person = 1
biryani_needed = biryani_per_person * guests

biryani_prepared = 10
enough_biryani = biryani_prepared == biryani_needed

biryani_per_guest = biryani_prepared / guests
print(biryani_per_guest)