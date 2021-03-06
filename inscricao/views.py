from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.views.generic.base import View
from .forms import RegistrarInscricaoForm, RegistrarDocumentoForm
from sc4net import get_json
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from .models import Candidato, Documento
from cadastro.models import Usuario
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin


# class RegistrarInscricaoView(LoginRequiredMixin, View):
class RegistrarInscricaoView(View):
    template_name = 'inscricao/dados_pessoais.html'

    # @method_decorator(login_required)
    def get(self, request):
        return render(request, self.template_name)

    # @method_decorator(login_required)
    def post(self, request):
        form = RegistrarInscricaoForm(request.POST)

        if form.is_valid():
            dados_form = form.data
            inscrito = Usuario.objects.get(cpf=dados_form['cpf'])
            inscricao = Candidato.objects.create(usuario = inscrito,
                                                 nome_civil=dados_form['nome_civil'],
                                                 nome_social=dados_form['nome_social'],
                                                 nome_apresentacao=dados_form['nome_apresentacao'],
                                                 nome_usual=dados_form['nome_usual'],
                                                 nome_mae=dados_form['nome_mae'],
                                                 nome_pai=dados_form['nome_pai'],
                                                 sexo=dados_form['sexo'],
                                                 data_nascimento=dados_form['data_nascimento'],
                                                 pais_nascimento=dados_form['pais_nascimento'],
                                                 estado_nascimento=dados_form['estado_nascimento'],
                                                 cidade_nascimento=dados_form['cidade_nascimento'],
                                                 rg=dados_form['rg'],
                                                 data_emissao=dados_form['data_emissao'],
                                                 orgao_rg=dados_form['orgao_rg'],
                                                 estado_emissao=dados_form['estado_emissao'],
                                                 email=dados_form['email'],
                                                 telefone=dados_form['telefone'],
                                                 cep=dados_form['cep'],
                                                 endereco=dados_form['endereco'],
                                                 complemento=dados_form['complemento'],
                                                 cidade=dados_form['cidade'],
                                                 estado=dados_form['estado'],
                                                 pais=dados_form['pais'],
                                                 )

        # form1 = RegistrarDocumentoForm(request.POST)

        # if form1.is_valid():
        #     dados_form1 = form1.data
            documento_pessoal = Documento.objects.create(candidato = inscricao,
                                                 titulo="documentação pessoal",
                                                 arquivo=request.POST['doc_pessoal'],
                                              )
            documento_titulo = Documento.objects.create(candidato=inscricao,
                                                         titulo="documentação de títulos",
                                                         arquivo=request.POST['doc_titulo'],
                                                         )
            documento_escolar = Documento.objects.create(candidato=inscricao,
                                                         titulo="documentação escolar",
                                                         arquivo=request.POST['doc_escolar'],
                                                         )


            return redirect('confirmar')


        return render(request, self.template_name, {'form': form})




    def confirmarInscricao(request):


        return render(request, 'inscricao/confirmardados.html', {'inscricao': Candidato.objects.last(),'documento': Documento.objects.last()})



    def lista_inscricoes(request):
        return render(request, 'inscricao/listagem.html', {'inscricao': Candidato.objects.all(),'documento': Documento.objects.all()})




# class RegistrarDocumentoView(View):
#     template_name = 'inscricao/documentacao.html'
#
#     def get(self, request):
#         return render(request, self.template_name)

    # def registrarDocumento(self, request):
    #
    #     render(request, 'inscricao/documentacao.html')
    #
    #     form = RegistrarDocumentoForm(request.POST)
    #
    #     if form.is_valid():
    #         dados_form = form.data
    #
    #
    #         documento = Documento.objects.create(titulo=dados_form['titulo'],
    #                                              arquivo=request.POST['doc_pessoal'],
    #                                           )
    #
    #
    #         documento.save()
    #
    #         # inscricao = Inscricao.objects.create(numero = 1,
    #         #                                      candidato = inscricao,
    #         #                                      # documento = documento,
    #         #                                      )
    #         # inscricao.save()
    #
    #         return redirect('index')
    #
    #     return render(request, self.template_name, {'form': form})
    #