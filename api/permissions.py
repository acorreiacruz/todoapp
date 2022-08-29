from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):

    message = "Você precisa ser o autor da receita para manipulá-la"

    def has_permission(self, request, view):
        return True if request.user.is_authenticated else False

    def has_object_permission(self, request, view, obj):
        return request.user == obj.author
