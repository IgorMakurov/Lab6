#Задание состоит из двух частей. 1 часть – написать программу в соответствии со своим вариантом задания.
#Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
#2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов)
#и целевую функцию для нахождения оптимального  решения.
#Вариант 13
#Конвейер сборки состоит из восьми технологических мест. На 2 из них требуется силовая подготовка (мужчины).
#Конвейер должен работать круглосуточно (3 смены). Сформировать все возможные варианты рабочего расписания, если в цехе работает 24 рабочих: 16 женщин и 8 мужчин.

import time
import itertools

#Генерирует расписания конвейера алгоритмическим способом
def generate_schedules_algorithmic(num_men, num_women, num_places, num_shifts, max_schedules=None):
    print("\nАлгоритмический способ:")
    start_time = time.time()

    men_places = [1, 2]
    workers = ['M' + str(i+1) for i in range(num_men)] + ['W' + str(i+1) for i in range(num_women)]

    schedule_count = 0
    for shift_combination in itertools.product(itertools.permutations(workers, num_places), repeat=num_shifts):
        
        valid_schedule = True
        for shift_workers in shift_combination:
            for place in men_places:
                if shift_workers[place - 1][0] != 'M':
                    valid_schedule = False
                    break
            if not valid_schedule:
                break
        
        if valid_schedule:
            schedule_count += 1
            yield shift_combination
            if max_schedules and schedule_count >= max_schedules:
                break

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\nВсего расписаний (алгоритмический способ): {schedule_count}")
    print(f"Время выполнения (алгоритмический способ): {elapsed_time:.4f} секунд")
    return elapsed_time

#Генерирует расписания конвейера с помощью функций Питона.
def generate_schedules_pythonic(num_men, num_women, num_places, num_shifts, max_schedules=None):
    print("\nС помощью функций Питона:")
    start_time = time.time()

    men_places = [1, 2]
    workers = ['M' + str(i+1) for i in range(num_men)] + ['W' + str(i+1) for i in range(num_women)]
    
    schedule_count = 0
    for shift_combination in itertools.product(itertools.permutations(workers, num_places), repeat=num_shifts):
       
        valid_schedule = True
        for shift_workers in shift_combination:
            if not all(shift_workers[place-1][0] == 'M' for place in men_places):
                valid_schedule = False
                break

        if valid_schedule:
            schedule_count += 1
            yield shift_combination
            if max_schedules and schedule_count >= max_schedules:
                break

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\nВсего расписаний (с помощью функций Питона): {schedule_count}")
    print(f"Время выполнения (с помощью функций Питона): {elapsed_time:.4f} секунд")
    return elapsed_time


if __name__ == "__main__":
    num_men = 16
    num_women = 8
    num_places = 4
    num_shifts = 3
    max_schedules = 1000 # Ограничение на количество расписаний

    start_time_alg = time.time()
    for i, schedule in enumerate(generate_schedules_algorithmic(num_men, num_women, num_places, num_shifts, max_schedules)):
        print(f"\nРасписание {i+1}:")
        for shift_index, workers_perm in enumerate(schedule):
            print(f"  Смена {shift_index+1}:", end=" ")
            for j, worker in enumerate(workers_perm):
                print(f"Место {j+1}: {worker}  ", end="")
            print()
    end_time_alg = time.time()
    time_algorithmic = end_time_alg - start_time_alg

    start_time_py = time.time()
    for i, schedule in enumerate(generate_schedules_pythonic(num_men, num_women, num_places, num_shifts, max_schedules)):
        print(f"\nРасписание {i+1}:")
        for shift_index, workers_perm in enumerate(schedule):
            print(f"  Смена {shift_index+1}:", end=" ")
            for j, worker in enumerate(workers_perm):
                print(f"Место {j+1}: {worker}  ", end="")
            print()
    end_time_py = time.time()
    time_pythonic = end_time_py - start_time_py


    print("\nСравнение времени выполнения:")
    print(f"Алгоритмическим способом: {time_algorithmic:.4f} секунд")
    print(f"с помощью функций Питона: {time_pythonic:.4f} секунд")
    if time_algorithmic < time_pythonic:
        print(f"Алгоритмический способ быстрее на {time_pythonic - time_algorithmic:.4f} секунд.")
    elif time_pythonic < time_algorithmic:
        print(f"Способ с помощью функций Питона быстрее на {time_algorithmic - time_pythonic:.4f} секунд.")
    else:
        print(f"Времена выполнения способов равны.")
