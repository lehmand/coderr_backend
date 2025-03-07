from rest_framework import permissions
from profile_app.models import UserProfile

class IsBusinessUser(permissions.BasePermission):

    message = "Nur Business-User dürfen Angebote erstellen."

    def has_permission(self, request, view):
        user_profile = UserProfile.objects.get(user_id=request.user.id)
        
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return user_profile.type == 'business'
    
class IsCreator(permissions.BasePermission):

    message = 'Nur Ersteller können ein Angebot bearbeiten oder löschen.'

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user_id == request.user.id
