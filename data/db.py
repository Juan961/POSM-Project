import psycopg2


endpoint = 'usb-project.cfbmmy7rkrlp.us-east-1.rds.amazonaws.com'
usuario = 'postgres'
contraseña = 'postgres'
nombre_db = 'USB-PROJECT'

conn = psycopg2.connect(
    host=endpoint,
    user=usuario,
    password=contraseña,
    dbname=nombre_db
)

endpoint = 'usb-project.cfbmmy7rkrlp.us-east-1.rds.amazonaws.com'
usuario = 'postgres'
contraseña = 'postgres'
nombre_db = 'USBPROJECT'

def get_conn():
    return conn

def get_cursor():
    return conn.cursor()

def commit_db():
    return conn.commit()
