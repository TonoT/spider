import pymysql


class mysql:
    def     get_mysql(config):
        conn = pymysql.connect(**config)

        return conn

    # def get_mysql(config):
    #     try:
    #         conn = pymysql.connect(**config)
    #
    #         # 检验数据库连接是否成功
    #         my_cursor = conn.cursor()
    #         my_cursor.execute('select id from table2')
    #         all = my_cursor.fetchall()
    #         print(all)
    #         return my_cursor
    #     except pymysql.Error as e:
    #         print(e)
    #         print('数据库操作失败')
    #     finally:
    #         # 若数据库连接成功，则关闭数据库
    #         print('over')
    #         if conn:
    #             conn.close()
    #

# # 执行sql语句，返回影响条数
#    data = my_cursor.execute('select id from table2')
#    one = my_cursor.fetchone()  # 获取一条数据
#    all = my_cursor.fetchall()
#    print(data)
#    print(one)
#    print(all)
#    print(my_cursor.description)  # description属性，获取的是数据库每个栏位情况
#    print(type(my_cursor.fetchone()))
#    # 将一行数据存储为字典
#    new_list = dict(zip([x[0] for x in my_cursor.description], [x for x in one]))
#    print(new_list)
