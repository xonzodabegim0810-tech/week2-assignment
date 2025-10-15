print("\n--- Simple Triangle Pattern ---")
height = int(input("Enter the desired height of a triangle: "))
for row_num in range(height + 1):
    for col_num in range(row_num):
        print("*", end="")
    print()
