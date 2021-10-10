"""djangoProject1 URL Configuration

The `urlpatterns` list routes URLs to controller. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function controller
    1. Add an import:  from my_app import controller
    2. Add a URL to urlpatterns:  url(r'^$', controller.home, name='home')
Class-based controller
    1. Add an import:  from other_app.controller import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from PostTN.controller import agences, users, systems, alerts
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Agence Urls
    url(r'^agence$', agences.GetAgence.as_view()),
    url(r'^cities$', agences.GetCities.as_view()),
    url(r'^agence/([0-9]+)$', agences.GetAgence.as_view()),
    url(r'^agence/store$', agences.StoreAgence.as_view()),
    url(r'^agence/update/([0-9]+)$', agences.UpdateAgence.as_view()),
    url(r'^agence/delete/([0-9]+)$', agences.DeleteAgence.as_view()),
    url(r'^agencesystem$', agences.GetSystemsAgence.as_view()),
    url(r'^agencesystem/([0-9]+)/([0-9]+)$', agences.AffectSystemToAgence.as_view()),
    url(r'^getsystems/([0-9]+)$', agences.getSystemsByAgenceID.as_view()),
    url(r'^agencesystem/delete/([0-9]+)/([0-9]+)$', agences.removeSystemsByAgenceID.as_view()),


    # User Urls
    url(r'^user$', users.GetUsers.as_view()),
    url(r'^user/([0-9]+)$', users.GetUsers.as_view()),
    url(r'^user/store$', users.StoreUser.as_view()),
    url(r'^user/update/([0-9]+)$', users.UpdateUser.as_view()),
    url(r'^user/delete/([0-9]+)$', users.DeleteUser.as_view()),
    url(r'^agenceuser/([0-9]+)/([0-9]+)$', users.AffectUserToAgence.as_view()),
    url(r'^userAgence$', users.GetUserAgence.as_view()),
    url(r'^profile$', users.GetUserInfo.as_view()),

    # System Urls
    url(r'^system$', systems.GetSystem.as_view()),
    url(r'^system/([0-9]+)$', systems.GetSystem.as_view()),
    url(r'^system/store$', systems.StoreSystem.as_view()),
    url(r'^system/update/([0-9]+)$', systems.UpdateSystem.as_view()),
    url(r'^system/delete/([0-9]+)$', systems.DeleteSystem.as_view()),
    url(r'^systemAlerts/([0-9]+)$', systems.GetSystemAlerts.as_view()),

    # Alert Urls
    url(r'^alert$', alerts.GetAlerts.as_view()),
    url(r'^GetAllNotification$', alerts.GetAllNotification.as_view()),
    url(r'^alert/([0-9]+)$', alerts.GetAlerts.as_view()),
    url(r'^alert/store$', alerts.StoreAlerts.as_view()),
    url(r'^alert/update/([0-9]+)$', alerts.UpdateAlerts.as_view()),
    url(r'^alert/delete/([0-9]+)$', alerts.DeleteAlerts.as_view()),
    url(r'^saveNotification/([0-9]+)/([0-9]+)/([0-9]+)$', alerts.SaveNotification.as_view()),
    url(r'^userNotification$', alerts.GetUserNotification.as_view()),
    url(r'^UpdateNotification/([0-9]+)/([0-9]+)$', alerts.UpdateNotification.as_view()),


    url(r'^GetInfos$', users.GetInfos.as_view()),
    url(r'^UpdateUserPassword$', users.UpdateUserPassword.as_view()),

    url(r'^auth$', ObtainAuthToken.as_view()),
]
