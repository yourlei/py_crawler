import json
import pymysql
from DBUtils.PooledDB import PooledDB
from crawler.settings import DBconfig


class MysqlPool:
  """数据库管理"""
  def __init__(self, app=None):
    if not hasattr(MysqlPool, "pool"):
      MysqlPool.getConnect()

    self.conn = MysqlPool.pool.connection()
    # cursor=pymysql.cursors.DictCursor
    self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

  @staticmethod
  def getConnect():
    """初始化连接池,返回连接对象"""
    MysqlPool.pool = PooledDB(
      creator = pymysql,
      mincached = 2,
      maxcached = 6,
      # maxshared = 3,
      maxconnections = 8,
      host = MYSQL_CONFIG["host"],
      port = MYSQL_CONFIG["port"],
      user = MYSQL_CONFIG["user"],
      passwd = MYSQL_CONFIG["password"],
      db = MYSQL_CONFIG["db"],
      use_unicode = True,
      charset = "utf8",
      ping = 0,
      blocking = True,
    )
    print("建立mysql连接池....")

  def insert(self, table, data):
    """插入数据"""
    keys = ', '.join(data.keys())
    values = ', '.join(['%s'] * len(data))
    sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
    print(sql, tuple(data.values()))
    try:
      self.cur.execute(sql, tuple(data.values()))
      self.conn.commit()
    except Exception as e:
      self.conn.rollback()
      self.conn.commit()
      raise e
    return True

  def insert_data(self, sql, params=[]):
    """插入行"""
    try:
      if not params:
        self.cur.execute(sql)
      else:
        self.cur.execute(sql, params)
      self.conn.commit()
    except Exception as e:
      self.conn.rollback()
      raise e
    
    return True
    
  def get_data(self, sql, params=None):
    """查询"""
    if params:
      self.cur.execute(sql, params)
    else:
      self.cur.execute(sql)

    data = self.cur.fetchall()
    return data

  def update_data(self, sql, params=[]):
    """更新"""
    try:
      self.cur.execute(sql, params)
      self.conn.commit()
    except Exception as e:
      self.conn.rollback()
      raise Exception(e)
    return True

  def findOne(self, table, col=[], params=[]):
    """
    验证记录是否存在
    Args:
      table: string, 数据表
      col:   list, 查询的列名
      params:list,参数列表
    """
    sql = "SELECT " + ",".join(col) + " FROM " + table + " WHERE deleted_at = '0000-01-01 00:00:00'"
    # WHERE条件
    for i in range(len(col)):
      col[i] = col[i] + " = %s"
    sql += " AND " + ",".join(col)

    self.cur.execute(sql, params)
    data = self.cur.fetchall()
    
    return data

  def update(self, table, uuid, args: object):
    """
    更新数据
    Args:
      table: string, 表名
      uuid:  string, 待更新的row uuid
      args:  object, 更新的数据
    """
    column = []
    values = []
    # 提取更新的列及值
    for key in args.keys():
      column.append("`" + key + "`" + " = %s")
      if isinstance(args[key], dict):
        args[key] = str(json.dumps(args[key]))
      values.append(args[key])
    # update sql
    sql = "UPDATE " + table + " SET " + ",".join(column) + " WHERE uuid = %s"
    values.append(uuid)
    try:
      self.cur.execute(sql, values)
      self.conn.commit()
    except Exception as e:
      self.conn.rollback()
      self.conn.commit()
      raise Exception(e)
    return True

  def dispose(self,isEnd=1):
    """
    释放连接
    """
    self.cur.close()
    self.conn.close()

if __name__ == "__main__":
  db = MysqlPool()
  result = db.get_data("select id, name from user")
