from rest_framework import permissions
from profile_app.models import UserProfile

class IsCustomer(permissions.BasePermission):

    def has_permission(self, request, view):
        
        user_profile = UserProfile.objects.get(user_id=request.user.id)

        if request.method in permissions.SAFE_METHODS:
            return True
        
        return user_profile.type == 'customer'