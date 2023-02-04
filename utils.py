import json


def load_users():
    """ Загружает данные из файла users.json и возвращает обычный list"""
    with open("./data/users.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def load_offers():
    """ Загружает данные из файла offers.json и возвращает обычный list"""
    with open("./data/offers.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def load_orders():
    """ Загружает данные из файла offers.json и возвращает обычный list"""
    with open("./data/orders.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data
