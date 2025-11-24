import string, random

def generate(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def main():
    try:
        n = int(input('Password length (e.g., 12): ').strip())
    except:
        n = 12
    print('Generated password:', generate(n))

if __name__ == '__main__':
    main()
