from models.support import MongoDB


def save_support_request(request):
    fields = ['priority', 'problem', 'description']
    priorities = ['alta', 'média', 'baixa']
    problems = ['Sistema eletrônico com defeito', 'Problema do software',
                'Dados incoerentes', 'Perfil de acesso', 'Sobre o contrato',
                'outros']

    if not all(field in request.keys() for field in fields):
        return {
            "erro": "Sua requisição não informou todos os campos necessários"
        }, 400

    if not request["priority"] in priorities:
        return {"erro": "A prioridade informada não é válida"}, 400

    if not request["problem"] in problems:
        return {"erro": "O problema informado não é válido"}, 400

    if not request["description"]:
        return {"erro": "Não é possível enviar descrição vazia"}, 400

    db = MongoDB()
    connection_is_alive = db.test_connection()
    if connection_is_alive:
        if(db.insert_one(request)):
            return {"message": "success"}, 200
    db.close_connection()

    return {'error': 'Something gone wrong'}, 500
