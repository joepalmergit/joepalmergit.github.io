# Sports: data dictionary

Synthetic teaching data. All files are standalone.

## 01_team_performance.csv
Rows: 36. Columns: 8.
**Row meaning:** One fictional team per completed league season.
**Interpretation notes:** Twelve-team double round-robin league. Points: 3 per win, 1 per draw. All team totals are internally consistent.
**Investigation prompt:** Compare points, goal difference and consistency across seasons.

| Column | Type | Meaning |
|---|---|---|
| team | Text | Team. Counts are whole numbers; categorical values use consistent spelling. |
| season | Text | Season. Counts are whole numbers; categorical values use consistent spelling. |
| played | Integer | Played. Counts are whole numbers; categorical values use consistent spelling. |
| wins | Integer | Wins. Counts are whole numbers; categorical values use consistent spelling. |
| draws | Integer | Draws. Counts are whole numbers; categorical values use consistent spelling. |
| losses | Integer | Losses. Counts are whole numbers; categorical values use consistent spelling. |
| goals_scored | Integer | Goals scored. Counts are whole numbers; categorical values use consistent spelling. |
| goals_conceded | Integer | Goals conceded. Counts are whole numbers; categorical values use consistent spelling. |

## 02_match_attendance.csv
Rows: 240. Columns: 6.
**Row meaning:** One match across several fictional venues.
**Interpretation notes:** Capacity is available capacity for that match, not necessarily full stadium capacity.
**Investigation prompt:** Compare attendance totals with weighted capacity utilisation.

| Column | Type | Meaning |
|---|---|---|
| match_id | Text | Unique match identifier within this file, except match_id in catering (one row per kiosk). |
| date | Text | Calendar date, YYYY-MM-DD. |
| competition | Text | Competition. Counts are whole numbers; categorical values use consistent spelling. |
| kick_off_time | Text | Local scheduled time, HH:MM. |
| attendance | Integer | Attendance. Counts are whole numbers; categorical values use consistent spelling. |
| available_capacity | Integer | Available spectator places for this match. |

## 03_player_performance.csv
Rows: 240. Columns: 6.
**Row meaning:** One fictional player over a completed season.
**Interpretation notes:** No real people. Compare within position and use a minimum-minutes threshold; totals and per-90 rates answer different questions.
**Investigation prompt:** Compare goals and assists per 90 with totals and investigate threshold sensitivity.

| Column | Type | Meaning |
|---|---|---|
| player | Text | Player. Counts are whole numbers; categorical values use consistent spelling. |
| position | Text | Position. Counts are whole numbers; categorical values use consistent spelling. |
| appearances | Integer | Appearances. Counts are whole numbers; categorical values use consistent spelling. |
| minutes_played | Integer | Minutes played. Counts are whole numbers; categorical values use consistent spelling. |
| goals | Integer | Goals. Counts are whole numbers; categorical values use consistent spelling. |
| assists | Integer | Assists. Counts are whole numbers; categorical values use consistent spelling. |

## 04_ticket_sales.csv
Rows: 288. Columns: 6.
**Row meaning:** One month, fixture category and ticket category.
**Interpretation notes:** Family prices are per ticket, not per group. Accessible seating is a ticket category, not a personal characteristic. Revenue is not profit.
**Investigation prompt:** Compare sell-through and revenue per sold ticket.

| Column | Type | Meaning |
|---|---|---|
| month | Text | Calendar month, YYYY-MM. |
| fixture_category | Text | Fixture category. Counts are whole numbers; categorical values use consistent spelling. |
| ticket_category | Text | Ticket category. Counts are whole numbers; categorical values use consistent spelling. |
| tickets_available | Integer | Tickets available. Counts are whole numbers; categorical values use consistent spelling. |
| tickets_sold | Integer | Tickets sold. Counts are whole numbers; categorical values use consistent spelling. |
| revenue_gbp | Integer | Sales revenue in pounds sterling; see dataset notes for scope. |

