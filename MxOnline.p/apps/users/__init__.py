import pymysql
pymysql.version_info = (1, 3, 13, "final", 0)
pymysql.install_as_MySQLdb()

default_app_config = 'users.apps.UsersConfig'    # -中文显示