# Chapter 8: Winningest Methods in Time Series Forecasting
In previous sections, we examined several models used in time series forecasting such as ARIMA, VAR, and Exponential Smoothing methods. While the main advantage of traditional statistical methods is their ability to perform more sophisticated inference tasks directly (e.g. hypothesis testing on parameters, causality testing), they usually lack predictive power because of their rigid assumptions. That is not to say that they are necessarily inferior when it comes to forecasting, but rather they are typically used as performance benchmarks.

In this section, we demonstrate several of the fundamental ideas and approaches used in recent forecasting competitions where challengers from all over the world competed in building time series forecasting models for both accuracy and uncertainty prediction tasks.

## Chapter Structure:
This section is designed as a mini-competition. Each competition (currently only M5) is assigned a directory where the following are included:

1. `README.md` - that briefly describes the competition, and data sources.
2. `Notebooks` - to describe the forecasting concepts used in the competition. (e.g., for M5--hierarchical time series forecasting)
3. `Entries` - this directory contains the following:
    * `Leaderboards Notebook` - an interactive notebook that displays the current rankings of entries along with published competition benchmarks and winning scores.
    * `Entry Subdirectory` - each subdirectory is labeled with the author of the entry (e.g., `PhD2024_ThomasShelby`). Entries should contain a notebook
    * `predictions` - a directory containing the predictions of each entry (subdirectories are named according to author). This is accessed by the the `Leaderboards Notebook` when reporting the current leaderboards.
4. `utils.py` which contains functions that are useful for the specific competition.