from rest_framework import serializers
from git import Repo
from datetime import datetime

class AuthorSerializer(serializers.Serializer):
    """
    Serializer for Git Authors
    """
    name = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255)


class CommitSerializer(serializers.Serializer):
    """
    Serializer for Git Commits
    """
    author = serializers.SerializerMethodField(method_name='get_author')
    committed_date = serializers.IntegerField()
    committed_datetime = serializers.DateTimeField()
    message = serializers.CharField(max_length=255)
    name_rev = serializers.CharField(max_length=255)
    summary = serializers.CharField(max_length=255)
    tree = serializers.CharField(max_length=255)
    hexsha = serializers.CharField(max_length=255)

    def get_author(self, instance):
        return AuthorSerializer(instance.author, many=False).data


class BranchSerializer(serializers.Serializer):
    """
    Serializer for Git branches
    """

    name = serializers.CharField(max_length=255)
    repo = serializers.CharField(max_length=255)
    path = serializers.CharField(max_length=510)
    commit = serializers.CharField(max_length=255)
    remote_name = serializers.CharField(max_length=510)
    commits = serializers.SerializerMethodField(method_name='get_commits')

    def get_commits(self, instance):
        repo = Repo('.')
        max_commits = None
        if 'max_commits' in self.context:
            max_commits = self.context['max_commits']
        commits = list(repo.iter_commits(instance.path, max_count=max_commits))
        return CommitSerializer(commits, many=True).data