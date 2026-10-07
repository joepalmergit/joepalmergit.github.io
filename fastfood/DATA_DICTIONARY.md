# Fast Food: data dictionary

Synthetic teaching data. All files are standalone.

## 01_product_sales.csv
Rows: 384. Columns: 5.
**Row meaning:** One product per calendar month.
**Interpretation notes:** Revenue is sales revenue, not profit. Prices are fixed within each product.
**Investigation prompt:** Compare rankings by units and revenue; investigate seasonality and year-on-year change.

| Column | Type | Meaning |
|---|---|---|
| product | Text | Product. Counts are whole numbers; categorical values use consistent spelling. |
| category | Text | Category. Counts are whole numbers; categorical values use consistent spelling. |
| month | Text | Calendar month, YYYY-MM. |
| units_sold | Integer | Units sold. Counts are whole numbers; categorical values use consistent spelling. |
| revenue_gbp | Decimal | Sales revenue in pounds sterling; see dataset notes for scope. |

## 02_branch_performance.csv
Rows: 192. Columns: 6.
**Row meaning:** One branch per calendar month.
**Interpretation notes:** Ratings use a 1-5 scale. Monthly ratings and waits are averages; weight by orders only as an approximation, not as a known survey count.
**Investigation prompt:** Compare total revenue, revenue per order and consistency.

| Column | Type | Meaning |
|---|---|---|
| branch | Text | Branch. Counts are whole numbers; categorical values use consistent spelling. |
| month | Text | Calendar month, YYYY-MM. |
| orders | Integer | Orders. Counts are whole numbers; categorical values use consistent spelling. |
| revenue_gbp | Decimal | Sales revenue in pounds sterling; see dataset notes for scope. |
| average_waiting_minutes | Decimal | Average waiting in minutes. |
| average_customer_rating | Decimal | Average customer rating, on a 1-5 scale. |

## 03_customer_satisfaction.csv
Rows: 2,400. Columns: 7.
**Row meaning:** One anonymous survey response.
**Interpretation notes:** All ratings use a 1-5 scale; responses are fictional and contain no personal data.
**Investigation prompt:** Compare visit types and investigate which rating most closely tracks overall satisfaction.

| Column | Type | Meaning |
|---|---|---|
| response_id | Text | Unique response identifier within this file, except match_id in catering (one row per kiosk). |
| visit_type | Text | Visit type. Counts are whole numbers; categorical values use consistent spelling. |
| time_of_day | Text | Time of day. Counts are whole numbers; categorical values use consistent spelling. |
| service_rating | Decimal | Service rating, on a 1-5 scale. |
| food_rating | Decimal | Food rating, on a 1-5 scale. |
| value_rating | Decimal | Value rating, on a 1-5 scale. |
| overall_rating | Decimal | Overall rating, on a 1-5 scale. |

## 04_delivery_performance.csv
Rows: 3,000. Columns: 8.
**Row meaning:** One delivery.
**Interpretation notes:** Late means delivery_minutes > promised_minutes. Date and day refer to order date.
**Investigation prompt:** Compare late-delivery rates by zone, hour and distance band.

| Column | Type | Meaning |
|---|---|---|
| delivery_id | Text | Unique delivery identifier within this file, except match_id in catering (one row per kiosk). |
| delivery_zone | Text | Delivery zone. Counts are whole numbers; categorical values use consistent spelling. |
| date | Text | Calendar date, YYYY-MM-DD. |
| day | Text | Day of week matching date. |
| order_hour | Integer | Order hour. Counts are whole numbers; categorical values use consistent spelling. |
| distance_km | Decimal | Distance km. Counts are whole numbers; categorical values use consistent spelling. |
| delivery_minutes | Decimal | Delivery in minutes. |
| promised_minutes | Integer | Promised in minutes. |

## 05_food_waste.csv
Rows: 2,080. Columns: 6.
**Row meaning:** One branch, ingredient category and week.
**Interpretation notes:** Waste is a subset of prepared quantity. Waste cost covers ingredient cost only.
**Investigation prompt:** Compare waste totals, weighted waste percentages and costs.

| Column | Type | Meaning |
|---|---|---|
| branch | Text | Branch. Counts are whole numbers; categorical values use consistent spelling. |
| week_beginning | Text | Monday starting the week, YYYY-MM-DD. |
| ingredient_category | Text | Ingredient category. Counts are whole numbers; categorical values use consistent spelling. |
| quantity_prepared_kg | Decimal | Quantity prepared in kilograms. |
| quantity_wasted_kg | Decimal | Quantity wasted in kilograms. |
| waste_cost_gbp | Decimal | Waste cost in pounds sterling. |

## 06_promotional_campaigns.csv
Rows: 120. Columns: 6.
**Row meaning:** One campaign.
**Interpretation notes:** Attribution is a fictional reporting rule, not proof of incremental sales. Revenue/spend is ROAS, not profit ROI.
**Investigation prompt:** Compare cost per attributed order and attributed revenue per pound spent.

| Column | Type | Meaning |
|---|---|---|
| campaign | Text | Campaign. Counts are whole numbers; categorical values use consistent spelling. |
| promotion_type | Text | Promotion type. Counts are whole numbers; categorical values use consistent spelling. |
| channel | Text | Channel. Counts are whole numbers; categorical values use consistent spelling. |
| campaign_spend_gbp | Integer | Campaign spend in pounds sterling. |
| orders_attributed | Integer | Orders attributed. Counts are whole numbers; categorical values use consistent spelling. |
| revenue_attributed_gbp | Decimal | Revenue attributed in pounds sterling. |

## 07_staffing_and_service.csv
Rows: 2,160. Columns: 7.
**Row meaning:** One branch, date and shift.
**Interpretation notes:** Staff hours are combined hours worked by all staff in the shift, not shift duration. Rating uses a 1-5 scale.
**Investigation prompt:** Compare orders per staff hour with waiting times and service ratings.

| Column | Type | Meaning |
|---|---|---|
| branch | Text | Branch. Counts are whole numbers; categorical values use consistent spelling. |
| date | Text | Calendar date, YYYY-MM-DD. |
| shift | Text | Shift. Counts are whole numbers; categorical values use consistent spelling. |
| staff_hours | Decimal | Combined staff working hours in the shift. |
| orders_handled | Integer | Orders handled. Counts are whole numbers; categorical values use consistent spelling. |
| average_waiting_minutes | Decimal | Average waiting in minutes. |
| service_rating | Decimal | Service rating, on a 1-5 scale. |

## 08_menu_nutrition.csv
Rows: 96. Columns: 7.
**Row meaning:** One fictional menu item.
**Interpretation notes:** Values are invented for numerical analysis, not dietary advice or real product information.
**Investigation prompt:** Compare category distributions and per-portion versus per-100-g rankings.

| Column | Type | Meaning |
|---|---|---|
| item | Text | Item. Counts are whole numbers; categorical values use consistent spelling. |
| category | Text | Category. Counts are whole numbers; categorical values use consistent spelling. |
| portion_size_g | Integer | Portion size in grams. |
| energy_kcal | Integer | Energy per portion in kilocalories. |
| sugar_g | Decimal | Sugar in grams. |
| salt_g | Decimal | Salt in grams. |
| price_gbp | Decimal | Price in pounds sterling. |
