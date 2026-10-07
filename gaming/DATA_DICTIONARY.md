# Gaming: data dictionary

Synthetic teaching data. All files are standalone.

## 01_game_sales.csv
Rows: 72. Columns: 6.
**Row meaning:** One title-platform combination.
**Interpretation notes:** Lifetime sales measured at 31 December 2025. Older titles have had longer to accumulate sales.
**Investigation prompt:** Compare genre and platform totals and account for release-year limitations.

| Column | Type | Meaning |
|---|---|---|
| title | Text | Title. Counts are whole numbers; categorical values use consistent spelling. |
| genre | Text | Genre. Counts are whole numbers; categorical values use consistent spelling. |
| platform | Text | Platform. Counts are whole numbers; categorical values use consistent spelling. |
| release_year | Integer | Release year. Counts are whole numbers; categorical values use consistent spelling. |
| units_sold | Integer | Units sold. Counts are whole numbers; categorical values use consistent spelling. |
| revenue_gbp | Decimal | Sales revenue in pounds sterling; see dataset notes for scope. |

## 02_weekly_player_activity.csv
Rows: 1,248. Columns: 5.
**Row meaning:** One game per week.
**Interpretation notes:** Active players are unique within a week, not across weeks. Sessions and hours cover those players.
**Investigation prompt:** Compare engagement per player and weekly trends; do not sum players as unique people.

| Column | Type | Meaning |
|---|---|---|
| game | Text | Game. Counts are whole numbers; categorical values use consistent spelling. |
| week_beginning | Text | Monday starting the week, YYYY-MM-DD. |
| active_players | Integer | Active players. Counts are whole numbers; categorical values use consistent spelling. |
| total_sessions | Integer | Total sessions. Counts are whole numbers; categorical values use consistent spelling. |
| total_play_hours | Decimal | Total play in hours. |

## 03_game_reviews.csv
Rows: 3,600. Columns: 6.
**Row meaning:** One anonymous review.
**Interpretation notes:** Scores use a 1-10 scale. Recommended is True/False; there are no personal data.
**Investigation prompt:** Compare mean, median, variability, recommendation percentage and review counts.

| Column | Type | Meaning |
|---|---|---|
| review_id | Text | Unique review identifier within this file, except match_id in catering (one row per kiosk). |
| title | Text | Title. Counts are whole numbers; categorical values use consistent spelling. |
| genre | Text | Genre. Counts are whole numbers; categorical values use consistent spelling. |
| platform | Text | Platform. Counts are whole numbers; categorical values use consistent spelling. |
| review_score | Decimal | Review score from 1 to 10. |
| recommended | Boolean | Boolean True or False. |

## 04_technical_performance.csv
Rows: 2,592. Columns: 7.
**Row meaning:** One benchmark run; three runs per configuration.
**Interpretation notes:** Hardware tiers and benchmarks are fictional. FPS means frames per second.
**Investigation prompt:** Compare settings and variability; calculate percentage of runs meeting a chosen FPS threshold.

| Column | Type | Meaning |
|---|---|---|
| test_id | Text | Unique test identifier within this file, except match_id in catering (one row per kiosk). |
| game | Text | Game. Counts are whole numbers; categorical values use consistent spelling. |
| hardware_tier | Text | Hardware tier. Counts are whole numbers; categorical values use consistent spelling. |
| graphics_preset | Text | Graphics preset. Counts are whole numbers; categorical values use consistent spelling. |
| resolution | Text | Display resolution in pixels (width x height). |
| average_fps | Decimal | Average frames per second. |
| minimum_fps | Decimal | Minimum frames per second. |

## 05_customer_support.csv
Rows: 2,400. Columns: 7.
**Row meaning:** One resolved support ticket.
**Interpretation notes:** Both time measures start at ticket creation. Ratings use a 1-5 scale.
**Investigation prompt:** Compare resolution distributions and associations with satisfaction.

| Column | Type | Meaning |
|---|---|---|
| ticket_id | Text | Unique ticket identifier within this file, except match_id in catering (one row per kiosk). |
| game | Text | Game. Counts are whole numbers; categorical values use consistent spelling. |
| issue_category | Text | Issue category. Counts are whole numbers; categorical values use consistent spelling. |
| platform | Text | Platform. Counts are whole numbers; categorical values use consistent spelling. |
| response_hours | Decimal | Response in hours. |
| resolution_hours | Decimal | Resolution in hours. |
| satisfaction_rating | Decimal | Satisfaction rating, on a 1-5 scale. |

## 06_in_game_events.csv
Rows: 144. Columns: 8.
**Row meaning:** One event.
**Interpretation notes:** Eligible players are the participation denominator; participants are the completion denominator. Ratings use 1-5.
**Investigation prompt:** Compare participation and completion rates, duration and satisfaction.

| Column | Type | Meaning |
|---|---|---|
| event | Text | Event. Counts are whole numbers; categorical values use consistent spelling. |
| game | Text | Game. Counts are whole numbers; categorical values use consistent spelling. |
| event_type | Text | Event type. Counts are whole numbers; categorical values use consistent spelling. |
| duration_days | Integer | Duration days. Counts are whole numbers; categorical values use consistent spelling. |
| eligible_players | Integer | Eligible players. Counts are whole numbers; categorical values use consistent spelling. |
| participants | Integer | Participants. Counts are whole numbers; categorical values use consistent spelling. |
| completions | Integer | Completions. Counts are whole numbers; categorical values use consistent spelling. |
| satisfaction_rating | Decimal | Satisfaction rating, on a 1-5 scale. |

## 07_store_promotions.csv
Rows: 180. Columns: 7.
**Row meaning:** One promotion.
**Interpretation notes:** Each unit is one purchase; page views may repeat. Units/page views is a view-to-sale ratio, not unique visitor conversion.
**Investigation prompt:** Compare units per day, revenue per day and view-to-sale ratios across discounts.

| Column | Type | Meaning |
|---|---|---|
| promotion | Text | Promotion. Counts are whole numbers; categorical values use consistent spelling. |
| genre | Text | Genre. Counts are whole numbers; categorical values use consistent spelling. |
| discount_percentage | Integer | Discount in percentage points, e.g. 20 means 20%. |
| promotion_days | Integer | Promotion days. Counts are whole numbers; categorical values use consistent spelling. |
| units_sold | Integer | Units sold. Counts are whole numbers; categorical values use consistent spelling. |
| revenue_gbp | Decimal | Sales revenue in pounds sterling; see dataset notes for scope. |
| page_views | Integer | Page views. Counts are whole numbers; categorical values use consistent spelling. |

## 08_player_retention.csv
Rows: 1,512. Columns: 7.
**Row meaning:** One game-platform-signup-month cohort.
**Interpretation notes:** Retention is cumulative survival: players still active through each milestone, so counts are nested. Follow-up complete to 31 December 2025.
**Investigation prompt:** Compare weighted retention rates and percentage-point versus relative drop-offs.

| Column | Type | Meaning |
|---|---|---|
| game | Text | Game. Counts are whole numbers; categorical values use consistent spelling. |
| platform | Text | Platform. Counts are whole numbers; categorical values use consistent spelling. |
| signup_month | Text | Signup cohort month, YYYY-MM. |
| new_players | Integer | New players. Counts are whole numbers; categorical values use consistent spelling. |
| retained_day_7 | Integer | Cohort players retained through day 7. |
| retained_day_30 | Integer | Cohort players retained through day 30. |
| retained_day_90 | Integer | Cohort players retained through day 90. |
