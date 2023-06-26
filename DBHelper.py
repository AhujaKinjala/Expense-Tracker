
from pymysql import *
from pymysql import cursors


def get_columns(description):
    # column names are present as the first element of the collection,
    # hence extract the first element[0], create tuple & return it.
    return tuple(map(lambda x: x[0], description))
def get_all_data(query, parameters=None):
    conn = connect(host='localhost', database='expense_tracker', user='Kinjala', password='akinjala')
    cur = conn.cursor()
    if (parameters is None):
        cur.execute(query)
    else:
        cur.execute(query,parameters)
    headers = get_columns(cur.description)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return (headers,)+result

def get_data(query, parameters=None):
    conn = connect(host='localhost', database='expense_tracker', user='Kinjala', password='akinjala')
    cur = conn.cursor(cursor=cursors.DictCursor)
    if (parameters is None):
        cur.execute(query)
    else:
        cur.execute(query,parameters)

    result = cur.fetchone()
    print(result)
    cur.close()
    conn.close()
    return result

def execute_query(query, parameters=None):
    conn = connect(host='localhost', database='expense_tracker', user='Kinjala', password='akinjala')
    cur = conn.cursor()
    if (parameters is None):
        cur.execute(query)
    else:
        cur.execute(query,parameters)
    conn.commit()
    cur.close()
    conn.close()
