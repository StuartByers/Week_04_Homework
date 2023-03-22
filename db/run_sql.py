import psycopg2
import psycopg2.extras as ext

def run_sql(sql, values=None):
    # set up a variable for connection
    conn = None
    # set up empty list
    results = []
    # try to connect to the database
    try: 
        conn = psycopg2.connect("dbname='music_collection'")
        # get a cursor
        cur = conn.cursor(cursor_factory=ext.DictCursor)
        # execute the sql
        cur.execute(sql, values)
        # commit the execution
        conn.commit()
        # get the results
        results = cur.fetchall()
        # close the database connection
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    # return the list
    return results