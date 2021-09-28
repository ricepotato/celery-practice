import sys
import celery
import logging
from proj.tasks import add, mul, xsum, sleep, divide_by_zero, div

log = logging.getLogger(f"mycelery.{__name__}")
log.addHandler(logging.StreamHandler())
log.setLevel(logging.INFO)


def main():
    # Shortcut to send a task message, but doesn’t support execution options.
    result = add.delay(2, 3)
    mul.delay(3, 4)
    xsum.delay([1, 2, 3, 4, 5])
    sleep_result = sleep.delay(3)
    divide_by_zero.delay()

    # The ready() method returns whether the task has finished processing or not
    log.info("add ready: %s", result.ready())
    log.info("add result: %s", result.get(timeout=1))

    log.info("sleep ready: %s", sleep_result.ready())
    try:
        log.info("sleep result: %s", sleep_result.get(timeout=1))
    except celery.exceptions.TimeoutError as e:
        log.error(e)

    divide_by_zero.apply_async(
        retry=True,
        retry_policy={
            "max_retries": 3,
            "interval_start": 0,
            "interval_step": 0.2,
            "interval_max": 0.2,
        },
    )

    div.delay(3, 4)

    return 0


if __name__ == "__main__":
    sys.exit(main())
