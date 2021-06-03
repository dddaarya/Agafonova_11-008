from matplotlib import pyplot as plt
import operator

address_and_num_of_houses = {}
address_and_quality = {}


def distance(x1, y1, x2, y2):
    """
    Расчет расстояния между двумя точками
    Args:
        x1 y1 : Координаты 1-ой точки
        x2 y2 : Координаты 2-ой точки
    Returns:
        float: расстояние между ними
    """
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def read_data(path):
    """
    Чтение файла и сохранение в словаре вида: ключ адрес, значения это кортеж (координата Х, коордианата Y, площадь)
    Пример: {'пр-кт Фатыха Амирхана д 91Б': (5.73063, 11.8712, 2095.0), ... }
    Args:
        path (str): путь к файлу
    Returns:
        dict: ключ адрес, значение (x, y, площадь)
    """
    database = {}
    with open(path, encoding="utf-8") as file:
        for line in file:
            address, x, y, s = line.split("	")
            database[address] = (float(x.strip()), float(y.strip()), float(s.strip()))
    return database


def task1(database):
    """
    Задача 1
    Args:
        database (dict): изначальный датасет словарь, ключ адрес, значение (x, y, площадь)
        помимо database могут быть любые другие аргументы
    Returns:
        list: координаты дома (x, y)
    """
    # num_of_houses_in_500m_radius = 0
    # max = 0
    # best_house = ""
    keys = list(database.keys())
    i = 0
    while i < len(keys):
        curr = keys[i]
        j = i
        while j < len(keys):
            if distance(database[curr][0], database[curr][1], database[keys[j]][0], database[keys[j]][1]) <= 0.5:
                if curr in address_and_num_of_houses:
                    address_and_num_of_houses[curr] += 1
                else:
                    address_and_num_of_houses[curr] = 1

                if keys[j] in address_and_num_of_houses:
                    address_and_num_of_houses[keys[j]] += 1
                else:
                    address_and_num_of_houses[keys[j]] = 1

                if curr in address_and_quality:
                    address_and_quality[curr] += 0.7 * database[curr][2] // 18
                else:
                    address_and_quality[curr] = 0.7 * database[curr][2] // 18

                if keys[j] in address_and_quality:
                    address_and_quality[keys[j]] += 0.7 * database[keys[j]][2] // 18
                else:
                    address_and_quality[keys[j]] = 0.7 * database[keys[j]][2] // 18

            j += 1
        i += 1
    result = max(address_and_num_of_houses.items(), key=operator.itemgetter(1))[0]
    return (database[result][0], database[result][1])


def task2(database):
    """
    Задача 2
    Args:
        database (dict): изначальный датасет словарь, ключ адрес, значение (x, y, площадь)
        помимо database могут быть любые другие аргументы
    Returns:
        list: координаты домов [(x1,y1), (x2,y2) ... (xn,yn)]
    """
    sorted_ = list(dict(sorted(address_and_num_of_houses.items(), key=lambda item: item[1])).keys())[::-1]
    count = 0
    i = 1
    best = []
    while count <= 10:
        if i == 0:
            best.append((database[sorted_[i]][0], database[sorted_[i]][1]))
            count += 1
        else:
            flag = True
            for best_item in best:
                if distance(best_item[0], best_item[1], database[sorted_[i]][0], database[sorted_[i]][1]) <= 1:
                    flag = False
                    break
            if flag:
                count += 1
                best.append((database[sorted_[i]][0], database[sorted_[i]][1]))
        i += 1
    return best


def task3(database):
    """
    Задача 3
    Args:
        database (dict): изначальный датасет словарь, ключ адрес, значение (x, y, площадь)
        помимо database могут быть любые другие аргументы
    Returns:
        list: координаты домов [(x1,y1), (x2,y2) ... (xn,yn)]
    """
    sorted_ = list(dict(sorted(address_and_quality.items(), key=lambda item: item[1])).keys())[::-1]
    print(sorted_)
    count = 0
    i = 1
    best = []
    while count <= 15:
        if i == 0:
            best.append((database[sorted_[i]][0], database[sorted_[i]][1]))
            count += 1
        else:
            flag = True
            for best_item in best:
                if distance(best_item[0], best_item[1], database[sorted_[i]][0], database[sorted_[i]][1]) <= 1:
                    flag = False
                    break
            if flag:
                count += 1
                best.append((database[sorted_[i]][0], database[sorted_[i]][1]))
        i += 1
    return best


def plot(database, best_coords):
    """
    НЕ МЕНЯТЬ КОД!
    Отрисовка точек 2D
    Args:
        database (dict): изначальный датасет словарь, ключ адрес, значение (x, y, площадь)
        best_coords (list): для задачи 1 это (x, y), для задачи 2-3 это [(x1,y1), (x2,y2) ... (xn,yn)]
    """
    plt.close()
    fig, ax = plt.subplots(figsize=(8, 8))
    plt.plot([coord[0] for coord in database.values()],
             [coord[1] for coord in database.values()], '.', ms=5, color='k', alpha=0.5)
    if isinstance(best_coords[0], tuple):
        for x, y in best_coords:
            circle = plt.Circle((x, y), 0.5, color='r', fill=False, zorder=2)
            ax.add_patch(circle)
        plt.plot([coord[0] for coord in best_coords],
                 [coord[1] for coord in best_coords], '.', ms=15, color='r')
    elif isinstance(best_coords[0], float):
        x, y = best_coords
        circle = plt.Circle((x, y), 0.5, color='r', fill=False, zorder=2)
        ax.add_patch(circle)
        plt.plot(*best_coords, '.', ms=15, color='r')
    else:
        raise ValueError("Проверь, что подаёшь список кортежей или кортеж из двух координат")
    plt.show()


def homework():
    path = "../data/buildings.txt"
    database = read_data(path)

    best_task1 = task1(database)
    plot(database, best_task1)

    best_task2 = task2(database)
    plot(database, best_task2)

    best_task3 = task3(database)
    plot(database, best_task3)


if __name__ == '__main__':
    homework()
