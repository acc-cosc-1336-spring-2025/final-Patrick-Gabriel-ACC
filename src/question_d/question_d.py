#write functions here, don't add input('') statements here!

# stock_module.py

class Stock:
    
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol

    def get_company_name(self):
        return self.__company_name


def stock_purchase_history():
    # Create stock instances
    stock1 = Stock("AAPL", "Apple Inc")
    stock2 = Stock("CAT", "Caterpillar")
    stock3 = Stock("EK", "Eastman Kodak")
    stock4 = Stock("GOOG", "Google")
    stock5 = Stock("MSFT", "Microsoft")

    # Add to dictionary
    stock_dict = {
        stock1.get_symbol(): stock1.get_company_name(),
        stock2.get_symbol(): stock2.get_company_name(),
        stock3.get_symbol(): stock3.get_company_name(),
        stock4.get_symbol(): stock4.get_company_name(),
        stock5.get_symbol(): stock5.get_company_name()
    }

    # Display the table
    print("Stock Purchase History")
    print(f"{'Symbol':<6}  {'Company Name'}")
    print("-" * 30)
    for symbol, company in stock_dict.items():
        print(f"{symbol:<6}  {company}")
