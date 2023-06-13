from pydantic import BaseModel
from datetime import datetime

class QuestionIdResponse(BaseModel):
    question=str
    response=str
    date=str
    status=bool

import couchdb
from couchdb.mapping import Document


from couchdb.mapping import Document, TextField, DateTimeField, BooleanField


class QuestionModel(Document):
    # _id = TextField()
    question = TextField()
    response = TextField()
    created_date_time = DateTimeField()
    updated_date_time = DateTimeField()
    indexed_date_time = DateTimeField()
    created_by = TextField()
    updated_by = TextField()
    thread_id = TextField()
    is_deleted = BooleanField()

class CouchDBConnection:

    def __init__(self):
        self.username = "root"
        self.password = "root"
        self.url = "20.169.172.120"
        self.port = "5984"
        self.address = "http://root:root@20.169.172.120:5984"
        self.conn = None
        try:
            self.conn = couchdb.Server(self.address)
            print("CouchDB version : ", self.conn.version())

        except Exception as e:  # TODO:- find exact exception
            print("Can't connect to couchdb ", e)

    def get_db(self, db_name):
        db = None

        try:
            db = self.conn[db_name]
        # except couchdb.http.ResourceNotFound as e:
        #     print(f"Can't find database : {db_name}")
        except Exception as e:
            print("Can't find database here ")
            print("Creating database now")
            return self.create_db(db_name)

        return db

    def load_model_by_id(self, db_name, model, doc_id):
        db = self.get_db(db_name)
        return model.load(db, doc_id)



def get_question_by_id(id):
        couch_client=CouchDBConnection()
        try:
            model = couch_client.load_model_by_id(
                "questions", QuestionModel, id)
            # print(model)
            # print(model)
            response_sechema = {
                "question":model.question,
                "response":model.response,
                "date":model.updated_date_time,
                "status":True
            }
            return response_sechema
        except Exception as e:
            response_sechema = {
                "question":"",
                "response":"",
                "date":str(datetime.now()),
                "status":False
            }
            return response_sechema
            raise DocumentNotFoundById(
                f"Document By {id.question_id} not found")