print("\033[H\033[J", end="")
# Петя – студент, а Катя – школьница. Он задумывает два натур-числа X и Y (X, Y ≤ 1000).
# Есть 2 подсказки: суммa чисел S и их произведение P. Помогите Кате отгадать числа.
# Примечание: числа S и P задавать не нужно, они будут передаваться в тестах. 
# В результате вы должны вывести все возможные пары чисел X и Y через пробел, такие что X <= Y.

s = 29
p = 204

# Решение #1:
# x = int((s/2-((s/2)**2-p)**0.5))
# y = int((s/2+((s/2)**2-p)**0.5))
# print(x, y)

# Решение #2:
# z = ((s/2)**2 - p )**0.5
# print(int(s/2 - z), int(s/2 + z))

# Решение #3:
# res = []
# for i in range(s + p):
#     if i == (s * i - p)**0.5:
#         res.append(i)
# print(*res if len(res) == 2 else res + res)

# Решение #4:
# stop = 0     # без stop выводит две одинак-пары чисел.
# for i in range(s + p):
#     if stop: break
#     for j in range(s + p):
#         if i + j == s and i * j == p:
#             stop = 1
#             print(*sorted([i, j])) # - по сути "print(i, j)", но отсорт-но по возрастанию.
#             break
# Решение #5:
for i in range(s + p):
    for j in range(s + p):
        if i + j == s and i * j == p:
            solutions = [min(i, j), max(i, j)]
            break
print(f'{solutions[0]} {solutions[1]}')