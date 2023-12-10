import pandas as pd

def calculate_distance_matrix(df)->pd.DataFrame():
    """
    Calculate a distance matrix based on the dataframe, df.
    Args:
        df (pandas.DataFrame)
        
    Returns:
        pandas.DataFrame: Distance matrix
    """
    return df.pivot(index='id_1', columns='id_2', values='distance')

def unroll_distance_matrix(df)->pd.DataFrame():
    """
    Unroll a distance matrix to a DataFrame in the style of the initial dataset.
    Args:
        df (pandas.DataFrame)
        
    Returns:
        pandas.DataFrame: Unrolled DataFrame containing columns 'id_start', 'id_end', and 'distance'.
    """
    df = df.stack().reset_index()
    df.columns = ['id_start', 'id_end', 'distance'] 
    return df

def find_ids_within_ten_percentage_threshold(df, reference_id)->pd.DataFrame():
    """
    Find all IDs whose average distance lies within 10% of the average distance of the reference ID.
    Args:
        df (pandas.DataFrame)
        reference_id (int)
        
    Returns: 
        pandas.DataFrame: DataFrame with IDs whose average distance is within the specified percentage threshold 
        of the reference ID's average distance.
    """
    ref_dist = df[df['id_start'] == reference_id]['distance'].mean()
    threshold = ref_dist * 0.1
    ids = df.groupby('id_start')['distance'].mean()
    ids = ids[(ids > ref_dist - threshold) & (ids < ref_dist + threshold)].index.tolist()
    return df[df['id_start'].isin(ids)]

def calculate_toll_rate(df)->pd.DataFrame():
    """
    Calculate toll rates for each vehicle type based on the unrolled DataFrame.
    Args:
        df (pandas.DataFrame)
        
    Returns:
        pandas.DataFrame
    """
    rates = {'car': 0.1, 'bus': 0.2, 'truck': 0.5}
    df['toll_rate'] = df['vehicle_type'].map(rates)
    return df

def calculate_time_based_toll_rates(df)->pd.DataFrame():
    """
    Calculate time-based toll rates for different time intervals within a day.
    Args:
        df (pandas.DataFrame)
        
    Returns:
        pandas.DataFrame
    """
    rates = {0: 0.5, 6: 1, 12: 1.5, 18: 1, 24: 0.5}
    df['hour'] = df['time'].dt.hour
    df['toll_rate'] = df['hour'].map(rates)
    return df
