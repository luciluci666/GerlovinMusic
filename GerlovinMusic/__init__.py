from .settings import SERVER_IP

if SERVER_IP != '127.0.0.1':
    import pymysql
    pymysql.install_as_MySQLdb()
