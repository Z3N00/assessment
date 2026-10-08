import sqlite3

def get_pending_customers():
    conn = sqlite3.connect('parts_avatar.db')
    cursor = conn.cursor()
    
    # Task: Select customer email and order_date where status is 'Pending'.
    query = """
    SELECT c.email, o.order_date
    FROM Customer c 
    INNER JOIN Orders o
    ON c.customer_id = o.customer_id
    WHERE o.status = 'Pending'
    """
    
    cursor.execute(query)
    return cursor.fetchall()
