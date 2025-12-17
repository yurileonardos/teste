from bs4 import BeautifulSoup


PRICE_KEYS = ["preço", "valor", "unitário", "total", "r$"]


def remove_price_columns(html):
    soup = BeautifulSoup(html, "html.parser")

    for table in soup.find_all("table"):
        rows = table.find_all("tr")
        if not rows:
            continue

        headers = rows[0].find_all(["th", "td"])
        price_indexes = []

        for i, h in enumerate(headers):
            txt = h.get_text(strip=True).lower()
            if any(k in txt for k in PRICE_KEYS):
                price_indexes.append(i)

        if not price_indexes:
            continue

        for row in rows:
            cells = row.find_all(["th", "td"])
            for i in sorted(price_indexes, reverse=True):
                if i < len(cells):
                    cells[i].decompose()

    return str(soup)
