numerals = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
def to_int(roman):
    numbers = []
    for char in roman:
        numbers.append(numerals[char])
    integer = 0
    for i in range(len(numbers)):
        if i==len(numbers)-1:
            integer+=numbers[i]
        else:
            if numbers[i+1]>numbers[i]:
                integer-=numbers[i]
            else:
                integer+=numbers[i]
    return integer
def single_roman(numeral,value):
    global roman
    global integer
    while integer>=value:
        roman+=numeral
        integer-=value
    return (roman,integer)
def to_best_roman(integer_in):
    global roman
    roman = ''
    global integer
    integer = integer_in
    single_roman('M',1000)
    single_roman( 'CM',900)
    single_roman( 'D',500)
    single_roman( 'CD',400)
    single_roman( 'C',100)
    single_roman( 'XC',90)
    single_roman( 'L',50)
    single_roman( 'XL',40)
    single_roman( 'X',10)
    single_roman( 'IX',9)
    single_roman( 'V',5)
    single_roman( 'IV',4)
    single_roman( 'I',1)
    return roman
roman_values =[x.strip() for x in open('roman.txt').readlines()]
int_values = [to_int(x) for x in roman_values]
total_chars = [len(x) for x in roman_values]
better_roman = [to_best_roman(x) for x in int_values]
new_total_chars = [len(x) for x in better_roman]
print sum(total_chars)-sum(new_total_chars)
