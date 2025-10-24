from rest_framework import permissions


class ViewPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in ['GET', 'OPTIONS', 'HEAD']:
            return True
        else:
            return request.user.is_staff
