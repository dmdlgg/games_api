from rest_framework import permissions 

class JogoPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True 
        else: 
            if request.user.is_staff:
                return True
            return False