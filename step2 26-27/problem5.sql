WITH RECURSIVE dates(dt) AS (
    SELECT '2025-07-30'
    UNION ALL
    SELECT date(dt, '+1 day')
    FROM dates
    WHERE dt < '2025-08-10'
),
sites AS (
    SELECT DISTINCT site_id
    FROM logs
    WHERE city_id = 'A'
      AND date("timestamp") BETWEEN '2025-07-30' AND '2025-08-10'
),
daily_raw AS (
    SELECT
        date("timestamp") AS dt,
        site_id,
        COUNT(*) AS cnt_a
    FROM logs
    WHERE city_id = 'A'
      AND date("timestamp") BETWEEN '2025-07-30' AND '2025-08-10'
    GROUP BY date("timestamp"), site_id
),
daily AS (
    SELECT
        d.dt,
        s.site_id,
        COALESCE(r.cnt_a, 0) AS cnt_a
    FROM dates d
    CROSS JOIN sites s
    LEFT JOIN daily_raw r
      ON r.dt = d.dt
     AND r.site_id = s.site_id
),
base AS (
    SELECT
        site_id,
        MAX(CASE WHEN dt = '2025-08-02' THEN cnt_a ELSE 0 END) AS outage_cnt,
        AVG(CASE WHEN dt <> '2025-08-02' THEN cnt_a END) AS avg_non_outage
    FROM daily
    GROUP BY site_id
),
stability AS (
    SELECT
        d.site_id,
        AVG(CASE WHEN d.dt <> '2025-08-02' THEN ABS(d.cnt_a - b.avg_non_outage) END) AS mad_non_outage
    FROM daily d
    JOIN base b ON b.site_id = d.site_id
    GROUP BY d.site_id
)
SELECT b.site_id
FROM base b
JOIN stability s ON s.site_id = b.site_id
WHERE b.avg_non_outage > 0
  AND 1.0 * b.outage_cnt / b.avg_non_outage >= 0.90
  AND COALESCE(s.mad_non_outage / NULLIF(b.avg_non_outage, 0), 0) <= 0.20
ORDER BY b.site_id;
