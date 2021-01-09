
import argparse
import math
import sys

parser = argparse.ArgumentParser(description='This is a loan calculator.')

parser.add_argument('--type', help='The type of payment should be either annuity or diff(differentiated)')
parser.add_argument('--payment', help='The amount to be payed monthly')
parser.add_argument('--principal', help='The principal amount')
parser.add_argument('--periods', help='The number of months in which the loan should be repayed')
parser.add_argument('--interest', help='Annual Interest')

args = parser.parse_args()

lst = [args.payment, args.principal, args.periods, args.interest]
new_list = [a for a in lst if a is not None]

for x in new_list:
    if float(x) < 0:
        print('Incorrect parameters')

if len(sys.argv) < 5:
    print('Incorrect parameters')
elif args.interest is None:
    print('Incorrect parameters')
elif args.type == 'annuity':
    if args.periods is None:
        p = int(args.principal)
        m = int(args.payment)
        i = float(args.interest)
        i /= 1200
        ans = math.ceil(math.log(m / (m - i * p), 1 + i))
        if ans < 12:
            print(f'It will take {ans} months to repay this loan!')
        elif ans % 12 == 0:
            if ans == 12:
                print('It will take 1 year to repay this loan')
            else:
                years = ans // 12
                print(f'It will take {years} years to repay this loan')
        else:
            years = ans // 12
            months = ans - 12 * years
            print(f'It will take {years} years and {months} months to repay this loan!')

        print(f'Overpayment = {p - m * ans}')
    elif args.payment is None:
        p = int(args.principal)
        periods = int(args.periods)
        i = float(args.interest)
        i /= 1200
        ans = math.ceil(p * i * ((1 + i) ** periods) / (((1 + i) ** periods) - 1))
        print(ans)
        print(f'Your monthly payment = {ans}!')

        print(f'Overpayment = {p - periods * ans}')

    elif args.principal is None:
        a = float(args.payment)
        periods = int(args.periods)
        i = float(args.interest)
        i /= 1200
        p = math.ceil(a * (((1 + i) ** periods) - 1) / (i * ((1 + i) ** periods)))
        print(f'Your loan principal = {p}!')

        print(f'Overpayment = {p - periods * a}')


elif args.type == 'diff':
    if args.payment is not None:
        print('Incorrect parameters')
    p = int(args.principal)
    i = float(args.interest)
    i /= 1200
    periods = int(args.periods)
    sum = 0
    for m in range(1, periods + 1):
        diff_payment = math.ceil((p / periods) + i * (p - ((p * (m - 1)) / periods)))
        sum += diff_payment
        print(f'Month {m}: payment is {diff_payment}')

    print(f'Overpayment = {p - sum}')


else:
    print('Incorrect parameters')