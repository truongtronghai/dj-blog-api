from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    # override method of parent
    def has_object_permission(self,request,view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user == obj.author:
            return True


class IsUserOrReadOnly(permissions.BasePermission):
    # override method of parent
    def has_object_permission(self,request,view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.id == obj.id:
            return True
