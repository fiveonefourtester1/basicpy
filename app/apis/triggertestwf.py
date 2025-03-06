from moose_lib import MooseClient
from dataclasses import dataclass

# curl "http://localhost:4000/consumption/triggertestwf"

@dataclass
class QueryParams:
    name: str = "Alice"
    age: int = 30
    city: str = "New York"

def run(client: MooseClient, params: QueryParams):
    # Execute a workflow from consumption api
    # This is the same as running the following command:
    # moose-cli workflow run testwf --input '{"minDailyActiveUsers":0,"limit":5}'
    return client.workflow.execute("testwf", params)