#importing the required libraries.
import random

#specifying valid keyboard entries.
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '! "\@#$%^&*()_-[]{};?<>.:/|~+'

#concatination of all valid keyboard entries.
all = lower + upper + numbers + symbols

#for a strong password, keep length >= 15.
length = 16

#generating random password.
password = "".join(random.sample(all, length))

print(password)
