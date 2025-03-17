from rest_framework import permissions
from profile_app.models import UserProfile
from django.contrib.auth.models import User

class IsCreator(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.reviewer.id == request.user.id

