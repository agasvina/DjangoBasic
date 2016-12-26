from rest_framework.permissions import (
    BasePermission,
    SAFE_METHODS,
)

class IsOwnerOrReadOnly(BasePermission):
    message = 'Only can be update by the owner of this message'
    my_safe_method = ['GET','PUT']

    def has_permission(self, request, view):
        if request.method in self.my_safe_method:
            return True
        return False

    def has_object_permission(self, request, view, object):
        if request.method in SAFE_METHODS:
            return True
        return object.user == request.user