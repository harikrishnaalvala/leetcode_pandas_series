import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    result = orders['customer_number'].value_counts().reset_index()
    result.columns = ['customer_number', 'order_count']
    
    if not result.empty:
        # Find the customer with the largest number of orders
        largest_customer = result.iloc[0]
        
        # Create a DataFrame with a single column 'customer_number' containing the largest customer number
        result_table = pd.DataFrame({'customer_number': [largest_customer['customer_number']]})
    else:
        # If the result DataFrame is empty, create an empty DataFrame
        result_table = pd.DataFrame(columns=['customer_number'])
    
    return result_table
