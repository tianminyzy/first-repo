import calculator
import datetime

calculator.add(3, 4)        # 7
calculator.subtract(3, 4)   # -1
calculator.multiply(3, 4)   # 12
calculator.divide(3, 4)     # 0.75
calculator.exp(3, 4)        # 81


release_date = datetime.date(1991,2,20)
print(f'Python was released in {release_date.year}')
print(datetime.date.today())