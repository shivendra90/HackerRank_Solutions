n, m = 7, 21

spaces = int((m-3)/2)
pillars = 1

for line in range(0, int(n/2)):
    print("-" * spaces + ".|." * pillars + "-" * spaces)
    
    spaces = spaces - 3
    pillars = int(pillars + 2)

print("-" * int((m-7)/2) + "WELCOME" + "-" * int((m-7)/2))

# Reset spaces
spaces = 3
pillars = pillars - 2

# Run for the bottom part
for line in range(int(n/2)):
    print("-" * spaces + ".|." * pillars + "-" * spaces)

    spaces += 3
    pillars -=2
