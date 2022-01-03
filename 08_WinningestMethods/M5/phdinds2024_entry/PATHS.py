import os

data_root = '../../..'
data_dir = 'data/M5_dataset'

train_path = os.path.join(data_root, data_dir, 'sales_train_evaluation.csv')
test_path = os.path.join(data_root, data_dir, 'sales_test_evaluation.csv')
prices_path = os.path.join(data_root, data_dir, 'sell_prices.csv')
calendar_path = os.path.join(data_root, data_dir, 'calendar.csv')
weights_path = os.path.join(data_root, data_dir, 'weights_evaluation.csv')

results_root = '.'
tuning = os.path.join(results_root, 'tuning')
predictions = os.path.join(results_root, 'predictions')
trained_models = os.path.join(results_root, 'trained_models')
# proportions_ref =