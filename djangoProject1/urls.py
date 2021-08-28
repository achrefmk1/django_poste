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

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Agence Urls
    url(r'^agence$', agences.GetAgence),
    url(r'^cities$', agences.GetCities),
    url(r'^agence/([0-9]+)$', agences.GetAgence),
    url(r'^agence/store$', agences.StoreAgence),
    url(r'^agence/update/([0-9]+)$', agences.UpdateAgence),
    url(r'^agence/delete/([0-9]+)$', agences.DeleteAgence),
    url(r'^agencesystem$', agences.GetSystemsAgence),
    url(r'^agencesystem/([0-9]+)/([0-9]+)$', agences.AffectSystemToAgence),
    url(r'^getsystems/([0-9]+)$', agences.getSystemsByAgenceID),

    # User Urls
    url(r'^user$', users.GetUser),
    url(r'^user/([0-9]+)$', users.GetUser),
    url(r'^user/store$', users.StoreUser),
    url(r'^user/update/([0-9]+)$', users.UpdateUser),
    url(r'^user/delete/([0-9]+)$', users.DeleteUser),
    url(r'^agenceuser/([0-9]+)/([0-9]+)$', users.AffectUserToAgence),
    url(r'^userAgence$', users.GetUserAgence),

    # System Urls
    url(r'^system$', systems.GetSystem),
    url(r'^system/([0-9]+)$', systems.GetSystem),
    url(r'^system/store$', systems.StoreSystem),
    url(r'^system/update/([0-9]+)$', systems.UpdateSystem),
    url(r'^system/delete/([0-9]+)$', systems.DeleteSystem),

    # Alert Urls
    url(r'^alert$', alerts.GetAlerts),
    url(r'^alert/([0-9]+)$', alerts.GetAlerts),
    url(r'^alert/store$', alerts.StoreAlerts),
    url(r'^alert/update/([0-9]+)$', alerts.UpdateAlerts),
    url(r'^alert/delete/([0-9]+)$', alerts.DeleteAlerts),
]
