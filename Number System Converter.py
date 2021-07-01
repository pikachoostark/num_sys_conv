def number_system_converter(number, start_base, end_base):
    # +2  -> +8, +10, +16;
    # +8  -> +2, +10, +16;
    # +10 -> +2, +8,  +16;
    # +16 -> +2, +8,  +10;


    # Для перевода: 2 -> 10; 8 -> 10
    # Алгоритм: СОСТАВЛЕНИЕ И РЕШЕНИЕ ПОЛИНОМА
    if (start_base in [2, 8, 16] and end_base == 10):
        hex_to_dec = {'A' : 10,
                      'B' : 11,
                      'C' : 12,
                      'D' : 13,
                      'E' : 14,
                      'F' : 15}

        # Зададим переменную для будущего ответа
        answer = 0.0
            
        # Если число целое
        if (str(number).find('.') == -1):
            # Степень start_base
            bit_number = 0
            # Костыль:
            if start_base == 16:
                number = str(number)

            # Перебираем все цифры в исходном числе
            while (number != 0 and number != ''):
                # Рассмотрим на двух примерах: (1101, 2, 10) и (432, 8, 10)
                if start_base == 16 :
                    intermediate_answer = number[-1]
                    if intermediate_answer in hex_to_dec :
                        intermediate_answer = hex_to_dec[intermediate_answer]
                    else :
                        intermediate_answer = int(intermediate_answer)
                    intermediate_answer = intermediate_answer * (start_base ** bit_number) 
                else :
                    intermediate_answer = (number % 10) * (start_base ** bit_number)
                        # 1.1) int_ans = (1101 % 10) * (2 ** 0) = 1 * 2**0 = 1
                        # 1.2) int_ans = (110  % 10) * (2 ** 1) = 0 * 2**1 = 0
                        # 1.3) int_ans = (11   % 10) * (2 ** 2) = 1 * 2**2 = 4
                        # 1.4) int_ans = (1    % 10) * (2 ** 3) = 1 * 2**3 = 8
                            # 2.1) int_ans = (432 % 10) * (8 ** 0) = 2 * 8**0 = 2
                            # 2.2) int_ans = (43  % 10) * (8 ** 1) = 3 * 8**1 = 24
                            # 2.3) int_ans = (4   % 10) * (8 ** 2) = 4 * 8**2 = 256
                                # 3.1) int_ans = 'FDA1'[-1] * (16 ** 0) = 1  * 16**0 = 1
                                # 3.2) int_ans = 'FDA'[-1]  * (16 ** 1) = 10 * 16**1 = 160
                                # 3.3) int_ans = 'FD'[-1]   * (16 ** 2) = 13 * 16**2 = 3328
                                # 3.4) int_ans = 'F'[-1]    * (16 ** 3) = 15 * 16**3 = 61440
                answer += intermediate_answer
                    # 1.1) ans = 0 + 1 = 1     | # 2.1) ans = 0  + 2 = 2      | # 3.1) ans = 0 + 1 = 1
                    # 1.2) ans = 1 + 0 = 1     | # 2.2) ans = 2  + 24 = 26    | # 3.2) ans = 160 + 1 = 161
                    # 1.3) ans = 1 + 4 = 5     | # 2.3) ans = 26 + 256 = 282  | # 3.3) ans = 161 + 3328 = 3489
                    # 1.4) ans = 5 + 8 = 13    |                              | # 3.4) ans = 3489 + 61440 = 64929
                if start_base == 16 :
                    number = number[:-1]
                else :
                    number //= 10
                    # 1.1) num = 1101 // 10 = 110  | # 2.1) num = 432 // 10 = 43 | # 3.1) num = 'FDA1'[:-1] = 'FDA'
                    # 1.2) num = 110  // 10 = 11   | # 2.2) num = 43  // 10 = 4  | # 3.2) num = 'FDA'[:-1]  = 'FD'
                    # 1.3) num = 11   // 10 = 1    | # 2.3) num = 4   // 10 = 0  | # 3.3) num = 'FD'[:-1]   = 'F'
                    # 1.4) num = 1    // 10 = 0    |                             | # 3.4) num = 'F'[:-1]    = ''
                bit_number += 1
                    # 1.1) bit_num = 0 + 1 = 1  | # 2.1) bit_num = 0 + 1 = 1 | # 3.1)  bit_num = 0 + 1 = 1
                    # 1.2) bit_num = 1 + 1 = 2  | # 2.2) bit_num = 1 + 1 = 2 | # 3.2)  bit_num = 1 + 1 = 2
                    # 1.3) bit_num = 2 + 1 = 3  | # 2.1) bit_num = 2 + 1 = 3 | # 3.3)  bit_num = 2 + 1 = 3
                    # 1.4) bit_num = 3 + 1 = 4  |                            | # 3.4)  bit_num = 3 + 1 = 4
            return int(answer)
        
        # Если число дробное
        else:
            # Начнём с дробной части
            bit_number = -1
            # Выпишем отдельно дробную часть
            # Округляем разницу между всем числом и его целой частью до количества знаков: длина числа - длина числа до точки, включительно
            # Если просто искать вышеупомянутую разницу, то могут возникать ошибки в следствие неидеальной арифметики чисел с плавающей точкой
            if start_base == 16 :
                fraction_number = str(number)[str(number).find('.') + 1:]
            else :
                fraction_number = round((number - (number // 1)), ((len(str(number)) - str(number).find('.')) - 1))
                
            # Прибавляем числа по правилу:
            # Перебираем числа, стоящие после точки. Аргумент range = их количеству (находили выше)
            for i in range(len(str(number)) - str(number).find('.') - (2 * start_base != 16)):
                # Рассмотрим на двух примерах: (1101.01, 2, 10) и (432.2, 8, 10)
                if start_base == 16 :
                    if fraction_number[0] in hex_to_dec :
                        intermediate_answer = hex_to_dec[fraction_number[0]]
                    else:
                        intermediate_answer = int(fraction_number[0])
                    intermediate_answer *= start_base ** bit_number                                                                          
                else    :
                    intermediate_answer = (fraction_number * 10 // 1) * (start_base ** bit_number)
                        # 1.1) int_ans = (0.01 * 10 // 1) * (2 ** -1) = (0.1 // 1) * 1 / 2 = 0 * 0.5   = 0    
                        # 1.2) int_ans = (0.1  * 10 // 1) * (2 ** -2) = (1   // 1) * 1 / 4 = 1 * 0.25  = 0.25
                        # 2.1) int_ans = (0.2 * 10 // 1)  * (8 ** -1) = (2   // 1) * 1 / 8 = 2 * 0.125 = 0.25
                answer += intermediate_answer
                    # 1.1) ans = 0 + 0    = 0    
                    # 1.2) ans = 0 + 0.25 = 0.25
                    # 2.1) ans = 0 + 0.25 = 0.25
                if start_base == 16:
                    fraction_number = fraction_number[1::]
                else : 
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
            if start_base == 16 :
                number = number[:str(number).find('.')]
            else : 
                number //= 1
            bit_number = 0
            while (number != 0 and number != ''):
                if start_base == 16 :
                    intermediate_answer = number[-1]
                    if intermediate_answer in hex_to_dec :
                        intermediate_answer = hex_to_dec[intermediate_answer]
                    else :
                        intermediate_answer = int(intermediate_answer)
                    intermediate_answer = intermediate_answer * (start_base ** bit_number) 
                else :
                    intermediate_answer = (number % 10) * (start_base ** bit_number)
                answer += intermediate_answer
                if start_base == 16 :
                    number = number[:-1]
                else :
                    number //= 10
                bit_number += 1
            
            return answer
            
    # Для перевода: 2 -> 8; 2 -> 16
    # Алгоритм: РАЗБИЕНИЕ НА ТРИАДЫ(ТЕТРАДЫ) И ПОСЛЕДОВАТЕЛЬЫЙ ПЕРЕВОД В НОВУЮ СС
    elif (start_base == 2 and end_base in [8, 16]):

        # Для восьмеричной системы разбиваем исходное число на триады
        if (end_base == 8):
            bin_to_oct = {'001' : '1',
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
                    answer_list.append(bin_to_oct[i])
                    answer += bin_to_oct[i]
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
                    answer_list.append(bin_to_oct[i])
                    answer += bin_to_oct[i]

                # Дробная часть
                answer_list.append('.')
                answer += '.'
                for i in range(len(fraction_number) // 3):
                    frac_nums_list.append(fraction_number[(i*3):((i*3)+3)])
                for i in frac_nums_list:
                    answer_list.append(bin_to_oct[i])
                    answer += bin_to_oct[i]
                        
                return answer
                
        elif (end_base == 16):
            bin_to_hex = {'0001' : '1',
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
                    answer_list.append(bin_to_hex[i])
                    answer += bin_to_hex[i]
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
                    answer_list.append(bin_to_hex[i])
                    answer += bin_to_hex[i]

                # Дробная часть
                answer_list.append('.')
                answer += '.'
                for i in range(len(fraction_number) // 4):
                    frac_nums_list.append(fraction_number[(i*4):((i*4)+4)])
                for i in frac_nums_list:
                    answer_list.append(bin_to_hex[i])
                    answer += bin_to_hex[i]
                        
                return answer
            
    # Для перевода: 10 -> 2; 10 -> 8; 10 -> 16
    # Алгоритм: ДЕЛЕНИЕ НА БАЗУ СС 
    elif (start_base == 10 and end_base in [2, 8, 16]):
        dec_to_hex = {10 : 'A',
                      11 : 'B',
                      12 : 'C',
                      13 : 'D',
                      14 : 'E',
                      15 : 'F'}
        
        # Зададим переменную для будущего ответа:
        answer = ''

        # Если число - целое
        if (str(number).find('.') == -1):

            # Перебираем все цифры в исходном числе
            while (number != 0):
                # Рассмотрим на трёх примерах: (75, 10, 2), (75, 10, 8) и (75, 10, 16)
                intermediate_answer = number % end_base
                    # 1.1) int_ans = 75 % 2 = 1 | # 2.1) int_ans = 75 % 8 = 3 | # 3.1) int_ans = 75 % 16 = 11
                    # 1.2) int_ans = 37 % 2 = 1 | # 2.2) int_ans = 9  % 8 = 1 | # 3.2) int_ans = 4  % 16 = 4
                    # 1.3) int_ans = 18 % 2 = 0 | # 2.3) int_ans = 1  % 8 = 1
                    # 1.4) int_ans = 9  % 2 = 1
                    # 1.5) int_ans = 4  % 2 = 0
                    # 1.6) int_ans = 2  % 2 = 0
                    # 1.7) int_ans = 1  % 2 = 1
                if (end_base == 16 and intermediate_answer in dec_to_hex):
                    intermediate_answer = dec_to_hex[intermediate_answer]
                answer = (str(intermediate_answer)) + answer
                    # 1.1) answer = '1' + '' = '1'             | # 2.1) answer = '3' + '' = '3'     | # 3.1) answer = 'B' + '' = 'B'
                    # 1.2) answer = '1' + '1' = '11'           | # 2.2) answer = '1' + '3' = '13'   | # 3.2) answer = '4' + 'B' = '4B'
                    # 1.3) answer = '0' + '11' = '011'         | # 2.3) answer = '1' + '13' = '113'
                    # 1.4) answer = '1' + '011' = '1011'       
                    # 1.5) answer = '0' + '1011' = '01011'     
                    # 1.6) answer = '0' + '01011' = '001011'   
                    # 1.7) answer = '1' + '001011' = '1001011' 
                number //= end_base
                    # 1.1) number = 75 // 2 = 37 | # 2.1) number = 75 // 8 = 9 | # 3.1) number = 75 // 16 = 4
                    # 1.2) number = 37 // 2 = 18 | # 2.2) number = 9  // 8 = 1 | # 3.1) number = 4  // 16 = 0
                    # 1.3) number = 18 // 2 = 9  | # 2.3) number = 1  // 8 = 0
                    # 1.4) number = 9  // 2 = 4
                    # 1.5) number = 4  // 2 = 2
                    # 1.6) number = 2  // 2 = 1
                    # 1.7) number = 1  // 2 = 0
            return answer

        # Если число дробное
        else:
            # Начнём с дробной части
            # Выпишем отдельно дробную часть
            # Округляем разницу между всем числом и его целой частью до количества знаков: длина числа - длина числа до точки, включительно
            # Если просто искать вышеупомянутую разницу, то могут возникать ошибки в следствие неидеальной арифметики чисел с плавающей точкой
            fraction_number = round((number - (number // 1)), ((len(str(number)) - str(number).find('.')) - 1))

            # Задаём точность таким образом:
            # Округляем до того же количества знаков, которое было в исходном числе
            counter_max = len(str(fraction_number)) - 2
            # Увеличим количество знаков, если перевод происходит в двоичную систему
            if end_base == 2 : counter_max *= 2
            fraction_answer = ''
            # Рассмотрим на трёх примерах: (75.453, 10, 2), (75.453, 10, 8) и (75.453, 10, 16)
            while (fraction_number != 0 and len(fraction_answer) < counter_max):
                intermediate_answer = int((fraction_number * end_base) // 1)
                    # 1.1) int_ans = int((0.453 * 2) // 1) = int(0.906 // 1) = int(0.0) = 0 
                    # 1.2) int_ans = int((0.906 * 2) // 1) = int(1.812 // 1) = int(1.0) = 1
                    # 1.3) int_ans = int((0.812 * 2) // 1) = int(1.624 // 1) = int(1.0) = 1
                    # 1.4) int_ans = int((0.624 * 2) // 1) = int(1.248 // 1) = int(1.0) = 1
                    # 1.5) int_ans = int((0.248 * 2) // 1) = int(0.496 // 1) = int(0.0) = 0
                    # 1.6) int_ans = int((0.496 * 2) // 1) = int(0.992 // 1) = int(0.0) = 0
                    # 1.7) int_ans = int((0.453 * 2) // 1) = int(0.906 // 1) = int(0.0) = 0
                        # 2.1) int_ans = int((0.453 * 8) // 1) = int(3.624 // 1) = int(3.0) = 3
                        # 2.2) int_ans = int((0.624 * 8) // 1) = int(4.992 // 1) = int(4.0) = 4
                        # 2.3) int_ans = int((0.992 * 8) // 1) = int(7.936 // 1) = int(7.0) = 7
                            # 3.1) int_ans = int((0.453 * 16) // 1) = int(7.248  // 1) = int(7.0) = 7
                            # 3.2) int_ans = int((0.248 * 16) // 1) = int(3.968  // 1) = int(3.0) = 3
                            # 3.3) int_ans = int((0.968 * 16) // 1) = int(15.688 // 1) = int(15.0) = 15
                if (end_base == 16 and intermediate_answer in dec_to_hex):
                    intermediate_answer = dec_to_hex[intermediate_answer]
                fraction_answer = fraction_answer + str(intermediate_answer)
                    # 1.1) frac_ans = '' + '0' = '0'
                    # 1.2) frac_ans = '0' + '1' = '01'
                    # 1.3) frac_ans = '01' + '1' = '011'
                    # 1.4) frac_ans = '011' + '1' = '0111'
                    # 1.5) frac_ans = '0111' + '0' = '01110'
                    # 1.6) frac_ans = '01110' + '0' = '011100'
                        # 2.1) frac_ans = '' + '3' = '3'
                        # 2.2) frac_ans = '3' + '4' = '34'
                        # 2.3) frac_ans = '34' + '7' = '347'
                            # 3.1) frac_ans = '' + '7' = '7'
                            # 3.2) frac_ans = '7' + '3' = '73'
                            # 3.3) frac_ans = '73' + 'F' = '73F'
                fraction_number = (fraction_number * end_base) % 1
                    # 1.1) frac_num = (0.453 * 2 ) % 1 = 0.906
                    # 1.2) frac_num = (0.906 * 2 ) % 1 = 0.812
                    # 1.3) frac_num = (0.812 * 2 ) % 1 = 0.624
                    # 1.4) frac_num = (0.624 * 2 ) % 1 = 0.248
                    # 1.5) frac_num = (0.248 * 2 ) % 1 = 0.496
                    # 1.6) frac_num = (0.496 * 2 ) % 1 = 0.992
                        # 2.1) frac_num = (0.453 * 8 ) % 1 = 0.624
                        # 2.2) frac_num = (0.624 * 8 ) % 1 = 0.992
                        # 2.3) frac_num = (0.992 * 8 ) % 1 = 0.936
                            # 3.1) frac_num = (0.453 * 16 ) % 1 = 0.248
                            # 3.2) frac_num = (0.248 * 16 ) % 1 = 0.968
                            # 3.3) frac_num = (0.968 * 16 ) % 1 = 0.688

            # Вернёмся к целой части
            # Делаем по полной аналогии с алгоритмом для целого числа
            number //= 1
            number = int(number)
            integral_answer = ''
            if number == 0: 
                answer = '0.' + fraction_answer
                return answer
            while (number != 0):
                intermediate_answer = number % end_base
                if (end_base == 16 and intermediate_answer in dec_to_hex):
                    intermediate_answer = dec_to_hex[intermediate_answer]
                integral_answer = (str(intermediate_answer)) + integral_answer
                number //= end_base
            answer = integral_answer + '.' + fraction_answer
            return answer

    # Для перевода: 8 -> 2; 16 -> 2
    # Алгоритм: ЗАМЕНА НА ДВОИЧНЫЙ ЭКВИВАЛЕНТ
    elif (start_base in [8, 16] and end_base == 2):
        checker = 0
        if start_base == 8:
            oct_to_bin = {'1' : '001',
                          '2' : '010',
                          '3' : '011',
                          '4' : '100',
                          '5' : '101',
                          '6' : '110',
                          '7' : '111'}
            answer = ''
            for i in str(number):
                if checker == 0:
                    answer += oct_to_bin[i][oct_to_bin[i].find('1')::]
                    checker = 1
                else:
                    answer += oct_to_bin[i]
            return answer
        
        elif start_base == 16:
            hex_to_bin = {'1' : '0001',
                          '2' : '0010',
                          '3' : '0011',
                          '4' : '0100',
                          '5' : '0101',
                          '6' : '0110',
                          '7' : '0111',
                          '8' : '1000',
                          '9' : '1001',
                          'A' : '1010',
                          'B' : '1011',
                          'C' : '1100',
                          'D' : '1101',
                          'E' : '1110',
                          'F' : '1111'}
            answer = ''
            for i in str(number):
                if checker == 0:
                    answer += hex_to_bin[i][hex_to_bin[i].find('1')::]
                    checker = 1
                else:
                    answer += hex_to_bin[i]
            return answer
        
    # Для перевода: 8 -> 16; 16 -> 6
    # Алгоритм: ЧЕРЕЗ ПРОМЕЖУТОЧНЫЙ ПЕРЕВОД В ДВОИЧНУЮ СИСТЕМУ
    elif (start_base in [8, 16] and end_base in [8, 16]):
        number_bin = number_system_converter(number, start_base, 2)
        answer = number_system_converter(number_bin, 2, end_base)
        return answer
        
