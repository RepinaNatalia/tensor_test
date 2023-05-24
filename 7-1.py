# Напишите класс Segment
# Для его инициализации нужно два кортежа с координатами точек (x1, y1), (x2, y2)
# Реализуйте методы классы:
# 1. length, который возвращает длину нашего отрезка, с округлением до 2 знаков после запятой
# 2. x_axis_intersection, который возвращает True, если отрезок пересекает ось абцисс, иначе False
# 3. y_axis_intersection, который возвращает True, если отрезок пересекает ось ординат, иначе False
# Например (Ввод --> Вывод) :
# Segment((2, 3), (4, 5)).length() --> 2.83
# Segment((-2, -3), (4, 5)).x_axis_intersection() --> True
# Segment((-2, -3), (4, -5)).y_axis_intersection() --> False

# Здесь пишем код

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ

class Segment:
    def __init__(self, lin1, lin2):
        self.x1 = lin1[0]
        self.y1 = lin1[1]
        self.x2 = lin2[0]
        self.y2 = lin2[1]

    def length(self):
        d = ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) **2) ** 0.5   # длина отрезка по координатам
        d1 = round(d,2)   # округляем до 2 знаков
        return (d1)

    def x_axis_intersection(self):
        self.xmin = min(self.x1, self.x2)   # находим левую и правую границы отрезка
        self.xmax = max(self.x1, self.x2)
        if self.xmin <= 0 <= self.xmax:
            return (True)
        else:
            return (False)

    def y_axis_intersection(self):
        self.ymin = min(self.y1, self.y2)   # находим верхнюю и нижнюю границы отрезка
        self.ymax = max(self.y1, self.y2)
        if self.ymin <= 0 <= self.ymax:
            return (True)
        else:
            return (False)



data = [Segment((2, 3), (4, 5)).length,
        Segment((1, 1), (1, 8)).length,
        Segment((0, 0), (0, 1)).length,
        Segment((15, 1), (18, 8)).length,
        Segment((-2, -3), (4, 5)).x_axis_intersection,
        Segment((-2, -3), (-4, -2)).x_axis_intersection,
        Segment((0, -3), (4, 5)).x_axis_intersection,
        Segment((2, 3), (4, 5)).y_axis_intersection,
        Segment((-2, -3), (4, 5)).y_axis_intersection,
        Segment((-2, 3), (4, 0)).y_axis_intersection
        ]


test_data = [2.83, 7.0, 1.0, 7.62, True, False, True, False, True, True]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')