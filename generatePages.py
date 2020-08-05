import sqlite3


def setup_database():
    images = {
        "Full Dr Pepper": "https://ui.assets-asda.com/dm/asdagroceries/5449000060501_T1",
        "Coke Zero": "https://ui.assets-asda.com/dm/asdagroceries/5449000031341_T1",
        "Full Coke": "https://ui.assets-asda.com/dm/asdagroceries/5449000051547_T1",
        "Full Pepsi": "TODO",
        "Fanta Fruit Twist": "TODO",
        "Sprite": "TODO",
        "Pepsi Max": "TODO",
        "Lilt": "TODO",
        "Emerge Energy Drink": "TODO",
    }
    batches = {
        "1": {"name": 1, "price": 50, "expiry": "2021-06-30"},
        "2": {"name": 3, "price": 70, "expiry": "2021-02-30"},
        "3": {"name": 4, "price": 80, "expiry": "2021-01-28"},
        "4": {"name": 5, "price": 50, "expiry": "2020-11-30"},
        "5": {"name": 6, "price": 50, "expiry": "2020-10-28"},
        "6": {"name": 7, "price": 50, "expiry": "2020-09-30"},
        "7": {"name": 8, "price": 50, "expiry": "2020-09-28"},
        "8": {"name": 9, "price": 50, "expiry": "2020-09-28"},
    }
    cans = {
        "0": "0",
        "1": "1",
        "2": "2",
    }
    conn = sqlite3.connect('shop.db')
    conn.execute("PRAGMA foreign_keys = 1")

    c = conn.cursor()
    c.executescript(open("setup.sql").read())
    conn.commit()

    for name, image in images.items():
        #print(f"INSERT INTO types (name, image) VALUES ({name}, {image})")
        conn.execute("INSERT INTO types (name, image) VALUES (?, ?)", (name, image))
    for batch in batches.values():
        #print(f"INSERT INTO batches (type, expiry, price) VALUES ({batch['name']}, {batch['expiry']}, {batch['price']})")
        conn.execute("INSERT INTO batches (type, expiry, price) VALUES (?, ?, ?)", (batch['name'], batch['expiry'], batch['price']))
    x = 1
    for can in range(x, x+2):  # Dr Peppers x 2
        conn.execute("INSERT INTO cans (batch) VALUES (?)", (1,))
        x += 1
    for can in range(x, x+60):  # Full Coke x 60
        conn.execute("INSERT INTO cans (batch) VALUES (?)", (2,))
        x += 1
    for can in range(x, x+15):  # Full Pepsi x 15
        conn.execute("INSERT INTO cans (batch) VALUES (?)", (3,))
        x += 1
    for can in range(x, x+20):  # Fanta Fruit Twist x 20
        conn.execute("INSERT INTO cans (batch) VALUES (?)", (4,))
        x += 1
    for can in range(x, x+24):  # Sprite x 24
        conn.execute("INSERT INTO cans (batch) VALUES (?)", (5,))
        x += 1
    for can in range(x, x+27):  # Pepsi Max x 27
        conn.execute("INSERT INTO cans (batch) VALUES (?)", (6,))
        x += 1
    for can in range(x, x+9):  # Lilt x 9
        conn.execute("INSERT INTO cans (batch) VALUES (?)", (7,))
        x += 1
    for can in range(x, x+15):  # Emerge Energy Drink x 15
        conn.execute("INSERT INTO cans (batch) VALUES (?)", (8,))
        x += 1
    conn.commit()

    conn.close()

def main():
    conn = sqlite3.connect('shop.db')
    conn.execute("PRAGMA foreign_keys = 1")

    for can, batch in conn.execute("SELECT can, batch FROM cans").fetchall():
        page = f"""<!DOCTYPE html><meta http-equiv="refresh" content="0; url=../B/{batch}.html">""".strip()
        open(f"C\\{can}.html", "w").write(page)

    for batch, name, price, expiry, image in conn.execute("SELECT batch, name, price, expiry, image FROM batches INNER JOIN types t on batches.type = t.type").fetchall():
        floatprice = float(price) / 100
        page = f"""<!DOCTYPE html>    
<title>Shop</title>
<p>This is the product page for {name}
<p>It costs &#163;{price:.2f} and they expire on {expiry}
<p><img src="{image}" alt="Can Image">""".strip()
        open(f"B\\{batch}.html", "w").write(page)

    conn.close()


# Run the main program
if __name__ == "__main__":
    setup_database()
    main()
