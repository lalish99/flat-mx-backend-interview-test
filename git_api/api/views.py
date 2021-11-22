from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.exceptions import NotAcceptable, NotFound
from rest_framework.response import Response
from git_api.api import serializers
from git import Repo
from rest_framework.decorators import action

class BranchViewSet(viewsets.ViewSet):
    """
    ViewSet for listing and retrieving repository branches.
    """

    serializer_class = serializers.BranchSerializer
    lookup_field = "commit"

    def list(self, request):
        """
        List all branches on repository.

        To avoid unnecesary saturation of this endpoint, the commits included within 
        the branches in this response, will be limited to a maximum of 5.
        """
        repo = Repo('.')
        remote_refs = repo.remote().refs
        serializer = serializers.BranchSerializer(remote_refs, many=True, context= { 'max_commits': 5 })
        return Response(serializer.data)


    def retrieve(self, request, commit=None):
        repo = Repo('.')
        remote_refs = repo.remote().refs
        def xx(ref):
            print(str(ref.commit), str(commit), str(ref.commit) == str(commit))
            return str(ref.commit) == str(commit)
        filtered = list(filter(xx, remote_refs))
        if len(filtered) == 1:
            branch = filtered[0]
            serialized = serializers.BranchSerializer(branch)
            return Response(serialized.data)
        if len(filtered) > 1:
            raise NotAcceptable(detail="Found 2 branches with same commit")
        raise NotFound

