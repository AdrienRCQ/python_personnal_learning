import importlib
import logging

logger = logging.getLogger(__name__)

def run_task(task_name: str):
    logger.info("Starting task: %s", task_name)

    try:
        module = importlib.import_module(f"services.tasks.{task_name}")
        result = module.run()
        logger.info("Task %s completed: %s", task_name, result)

    except Exception:
        logger.exception("Task %s failed", task_name)
