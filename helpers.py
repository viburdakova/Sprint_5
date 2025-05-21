import string
import random

def generate_unique_email():
    random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"test_{random_str}@mail.com"

def generate_invalid_email():
    random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"test_{random_str}123123"

title_text = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
description_text = ''.join(random.choices(string.ascii_letters + string.digits + ' ,.', k=50))
price_value = random.randint(500000, 1000000)