## 05_supporter_satisfaction.csv
Rows: 2,400. Columns: 7.
**Row meaning:** One anonymous supporter survey response.
**Interpretation notes:** Ratings use a 1-5 scale. No personal information is included.
**Investigation prompt:** Compare seating areas, distributions and the queue-satisfaction association.

| Column | Type | Meaning |
|---|---|---|
| response_id | Text | Unique response identifier within this file, except match_id in catering (one row per kiosk). |
| match_category | Text | Match category. Counts are whole numbers; categorical values use consistent spelling. |
| seating_area | Text | Seating area. Counts are whole numbers; categorical values use consistent spelling. |
| queue_minutes | Decimal | Queue in minutes. |
| facilities_rating | Decimal | Facilities rating, on a 1-5 scale. |
| value_rating | Decimal | Value rating, on a 1-5 scale. |
| overall_rating | Decimal | Overall rating, on a 1-5 scale. |

## 06_merchandise_sales.csv
Rows: 864. Columns: 7.
**Row meaning:** One product-channel-month combination.
**Interpretation notes:** Revenue is gross sales before refunds; returns are returned units from that sales cohort.
**Investigation prompt:** Compare sales seasonality, channels and weighted return rates.

| Column | Type | Meaning |
|---|---|---|
| product | Text | Product. Counts are whole numbers; categorical values use consistent spelling. |
| category | Text | Category. Counts are whole numbers; categorical values use consistent spelling. |
| sales_channel | Text | Sales channel. Counts are whole numbers; categorical values use consistent spelling. |
| month | Text | Calendar month, YYYY-MM. |
| units_sold | Integer | Units sold. Counts are whole numbers; categorical values use consistent spelling. |
| revenue_gbp | Integer | Sales revenue in pounds sterling; see dataset notes for scope. |
| returns | Integer | Returns. Counts are whole numbers; categorical values use consistent spelling. |

## 07_training_attendance.csv
Rows: 384. Columns: 6.
**Row meaning:** One squad-month-session-type combination.
**Interpretation notes:** Player places are all available attendance slots. Attendances count visits, not unique players. Squads do not identify protected characteristics.
**Investigation prompt:** Compare weighted attendance rates and seasonal patterns.

| Column | Type | Meaning |
|---|---|---|
| squad | Text | Squad. Counts are whole numbers; categorical values use consistent spelling. |
| month | Text | Calendar month, YYYY-MM. |
| session_type | Text | Session type. Counts are whole numbers; categorical values use consistent spelling. |
| sessions_offered | Integer | Sessions offered. Counts are whole numbers; categorical values use consistent spelling. |
| player_places_available | Integer | Total attendance slots across offered sessions. |
| player_attendances | Integer | Total occupied attendance slots, not unique players. |

## 08_match_day_catering.csv
Rows: 600. Columns: 8.
**Row meaning:** One kiosk per match.
**Interpretation notes:** Attendance is repeated for every kiosk at the same match: do not sum it across kiosks. Waste units are unsold prepared items, separate from sold items.
**Investigation prompt:** Compare revenue per transaction, queue times and waste/(sold+waste).

| Column | Type | Meaning |
|---|---|---|
| match_id | Text | Unique match identifier within this file, except match_id in catering (one row per kiosk). |
| kiosk | Text | Kiosk. Counts are whole numbers; categorical values use consistent spelling. |
| attendance | Integer | Attendance. Counts are whole numbers; categorical values use consistent spelling. |
| transactions | Integer | Transactions. Counts are whole numbers; categorical values use consistent spelling. |
| items_sold | Integer | Items sold. Counts are whole numbers; categorical values use consistent spelling. |
| revenue_gbp | Decimal | Sales revenue in pounds sterling; see dataset notes for scope. |
| average_queue_minutes | Decimal | Average queue in minutes. |
| waste_units | Integer | Waste units. Counts are whole numbers; categorical values use consistent spelling. |
