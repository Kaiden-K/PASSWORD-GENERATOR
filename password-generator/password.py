#Kaiden made this project please like and subscribe to my yt channel bye

import random

lower = "qwertyuioplkjhgfdsazxcvbnm"
upper = "QWERTYUIOPLKJHGFDSAZXCVBNM"
numbers = "0123456789"
symbols = "@?><!£$%^&*"

string = lower + upper + numbers + symbols
length = 8
password = "".join(random.sample(string,length))
print("Your New Password Is:" + password)

