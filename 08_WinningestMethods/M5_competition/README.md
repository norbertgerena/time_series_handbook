# Welcome to the M5 Competition (PhDinDS Version)

This subsection of `Chapter 8: Winningest Methods` highlights entries of the PhD in Data Science students of Asian Institute of Management to the M5 Accuracy Competition which compared perfromances of various techniques in time series forecasting to accurately predict the next `28` days of Unit Sales of Walmart. Such is a hierarchical forecasting challenge where time series of counts are presented in `12` aggregation levels, *see table below*.

| Level id | Level description                                                    | Aggregation level | Number of series |
|----------|----------------------------------------------------------------------|-------------------|------------------|
| 1        | Unit sales of all products, aggregated for all stores/states         | Total             | 1                |
| 2        | Unit sales of all products, aggregated for each State                | State             | 3                |
| 3        | Unit sales of all products, aggregated for each store                | Store             | 10               |
| 4        | Unit sales of all products, aggregated for each category             | Category          | 3                |
| 5        | Unit sales of all products, aggregated for each department           | Department        | 7                |
| 6        | Unit sales of all products, aggregated for each State and category   | State-Category    | 9                |
| 7        | Unit sales of all products, aggregated for each State and department | State-Department  | 21               |
| 8        | Unit sales of all products, aggregated for each store and category   | Store-Category    | 30               |
| 9        | Unit sales of all products, aggregated for each store and department | Store-Department  | 70               |
| 10       | Unit sales of product i, aggregated for all stores/states            | Product           | 3,049            |
| 11       | Unit sales of product i, aggregated for each State                   | Product-State     | 9,147            |
| 12       | Unit sales of product i, aggregated for each store                   | Product-Store     | 30,490           |
| Total    |                                                                      |                   | 42,840           |

The series and supporting information needed for this competition are contained in the following files:

| Filename | Description | Columns |
|---|---|---|
| calendar.csv | Information on each day spanning the entire dataset (from training to evaluation) specific to indicators of day of week, month, year, holiday events (`event_name` columns) and sales promotions events (`snap_` columns).  Daily granularity. | wm_yr_wk (e.g., 11101), weekday (e.g., Saturday), wday (e.g., 1), month (e.g., 1), year (e.g., 2011), event_name_1 etc, snap_CA etc. |
| sales_test_evaluation.csv | Final evaluation set used in the competition (merely for practice, actual results were based on `sales_test_evaluation.csv`). Contains ids that map to state, store, category, department, and item. Each series has 28 days of unit sales data that follow the last day of `sales_train_evaluation.csv`. | ids, `d_1941` to `d_1969` |
| sales_test_validation.csv | Preliminary evaluation set used in the competition (merely for practice, actual results were based on `sales_test_evaluation.csv`). Contains ids that map to state, store, category, department, and item. Each series has 28 days of unit sales data that follow the last day of `sales_train_validation.csv`. | ids, `d_1914` to `d_1941` |
| sales_train_evaluation.csv | Final training data containing ids that map to state, store, category, department, and item. Each series has 1941 days of unit sales data because of the appended validation set. | ids, `d_1` to `d_1941` |
| sales_train_validation.csv | Initial/Preliminary training data containing ids that map to state, store, category, department, and item. Each series has 1913 days of unit sales data. | ids, `d_1` to `d_1913` |
| sell_prices.csv | Weekly sell prices at store_id-item_id aggregation level, level 12. These can be used as exogenous variables that may improve model performance. | store_id (e.g., CA_1), item_id (e.g., HOBBIES_1_001), wm_yr_wk (e.g., 11325), sell_price (9.58) |
| weights_evaluation.csv | Final importance of every series in each aggregation level as determined by the `weight` column of this dataframe. These weights are used in calculating the WRMSSE of an entry model (forecaster). | Level_id (e.g., Level12), Agg_Level_1 (e.g., HOBBIES_1_001), Agg_Level_2 (e.g., CA_1), Dollar_Sales (e.g., 276.54), weight (e.g., 0.000071) |
| weights_validation.csv | Preliminary importance of every series in each aggregation level as determined by the `weight` column of this dataframe. These weights are used in calculating the WRMSSE of an entry model (forecaster). | Level_id (e.g., Level12), Agg_Level_1 (e.g., HOBBIES_1_001), Agg_Level_2 (e.g., CA_1), Dollar_Sales (e.g., 224.94), weight (e.g., 0.000060) |

These files can be found in the the `data/M5_dataset` directory of this repo.


## Competition Mechanics

### Metrics and Evaluation : *Begin with the end in mind*
As with the original M5 competition, the objective is to minimize the forecasting error--measured by the Weighted Root Mean-Squared Scaled Error (RMSSE). This metric scales the usual root mean-squared error and aggregates the forecasting error of all the 42,840 forecasts (1 per series) in a weighted manner. These weights are provided by the `M5 Competition` and are based on the Dollar amount of sales for each of the 42,840 series. *Care must be taken into account in evaluating the results due to differences in `weights_evaluation.csv` and `weights_validation.csv`--differences are due to live updating of the proportion dollar amount of sales in the days that followed*. The former SHOULD be used in evaluating the final (entry) forecasts' WRMSSE while the latter for tuning the model--for entries that use WRMSSE as a tuning objective.

*Honor Code: Unlike the original M5 competition, the evaluation set (last 28-day actual data) is already made available to entrants--mainly because M5 is already finished. While it is tempting to fit forecasting performance to the actual evaluation set, DO NOT, as this defeats the purpose of the competition.*


### Leaderboards
For easy comparison, the leaderboards and competition benchmarks are already presented as a markdown table in `M5_phdinds_leaderboards.ipynb`. Entrants may update the results with their own scores and method descriptions, supported by a full discussion of their entry similar to the `phdinds2024_entry` directory. Entries are expected to provide code that supports the reported WRMSSE in the leaderboards notebook. Ideally, this chapter will serve as a compilation of practical considerations, and best practices in forecasting sales data--and other similar time series of counts.


### M5 Winningest Methods and Benchmarks



### Other Competition Details



### References


