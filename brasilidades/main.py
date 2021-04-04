# from cpforcnpj import Documento
# from telefonesbr import TelefonesBr
# from databr import DataBr
from acesso_cep import BuscarEndereco

# cpf = "06855278671"
# novo_cpf = Documento.cria_documento(cpf)
# print(f"novo cpf: {novo_cpf}")
# cpnj = "47870007000128"
# cnpj_cadastrado = Documento.cria_documento(
#     cpnj,
# )
# print(f"cnpj cadastrado: {cnpj_cadastrado }")

# telefone = "31983348121"
# telefone_cadastrado = TelefonesBr(telefone)
# print(telefone_cadastrado)

# novo_cadastro = DataBr()
# print(novo_cadastro)
cep = "31310220"
endereco_cadastrado = BuscarEndereco(cep)
print(endereco_cadastrado)