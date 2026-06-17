with silver as (
    select * from {{ ref('silver_cours_apple') }}
)
select
    date,
    close,
    volume,
    variation_pct,

    -- Moyennes mobiles
    round(avg(close) over (order by date rows between 6 preceding and current row)::numeric, 2) as ma_7j,
    round(avg(close) over (order by date rows between 29 preceding and current row)::numeric, 2) as ma_30j,

    -- Volume moyen 7j
    round(avg(volume) over (order by date rows between 6 preceding and current row)::numeric, 0) as vol_moy_7j,

    -- Volatilité rolling 7j
    round(stddev(close) over (order by date rows between 6 preceding and current row)::numeric, 2) as volatilite_7j

from silver
order by date