import sqlite3

def get_customer_spend():
    conn = sqlite3.connect('parts_avatar.db')
    cursor = conn.cursor()
    
    # Task: Join Customers, Orders, and Order_Items to calculate 
    # total spend (price * quantity) per Customer Name.
    query = """
    SELECT c.name, SUM(oi.price * oi.quantity) as total_spend
    FROM Customers c
    JOIN Orders o 
    ON c.customer_id = o.customer_id
    JOIN Order_Items oi
    ON o.order_id = oi.order_id
    GROUP BY c.customer_id, c.name
    """
    
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results
