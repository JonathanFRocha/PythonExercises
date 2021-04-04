import requests


class BuscarEndereco:
    def __init__(self, cep):
        if self.cep_valido(cep):
            self.cep = cep
        else:
            raise ValueError("Cep Inválido!!")

    def __str__(self):
        return self.formatar_cep()

    def cep_valido(self, cep):
        return len(cep) == 8

    def formatar_cep(self):
        return f"{self.cep[:5]}-{self.cep[5:]}"

    def acessa_api_cep(self):
        resp = requests.get("https://viacep.com.br/ws/{}/json/".format(self.cep))
        data = resp.json()
        return (data["bairro"], data["localidade"], data["uf"])
