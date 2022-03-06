class Clients:
    def __init__(self, surname, name, payment, cost):
        self.surname = surname
        self.name = name
        self.payment = sum(payment)
        self.cost = sum(cost)
    def get_balance(self):
        return self.payment - self.cost
    def __str__(self):
        return f'Клиент "{self.name} {self.surname}". Баланс: {self.get_balance()} руб.'

print(".........")

clients = [
            {'surname': 'Donald', 'name': 'Freeman', 'payment': {321, 456, 789}, 'cost': {112, 356, 787}},
            {'surname': 'Martin', 'name': 'Jackson', 'payment': {112, 657, 1020}, 'cost': {399, 200, 630}},
            {'surname': 'Label', 'name': 'Black', 'payment': {312, 645, 787}, 'cost': {321, 123, 350}}
          ]
for client in clients:
    o_client = Clients(client['surname'], client['name'], client['payment'], client['cost'])
    print(o_client)

print(".........")