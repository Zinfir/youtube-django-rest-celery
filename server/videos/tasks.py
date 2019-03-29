from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

from videos.utils import save_videos
logger = get_task_logger(__name__)


@periodic_task(
    run_every=(crontab(minute='*/10')),
    name="task_save_videos",
    ignore_result=True
)
def task_save_videos():
    """
    Saves video list
    """
    save_videos()
    logger.info("Saved video list")
