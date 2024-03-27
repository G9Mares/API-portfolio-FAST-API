import mysql.connector

class MyConexion:
    """This class have diferents methods to interact and process information through a MySQL connection.
    """    
    def __init__(self, host:str, user:str, password:str):     
      try:
        self.conexion = mysql.connector.connect(
          user=user,
          host=host,
          password=password
        )
        self.cursor = self.conexion.cursor()
      except Exception as e:
         print("An error has ocurred during the conexion rhit the database \n "+ e)

    
    
    def create_db(self):
        self.cursor.execute("SHOW DATABASES")
    
    def create_models(self):
        print(2)