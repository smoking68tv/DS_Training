import numpy as np

def game_core(number):
    "Определяем последовательность чисел. Выполняем бинарный поиск по списку"
    "Функция принимает загаданное число и возвращает число попыток"

    count = 1
    start_value = 1
    end_value = 101
    values = list(range(start_value, end_value+1))

    min_item = 0 
    max_item = len(values) - 1
        
    while min_item <= max_item:
        count += 1
        mid_item = (min_item + max_item) // 2
        if number < values[mid_item]: max_item = mid_item - 1
        elif number > values[mid_item]: min_item = mid_item + 1
        else: break
    return(count)
        
def score_game(game_core):
    "Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"
    
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))

    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))

    print(f"Алгоритм угадывает число в среднем за {score} попыток")
    return(score)

score_game(game_core) # Запуск игры
