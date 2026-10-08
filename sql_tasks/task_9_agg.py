import sqlite3

def get_popular_skus():
    conn = sqlite3.connect('parts_avatar.db')
    cursor = conn.cursor()
    
    # Task: Return SKUs where the SUM of quantity across all orders is > 1.
    query = """
    SELECT sku, SUM(quantity) as total_quantity
    FROM Order_Items
    GROUP BY sku
    HAVING SUM(quantity) > 1
    """
    
    cursor.execute(query)
    return cursor.fetchall()
