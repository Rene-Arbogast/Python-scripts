# Python 3.13.2 (tags/v3.13.2:f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.

import sys, os
pathname = "C:\\Rene\\Personal\\Music\\TNMC\\TNMC_Charts\\Trumpet 2\\"

def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()

print (pathname)
print (os.walk(pathname)[0])

[x[0] for x in os.walk(pathname)]
print (x)
