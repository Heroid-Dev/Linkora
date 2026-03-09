from rest_framework.permissions import BasePermission

class IsEmployer(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.groups.filter(name='employer').exists()
        )

class IsApplicant(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.groups.filter(name='applicant').exists()
        )

class IsJobOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.employee == request.user.profile

class IsApplicationOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.applicant == request.user.profile
