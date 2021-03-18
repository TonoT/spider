from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, create_engine

Base = declarative_base()


class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))







if __name__ == '__main__':
    # engine = create_engine('mysql+pymysql://root:123456@localhost:3306/mytest')
    # # 创建DBSession类型:
    # DBSession = sessionmaker(bind=engine)
    # #
    # # session = DBSession()
    # # # 创建新User对象:
    # # new_user = User(id='5', name='Bob')
    # # # 添加到session:
    # # session.add(new_user)
    # # # 提交即保存到数据库:
    # # session.commit()
    # # # 关闭session:
    # # session.close()
    # session = DBSession()
    # all = session.query(User).filter(User.id == 5).one()
    # print(all.__dict__)
    # session.close()
    # s=[1,2,3,4,5]
    # print(list(map(str,s)))
    x=4
    x=+2
    print(x)
