import pandas as pd


def join_data():
    orders = pd.read_csv('orders_data')
    customers = pd.read_csv('customers_data')
    order_count_by_customer = orders.\
        join(customers.set_index('order_customer_id'),
             on='customer_id',
             how='inner').\
        groupby('customer_id').\
        agg(['count']).\
        rename(columns={'count': 'order_count'})
    order_count_by_customer.to_csv('target_dir')
    return
