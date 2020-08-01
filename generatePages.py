import sqlite3


def setup_database():
    images = {
        "Dr Pepper": "https://ui.assets-asda.com/dm/asdagroceries/5449000060501_T1",
        "Coke Zero": "https://ui.assets-asda.com/dm/asdagroceries/5449000031341_T1",
        "Full Coke": "https://ui.assets-asda.com/dm/asdagroceries/5449000051547_T1",
    }
    batches = {
        "0": {"name": 1, "price": 0.55, "expiry": "2021-06-30"},
        "1": {"name": 2, "price": 0.50, "expiry": "2020-06-30"},
        "2": {"name": 3, "price": 0.60, "expiry": "2021-02-28"},
    }
    cans = {
        "0": "0",
        "1": "1",
        "2": "2",
    }
    conn = sqlite3.connect('shop.db')
    conn.execute("PRAGMA foreign_keys = 1")

    for name, image in images.items():
        conn.execute("INSERT INTO types (name, image) VALUES (?, ?)", (name, image))
    for batch in batches.values():
        conn.execute("INSERT INTO batches (type, expiry, price) VALUES (?, ?, ?)", (batch['name'], batch['expiry'], batch['price']))
    for can in range(3):
        conn.execute("INSERT INTO cans (batch) VALUES (?)", (can + 1,))
    conn.commit()

    conn.close()

def main():
    conn = sqlite3.connect('shop.db')
    conn.execute("PRAGMA foreign_keys = 1")

    for can, batch in conn.execute("SELECT can, batch FROM cans").fetchall():
        page = f"""<!DOCTYPE html><meta http-equiv="refresh" content="0; url=../B/{batch}.html">""".strip()
        open(f"C\\{can}.html", "w").write(page)

    for batch, name, price, expiry, image in conn.execute("SELECT batch, name, price, expiry, image FROM batches INNER JOIN types t on batches.type = t.type").fetchall():
        page = f"""
<html>    
  <head>      
    <title>Can Shop</title>
  </head>    
  <body> 
    <p>This is the product page for {name}</p>
    <p>It costs &#163;{price:.2f} and they expire on {expiry}</p>
    <p><img src="{image}"><img></p>
  </body>  
</html>""".strip()
        open(f"B\\{batch}.html", "w").write(page)

    conn.close()


# Run the main program
if __name__ == "__main__":
    #setup_database()
    main()
