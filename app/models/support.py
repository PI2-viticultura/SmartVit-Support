from settings import load_database_params
from extensions import client
import pymongo
import os


class MongoDB():
    def __init__(self):
        """Constructor to model class."""
        if(os.getenv('ENVIRONMENT') != 'developing_local'):
            self.client = client
        else:
            self.params = load_database_params()
            try:
                self.client = pymongo.MongoClient(
                    **self.params, serverSelectionTimeoutMS=10
                )
            except Exception as err:
                print(f'Erro ao conectar no banco de dados: {err}')

    def test_connection(self):
        try:
            self.client.server_info()
            return True
        except Exception as err:
            print(f'Erro ao conectar no banco de dados: {err}')
            return False

    def close_connection(self):
        self.client.close()

    def get_collection(self):
        db = self.client[os.getenv("DBNAME", "smart-dev")]
        collection = db['support']
        return collection

    def insert_one(self, body):
        try:
            collection = self.get_collection()
            collection.insert_one(body)
            return True
        except Exception as err:
            print(f'Erro ao inserir no banco de dados: {err}')
            return False

    def update_one(self, document, body):
        try:
            collection = self.get_collection()

            collection.update_one(
                {"id": body["id"]},
                {"$set": {body}}
            )

        except Exception as err:
            print(f'Erro ao atualizar no banco de dados: {err}')

    def delete_one(self, identifier):
        try:
            collection = self.get_collection()
            res = collection.delete_one({"id": identifier})
            if res.deleted_count == 1:
                print(f'mensagem {identifier} removida com sucesso')
            else:
                print(f'Erro ao remover a mensagem {identifier}:'
                      ' nenhuma mensagem encontrada para o id')
        except Exception as err:
            print(f'Erro ao deletar no banco de dados: {err}')

    def get_one(self, identifier):
        collection = self.get_collection()
        document = collection.find_one({"id": identifier})
        return document

    def get_all(self):
        collection = self.get_collection()
        document = collection.find()
        return document
