import os

FILE = 'tasks.txt'

def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE,'r') as f:
        return [line.strip() for line in f if line.strip()]

def save_tasks(tasks):
    with open(FILE,'w') as f:
        for t in tasks:
            f.write(t + '\n')

def main():
    tasks = load_tasks()
    while True:
        print('\n1. Add task\n2. Remove task\n3. List tasks\n4. Exit')
        choice = input('Choose: ').strip()
        if choice == '1':
            t = input('Enter task: ').strip()
            tasks.append(t)
            save_tasks(tasks)
            print('Added.')
        elif choice == '2':
            for i,t in enumerate(tasks,1):
                print(i, t)
            idx = input('Enter number to remove: ').strip()
            try:
                idx = int(idx)-1
                tasks.pop(idx)
                save_tasks(tasks)
                print('Removed.')
            except:
                print('Invalid choice.')
        elif choice == '3':
            print('\n-- Tasks --')
            for i,t in enumerate(tasks,1):
                print(i, t)
        elif choice == '4':
            break
        else:
            print('Unknown option.')

if __name__ == '__main__':
    main()
