print("Примерный калькулятор возраста по росту и весу(!ПРИСУТСТВУЮТ НЕБОЛЬШИЕ БАГИ!)")
rost = int(input("Ваш рост(см): "))
ves = int(input("Ваш вес(кг): "))
class Neuronyourage:
    def __init__(self):
        super().__init__()
    def youreage(self):
        masa1 = ves + rost
        masa2 = masa1 // (masa1 // 3)
        masa3 = masa2 + (masa2 // 2) * 10
        masa4 = masa3 * (masa2 // 1.2) * (masa1 // (rost + ves - masa3))
        masa5 = masa4 + (masa3 * (masa1 // ves))
        masa6 = masa5 // masa3 * (ves // 5)
        masa7 = masa6 // masa3 * (rost // ves) * (ves * rost // (ves + rost + ves // (masa1 * (ves + (rost - (rost // (rost // 2)))))))
        masa8 = masa7 // masa1 * (ves + (rost // (rost - ves)))
        masa9 = masa8 // (ves - (rost // ves))
        masa10 = masa9 * (rost - (ves * 2))
        masa11 = masa10 // (rost - (ves + ves))
        masa12 = masa11 * (ves + (ves + rost) // (ves - (ves // 5)))
        masa13 = masa12 // (ves - (ves // 2))
        masa14 = masa13 * (ves - (rost // ves))
        masa15 = masa14 // ves * (rost - (ves * 2))
        masa16 = masa15 // ves * (ves - (rost // ves))
        masa17 = masa16 // ves + (ves * (ves - (ves - (rost // (ves * 2)))))
        masa18 = masa17 // (rost // (ves - (rost // ves)))
        masa20 = masa18
        age = masa20
        print(f"Ваш примерный возраст: {age} лет.")
    def bye(self):
        print("Пока!")
Neuronyourage().youreage()
Neuronyourage().bye()
