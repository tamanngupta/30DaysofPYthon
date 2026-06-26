import random
import string 
def random_user_id():
    all_charecters = string.ascii_lowercase + string.digits 
    random_chars = random.choices(all_charceters, k=6)
    user_id = "".join(random_chars)
    return user_id

print(random_user_id)