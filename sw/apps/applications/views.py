from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .services import create_application, update_application_status
from .serializers import ApplicationSerializer


class CreateApplicationView(APIView):                            #эндпоинт создать отклик

    async def post(self, request, vacancy_id):                   #запостить отклик
        user = request.user                                      #запрос относительно текущего пользователя

        application = await create_application(user, vacancy_id) #вызов бизнес логики

        return Response(
            ApplicationSerializer(application).data,
            status=status.HTTP_201_CREATED
        )


class UpdateStatusView(APIView):
    permission_classes = [IsEmployerOrAdmin]

    async def patch(self, request, application_id):
        try:
            application = await Application.objects.aget(id=application_id)
        except Application.DoesNotExist:
            return Response({"error": "Not found"}, status=404)

        #  проверка прав
        self.check_object_permissions(request, application)

        new_status = request.data.get("status")

        if new_status not in ["pending", "accepted", "rejected"]:
            return Response({"error": "Invalid status"}, status=400)

        application = await update_application_status(
            application_id,
            new_status
        )

        return Response(
            ApplicationSerializer(application).data
        )