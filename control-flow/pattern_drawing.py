while True:
    pattern_size = int(input("Enter the size of the pattern: "))
    if pattern_size > 0:
        break
    print("Please enter a positive integer.")
    
rows = 0
    
while rows < pattern_size:
    columns = 0
    while columns < pattern_size:
        print("*", end="")
        columns += 1
    print()
    rows += 1
