import json

from qrcodegen import QrCode, QrSegment

def base36encode(number):
    alphabet, base36 = ['0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', '']
    while number:
        number, i = divmod(number, 36)
        base36 = alphabet[i] + base36
    return base36 or alphabet[0]

def main() -> None:
    images = {
        "Dr Pepper": "https://ui.assets-asda.com/dm/asdagroceries/5449000060501_T1",
        "Coke Zero": "https://ui.assets-asda.com/dm/asdagroceries/5449000031341_T1",
        "Full Coke": "https://ui.assets-asda.com/dm/asdagroceries/5449000051547_T1",
    }
    batches = {
        "0": {"name": "Dr Pepper", "price": 0.55, "expiry": "2021-06-30"},
        "1": {"name": "Coke Zero", "price": 0.50, "expiry": "2020-06-30"},
        "2": {"name": "Full Coke", "price": 0.60, "expiry": "2021-02-28"},
    }
    cans = {
        "0": "0",
        "1": "1",
        "2": "2",
        "4": "2",
        "5": "2",
    }
    for i in range(100):
        cans[str(i)] = "2"
        
    tracks = {}
    for can, batch in cans.items():
        tracks[can] = batches[batch]
    open("prices.json", "w").write(json.dumps(tracks))
    
    for can, batch in cans.items():
        encoded_can = base36encode(int(can))
        page = f"""<!DOCTYPE html><meta http-equiv="refresh" content="0; url=../B/{batch}.html">""".strip()
        open(f"C\\{encoded_can}.html", "w").write(page)
        
        segs = [
            QrSegment.make_alphanumeric("FAIRBAIRN.XYZ/C/" + encoded_can),
            #QrSegment.make_alphanumeric("FAIRBAIRN.XYZ/C/"),
            #QrSegment.make_numeric(str(can))
            ]
        qr = QrCode.encode_segments(segs, QrCode.Ecc.LOW)
        open(f"codes\\{encoded_can}.svg", "w").write(qr.to_svg_str(4))

    for batch, details in batches.items():
        page = f"""
<html>    
  <head>      
    <title>Can Shop</title>
  </head>    
  <body> 
    <p>This is the product page for {details['name']}</p>
    <p>It costs &#163;{details['price']:.2f} and they expire on {details['expiry']}</p>
    <p><img src="{images[details['name']]}"><img></p>
  </body>  
</html>""".strip()
        open(f"B\\{batch}.html", "w").write(page)

# Run the main program
if __name__ == "__main__":
    main()
