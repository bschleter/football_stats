#2022 football stats main
import scrapy
import pandas as pd

class StatsSpider(scrapy.Spider):
    name = "stats"
    start_urls = [
        "https://www.pro-football-reference.com/years/2022/passing_advanced.htm",
        "https://www.pro-football-reference.com/years/2022/passing.htm",
        "https://www.pro-football-reference.com/years/2022/rushing.htm",
        "https://www.pro-football-reference.com/years/2022/rushing_advanced.htm",
        "https://www.pro-football-reference.com/years/2022/receiving.htm",
        "https://www.pro-football-reference.com/years/2022/receiving_advanced.htm",
        "https://www.pro-football-reference.com/years/2022/fantasy.htm",
        "https://www.pro-football-reference.com/years/2022/redzone-rushing.htm",
        "https://www.pro-football-reference.com/years/2022/redzone-passing.htm",
        "https://www.pro-football-reference.com/years/2022/redzone-receiving.htm",
        "https://www.pro-football-reference.com/years/2022/advanced.htm",
        "https://www.pro-football-reference.com/years/2022/kicking.htm",
    ]

    def parse(self, response):
        # Extract table data and convert it to a DataFrame
        table = response.css("table").getall()[0]
        df = pd.read_html(table)[0]
        
        # Save DataFrame to a CSV file
        table_id = response.css("table").attrib["id"]
        df.to_csv(f"{table_id}.csv", index=False)
