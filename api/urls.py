from api.spectacular.urls import urlpatterns as doc_urls
from accounts.urls import urlpatterns as accounts
from statistic.urls import urlpatterns as statistica
from courses.urls import urlpatterns as courses
from instructor.urls import urlpatterns as instructor
from news.urls import urlpatterns as news
from admin_control.urls import urlpatterns as admin_control
from feedback.urls import urlpatterns as feedback

app_name = 'api'

urlpatterns = []

urlpatterns += doc_urls
urlpatterns += accounts
urlpatterns += statistica
urlpatterns += courses
urlpatterns += instructor
urlpatterns += news
urlpatterns += admin_control
urlpatterns += feedback