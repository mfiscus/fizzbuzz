#!/usr/bin/env python3

class fizzbuzz:        
    def fizz(self):
        if self%3 == 0:
            return 'fizz'

    def buzz(self):
        if self%5 == 0:
            return 'buzz'

def loop():
    for i in range(1, 101):
        fizz = fizzbuzz.fizz(i)
        buzz = fizzbuzz.buzz(i)

        if fizz is not None and buzz is not None:
            print(f'{fizz}{buzz}')
        elif fizz is not None:
            print(f'{fizz}')
        elif buzz is not None:
            print(f'{buzz}')
        else:
            print(f'{i}')

if __name__ == '__main__': loop()