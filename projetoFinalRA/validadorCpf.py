def validar_cpf(cpf):
    # Verifica se tem exatamente 11 dígitos numéricos
    if not cpf.isdigit() or len(cpf) != 11:
        return False

    # Elimina CPFs com todos os dígitos iguais
    if cpf == cpf[0] * 11:
        return False

    # Validação do primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10 % 11) % 10
    if digito1 != int(cpf[9]):
        return False

    # Validação do segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10 % 11) % 10
    if digito2 != int(cpf[10]):
        return False

    return True
