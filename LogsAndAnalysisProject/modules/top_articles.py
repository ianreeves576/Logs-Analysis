from modules import connection
from modules import formatter


def get_top_articles():
    conn = connection.get_connection()
    conn.execute('''
        SELECT
        count (log.path) AS NumberOfViews,
        articles.slug,
        articles.title,
        authors.name
        FROM log, articles, authors
        WHERE log.path != '/' AND
        articles.slug = SUBSTR(log.path, length('/article/') + 1)
        And articles.author = authors.id
        GROUP BY articles.slug, authors.name, articles.title
        ORDER BY NumberOfViews desc
        LIMIT 3;
        ''')

    return conn


def print_top_articles():
    print("Top articles:")
    formatter.repeat_separator()
    for item in get_top_articles():
        print("The total views for the article '" + str(item[2]) +
              "', by the author '" + str(item[3]) +
              "' on the page '" + str(item[1]) +
              "' are " + formatter.format_num(item[0]) + '.')
        formatter.repeat_separator()