from EbayScraper import EbayScraper

scraper = EbayScraper()
search_term = "Dell Ultrabook E7450 Core "
num_pages = 5
items = scraper._get_items(f"{scraper.base_url}?_nkw={search_term.replace(' ', '+')}&_pgn={num_pages}")
df = scraper.dataFrame