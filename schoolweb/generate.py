import string
import random
def generate_code(stringSize, NumberSize):
  return ''.join(random.choice(string.ascii_uppercase) for _ in range(stringSize)) + ''.join(random.choice(string.digits) for _ in range(NumberSize))