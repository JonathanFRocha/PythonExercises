from validate_docbr import CPF, CNPJ


class Documento:
    @staticmethod
    def cria_documento(documento):
        cnpj = len(documento) == 14
        cpf = len(documento) == 11
        if cpf:
            return DocCpf(documento)
        elif cnpj:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de Digitos invalidos")


class DocCpf:
    def __init__(self, documento):
        if self.cpf_valido(documento):
            self.documento = documento
        else:
            raise ValueError("CPF Inválido!!")

    def __str__(self):
        return self.format_cpf()

    def cpf_valido(self, documento):
        validar = CPF()
        return validar.validate(documento)

    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.documento)


class DocCnpj:
    def __init__(self, documento):
        if self.cnpj_valido(documento):
            self.documento = documento
        else:
            raise ValueError("CNPJ Inválido!")

    def __str__(self):
        return self.format_cnpj()

    def cnpj_valido(self, documento):
        validar = CNPJ()
        return validar.validate(documento)

    def format_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.documento)
