def num2words(num):
    units = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    teens = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    tens = ['', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    hundreds = ['', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
    thousands = ['', 'одна тысяча', 'две тысячи', 'три тысячи', 'четыре тысячи', 'пять тысяч', 'шесть тысяч', 'семь тысяч', 'восемь тысяч', 'девять тысяч']

    if num < 10:
        return units[num]
    elif num < 20:
        return teens[num - 10]
    elif num < 100:
        return tens[num // 10] + ('' if num % 10 == 0 else ' ' + units[num % 10])
    elif num < 1000:
        return hundreds[num // 100] + ('' if num % 100 == 0 else ' ' + num2words(num % 100))
    elif num < 10000:
        return thousands[num // 1000] + ('' if num % 1000 == 0 else ' ' + num2words(num % 1000))
    elif num < 100000:
        return num2words(num // 1000) + ' тысяч' + ('' if num % 1000 == 0 else ' ' + num2words(num % 1000))
    else:
        return "Число вне диапазона."

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

if __name__ == "__main__":
    main()
