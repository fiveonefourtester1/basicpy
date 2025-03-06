from moose_lib import task

@task(retries=1)
def task2(input: dict):  # The name of your script
    """
    Description of what this script does
    """
    # The body of your script goes here
    task2.logger.info("Hello World from step2")
    task2.logger.info(f'step2 input data: {input}')

    # The return value is the output of the script.
    # The return value should be a dictionary with at least:
    # - task: the task name (e.g., "extract", "transform")
    # - data: the actual data being passed to the next task
    return {
        "task": "task2",  # The task name is the name of the script
        "data": None     # The data being passed to the next task (4MB limit)
    }
