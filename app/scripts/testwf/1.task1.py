from moose_lib import task

@task(retries=1)
def task1(input: dict):  # The name of your script
    """
    Description of what this script does
    """
    # The body of your script goes here
    task1.logger.info("Hello World from step1")
    task1.logger.info(f'step1 input data: {input}')

    # The return value is the output of the script.
    # The return value should be a dictionary with at least:
    # - task: the task name (e.g., "extract", "transform")
    # - data: the actual data being passed to the next task
    return {
        "task": "task1",  # The task name is the name of the script
        "data": {
            "id": f"{input.get("name")}-{input.get("age")}-{input.get("city")}",
        }
    }
