# from functools import reduce

# linux = [30, 500_000]
# windows = [20, 400_000]


# def get_monthly_total(class_info: list) -> int:
#     return reduce(lambda x, y: x*y, class_info)


# # 월 수업료 총액
# print(
#     f'월 수업료 총액: {(get_monthly_total(linux) + get_monthly_total(windows)):,}원')

# # Discount 수업료 총액
# print(
#     f'Discount된 수업료 총액: {(get_monthly_total(linux)*0.95 + get_monthly_total(windows)*0.9):,}원')


# def change_f_to_c(f: float) -> float:
#     return (f-32)/1.8


# # 온도 단위 변경
# print(f'화씨 50도 : 섭씨 {change_f_to_c(50)}도')

# print("Linux\n" * 10)

# s = "Linux is not Unix"
# listed_s = s.split()
# listed_s[0], listed_s[-1] = listed_s[-1], listed_s[0]
# print(" ".join(listed_s))

# x = "abcdef"
# print(x[1:]+x[0])

# x = input("a: ")
# y = input("b: ")
# calc_list = ["+", "-", "*", "/", "%"]

# print("")
# for c in range(calc_list):
#     print(f'{c}: {eval(x+c+y)}')

# 문제 1
import random


def quiz1():
    n1, n2 = [random.randrange(10, 100) for _ in range(2)]
    print(n1, n2)
    print(n1*n2 if (n1+n2) % 2 else n1+n2)


def quiz2():
    n1, n2 = [random.randrange(10, 100) for _ in range(2)]
    print(n1, n2)
    result = int(input("합: "))
    if n1+n2 == result:
        print("정답")
    else:
        print("오답")


quiz1()
quiz2()
