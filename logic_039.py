import datetime
import random
def capitalize_string(text):
    return text.upper()
def get_today_date():
    return datetime.date.today(). strftime("%Y_%m_%d")
def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)
def get_random_number():
    return random.randint(1, 50)
def get_full_name():
    return "Ezenwoke Joy"


