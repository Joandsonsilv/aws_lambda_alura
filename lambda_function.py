def lambda_handler(event, context):

    print(f"Nome: {event['nome']}")
    print(f"Idade: {event['idade']}")
    print(f"Cargo: {event['cargo']}")
    print(f"Salario: {event['salario']}")

    if event["salario"] > 5000:
        print("Faixa salarial alta!")
    else:
        print("Faixa salarial média!")

    return {
        "statusCode": 200,
        "body": "Codigo sendo executado com sucesso."

    }

event = {
        "nome": "João",
        "idade": 20,
        "cargo": "Estagiario",
        "salario": 2500
    }

resultado = lambda_handler(event, None)
print(resultado)