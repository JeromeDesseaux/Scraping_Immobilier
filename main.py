from scrapers.lbc import LBCScraper
from enums.homes import HomeType

if __name__ == "__main__":
    lbc_scraper = LBCScraper(home_type=HomeType.HOME, category=9, location=76230, price=(0, 350000))
    lbc_scraper.export()