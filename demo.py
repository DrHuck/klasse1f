def calculate_next_fibonacci_number(a1, a2):
    return a1 + a2


a_old = 1
a_current = 1

print(a_old)
print(a_current)

for k in range(20):
    swap = a_current
    a_current = calculate_next_fibonacci_number(a_current, a_old)
    print(a_current)
    a_old = swap

hallo
zweite veränderung