from django.urls import path

from .views import ApiOverview,TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete
urlpatterns = [
	path('', ApiOverview.as_view(), name="api-overview"),
	path('task-list/',  TaskList.as_view(), name="task-list"),
	path('task-detail/<str:pk>/', TaskDetail.as_view(), name="task-detail"),
	path('task-create/', TaskCreate.as_view(), name="task-create"),

	path('task-update/<str:pk>/', TaskUpdate.as_view(), name="task-update"),
	path('task-delete/<str:pk>/', TaskDelete.as_view(), name="task-delete"),
]
