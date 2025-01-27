#Задание состоит из двух частей. 1 часть – написать программу в соответствии со своим вариантом задания.
#Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
#2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов)
#и целевую функцию для нахождения оптимального  решения.
#Вариант 13
#Конвейер сборки состоит из восьми технологических мест. На 2 из них требуется силовая подготовка (мужчины).
#Конвейер должен работать круглосуточно (3 смены). Сформировать все возможные варианты рабочего расписания, если в цехе работает 24 рабочих: 16 женщин и 8 мужчин.

#Дополнительное условие: мужчины могут работать не больше двух смен в день, женщины – не больше одной.
#Целевая функция: найти самый лучший вариант расписания, если эффективность одного мужчины – 100, а одной женщины – 75.

import time
import itertools
from collections import defaultdict

# Функция для проверки ограничений по сменам
def check_shift_limits(schedule, num_men, num_women, num_places, num_shifts):
    workers = ['M' + str(i+1) for i in range(num_men)] + ['W' + str(i+1) for i in range(num_women)]
    for worker in workers:
      shift_count = 0
      for shift_workers in schedule:
          for place_worker in shift_workers:
            if place_worker == worker:
                shift_count+=1
      if worker[0] == 'M' and shift_count > 2:
        return False
      if worker[0] == 'W' and shift_count > 1:
        return False
    return True

# Функция для расчета эффективности расписания
def calculate_efficiency(schedule, num_men, num_women):
    efficiency = 0
    for shift_workers in schedule:
        for worker in shift_workers:
            if worker[0] == 'M':
                efficiency += 100
            elif worker[0] == 'W':
                efficiency += 75
    return efficiency

# Генерирует расписания конвейера алгоритмическим способом
def generate_schedules_algorithmic(num_men, num_women, num_places, num_shifts, max_schedules=None):
    print("\nАлгоритмический способ:")
    start_time = time.time()

    men_places = [1, 2]
    workers = ['M' + str(i+1) for i in range(num_men)] + ['W' + str(i+1) for i in range(num_women)]
    schedule_count = 0
    all_schedules = []
    best_schedule = None
    best_efficiency = 0
    
    for shift_combination in itertools.product(itertools.permutations(workers, num_places), repeat=num_shifts):
        
        valid_schedule = True
        for shift_workers in shift_combination:
            for place in men_places:
                if shift_workers[place - 1][0] != 'M':
                    valid_schedule = False
                    break
            if not valid_schedule:
                break
        if valid_schedule and check_shift_limits(shift_combination, num_men, num_women, num_places, num_shifts):
            efficiency = calculate_efficiency(shift_combination, num_men, num_women)
            all_schedules.append(shift_combination)
            if efficiency > best_efficiency:
                best_schedule = shift_combination
                best_efficiency = efficiency
            schedule_count += 1
            if max_schedules and schedule_count >= max_schedules:
                  break

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\nВсего расписаний (алгоритмический способ): {schedule_count}")
    print(f"Время выполнения (алгоритмический способ): {elapsed_time:.4f} секунд")
    print(f"Наилучшая эффективность (алгоритмический способ): {best_efficiency}")
    return elapsed_time, all_schedules, best_schedule

# Генерирует расписания конвейера с помощью функций Питона.
def generate_schedules_pythonic(num_men, num_women, num_places, num_shifts, max_schedules=None):
    print("\nС помощью функций Питона:")
    start_time = time.time()

    men_places = [1, 2]
    workers = ['M' + str(i+1) for i in range(num_men)] + ['W' + str(i+1) for i in range(num_women)]
    
    schedule_count = 0
    all_schedules = []
    best_schedule = None
    best_efficiency = 0

    for shift_combination in itertools.product(itertools.permutations(workers, num_places), repeat=num_shifts):
       
        valid_schedule = True
        for shift_workers in shift_combination:
            if not all(shift_workers[place-1][0] == 'M' for place in men_places):
                valid_schedule = False
                break
        
        if valid_schedule and check_shift_limits(shift_combination, num_men, num_women, num_places, num_shifts):
            efficiency = calculate_efficiency(shift_combination, num_men, num_women)
            all_schedules.append(shift_combination)
            if efficiency > best_efficiency:
                best_schedule = shift_combination
                best_efficiency = efficiency
            schedule_count += 1
            if max_schedules and schedule_count >= max_schedules:
                break

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\nВсего расписаний (с помощью функций Питона): {schedule_count}")
    print(f"Время выполнения (с помощью функций Питона): {elapsed_time:.4f} секунд")
    print(f"Наилучшая эффективность (с помощью функций Питона): {best_efficiency}")
    return elapsed_time, all_schedules, best_schedule


