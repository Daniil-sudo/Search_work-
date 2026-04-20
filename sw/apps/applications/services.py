from .models import Application
from vacancies.models import Vacancy                     #импортируетм созданную вакансию в приложении вакансии


async def create_application(user, vacancy_id):          #создается отклик
    vacancy = await Vacancy.objects.aget(id=vacancy_id)  #получаем вакансию из бд

    # проверка: не откликался ли уже
    exists = await Application.objects.filter(
        user=user,
        vacancy=vacancy
    ).aexists()                                          #проверка есть отклик

    if exists:
        raise Exception("Вы уже откликались на эту вакансию")  #не разрешает откликнуться еще раз

    application = await Application.objects.acreate(
        user=user,
        vacancy=vacancy
    )                                                          #создается запись в бд

    return application


async def update_application_status(application_id, status):   #функция обновления статуса
    application = await Application.objects.aget(id=application_id)  #получить отклик

    application.status = status                                #смена статуса
    await application.asave()

    return application