import json

'''
функцию `get_last_operations()`,
которая будет выводить на экран список
из 5 последних выполненных клиентом операций
'''


def get_operations(data):
    operations = [op for op in data if op.get('state') == 'EXECUTED']
    operations = sorted(operations, key=lambda op: op.get('date'), reverse=True)[:5]
    for op in operations:
        date = op['date']
        description = op['description']
        from_ = op.get('from', '')
        to = op['to']
        amount = op.get('operationAmount', {}).get('amount')
        currency = op.get('operationAmount', {}).get('currency', {}).get('name')
        masked_card = from_[:6] + ' XX** **** ' + from_[-4:]
        masked_account = '**' + to[-4:]

        print(f'{date} {description}\n{masked_card} -> Счет {masked_account}\n{amount} {currency}\n')



