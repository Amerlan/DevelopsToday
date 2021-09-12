from conf.celery import celery_app
from posts.models import Post


@celery_app.task
def reset_upvote():
    Post.upvotes.through.objects.all().delete()
    return 1
