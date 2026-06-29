from infrastructure.scrapers.inria_scraper import InriaScraper


def test_debug_html():

    scraper = InriaScraper()

    document = scraper._fetch_document()

    selectors = [
        "article",
        ".offer",
        ".job",
        ".job-item",
        ".card",
        ".list-group-item",
        "li",
        "tr",
        "div",
    ]

    for selector in selectors:
        print(selector, len(document.css(selector)))

    with open("debug_inria.html", "w", encoding="utf-8") as f:
        f.write(document.html)