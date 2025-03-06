## Example Streaming Function: Transforms Foo data to Bar data

from moose_lib import StreamingFunction
from app.datamodels.models import Foo, Bar # Import your Moose data models to use in the streaming function
from datetime import datetime

# The 'run' function contains the logic that runs on each new data point in the Foo stream.
# For more details on how Moose streaming functions work, see: https://docs.moosejs.com
def run(foo: Foo) -> Bar:
    return Bar(
        primary_key=foo.primary_key,
        utc_timestamp=datetime.fromtimestamp(foo.timestamp),
        has_text=foo.optional_text is not None,
        text_length=len(foo.optional_text) if foo.optional_text else 0
    )

Foo__Bar = StreamingFunction(run=run) # Register the run function as a streaming function.
