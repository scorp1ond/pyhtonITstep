# my_list = ['orange','banana', 'apple']

# print(my_list[10])

# def recursion():
#     recursion()

# recursion()

# var = recursion
# var()
operators = ['+','-','*','/']

while(True):
    try:
        num1 = float(input('enter first num: '))
        num2 = float(input('enter secornd num: '))
        action = input(' enter operation(+ - * /): ')
        if action not in operators:
            raise Exception(action)

        match action:
            case '+': print(f'{num1} + {num2} = {num1 + num2}')
            case '-': print(f'{num1} - {num2} = {num1 - num2}')
            case '*': print(f'{num1} * {num2} = {num1 * num2}')
            case '/': print(f'{num1} / {num2} = {num1 / num2}')
    except ZeroDivisionError:
        print('you cant devide by zero')
    except ValueError:
        print('incorrect number')
    except Exception as ex:
        print(f'incorrect operation {ex.args[0]}')
    finally:
        repeat = input('you want to continue (Y/N)')
        if repeat.lower() == 'n':
            break


try:
    price = float(input('enter price: '))
    discount = float(input('enter discount percent: '))

    final_price = price - (price * discount / 100)
    print('final price:', final_price)

except ValueError:
    print('incorrect number')

try:
    dollars = float(input('enter dollars: '))
    rate = float(input('enter exchange rate: '))

    if rate == 0:
        raise Exception('rate cant be zero')

    euros = dollars * rate
    print('euros:', euros)

except ValueError:
    print('incorrect number')

except Exception as ex:
    print(ex)

finally:
    print('operation finished')


try:
    grades = input('enter grades: ')
    grades_list = grades.split()

    numbers = []
    for g in grades_list:
        numbers.append(float(g))

    avg = sum(numbers) / len(numbers)
    print('average:', avg)

except ValueError:
    print('incorrect grade')

except ZeroDivisionError:
    print('no grades')

finally:
    print('calculations finished')

balance = 1000

try:
    amount = float(input('enter amount to withdraw: '))

    if amount % 10 != 0 or amount > balance:
        raise Exception('incorrect withdraw amount')

    balance -= amount
    print('take your money')
    print('balance:', balance)

except ValueError:
    print('incorrect number')

except Exception as ex:
    print(ex)

finally:
    print('transaction finished')

try:
    order = input('enter order number: ')

    if not order.startswith('ord') or not order[3:].isdigit():
        raise Exception('wrong order format')

    print('order number is correct')

except Exception as ex:
    print(ex)

finally:
    print('check finished')

try:
    data = input('enter numbers: ')
    items = data.split()

    numbers = []

    for i in items:
        try:
            numbers.append(float(i))
        except ValueError:
            print('skipped value', i)

    total = sum(numbers)
    avg = total / len(numbers)

    print('sum:', total)
    print('average:', avg)

except ZeroDivisionError:
    print('no valid numbers')

finally:
    print('data processing finished')



