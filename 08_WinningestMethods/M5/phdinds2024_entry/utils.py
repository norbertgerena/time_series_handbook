"""Utility funcitons used for consumption forecasting.
Functions are specific to the preparation of inputs in
a Multioutput Regression approach.

BY: Mike Dorosan and Basti Ibañez
DATE: Dec 2021
"""

import pandas as pd
import numpy as np


def create_calendar_cols(dataframe, date_col='Date'):
    """Create new calendar categorical columns from a datetime-like series
    
    Note: Current functionality is specific to MWCI monthly consumption data.
    """
    
    if not dataframe[date_col].dtype == '<M8[ns]':
        dataframe[date_col] = pd.to_datetime(dataframe[date_col])
    
    # Add other calendar cols depending on datetime granularity
    dataframe['month'] = dataframe[date_col].dt.month
    dataframe['year'] = dataframe[date_col].dt.year
    
    return dataframe

# not used
def ohe_cat_cols(dataframe, cat_cols):
    """One-hot encode categorical columns
    
    Parameters
    ----------
    dataframe : pd.DataFrame
        input dataframe for OHE
    cat_cols : str list
        list of categorical column labels to OHE
    
    Returns
    ----------
    dataframe : pd.DataFrame
        updated dataframe after OHE
    dummy_cat_cols : str list
        list of newly created suffixed dummy columns
    """
    old_cols = dataframe.columns.to_list()
    df_cat_cols = dataframe[cat_cols]
    dataframe = pd.get_dummies(dataframe, columns=cat_cols)
    dataframe = pd.concat([dataframe, df_cat_cols], axis=1)
    dummy_cat_cols = set(dataframe.columns.to_list()) - set(old_cols)
    return dataframe, list(dummy_cat_cols)

def _restructure(arr, lookback=1, step=1, delay=0):
    """Restructure arr based on lookback, step, and delay
    
    Parameters
    ----------
    look_back : int
        lookback window
    step : int
        n-step forecasts (one-step or multi-step forecasts)
    delay : int
        gap from end of lookback array to beginning of the prediction horizon
        
    Return
    ----------
    X, Y : tuple
        feature and target arrays for an ML prediction problem.
    """
    x_data, y_data = [], []

    for i in range(len(arr) - lookback - step - delay + 1):
        x_temp = arr[i: i + lookback]
        x_data.append(x_temp)
        y_data.append(arr[i + lookback + delay : i + lookback + delay + step])
    
    return np.array(x_data), np.array(y_data)

