# Sector Insights Challenge

All data in this pack are synthetic, generated for teaching. All organisations, games, menu items and players are fictional. These are not real-world statistics.

## Working rules
- Analyse each CSV independently. No joins, merges or cleaning are required.
- Each file is UTF-8, comma-separated, with one header row and no index column.
- Dates use YYYY-MM-DD; months use YYYY-MM. Monetary amounts are GBP.
- Ratings are 1-5 unless the dictionary specifies otherwise.
- There are no missing values or duplicate full rows. Repeated categories and legitimate repeated observations are intentional.
- Converting a date column to datetime is normal analysis, not a data-cleaning task.
- Relationships are associations, not proof of causation. Do not infer links across separate datasets.
- Use totals divided by totals for weighted rates where appropriate. Explain denominators.

## For each dataset
1. Explain what one row represents.
2. Ask three questions: comparison, pattern/relationship, and deeper investigation.
3. Use filtering, sorting, grouping and summary statistics.
4. Calculate at least one useful measure.
5. Produce two purposeful charts and three numerical insights.
6. Explain one limitation.

## Group submission
Eight analysis sections/notebooks; 24 questions; 16 charts; 24 supported insights; a client presentation with three prioritised recommendations; individual explanation of one calculation and one limitation.

## Getting started
Read a file with pandas.read_csv("01_product_sales.csv") (substitute your filename). No additional files are needed for any analysis.
