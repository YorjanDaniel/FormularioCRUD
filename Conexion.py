# Conexion.py
import mysql.connector

class CConexion:
    @staticmethod
    def ConexionBaseDatos():
        try:
            conexion = mysql.connector.connect(
                user="****",          
                password="*****", 
                host="*****",     
                database="clientes",  
                port="****"           
            )
            print("Conexión exitosa")
            return conexion
        except mysql.connector.Error as error:
            print(f"Error al conectarse a la base de datos: {error}")
            return None
