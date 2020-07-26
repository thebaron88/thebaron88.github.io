import json

from qrcodegen import QrCode, QrSegment


def main() -> None:
    track = {
        "0": {"name": "Dr Pepper", "price": 0.55, "expiry": "2021-06-30"},
        "1": {"name": "Coke Zero", "price": 0.50, "expiry": "2020-06-30"},
        "2": {"name": "Full Coke", "price": 0.60, "expiry": "2021-02-28"},
    }
    open("prices.json", "w").write(json.dumps(track))
    for can, details in track.items():
        page = f"""<!DOCTYPE html><meta http-equiv="refresh" content="0; url=../main.html?C={can}">""".strip()
        open(f"C\\{can}.html", "w").write(page)
        segs = [
            QrSegment.make_alphanumeric("FAIRBAIRN.XYZ/C/"),
            QrSegment.make_numeric(str(can))]
        qr = QrCode.encode_segments(segs, QrCode.Ecc.LOW)
        open(f"codes\\{can}.svg", "w").write(qr.to_svg_str(4))


# Run the main program
if __name__ == "__main__":
    main()
