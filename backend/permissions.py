from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Instance must have an attribute named `owner`.
        return obj.owner == request.user.username

class IsRequestingSelf(permissions.BasePermission):
    def has_permission(self, request, view, **kwargs):
        print(request.user, view.kwargs.get('username'))
        return  view.kwargs.get('username') == request.user.username