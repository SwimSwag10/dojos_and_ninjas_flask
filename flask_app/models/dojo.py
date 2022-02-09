from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__( self , db_data ):
        self.id = db_data['id']
        self.name = db_data['name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def dojo_save( cls , data ):
        query = "INSERT INTO dojos ( name , created_at , updated_at ) VALUES (%(name)s,NOW(),NOW());"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)

    @classmethod
    def dojo_get_all(cls):
        query = "SELECT * FROM dojos;"
        dojos_from_db =  connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos =[]
        for b in dojos_from_db:
            dojos.append(cls(b))
        return dojos

    @classmethod
    def dojo_get_one(cls,data):
        query = "SELECT * FROM dojos WHERE dojos.id = %(id)s;"
        dojos_from_db = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)

        return cls(dojos_from_db[0])

    @classmethod
    def dojo_update(cls,data):
        query = "UPDATE dojos SET name=%(name)s,updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)

    @classmethod
    def dojo_destroy(cls,data):
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)