def num2words(num):
    units = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    teens = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    tens = ['', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    thousands = [''] + ['тысяч', 'миллион', 'миллиард', 'триллион']
    if num < 10:
        return units[num]
    elif num < 20:
        return teens[num - 10]
    elif num < 100:
        return tens[num // 10] + ('' if num % 10 == 0 else ' ' + units[num % 10])
    else:
        return units[num // 100] + ' сто' + ('' if num % 100 == 0 else ' ' + num2words(num % 100))

def rubles(num):
    if num % 10 == 1 and num % 100 != 11:
        return 'рубль'
    elif 2 <= num % 10 <= 4 and (num % 100 < 10 or num % 100 >= 20):
        return 'рубля'
    else:
        return 'рублей'

def main():
    try:
        num = int(input("Введите число от 1 до 100000: "))
        if 1 <= num <= 100000:
            print(f"{num2words(num)} {rubles(num)}")
        else:
            print("Число вне диапазона.")
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите целое число.")