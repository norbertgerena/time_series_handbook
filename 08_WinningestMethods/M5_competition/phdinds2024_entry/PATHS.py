import os

# data_root = '../../..'
data_root = '~/time_series_handbook'
raw_data_dir = 'data/m5/raw'

train_path = os.path.join(data_root, raw_data_dir, 'sales_train_evaluation.csv')
test_path = os.path.join(data_root, raw_data_dir, 'sales_test_evaluation.csv')
prices_path = os.path.join(data_root, raw_data_dir, 'sell_prices.csv')
calendar_path = os.path.join(data_root, raw_data_dir, 'calendar.csv')
weights_eval_path = os.path.join(data_root, raw_data_dir, 'weights_evaluation.csv')
weights_val_path = os.path.join(data_root, raw_data_dir, 'weights_validation.csv')

results_dir = '.'
tuning = os.path.join(results_dir, 'tuning')
predictions = os.path.join(results_dir, 'predictions')
trained_models = os.path.join(results_dir, 'trained_models')

processed_data_dir = 'data/m5/processed'
proportions_reference = os.path.join(data_root, processed_data_dir, 'proportions_reference.csv')