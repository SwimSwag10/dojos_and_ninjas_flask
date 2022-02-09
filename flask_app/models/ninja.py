from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__( self , db_data ):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.age = db_data['age']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def ninja_save( cls , data ):
        query = "INSERT INTO ninjas ( first_name , last_name, age, dojo_id, created_at , updated_at ) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s,NOW(),NOW());"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)

    @classmethod
    def ninja_get_all(cls):
        query = "SELECT * FROM ninjas;"
        ninajs_from_db =  connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        ninjas =[]
        for b in ninajs_from_db:
            ninjas.append(cls(b))
        return ninjas

    @classmethod
    def ninja_get_one(cls,data):
        query = "SELECT * FROM ninjas WHERE ninas.id = %(id)s;"
        ninajs_from_db = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)

        return cls(ninajs_from_db[0])

    @classmethod
    def ninja_update(cls,data):
        query = "UPDATE ninjas SET first_name=%(first_name)s, last_name=%(bun)s, age=%(age)s,updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)

    @classmethod
    def ninja_destroy(cls,data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)