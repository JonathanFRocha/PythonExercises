from datetime import datetime


class DataBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.formatar_data()

    def pegar_mes(self):
        meses_do_ano = [
            "janeiro",
            "fevereiro",
            "março",
            "abril",
            "maio",
            "junho",
            "julho",
            "agosto",
            "setembro",
            "outubro",
            "novembro",
            "dezembro",
        ]
        indice_mes = self.momento_cadastro.month() - 1
        return meses_do_ano[indice_mes]

    def pegar_dia_semana(self):
        dia_semana_lista = ["segunda", "terça", "quarta", "quinta", "sexta"]
        indice_dia_semana = self.momento_cadastro.weekday()
        return dia_semana_lista[indice_dia_semana]

    def formatar_data(self):
        return self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
