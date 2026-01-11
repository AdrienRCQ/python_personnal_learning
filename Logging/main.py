from Logging_config import setup_logging
from services.task_runner import run_task

def main():
    setup_logging()

    run_task("divide")
    run_task("cleanup")

if __name__ == "__main__":
    main()
