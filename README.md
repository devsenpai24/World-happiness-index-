World Happiness Index Analysis
Overview

This project demonstrates data cleaning, exploration, and basic visualization of country-level happiness data using Python, Pandas, NumPy, and Matplotlib.
It focuses on understanding relationships between Ladder Score and GDP per capita.

Features

Inspect and explore dataset (head(), info(), describe(), missing values).

Compute NumPy statistics: mean, median, standard deviation, min, max for Ladder Score.

Clean data: remove extra spaces in column names, handle missing values.

Normalize Log GDP per capita to 0–1 (GDP Normalized).

Ready for visualization with histograms and scatter plots.

GDP Normalization

Normalization scales GDP values between 0 and 1 for easier comparison:

GDP Normalized
=
GDP value
−
Min GDP
Max GDP
−
Min GDP
GDP Normalized=
Max GDP−Min GDP
GDP value−Min GDP
	​


0 → lowest GDP, 1 → highest GDP

NaN values remain unchanged

Example:

Country	Log GDP per capita	GDP Normalized
A	10.5	0.625
B	12.0	1.0
C	8.0	0.0
Installation

Install required Python libraries:

pip install pandas numpy matplotlib

Usage

Place your dataset CSV (dev.csv) in the project folder.

Run the Python script:

python your_script_name.py


The script outputs:

Cleaned data preview

Ladder Score statistics

GDP Normalized column

Visualization-ready DataFrame
