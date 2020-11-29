from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    message = 'You must be the owner of this memory object!'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.user
