import csv, os

FILE = 'expenses.csv'

def load_expenses():
    expenses = []
    if os.path.exists(FILE):
        with open(FILE, newline='') as f:
            reader = csv.DictReader(f)
            for r in reader:
                r['amount'] = float(r['amount'])
                expenses.append(r)
    return expenses

def save_expenses(expenses):
    with open(FILE, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['amount','category'])
        writer.writeheader()
        for e in expenses:
            writer.writerow({'amount': e['amount'], 'category': e['category']})

def add_expense(expenses):
    try:
        amount = float(input('Enter amount: ').strip())
    except:
        print('Invalid amount')
        return
    category = input('Enter category (food/travel/etc): ').strip()
    expenses.append({'amount': amount, 'category': category})
    save_expenses(expenses)
    print('Saved.')

def summary(expenses):
    total = sum(e['amount'] for e in expenses)
    by_cat = {}
    for e in expenses:
        by_cat[e['category']] = by_cat.get(e['category'], 0) + e['amount']
    if by_cat:
        top_cat = max(by_cat, key=lambda k: by_cat[k])
    else:
        top_cat = None
    print('\n=== Summary ===')
    print('Total spent: Rs', total)
    if top_cat:
        print('Top category:', top_cat, '-> Rs', by_cat[top_cat])
    print('===============\n')

def main():
    expenses = load_expenses()
    print('Expense Tracker - type "stop" to exit.')
    while True:
        cmd = input('Type "add" to add expense, "summary" to view summary, "stop" to exit: ').strip().lower()
        if cmd == 'add':
            add_expense(expenses)
        elif cmd == 'summary':
            summary(expenses)
        elif cmd == 'stop':
            print('Goodbye!')
            break
        else:
            print('Unknown command.')

if __name__ == "__main__":
    main()