def create_dataset(dataset, endo, exo_num=None, exo_cat=None, lookback=6, step=6, 
                   delay=0, 
                   lookback_endo=True, 
                   lookback_exo_num=True, lookahead_exo_num=False, 
                   lookback_exo_cat=False, lookahead_exo_cat=True):
    """Create dataset for n-step forecasting. If categorical exogenous
    variables are used, only the prediction horizon is tagged with these
    (i.e., 'for what month are prediciting?', 'for which DMA?').
    
    Parameters
    ----------
    dataset : pd.DataFrame
        dataframe of exo and endogenous variables, 
        rows are sorted chronologically (start to end)
    endo : str
        col name of endogenous data to forecast
    exo_num : str list, default None
        col name/s of exogenous numerical columns used in forecasting
    exo_cat: str list, default None
        categorical exogenous cols (indicator variables, month, holiday etc)
    lookback : int
        lookback window
    step : int
        n-step forecasts (one-step or multi-step forecasts)
    delay : int
        gap from end of lookback array to beginning of the prediction horizon
    lookback_endo : bool, default=False
        If True, use lookback endogenous data as predictors. Otherwise, use
        exogenous data only.
    lookback_exo_num : bool, default=True
        If True, use lookback exo num data
    lookahead_exo_num : bool, default=False
        If True, use lookahead (step) exo num data
    lookback_exo_cat : bool, default=False
        If True, use lookback exo cat data
    lookahead_exo_cat : bool, default=True
        If True, use lookahead (step) exo cat data
   
    Returns
    ----------
    predictors, target, cat_cols_indices: tuple
        Restructured dataset for machine learning, and categorical columns indices
    """
    # create variables list
    if bool(exo_num):
        if bool(exo_cat):
            variables = [endo] + sorted(exo_num) + sorted(exo_cat)
        else:
            variables = [endo] + sorted(exo_num) # fixed bug variables = [endo] = exo_num
    else:
        if bool(exo_cat):
            variables = [endo] + sorted(exo_cat)
        else:
            variables = [endo]
    
    # exo num array list
    exo_num_step_arr_list = []
    exo_num_lookback_arr_list = []
    
    # exo cat array list
    exo_cat_step_arr_list = []
    exo_cat_lookback_arr_list = []
    
    for var in variables:
        lookback_arr, step_arr = _restructure(dataset[var], lookback, step, delay)
        
        # target feature
        if var==endo: 
            targets = step_arr
            target_lookback = lookback_arr
            
        # exo num feature
        elif bool(exo_num) and var in exo_num: 
            exo_num_step_arr_list.append(step_arr)
            exo_num_lookback_arr_list.append(lookback_arr)
            
        # cat feature
        else: 
            exo_cat_step_arr_list.append(step_arr)
            exo_cat_lookback_arr_list.append(lookback_arr)
            
    # predictors default to None
    cat_cols_indices = []
    predictors = None
    
    if lookback_endo:
        predictors = target_lookback 
    
    if lookahead_exo_cat:
        temp_lookahead_exo_cat = np.concatenate(exo_cat_step_arr_list, axis=1)
        if predictors is None:
            predictors = temp_lookahead_exo_cat
            cat_cols_indices += list(range(0, predictors.shape[1]))
        else:
            cat_cols_indices += list(range(predictors.shape[1], predictors.shape[1] +\
                                         temp_lookahead_exo_cat.shape[1]))
            predictors = np.concatenate([predictors, temp_lookahead_exo_cat], axis=1)
    
    if lookback_exo_cat: # lookback on cat features
        temp_lookback_exo_cat = np.concatenate(exo_cat_lookback_arr_list, axis=1)
        if predictors is None:
            predictors = temp_lookback_exo_cat
            cat_cols_indices += list(range(0, predictors.shape[1]))
        else:
            cat_cols_indices += list(range(predictors.shape[1], predictors.shape[1] +\
                                         temp_lookback_exo_cat.shape[1]))
            predictors = np.concatenate([predictors, temp_lookback_exo_cat], axis=1)
        
    if lookahead_exo_num: # lookahead on exo_num features
        temp_lookahead_exo_num = np.concatenate(exo_num_step_arr_list, axis=1)
        if predictors is None:
            predictors = temp_lookahead_exo_num 
        else:
            predictors = np.concatenate([predictors, temp_lookahead_exo_num], axis=1)
        
    if lookback_exo_num: # lookback on exo_num features
        temp_lookback_exo_num = np.concatenate(exo_num_lookback_arr_list, axis=1)
        if predictors is None:
            predictors = temp_lookback_exo_num
        else:
            predictors = np.concatenate([predictors, temp_lookback_exo_num], axis=1)
      
    return predictors, targets, cat_cols_indices

level_indexes = {
    'Level1' : None,
    'Level2': 'state_id', 
    'Level3': 'store_id', 
    'Level4': 'cat_id', 
    'Level5': 'dept_id',
    'Level6': ['state_id', 'cat_id'], 
    'Level7' : ['state_id', 'dept_id'],
    'Level8' : ['store_id', 'cat_id'],
    'Level9' : ['store_id', 'dept_id'],
    'Level10': ['item_id'],
    'Level11': ['state_id', 'item_id'],
    'Level12': ['item_id', 'store_id']
}

def generate_bu(level_id, forecast_df):
    """Return forecasted dataframe of level_id using bottom up approach 
    from a reference forecast dataframe of a bottom aggregation level
    """
    index = level_indexes[level_id]
    if index:
        level_forecasts = forecast_df.groupby(index).sum()
    else:
        level_forecasts = forecast_df.sum().to_frame().T
    return level_forecasts

def get_prop_averages(level_id, prop_reference, T):
    """Returns the proportions of historical averages across a period T"""
    index = level_indexes[level_id]
    if index:
        yjts = prop_reference.groupby(index).sum()
        yts = yjts.sum()
        pjs = ((yjts.sum(axis=1)/T) / (yts/T).sum())
        return pjs
    else:
        raise "Inputted the top-most level. Try again."
        return None
    
def get_ave_proportions(level_id, prop_reference, T):
    """Returns the average historical proportions across a period T"""
    index = level_indexes[level_id]
    if index:
        yjts = prop_reference.groupby(index).sum()
        yts = yjts.sum()
        pjs = yjts.apply(lambda row: (row / yts).sum()/T, axis=1)
        return pjs
    else:
        raise "Inputted the top-most level. Try again."
        return None
    
def generate_td(level_id, forecast_df, method, **kwargs):
    """Return forecasted dataframe of level_id using top_down approach 
    from a reference/base forecast dataframe of a higher aggregation level
    """
    pjs = method(level_id, **kwargs)
    yts = forecast_df.sum()
    index = level_indexes[level_id]
    level_forecasts = yts.apply(lambda x: x*pjs).round().astype(int).T
    return level_forecasts