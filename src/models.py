from datetime import datetime


def get_convert_date(date: str):
    """
    Получаем дату в нужном формате.
    :param date: Дата в старом формате.
    :return: Дата в нужном формате.
    """
    date_form = datetime.fromisoformat(date)
    return date_form.strftime("%d.%m.%Y")


def get_convert_info(info_payment: str):
    """
    Получаем замаскированные данные по счетам и картам.
    :param info_payment: Данные по счетам и картам.
    :return: Замаскированные данные по счетам и картам.
    """
    if info_payment:
        info_list = info_payment.split()
        if info_payment.startswith("Счет"):
            check = info_list.pop()
            check = f"**{check[-4:]}"
            info_list.append(check)
        else:
            check = info_list.pop()
            check = f"{check[:-12]} {check[-12:-10]}** **** {check[-4:]}"
            info_list.append(check)
        return " ".join(info_list)
    return "Нет информации"


class Operation:
    def __init__(
            self,
            pk: int,
            date: str,
            state: str,
            amount: dict,
            description: str,
            from_: str,
            to: str
    ):
        self.pk = pk                                # id транзакциии
        self.date = get_convert_date(date)          # информация о дате совершения операции
        self.state = state                          # статус перевода
        self.amount = amount                        # сумма операции и валюта
        self.description = description              # описание типа перевода
        self.from_ = get_convert_info(from_)        # откуда
        self.to = get_convert_info(to)              # куда

    def get_date(self):
        """
        :return: Дата проведения операции.
        """
        return self.date

    def __str__(self):
        return (f"{self.date} {self.description}\n"
                f"{self.from_} -> {self.to}\n"
                f"{self.amount['amount']} {self.amount['currency']['name']}")
