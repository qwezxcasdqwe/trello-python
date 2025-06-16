from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='Admin').exists()

class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='Manager').exists()

class IsMember(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='Member').exists()
