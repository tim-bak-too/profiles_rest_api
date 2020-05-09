from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to update their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check if user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """Allow user to update their own feed status"""

    def has_object_permission(self, request, view, obj):
        """Check if user is trying to update their own feed status"""
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.user_profile.id == request.user.id
