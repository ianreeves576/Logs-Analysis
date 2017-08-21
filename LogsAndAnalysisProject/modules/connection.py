import psycopg2


def get_connection(**kwargs):
    dbname = kwargs.get('dbname', 'postgres')
    user = kwargs.get('name', 'postgres')
    password = kwargs.get('password', 'start')
    conn = psycopg2.connect(f"dbname={dbname} user={user} password={password}")
    cur = conn.cursor()
    return cur


