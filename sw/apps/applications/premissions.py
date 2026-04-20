from rest_framework.permissions import BasePermission


class IsEmployerOrAdmin(BasePermission):
    """
    Разрешает менять статус:
    - работодателю (владельцу вакансии)
    - администратору
    """

    def has_object_permission(self, request, view, obj):
        user = request.user

        # админ может всё
        if user.is_superuser:
            return True

        # работодатель (владелец вакансии)
        return obj.vacancy.user == user