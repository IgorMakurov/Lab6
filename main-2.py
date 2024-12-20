#Задание состоит из двух частей. 1 часть – написать программу в соответствии со своим вариантом задания.
#Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
#2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов)
#и целевую функцию для нахождения оптимального  решения.
#Вариант 13
#Конвейер сборки состоит из восьми технологических мест. На 2 из них требуется силовая подготовка (мужчины).
#Конвейер должен работать круглосуточно (3 смены). Сформировать все возможные варианты рабочего расписания, если в цехе работает 24 рабочих: 16 женщин и 8 мужчин.

#Дополнительное условие: каждая женщина может работать только в одной смене в день

import time
import itertools

# Константы
NUM_STATIONS = 8
NUM_SHIFTS = 3
TOTAL_WORKERS = 24
NUM_WOMEN = 16
NUM_MEN = 8
POWER_STATIONS = [2, 5]  # Индексы станций, требующих мужчин (нумерация с 1)

#Проверяет мужчин на силовых станциях и чтобы женщины не повторялись
def is_valid_schedule_advanced(schedule):
    # Проверка наличия мужчин на силовых станциях
    for shift_schedule in schedule:
        for station_index in POWER_STATIONS:
          station = station_index - 1
          if shift_schedule[station] == 0:
              pass
          else:
              return False
    # Проверка, что каждая женщина работает только в одну смену
    women_shifts = [None] * NUM_WOMEN  # Для каждой женщины записываем номер ее смены
    for shift_index, shift_schedule in enumerate(schedule):
        for station_index, worker_type in enumerate(shift_schedule):
            if worker_type == 1:  # Если на позиции женщина
                woman_id = shift_index * NUM_STATIONS + station_index  # Уникальный ID для каждой женщины
                if women_shifts[woman_id % NUM_WOMEN] is None:
                    women_shifts[woman_id % NUM_WOMEN] = shift_index
                elif women_shifts[woman_id % NUM_WOMEN] != shift_index:
                    return False  # Женщина работает в более чем одной смене
    return True

#Выводит расписание
def print_schedule(schedule):
    for shift, shift_schedule in enumerate(schedule, 1):
        print(f"Смена {shift}:", end=" ")
        for station, worker_type in enumerate(shift_schedule, 1):
            print(f"Ст{station}: {'М' if worker_type == 0 else 'Ж'}", end=" ")
        print()

#Генерирует расписания
def generate_schedules_advanced():
    print("Генерация расписаний с ограничением: Каждая женщина может работать только в одной смене в день:\n")
    schedules_count = 0
    all_shift_options = list(generate_shift_options())

    for schedule in itertools.product(all_shift_options, repeat=NUM_SHIFTS):
        if is_valid_schedule_advanced(schedule):
            schedules_count += 1
            print_schedule(schedule)
    print(f"\nВсего допустимых расписаний: {schedules_count}\n")

#Генерирует расписание на одну смену
def generate_shift_options():
  for p0 in range(2):
    for p1 in range(2):
      for p2 in range(2):
        for p3 in range(2):
          for p4 in range(2):
            for p5 in range(2):
              for p6 in range(2):
                for p7 in range(2):
                  yield [p0, p1, p2, p3, p4, p5, p6, p7]


# Запуск
start_time = time.time()
generate_schedules_advanced()
end_time = time.time()
print(f"Время выполнения: {end_time - start_time:.4f} секунд")