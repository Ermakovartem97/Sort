from stupid import sort_stupid
from bubble import sort_bubble
from cocktail import sort_cocktaill

from testSort import test_sort

print("Параметры сортировки: 100 списков по 400 чисел от -100 до 100")
print("Глупая сортировка: ", test_sort(sort_stupid), " сложность O(n3)")
print("Cортировка пузырьком: ", test_sort(sort_bubble), " сложность O(n3)")
print("Шейкерная сортировка: ", test_sort(sort_cocktaill), " сложность O(n3)")

