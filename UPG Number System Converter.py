def number_system_converter(number, start_base, end_base):
    # 2  -> +8, +10, +16;
    # 8  -> 2, +10, 16;
    # 10 -> 2, 8,  16;
    # 16 -> 2, 8,  10;

    # Если начальная система счисления меньше, чем конечная:
    if (start_base < end_base):
        # 2 -> 8, +10, 16;
        # 8 -> +10, 16;
        # 10 -> 16;

        # Для перевода: 2 -> 10; 8 -> 10
        # Алгоритм: СОСТАВЛЕНИЕ И РЕШЕНИЕ ПОЛИНОМА
        if (start_base in [2, 8] and end_base == 10):

            # Зададим переменную для будущего ответа
            answer = 0
            
            # Если число целое
            if (str(number).find('.') == -1):
                # Степень start_base
                bit_number = 0

                # Перебираем все цифры в исходном числе
                while (number != 0):
                    # Рассмотрим на двух примерах: (1101, 2, 10) и (432, 8, 10)
                    intermediate_answer = (number % 10) * (start_base ** bit_number)
                        # 1.1) int_ans = (1101 % 10) * (2 ** 0) = 1 * 2**0 = 1 | # 2.1) int_ans = (432 % 10) * (8 ** 0) = 2 * 8**0 = 2
                        # 1.2) int_ans = (110  % 10) * (2 ** 1) = 0 * 2**1 = 0 | # 2.2) int_ans = (43  % 10) * (8 ** 1) = 3 * 8**1 = 24
                        # 1.3) int_ans = (11   % 10) * (2 ** 2) = 1 * 2**2 = 4 | # 2.3) int_ans = (4   % 10) * (8 ** 2) = 4 * 8**2 = 256
                        # 1.4) int_ans = (1    % 10) * (2 ** 3) = 1 * 2**3 = 8
                    answer += intermediate_answer
                        # 1.1) ans = 0 + 1 = 1                                 | # 2.1) ans = 0  + 2 = 2
                        # 1.2) ans = 1 + 0 = 1                                 | # 2.2) ans = 2  + 24 = 26
                        # 1.3) ans = 1 + 4 = 5                                 | # 2.3) ans = 26 + 256 = 282
                        # 1.4) ans = 5 + 8 = 13
                    number //= 10
                        # 1.1) num = 1101 // 10 = 110                          | # 2.1) num = 432 // 10 = 43
                        # 1.2) num = 110  // 10 = 11                           | # 2.2) num = 43  // 10 = 4
                        # 1.3) num = 11   // 10 = 1                            | # 2.3) num = 4   // 10 = 0
                        # 1.4) num = 1    // 10 = 0
                    bit_number += 1
                        # 1.1) bit_num = 0 + 1 = 1                             | # 2.1) bit_num = 0 + 1 = 1
                        # 1.2) bit_num = 1 + 1 = 2                             | # 2.2) bit_num = 1 + 1 = 2
                        # 1.3) bit_num = 2 + 1 = 3                             | # 2.1) bit_num = 2 + 1 = 3
                        # 1.4) bit_num = 3 + 1 = 4
                return answer
        
            # Если число дробное
            else:
                # Начнём с дробной части
                bit_number = -1
                # Выпишем отдельно дробную часть
                # Округляем разницу между всем числом и его целой частью до количества знаков: длина числа - длина числа до точки, включительно
                # Если просто искать вышеупомянутую разницу, то могут возникать ошибки в следствие неидеальной арифметики чисел с плавающей точкой
                fraction_number = round((number - (number // 1)), ((len(str(number)) - str(number).find('.')) - 1))
                
                # Прибавляем числа по правилу:
                # Перебираем числа, стоящие после точки. Аргумент range = их количеству (находили выше)
                for i in range((len(str(number)) - str(number).find('.')) - 1):
                    # Рассмотрим на двух примерах: (1101.01, 2, 10) и (432.2, 8, 10)
                    intermediate_answer = (fraction_number * 10 // 1) * (start_base ** bit_number)
                        # 1.1) int_ans = (0.01 * 10 // 1) * (2 ** -1) = (0.1 // 1) * 1 / 2 = 0 * 0.5   = 0    
                        # 1.2) int_ans = (0.1  * 10 // 1) * (2 ** -2) = (1   // 1) * 1 / 4 = 1 * 0.25  = 0.25
                        # 2.1) int_ans = (0.2 * 10 // 1)  * (8 ** -1) = (2   // 1) * 1 / 8 = 2 * 0.125 = 0.25
                    answer += intermediate_answer
                        # 1.1) ans = 0 + 0    = 0    
                        # 1.2) ans = 0 + 0.25 = 0.25
                        # 2.1) ans = 0 + 0.25 = 0.25
                    fraction_number = fraction_number * 10 - fraction_number * 10 // 1
                        # 1.1) frac_num = (0.01 * 10) - (0.01 * 10 // 1) = 0.1 - (0.1 // 1) = 0.1 - 0 = 0.1   
                        # 1.2) frac_num = (0.1  * 10) - (0.1  * 10 // 1) = 1   - (1   // 1) = 1   - 1 = 0
                        # 2.1) frac_num = (0.2  * 10) - (0.2  * 10 // 1) = 2   - (2   // 1) = 2   - 2 = 0
                    bit_number -= 1
                        # 1.1) bit_num = -1 - 1 = -2 
                        # 1.2) bit_num = -2 - 1 = -3
                        # 2.1) bit_num = -1 - 1 = -2
            
                # Вернёмся к целой части
                # Делаем по полной аналогии с алгоритмом для целого числа
                number //= 1
                bit_number = 0
                while (number != 0):
                    intermediate_answer = (number % 10) * (start_base ** bit_number)
                    answer += intermediate_answer
                    number //= 10
                    bit_number += 1
            
                return answer
            # Для перевода: 2 -> 8; 2 -> 16
            # Алгоритм: РАЗБИЕНИЕ НА ТРИАДЫ(ТЕТРАДЫ) И ПОСЛЕДОВАТЕЛЬЫЙ ПЕРЕВОД В НОВУЮ СС
        elif (start_base == 2 and end_base in [8, 16]):

            # Для восьмеричной системы разбиваем исходное число на триады
            if (end_base == 8):
                to_oct_base = {'001' : '1',
                               '010' : '2',
                               '011' : '3',
                               '100' : '4',
                               '101' : '5',
                               '110' : '6',
                               '111' : '7'}
                
                # Если число целое:
                if (str(number).find('.') == -1):
                    # Преобразуем число в строку, при необходимости добавляем вначале нули.
                    # Длина числа [7, 8, 9] + ...
                        # Длина числа % 3 [1, 2, 0]
                        # Результат - 3   [-2, -1, -3]
                        # Результат % -3  [-2, -1, 0]
                        # Модуль рез-та   [2, 1, 0]
                    string_num = str(number).rjust(len(str(number)) + abs((((len(str(number)) % 3) - 3) % -3)), '0')
                    # Создадим список для итогового ответа
                    nums_list = []
                    answer_list = []
                    answer = ''
                    for i in range(len(string_num) // 3):
                        nums_list.append(string_num[(i*3):((i*3)+3)])
                    for i in nums_list:
                        answer_list.append(to_oct_base[i])
                        answer += to_oct_base[i]
                    return answer

                # Если число дробное:
                else:
                    fraction_number = str(number)[(str(number).find('.') + 1):len(str(number))]
                    integral_number = str(number)[0:str(number).find('.')]
                    fraction_number = fraction_number.ljust(len(str(fraction_number)) + abs((((len(str(fraction_number)) % 3) - 3) % -3)), '0')
                    integral_number = integral_number.rjust(len(str(integral_number)) + abs((((len(str(integral_number)) % 3) - 3) % -3)), '0')
                    # Создадим список для итогового ответа
                    int_nums_list = []
                    frac_nums_list = []
                    answer_list = []
                    answer = ''
                    # Целая часть
                    for i in range(len(integral_number) // 3):
                        int_nums_list.append(integral_number[(i*3):((i*3)+3)])
                    for i in int_nums_list:
                        answer_list.append(to_oct_base[i])
                        answer += to_oct_base[i]

                    # Дробная часть
                    answer_list.append('.')
                    answer += '.'
                    for i in range(len(fraction_number) // 3):
                        frac_nums_list.append(fraction_number[(i*3):((i*3)+3)])
                    for i in frac_nums_list:
                        answer_list.append(to_oct_base[i])
                        answer += to_oct_base[i]
                        
                    return answer
                
            elif (end_base == 16):
                to_hex_base = {'0001' : '1',
                               '0010' : '2',
                               '0011' : '3',
                               '0100' : '4',
                               '0101' : '5',
                               '0110' : '6',
                               '0111' : '7',
                               '1000' : '8',
                               '1001' : '9',
                               '1010' : 'A',
                               '1011' : 'B',
                               '1100' : 'C',
                               '1101' : 'D',
                               '1110' : 'E',
                               '1111' : 'F'}

                # Если число целое:
                if (str(number).find('.') == -1):

                    string_num = str(number).rjust(len(str(number)) + abs((((len(str(number)) % 4) - 4) % -4)), '0')
                    nums_list = []
                    answer_list = []
                    answer = ''
                    for i in range(len(string_num) // 4):
                        nums_list.append(string_num[(i*4):((i*4)+4)])
                    for i in nums_list:
                        answer_list.append(to_hex_base[i])
                        answer += to_hex_base[i]
                    return answer
                
                # Если число дробное:
                else:
                    fraction_number = str(number)[(str(number).find('.') + 1):len(str(number))]
                    integral_number = str(number)[0:str(number).find('.')]
                    fraction_number = fraction_number.ljust(len(str(fraction_number)) + abs((((len(str(fraction_number)) % 4) - 4) % -4)), '0')
                    integral_number = integral_number.rjust(len(str(integral_number)) + abs((((len(str(integral_number)) % 4) - 4) % -4)), '0')
                    # Создадим список для итогового ответа
                    int_nums_list = []
                    frac_nums_list = []
                    answer_list = []
                    answer = ''
                    # Целая часть
                    for i in range(len(integral_number) // 4):
                        int_nums_list.append(integral_number[(i*4):((i*4)+4)])
                    for i in int_nums_list:
                        answer_list.append(to_hex_base[i])
                        answer += to_hex_base[i]

                    # Дробная часть
                    answer_list.append('.')
                    answer += '.'
                    for i in range(len(fraction_number) // 4):
                        frac_nums_list.append(fraction_number[(i*4):((i*4)+4)])
                    for i in frac_nums_list:
                        answer_list.append(to_hex_base[i])
                        answer += to_hex_base[i]
                        
                    return answer
