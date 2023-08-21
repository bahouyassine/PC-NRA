from EbayScraper import EbayScraper

# Create an instance of the EbayScraper class
scraper = EbayScraper()


# Call the search_price method with the product you want to search
search_term = "dell latitude E7450 i5"
num_pages = 5


# Call the _save_to_file method
items = scraper._get_items(f"{scraper.base_url}?_nkw={search_term.replace(' ', '+')}&_pgn={num_pages}")
