class Scraper():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    def get_formatted_url(self) -> str:
        """Returns the formatted url from given function parameters

        Returns:
            str: Formatted URL
        """
        pass

    def _get_results(self) -> dict:
        """Returns a dictionary containing all the scraped records"""
        pass

    def export(self) -> None:
        """Saves records into a proper csv file"""
        pass