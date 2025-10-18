print("--- Specific Requirements ---")
print("-First item-")
name1 = input("Item name: ")
price1 = float(input("Price: "))
quantity1 = float(input("Quantity: "))

print("-Second item-")
name2 = input("Item name: ")
price2 = float(input("Price: "))
quantity2 = float(input("Quantity: "))

print("-Third item-")
name3 = input("Item name: ")
price3 = float(input("Price: "))
quantity3 = float(input("Quantity: "))
total_items = int(input("Enter total items: "))

customer = input("Enter your name: ")
is_member = input("Are you member of this store(yes/no)? ")
total_previous_purcheses = int(input("Enter total amount of previous purcheses(in sum): "))

true = 1 or false = 0
subtotal = price1 + price2 + price3

is_member = true
discount = is_member * 0.10 * subtotal
is_bulk = (total_items > 5) == true
bulk_discount =  is_bulk* 0.05 * subtotal
is_loyal = total_previous_purcheses >= 1000000 == true
loyalty_discount = is_loyal * 0.03 *subtotal 

discounts_stack = is_member + bulk_discount + loyalty_discount
tax_amount = (subtotal - discounts_stack) * 0.12 
shipping_status = subtotal <= 500000 ==true
shipping = shipping_status * 25000
final_total = tax_amount + discounts_stack + shipping
total_saved = subtotal - final_total

print(f"{'+' * 40}")
print("--- Electronic store ---")
print(f"\n\n{'+' * 40}")
print("-" * 40)
print(f"Customer name: {customer}")
print(f"Membership status: {is_member}")
print("-" * 40)
print(f"Item 1: {name1}, {quantity1}, {price1}")
print(f"Item 2: {name2}, {quantity2}, {price2}")
print(f"Item 3: {name3}, {quantity3}, {price3}")
print(f"Subtotal before discounts: {subtotal}")
print(f"Member discount:    {is_member}")
print(f"Discount amount:    {discount}")
print(f"Bulk discount:      {is_bulk}" )
print(f"Discount amount:    {bulk_discount}")
print(f"Loyalty discount:   {is_loyal}")
print(f"Discount amount:    {loyalty_discount}")
print(f"Total discount applied:    {discounts_stack}")
print(f"Subtotal after discounts:  {subtotal - discounts_stack}\n")
print("-" * 40)
print(f"Tax amount: {tax_amount}")
print(f"Shipping status: {shipping_status}")
print(f"Shipping cost: {shipping}")
print("-" * 40)
print(f"Final total: {final_total}")
print(f"Total_saved: {total_saved}")
print("-" * 40)
print("+" * 40)