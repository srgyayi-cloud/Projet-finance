with source as (
    select * from {{ source('public', 'cours_apple') }}
)

select
    date,
    open,
    high,
    low,
    close,
    volume,
    close - lag(close) over (order by date) as variation_absolue,
    round(
        ((close - lag(close) over (order by date)) / lag(close) over (order by date) * 100)::numeric, 2
    ) as variation_pct
from source