if __name__ == "__main__":
    num_men = 8
    num_women = 16
    num_places = 4
    num_shifts = 3
    max_schedules = 1000  # Ограничение на количество расписаний

    start_time_alg = time.time()
    time_algorithmic, all_schedules_alg, best_schedule_alg = generate_schedules_algorithmic(num_men, num_women, num_places, num_shifts, max_schedules)
    end_time_alg = time.time()
    time_algorithmic = end_time_alg - start_time_alg


    start_time_py = time.time()
    time_pythonic, all_schedules_py, best_schedule_py = generate_schedules_pythonic(num_men, num_women, num_places, num_shifts, max_schedules)
    end_time_py = time.time()
    time_pythonic = end_time_py - start_time_py

    output_lines_alg = []
    output_lines_alg.append("\nВсе расписания (алгоритмический способ):")
    for i, schedule in enumerate(all_schedules_alg):
        output_lines_alg.append(f"\nРасписание {i+1}:")
        for shift_index, workers_perm in enumerate(schedule):
             output_lines_alg.append(f"  Смена {shift_index+1}:" + " ".join(f"Место {j+1}: {worker}  " for j, worker in enumerate(workers_perm)))
    if best_schedule_alg:
        output_lines_alg.append(f"\nНаилучшее расписание (алгоритмический способ):")
        for shift_index, workers_perm in enumerate(best_schedule_alg):
            output_lines_alg.append(f"  Смена {shift_index+1}:" + " ".join(f"Место {j+1}: {worker}  " for j, worker in enumerate(workers_perm)))
    else:
        output_lines_alg.append("\nНе найдено ни одного корректного расписания (алгоритмический способ)")

    print("\n".join(output_lines_alg))



    output_lines_py = []
    output_lines_py.append("\nВсе расписания (с помощью функций Питона):")
    for i, schedule in enumerate(all_schedules_py):
        output_lines_py.append(f"\nРасписание {i+1}:")
        for shift_index, workers_perm in enumerate(schedule):
             output_lines_py.append(f"  Смена {shift_index+1}:" + " ".join(f"Место {j+1}: {worker}  " for j, worker in enumerate(workers_perm)))
    if best_schedule_py:
        output_lines_py.append(f"\nНаилучшее расписание (с помощью функций Питона):")
        for shift_index, workers_perm in enumerate(best_schedule_py):
             output_lines_py.append(f"  Смена {shift_index+1}:" + " ".join(f"Место {j+1}: {worker}  " for j, worker in enumerate(workers_perm)))
    else:
        output_lines_py.append("\nНе найдено ни одного корректного расписания (с помощью функций Питона)")

    print("\n".join(output_lines_py))


    print("\nСравнение времени выполнения:")
    print(f"Алгоритмическим способом: {time_algorithmic:.4f} секунд")
    print(f"с помощью функций Питона: {time_pythonic:.4f} секунд")
    if time_algorithmic < time_pythonic:
        print(f"Алгоритмический способ быстрее на {time_pythonic - time_algorithmic:.4f} секунд.")
    elif time_pythonic < time_algorithmic:
        print(f"Способ с помощью функций Питона быстрее на {time_algorithmic - time_pythonic:.4f} секунд.")
    else:
        print(f"Времена выполнения способов равны.")
