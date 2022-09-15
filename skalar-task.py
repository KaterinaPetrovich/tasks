# Дан словарь вида (вложенность не известна)
X = {"a": 1,
     "b": 2,
     "c": {"d": 3,
           "e": {
               "h": 4,
               "g": 5
           },
           "k": 7,

           },

     }

# вывести его на экран в виде строк:
# a = 1
# b = 2
# c.d = 3
# c.e.h = 4
# c.e.g = 5
# c.k = 7

result = []


def func(a):
    global result
    if isinstance(a, int):
        print(".".join(result), "=", a)
        result.pop(len(result) - 1)

    else:
        for key in a:
            result.append(key)
            func(a[key])
        if result:
            result.pop(len(result) - 1)

func(X)

