import re


class ValidCarNumber:

    def is_valid(self, number):

        numb = re.match(r'^(\d{2})+([A-Z]{2})+(\d{3})+([A-Z]{3})', number)

        if numb:

            print('Номер валидный!')


        else:

            print('Номер не валидный!')


numbers = input()

numb1 = ValidCarNumber()

numb1.is_valid(numbers)
3