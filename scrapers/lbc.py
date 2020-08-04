import requests
import bs4
import re

from enums.homes import HomeType
from typing import Type, Tuple, List, Optional
from .scraper import Scraper
import pandas as pd


class LBCScraper(Scraper):
    def __init__(self, home_type: Type[HomeType], location: int, category: int, price: Tuple[int, int]):
        self.home_type = home_type.value
        self.location = location
        self.category = category
        self.price_min = price[0] if price[0] is not 0 else 'min'
        self.price_max = price[1]

    def _get_formatted_url(self) -> str:
        URL: str = f"""
                https://www.leboncoin.fr/recherche/?
                category={self.category}&
                locations={self.location}&
                real_estate_type={self.home_type}&
                price={self.price_min}-{self.price_max}
            """
        return re.sub(r'\s*\n\s*', '', URL)

    def get_results(self) -> List[dict]:
        result = requests.get(self._get_formatted_url(), headers=self.headers)
        soup = bs4.BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all("li", {"class":"_3DFQ-"})
        res = []
        for result in results:
            res.append({
                'title': result.find('p', {'class': '_2tubl'}).getText(),
                'price': int(result.find('span', {'class': '_1JRvz'}).getText().replace('€', '').replace(' ', ''))
            })
        return res

    def export(self, path: Optional[str] = './leboncoin.csv') -> None:
        res = self.get_results()
        df = pd.DataFrame(res)
        df.to_csv(path)
        print(f'[SUCCES] Résultats LEBONCOIN écrits avec succès dans le fichier {path}')

