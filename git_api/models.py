from django.db import models

class PullRequest(models.Model):
    """
    Class containing model structure for Pull Requests

    Pull Requests contain information for merging branches.
    """

    class StatusChoices(models.TextChoices):
        """
        Type of pages whcih will specify a page content
        """
        OPEN = "OPEN"
        CLOSED = "CLOSED"
        MERGED = "MERGED"

    status = models.CharField(
        max_length=15,
        choices=StatusChoices.choices,
        default=StatusChoices.OPEN
    )
    author = models.CharField(
        max_length=255,
    )
    title = models.CharField(
        max_length=255,
    )
    description = models.TextField()
    base_branch = models.CharField(
        max_length=255,
        default=None
    )
    rebase_branch = models.CharField(
        max_length=255,
        default=None
    )