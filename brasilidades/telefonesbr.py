import re


class TelefonesBr:
    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError("Número de Telefone Inválido!")

    def __str__(self):
        return self.format_telefone()

    def valida_telefone(self, telefone):
        padrao = "([1-9]{2,3})?([1-9]{2})([1-9]{4,5})([1-9]{4})"
        return re.search(padrao, telefone)

    def format_telefone(self):
        padrao = "([1-9]{2,3})?([1-9]{2})([1-9]{4,5})([1-9]{4})"
        found = re.search(padrao, self.numero)
        return "+{}({}){}-{}".format(
            found.group(1), found.group(2), found.group(3), found.group(4)
        )