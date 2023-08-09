from rest_framework.permissions import BasePermission


class OwnerOrSuperUser(BasePermission):
    def has_permission(self, request, view):
        print(view.get_object())
        if request.user.email == view.get_object().user:
            return True
