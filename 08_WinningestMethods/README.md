# Chapter 8: Winningest Methods in Time Series Forecasting
In previous sections, we examined several models used in time series forecasting such as ARIMA, VAR, and Exponential Smoothing methods. While the main advantage of traditional statistical methods is their ability to perform more sophisticated inference tasks directly (e.g. hypothesis testing on parameters, causality testing), they usually lack predictive power because of their rigid assumptions. That is not to say that they are necessarily inferior when it comes to forecasting, but rather they are typically used as performance benchmarks.

In this section, we demonstrate several of the fundamental ideas and approaches used in recent forecasting competitions where challengers from all over the world competed in building time series forecasting models for both accuracy and uncertainty prediction tasks.



## Chapter Structure:
The chapter introduces different forecasting techniques with focus on non-parameteric methods in the (Subsection 1)`lightgbm_m5_forecasting.ipynb` notebook. This is further supplemented by demonstrations on how such techniques are used in a different data set (Subsection 2)`lightgbm_jena_forecasting.ipynb`, in tuning (Subsection 3) `lightgbm_m5_tuning.ipynb`. Another section (Subsection 4) `hierarchical_forecasting.ipynb` is included to discuss techniques specific to hierarchical forecasting pursuits  (e.g., M5 competition).


## Mini-competition Structure
The reset of the chapter is designed as a mini-competition. Each competition (currently only M5) is assigned a directory where the following are included:

1. `README.md` - that briefly describes the competition, and data sources.
2. `Leaderboards Notebook` - each competition subdirectory provided with a leaderboards notebook to facilitate performance comparison.
2. `Entries` - this directory may contain the following:
    * `README.md` - (required) to provide a brief description of the entry as well as details on how to navigate through the files provided.
    * `Notebook` - (required) 1 or more notebook that supports the reported WRMSSE scores in the leaderboards section of the competition.
    * `trained_models` - (not required) included in .gitignore, this folder contains re-trained models on best paramters.
    * `predictions` - (not required) included in .gitignore, this folder contains the resulting predictions. 
    * `tuning` - (not required) included in .gitignore, this folder contains files used in tuning. Such as `.db` files for optuna experiments
    * `utils.py` (required) which contains functions that are useful for the specific competition.
    * `PATHS.py` (not required) which contains file paths used in the Notebooks.