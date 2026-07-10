# Cloud Cost Forecasting Tool 

## Overview

This tool uses historical monthly cloud cost and commitmemnt data across multiple clouds to provide a forecast of future monthly costs till the end of period provided. The report generated includes information such as the gap from the cloud commitment and growth rate required to meet it, as well as supporting visualisations. The tool uses a method suggestor function to reccommend a forecasting method based on the patterns of the data provided.

## Features

* Upload historical cloud spend data
* Upload cloud commitment data
* Support for multiple cloud providers
* Statistical forecasting methods:
    - Run Rate ( Suggested when < 3 months of data available ) 
    - Moving Average ( Suggested when volatility or no data patterns are detected)
    - Single Exponential Smoothing ( Suggested when overall stable data or a recent level-off are detected )
    - Holt Double Exponential Smoothing ( Suggested when a trend and no volatility are detected )
    - Holt-Winters Triple Exponential Smoothing ( Optional selection from user's end when data exhibits seasonality and > 24 months of data available )
* Optional monthly planned project adjustments
* Gap analysis against commitment
* Required monthly growth rate calculation
* Monthly spend forecast visualisation
* Cumulative spend vs. commitment visualisation
* Save/Load report functionality


## Required Input Files & Format

* Spend Data — csv with the following columns:
  
    `cloud` :	Cloud provider name
  
    `year_month` :	Month in YYYY-MM format
  
    `spend`	: Historical monthly spend

    - Example:
      
          cloud,year_month,spend
          AWS,2025-01,12000
          AWS,2025-02,12500
  
* Commitment Data — csv with the following columns:
  
    `cloud` :	Cloud provider name
  
    `period_start` :	Commitment start date in YYYY-MM format
  
    `period_end` : Commitment end date in YYYY-MM format
  
    `commitment` : Total contracted spend

    - Example:
 
          cloud,period_start,period_end,commitment
          AWS,2025-01,2025-12,180000

## Repository Contents

* `app.py` 
* `validation.py` 
* `forecasting.py` 
* `reporting.py` 
* README
