from rest_framework import serializers
from git import Repo
from datetime import datetime

class AuthorSerializer(serializers.Serializer):
    """
    Serializer for Git Authors
    """
    name = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255)

class CommitStatsSerializer(serializers.Serializer):
    """
    Serializer for Git Commit Stats

    Stats contain information on insertions, deletions, files, and lines
    """
    insertions = serializers.IntegerField()
    deletions = serializers.IntegerField()
    lines = serializers.IntegerField()
    files = serializers.IntegerField(required=False)

class CommitFileStatsSerializer(serializers.Serializer):
    """
    Serializer for Git File Commit Stats

    Stats for a specific file in a commit, includes all the stats inside 
    CommitStatsSerializer, with the exception of files.
    """
    file_name = serializers.CharField(max_length=255)
    stats = serializers.SerializerMethodField(method_name='get_stats')

    def get_stats(self, instance):
        return CommitStatsSerializer(instance['stats'], many=False).data

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
    total_stats = serializers.SerializerMethodField(method_name='get_total_stats')
    file_stats = serializers.SerializerMethodField(method_name='get_file_stats')

    def get_total_stats(self, instance):
        return CommitStatsSerializer(instance.stats.total).data

    def get_file_stats(self, instance):
        files = instance.stats.files
        def custom_map(file_name):
            d = {}
            d['file_name'] = file_name
            d['stats'] = files[file_name]
            print(d)
            return d
        mapped_stats = map(custom_map, files.keys())
        return CommitFileStatsSerializer(mapped_stats, many=True).data

    def get_author(self, instance):
        print(instance.stats)
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