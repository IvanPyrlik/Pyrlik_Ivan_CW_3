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
        self.pk = pk                    # id транзакциии
        self.date = date                # информация о дате совершения операции
        self.state = state              # статус перевода
        self.amount = amount            # сумма операции и валюта
        self.description = description  # описание типа перевода
        self.from_ = from_              # откуда
        self.to = to                    # куда



