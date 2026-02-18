import pandas as pd

orders = pd.read_excel("C:/Users/maria.verdu/Desktop/p1/data/raw/orders.xlsx", parse_dates=['OrderDate'])
order_items = pd.read_excel("C:/Users/maria.verdu/Desktop/p1/data/raw/order_items.xlsx")
customers = pd.read_excel("C:/Users/maria.verdu/Desktop/p1/data/raw/customers.xlsx", parse_dates=['SignUpDate'])
customer_segments = pd.read_excel("C:/Users/maria.verdu/Desktop/p1/data/raw/customer_segments.xlsx")
products = pd.read_excel("C:/Users/maria.verdu/Desktop/p1/data/raw/products.xlsx")
product_inventory = pd.read_excel("C:/Users/maria.verdu/Desktop/p1/data/raw/product_inventory.xlsx")
product_returns = pd.read_excel("C:/Users/maria.verdu/Desktop/p1/data/raw/product_returns.xlsx", parse_dates=['ReturnDate'])
marketing_campaigns = pd.read_excel("C:/Users/maria.verdu/Desktop/p1/data/raw/marketing_campaigns.xlsx", parse_dates=['StartDate','EndDate'])
campaign_performance = pd.read_excel("C:/Users/maria.verdu/Desktop/p1/data/raw/campaign_performance.xlsx", parse_dates=['Date'])
email_log = pd.read_excel("C:/Users/maria.verdu/Desktop/p1/data/raw/email_marketing_log.xlsx", parse_dates=['SentDate'])

# Data cleaning
orders.drop_duplicates(inplace=True)
order_items.drop_duplicates(inplace=True)
customers.drop_duplicates(inplace=True)
customer_segments.drop_duplicates(inplace=True)
products.drop_duplicates(inplace=True)

orders.fillna({'TotalAmount':0, 'OrderStatus':'Unknown'}, inplace=True)
order_items.fillna({'Quantity':0, 'PricePerUnit':0}, inplace=True)
products.fillna({'UnitPrice':0}, inplace=True)
customers.fillna({'City':'Unknown', 'Country':'Unknown'}, inplace=True)

# dim_customer
dim_customer = customers.merge(customer_segments, on='CustomerID', how='left')
dim_customer = dim_customer[['CustomerID','FullName','Email','SignUpDate','City','Country','SegmentName']]

# dim_product
dim_product = products.merge(product_inventory.groupby('ProductID')['StockQuantity'].sum().reset_index(),
                             on='ProductID', how='left')
dim_product = dim_product[['ProductID','ProductName','Category','Brand','UnitPrice','StockQuantity']]

# dim_date
all_dates = pd.date_range(start=orders['OrderDate'].min(), end=orders['OrderDate'].max())
dim_date = pd.DataFrame({'Date': all_dates})
dim_date['Year'] = dim_date['Date'].dt.year
dim_date['Month'] = dim_date['Date'].dt.month
dim_date['Day'] = dim_date['Date'].dt.day
dim_date['Weekday'] = dim_date['Date'].dt.day_name()

# dim_campaign
dim_campaign = marketing_campaigns[['CampaignID', 'CampaignName', 'Channel', 'StartDate', 'EndDate', 'Budget']].drop_duplicates()

# Fact sales
fact_sales = order_items.merge(orders[['OrderID','CustomerID','OrderDate','TotalAmount']], on='OrderID', how='left')
fact_sales = fact_sales.merge(products[['ProductID','ProductName','Category']], on='ProductID', how='left')

# Include returns
returns = product_returns.groupby('OrderID')['ProductID'].count().reset_index().rename(columns={'ProductID':'Returns'})
fact_sales = fact_sales.merge(returns, on='OrderID', how='left')
fact_sales['Returns'] = fact_sales['Returns'].fillna(0)

# Marketing KPIs
fact_sales = fact_sales.merge(email_log[['CustomerID','CampaignID']], on='CustomerID', how='left')
fact_sales = fact_sales.merge(marketing_campaigns[['CampaignID','CampaignName']], on='CampaignID', how='left')

fact_sales['Revenue'] = fact_sales['Quantity'] * fact_sales['PricePerUnit']
fact_sales['ReturnRate'] = fact_sales['Returns'] / fact_sales['Quantity']

# Save processed tables
dim_customer.to_csv("C:/Users/maria.verdu/Desktop/p1/data/processed/dim_customer.csv", index=False)
dim_product.to_csv("C:/Users/maria.verdu/Desktop/p1/data/processed/dim_product.csv", index=False)
dim_date.to_csv("C:/Users/maria.verdu/Desktop/p1/data/processed/dim_date.csv", index=False)
dim_campaign.to_csv("C:/Users/maria.verdu/Desktop/p1/data/processed/dim_campaign.csv", index=False)
fact_sales.to_csv("C:/Users/maria.verdu/Desktop/p1/data/processed/fact_sales.csv", index=False)


