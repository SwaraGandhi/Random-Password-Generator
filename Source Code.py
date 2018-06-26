import string
from random import *
characters = string.ascii_letters + string.digits
password = "".join(choice(characters) for a in range(randint(1,128)))
print password
