class Store:
    def __init__(self, name, address):                                # Инициализация магазина с именем и адресом
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):                              # Добавление товара в магазин
        self.items[item_name] = price
        print(f"Добавлен {item_name} с ценой {price} руб.")

    def remove_item(self, item_name):                                  # Удаление товара из магазина, если он существует
        if item_name in self.items:
            del self.items[item_name]
            print(f"Удален {item_name} из {self.name}")
        else:
            print(f"{item_name} не найден в {self.name}")

    def get_price(self, item_name):                                    # Получение цены товара, если он существует в магазине
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):                      # Обновление цены товара, если он существует в магазине
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена на {item_name} обновлена до {new_price} руб.")
        else:
            print(f"{item_name} не найден в {self.name}")

    def list_items(self):                                              # Перечисление всех товаров в магазине с их ценами
        print(f"{self.name} адрес: {self.address}")
        for item_name, price in self.items.items():
            print(f"{item_name}: {price} руб.")

# Создание объектов класса Store
store1 = Store("Продуктовый магазин", "ул.Ленина 251")
store2 = Store("Магазин электроники", "ул.Дубовая 456")
store3 = Store("Магазин одежды", "ул.Кленовая 789")

# Тестирование
store1.list_items()                                    # Печать всех товаров в магазине

# Добавление товаров в магазин
store1.add_item("яблоки", 150)
store1.add_item("бананы", 132)
store1.add_item("хлеб", 45)
store1.add_item("молоко", 83)
store1.add_item("гречка", 71)

store1.add_item("апельсины", 143)
price = store1.get_price("яблоки")
print(f"Цена на яблоки: {price} руб.")
store1.update_price("яблоки", 210)
store1.remove_item("бананы")
price = store1.get_price("бананы")
print(f"Цена на бананы: {price} руб.")

store1.list_items()                                    # Печать всех товаров в магазине