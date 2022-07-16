from django.urls import path
from graphene_django.views import GraphQLView

from .schema import schema
from api import views

urlpatterns = [
    path('', views.index),
    path('graphql', GraphQLView.as_view(graphiql=True, schema=schema), name='graphql')
]
