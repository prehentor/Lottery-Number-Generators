import numpy as np
import time

def EurojackpotNumberGenerator():
    
    t_start = np.random.randint(30)
    t_stop = np.random.randint(99)

    eta = t_start + t_stop / 100
    print('Remaining waiting time:', eta, 's')

    time.sleep(eta)

    five_numbers = np.random.choice(range(1,51), size=5, replace=False)
    two_numbers = np.random.choice(range(1,13), size=2, replace=False)

    print('Five numbers from 1 to 50:', sorted(five_numbers))
    print('Two numbers from 1 to 12:', sorted(two_numbers))

if __name__ == '__main__':
    EurojackpotNumberGenerator()