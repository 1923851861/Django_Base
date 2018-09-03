import pymysql

pymysql.install_as_MySQLdb()    #由于是python3版本以上，mysqldb不支持，通过该命令可转换，（如果是sqllite库就不需要了）在每个app中都需要设置