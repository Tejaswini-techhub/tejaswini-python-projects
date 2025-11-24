def get_marks(subjects):
    marks = {}
    for s in subjects:
        while True:
            try:
                m = float(input(f'Enter marks for {s}: ').strip())
                if 0 <= m <= 100:
                    marks[s] = m
                    break
                else:
                    print('Enter marks between 0 and 100.')
            except:
                print('Please enter a number.')
    return marks

def calculate(marks):
    total = sum(marks.values())
    avg = total / len(marks)
    passed = all(m >= 35 for m in marks.values())
    return total, avg, passed

def main():
    name = input('Student name: ').strip()
    roll = input('Roll number: ').strip()
    subjects = ['Maths','Physics','Chemistry','English','Computer']
    marks = get_marks(subjects)
    total, avg, passed = calculate(marks)
    print('\n--- Result ---')
    print('Name:', name)
    print('Roll:', roll)
    for s in subjects:
        print(f'{s}: {marks[s]}')
    print('Total:', total)
    print('Average:', round(avg,2))
    print('Result:', 'PASS' if passed else 'FAIL')
    print('---------------\n')

if __name__ == "__main__":
    main()
