# This block is used to aggregate the data from the Bar table into a materialized view
from moose_lib import (
  Blocks
)

MV_NAME = "BarAggregated_MV" # The name of the materialized view

# The query to create the materialized view, which is executed when the block is set up
MV_QUERY = """
CREATE MATERIALIZED VIEW BarAggregated_MV
ENGINE = MergeTree()
ORDER BY day_of_month
POPULATE
AS
SELECT
  toDayOfMonth(utc_timestamp) as day_of_month,
  count(primary_key) as total_rows,
  countIf(has_text) as rows_with_text,
  sum(text_length) as total_text_length,
  max(text_length) as max_text_length
FROM Bar_0_0
GROUP BY toDayOfMonth(utc_timestamp)
"""

# The query to drop the materialized view, which is executed when the block is torn down
DROP_MV_QUERY = f"DROP TABLE IF EXISTS {MV_NAME}"

# The block to create the materialized view
block = Blocks(teardown=[DROP_MV_QUERY], setup=[MV_QUERY])
