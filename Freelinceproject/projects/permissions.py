from rest_framework import permissions


class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'


class IsClient(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'client'


class IsFreelancer(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'freelancer'


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True


        if hasattr(obj, "client"):
            return obj.client == request.user


        if hasattr(obj, "reviewer"):
            return obj.reviewer == request.user


        if hasattr(obj, "id") and obj == request.user:
            return True

        return False


from rest_framework import permissions

class IsOfferOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.freelancer == request.user
