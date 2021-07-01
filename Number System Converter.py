def number_system_converter(number, start_base, end_base):

    to_hex_table = {2 : {1010 : 'A',
                         1011 : 'B',
                         1100 : 'C',
                         1101 : 'D',
                         1110 : 'E',
                         1111 : 'F'},
                    8 : {12 : 'A',
                         13 : 'B',
                         14 : 'C',
                         15 : 'D',
                         16 : 'E',
                         17 : 'F'},
                    10 : {10 : 'A',
                          11 : 'B',
                          12 : 'C',
                          13 : 'D',
                          14 : 'E',
                          15 : 'F'}}
    
    # На всякий случай сохраню заданное число:
    start_number = number
    
    # Рассмотрим первый случай: s < h
    # Необходимо использовать арифметику СС-h.
    if (start_base < end_base):
        # Зададим переменную для будущего ответа:
        answer = 0.0
        
        # Если number - целое число:
        if (str(number).find('.') == -1):
            bit_number = 0
            # Прибавляем числа по правилу:
            while (number != 0):
                intermediate_answer = (number % 10) * (start_base ** bit_number)
                answer += intermediate_answer
                number //= 10
                bit_number += 1
            # Возвращаем ответ.
            return answer
        # Если number - дробное число:
        else:
            # Начнём с дробной части
            bit_number = -1
            # Выпишем отдельно дробную часть
            fraction_number = round((number - (number // 1)), ((len(str(number)) - str(number).find('.')) - 1))
            # Прибавляем числа по правилу:
            for i in range((len(str(number)) - str(number).find('.')) - 1):
                intermediate_answer = (fraction_number * 10 // 1) * (start_base ** bit_number)
                answer += intermediate_answer
                fraction_number = fraction_number * 10 - fraction_number * 10 // 1
                bit_number -= 1
            # Вернёмся к целой части 
            number //= 1
            bit_number = 0
            while (number != 0):
                intermediate_answer = (number % 10) * (start_base ** bit_number)
                answer += intermediate_answer
                number //= 10
                bit_number += 1
            
            return answer

    else:
        # Зададим переменную для будущего ответа:
        answer = ''
        # Если number - целое число:
        if (str(number).find('.') == -1):
            while (number != 0):
                intermediate_answer = number % end_base
                if (end_base == 16):
                    if ((intermediate_answer == 10) and start_base == 10) or ((intermediate_answer == 1010) and start_base == 2) or ((intermediate_answer == 12) and start_base == 8):
                           intermediate_answer = 'A'
                    elif  ((intermediate_answer == 11) and start_base == 10) or ((intermediate_answer == 1011) and start_base == 2) or ((intermediate_answer == 13) and start_base == 8):
                              intermediate_answer = 'B'
                    elif  ((intermediate_answer == 12) and start_base == 10) or ((intermediate_answer == 1100) and start_base == 2) or ((intermediate_answer == 14) and start_base == 8):
                              intermediate_answer = 'C'
                    elif  ((intermediate_answer == 13) and start_base == 10) or ((intermediate_answer == 1101) and start_base == 2) or ((intermediate_answer == 15) and start_base == 8):
                              intermediate_answer = 'D'
                    elif  ((intermediate_answer == 14) and start_base == 10) or ((intermediate_answer == 1110) and start_base == 2) or ((intermediate_answer == 16) and start_base == 8):
                              intermediate_answer = 'E'
                    elif  ((intermediate_answer == 15) and start_base == 10) or ((intermediate_answer == 1111) and start_base == 2) or ((intermediate_answer == 17) and start_base == 8):
                              intermediate_answer = 'F'
                answer = (str(intermediate_answer)) + answer
                number //= end_base
            return answer
        else:
            # Начнём с дробной части
            # Выпишем отдельно дробную часть
            fraction_number = round((number - (number // 1)), ((len(str(number)) - str(number).find('.')) - 1))
            counter_max = len(str(fraction_number)) - 2
            counter = 0
            fraction_answer = ''
            while (number != 0 and counter <= counter_max and len(fraction_answer) <= counter_max + 2):
                intermediate_answer = int((fraction_number * end_base) // 1)
                if (end_base == 16):
                    if ((intermediate_answer == 10) and start_base == 10) or ((intermediate_answer == 1010) and start_base == 2) or ((intermediate_answer == 12) and start_base == 8):
                           intermediate_answer = 'A'
                    elif  ((intermediate_answer == 11) and start_base == 10) or ((intermediate_answer == 1011) and start_base == 2) or ((intermediate_answer == 13) and start_base == 8):
                              intermediate_answer = 'B'
                    elif  ((intermediate_answer == 12) and start_base == 10) or ((intermediate_answer == 1100) and start_base == 2) or ((intermediate_answer == 14) and start_base == 8):
                              intermediate_answer = 'C'
                    elif  ((intermediate_answer == 13) and start_base == 10) or ((intermediate_answer == 1101) and start_base == 2) or ((intermediate_answer == 15) and start_base == 8):
                              intermediate_answer = 'D'
                    elif  ((intermediate_answer == 14) and start_base == 10) or ((intermediate_answer == 1110) and start_base == 2) or ((intermediate_answer == 16) and start_base == 8):
                              intermediate_answer = 'E'
                    elif  ((intermediate_answer == 15) and start_base == 10) or ((intermediate_answer == 1111) and start_base == 2) or ((intermediate_answer == 17) and start_base == 8):
                              intermediate_answer = 'F'
                answer = (str(intermediate_answer)) + answer
                fraction_answer = fraction_answer + str(intermediate_answer)
                if (fraction_number * end_base // 1) != 0:
                    counter += 1
                fraction_number = (fraction_number * end_base) % 1

            # Вернёмся к целой части 
            number //= 1
            number = int(number)
            answer = ''
            if number == 0: 
                answer = '0.' + fraction_answer
                return answer
            while (number != 0):
                intermediate_answer = number % end_base
                if (end_base == 16):
                    if ((intermediate_answer == 10) and start_base == 10) or ((intermediate_answer == 1010) and start_base == 2) or ((intermediate_answer == 12) and start_base == 8):
                           intermediate_answer = 'A'
                    elif  ((intermediate_answer == 11) and start_base == 10) or ((intermediate_answer == 1011) and start_base == 2) or ((intermediate_answer == 13) and start_base == 8):
                              intermediate_answer = 'B'
                    elif  ((intermediate_answer == 12) and start_base == 10) or ((intermediate_answer == 1100) and start_base == 2) or ((intermediate_answer == 14) and start_base == 8):
                              intermediate_answer = 'C'
                    elif  ((intermediate_answer == 13) and start_base == 10) or ((intermediate_answer == 1101) and start_base == 2) or ((intermediate_answer == 15) and start_base == 8):
                              intermediate_answer = 'D'
                    elif  ((intermediate_answer == 14) and start_base == 10) or ((intermediate_answer == 1110) and start_base == 2) or ((intermediate_answer == 16) and start_base == 8):
                              intermediate_answer = 'E'
                    elif  ((intermediate_answer == 15) and start_base == 10) or ((intermediate_answer == 1111) and start_base == 2) or ((intermediate_answer == 17) and start_base == 8):
                              intermediate_answer = 'F'
                answer = (str(intermediate_answer)) + answer
                number //= end_base
           # answer = answer + '.' + fraction_answer
            return answer + '.' + fraction_answer


#print(number_system_converter(0.453, 10, 2))
#print(number_system_converter(0.453, 10, 8))
#        
#print(number_system_converter(1101.01, 2, 10))
#print(number_system_converter(1101, 2, 10))
#print(number_system_converter(432, 8, 10))
#
#print(number_system_converter(75, 10, 2))
#print(number_system_converter(75, 10, 8))

print(number_system_converter(75.453, 10, 2))
print(number_system_converter(75.453, 10, 8))
print(number_system_converter(432.2, 8, 10))

# Нужно добавить вариант с 16-иричной системой
