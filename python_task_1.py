import pandas as pd

def generate_car_matrix(df)->pd.DataFrame:
    """
    Creates a DataFrame for id combinations.
    Args:
        df (pandas.DataFrame)
        
    Returns:
        pandas.DataFrame: Matrix generated with 'car' values, 
        where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    return df.pivot(index='id_1', columns='id_2', values='car')

def get_type_count(df)->dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.
    Args: 
        df (pandas.DataFrame)
        
    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    return df['car'].value_counts().to_dict()

def get_bus_indexes(df)->list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.
    Args:
        df (pandas.DataFrame)
        
    Returns: 
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    mean = df['bus'].mean()
    return df[df['bus'] > 2*mean].index.tolist()

def filter_routes(df)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.
    Args:
        df (pandas.DataFrame)
        
    Returns:
        list: List of route names with average 'truck' values greater than 7. 
    """
    return df.groupby('route')['truck'].mean()[df.groupby('route')['truck'].mean() > 7].index.tolist()

def multiply_matrix(matrix)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.
    Args:
        matrix (pandas.DataFrame)
        
    Returns: 
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    matrix = matrix.copy()
    matrix[matrix%2 == 0] *= 2
    matrix[matrix%3 == 0] *= 3 
    return matrix

def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period
    
    Args:
        df (pandas.DataFrame)
        
    Returns:
        pd.Series: return a boolean series  
    """
    grouped = df.groupby(['id_1', 'id_2'])
    hour_range = grouped['hour'].nunique() == 24
    day_range = grouped['day'].nunique() == 7
    return pd.Series([all(hour_range), all(day_range)], index=['hour_covered', 'day_covered'])
