**DataFrame Info**

- RangeIndex: Indicates that there are 10 rows (entries) in the DataFrame, indexed from 0 to 9.
- Data columns (total 12 columns): Shows that there are 12 columns in the DataFrame.
- Non-Null Count: Indicates the number of non-null (non-missing) values in each column.
- Dtype: Specifies the data type of each column (e.g., int64, float64, object).
- Summary Statistics

**This part provides summary statistics for each numerical column:**

 - count: Number of non-null entries (10 for most columns, 9 for 'Age' since one entry is missing).
 - mean: Average value of the column.
 - std: Standard deviation, which measures the amount of variation in the column.
 - min: Minimum value in the column.
 - 25%: 25th percentile, or the value below which 25% of the data falls.
 - 50%: Median or 50th percentile.
 - 75%: 75th percentile, or the value below which 75% of the data falls.
 - max: Maximum value in the column.
 - Key Observations
 - The 'Age' column has one missing value (9 non-null out of 10).
 - The 'Cabin' column has many missing values (only 3 non-null out of 10).
 - The average age of passengers in this sample is approximately 28.1 years.
 - The average fare is approximately 27.02 units.
 - 50% of the passengers in this sample survived, as indicated by the mean of the 'Survived' column being 0.5.