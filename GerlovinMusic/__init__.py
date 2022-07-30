from .settings import SERVER_IP

if SERVER_IP != '83.229.83.226':
    import pymysql
    pymysql.install_as_MySQLdb()
