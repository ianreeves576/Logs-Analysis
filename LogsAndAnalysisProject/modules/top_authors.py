from modules import connection
from modules import formatter

def get_top_authors():
    conn = connection.get_connection()
    conn.execute('''SELECT
        count (authors.id) AS NumberOfViews,
        authors.name
        FROM log, authors, articles
        Where log.path != '/' AND
        articles.slug =
        SUBSTRING(log.path, LENGTH('/article/') + 1)
        AND articles.author = authors.id
        GROUP BY authors.name,
        authors.id
        ORDER BY NumberOfViews DESC;
    ''')

    return conn

def print_top_authors():
    print("Top authors:")
    formatter.repeat_separator()
    for item in get_top_authors():
        print("The totl views for the author '" + str(item[1]) +
              "' are " + formatter.format_num(item[0]) + '.')
    formatter.repeat_separator()