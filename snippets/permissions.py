from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    '''
    Custom permission to only allow owners of an object to edit it.
    '''

    def has_object_permission(self, request, view, obj):
        # GET, HEAD, OPTIONS are allowed for anyone
        if request.method in permissions.SAFE_METHODS:
            return True
        # write permissions only allow for the owner of the object
        return obj.owner == request.user
