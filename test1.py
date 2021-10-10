class Myclass:
    def ass2(x):
        z = input("- Choose any crypto here: ")
        url = f'https://coinmarketcap.com/currencies/{z}/news/'
        driver = webdriver.Firefox()
        driver.get(url)
        page = driver.page_source
        page_soup = BeautifulSoup(page, 'html.parser')
        headers = page_soup.findAll("h3", {"class": "sc-1q9q90x-0", "class": "gEZmSc"})
        result = page_soup.findAll("section", "wrapper")
        print(result[0].text)