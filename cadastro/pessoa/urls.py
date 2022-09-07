from django.urls import path
from .views import ListaPessoaView, CreatePessoaView,PessoaUpdateView, PessoaDeleteView
from .import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(ListaPessoaView.as_view()), name='pessoa.index'),
    path('novo/', login_required(CreatePessoaView.as_view()), name='create'),
    path('<int:pk>/editar',  login_required(PessoaUpdateView.as_view()), name='editar'),
    path('<int:pk>/excluir', login_required(PessoaDeleteView.as_view()), name='excluir'),

    path('<int:pk_pessoa>/contatos', login_required(views.contatos), name='contatos'),
    path('<int:pk_pessoa>/contato/novo/',
         login_required(views.contato_novo), name='contato.novo'),
    path('<int:pk_pessoa>/contato/<int:pk>/editar',
         login_required(views.contato_editar), name='contato.editar'),
    path('<int:pk_pessoa>/contato/<int:pk>/remover',
         login_required(views.contato_remover), name='contato.remover'),
]
