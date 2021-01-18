from flask import flash, redirect, url_for

def extract_if_any(cursor, is_numeric):
    ret = cursor.fetchall()
    if ret:
        return ret[0][0]
    else:
        return 0

def handle_postgres_error(err, cursor, conn, redirect_url):
    flash(err.pgerror)
    conn.commit()
    cursor.execute("SET SEARCH_PATH TO zwiazek")
    return redirect(url_for(redirect_url))