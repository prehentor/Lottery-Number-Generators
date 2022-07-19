import numpy as np

while True:
    try:
        n = int(input('Choose the number of tickets: '))
        assert n>0
        break
    except Exception:
        print('You should enter a positive integer. Please try again.')
    
for i in range(n):
    result = np.random.choice(range(1, 50), size=6, replace=False)
    print(f'Ticket number {i+1}:', sorted(result))

print('Good luck!')