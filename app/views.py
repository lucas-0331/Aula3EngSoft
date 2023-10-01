from django.shortcuts import render
from . models import *

# Create your views here.
def matricula(request):
    if request.POST:
        nova_matricula = Matricula()
        nova_matricula.dataInicio = request.POST.get('data')
        nova_matricula.dataFinal = request.POST.get('data2')
        try:
            instituicao = Instituicao.objects.get(pk = request.POST.get('instituicao'))
            pessoa = Pessoa.objects.get(pk = request.POST.get('pessoa'))
            curso = Curso.objects.get(pk = request.POST.get('curso'))
            nova_matricula.instituicao = instituicao
            nova_matricula.pessoa = pessoa
            nova_matricula.curso = curso
            nova_matricula.save()
        except Instituicao.DoesNotExist:
            print('Instituição não encontrado')
        except Pessoa.DoesNotExist:
            print('Pessoa não encontrado')
        except Curso.DoesNotExist:
            print('Ocupacao não encontrada')
        except Exception as e:
            print('Erro de integridade:', e)

    matriculas = {
        'instituicao':Instituicao.objects.all(),
        'curso':Curso.objects.all(),
        'pessoa':Pessoa.objects.all(),
    }
    
    return render(request, 'matricula/matricula.html', matriculas)

def cidade(request):
    cidades = {
        'cidade':Cidade.objects.all()
    }
    
    return render(request, 'cidade/cidade.html', cidades)

def pessoa(request):
    pessoas = {
        'pessoa':Pessoa.objects.all()
    }
    
    return render(request, 'pessoa/pessoa.html', pessoas)

def areasaber(request):
    areassaberes = {
        'areasaber':AreaSaber.objects.all()
    }
    
    return render(request, 'areasaber/areasaber.html', areassaberes)

def instituicao(request):
    instituicoes = {
        'instituicao':Instituicao.objects.all()
    }
    
    return render(request, 'instituicao/instituicao.html', instituicoes)

def curso(request):
    cursos = {
        'curso':Curso.objects.all()
    }
    
    return render(request, 'curso/curso.html', cursos)

def disciplina(request):
    disciplinas = {
        'disciplina':Disciplina.objects.all()
    }
    
    return render(request, 'disciplina/disciplina.html', disciplinas)

def matriculado(request):
    matriculados = {
        'matriculado':Matricula.objects.all()
    }
    
    return render(request, 'matricula/matriculado.html', matriculados)

def avaliacao(request):
    avaliacoes = {
        'avaliacao':Avaliacao.objects.all()
    }

    return render(request, 'avaliacao/avaliacao.html', avaliacoes)

def frequencia(request):
    frequencias = {
        'frequencia':Frequencia.objects.all()
    }

    return render(request, 'frequencia/frequencia.html', frequencias)

def periodoturma(request):
    periodoturmas = {
        'periodoturma':PeriodoTurma.objects.all()
    }

    return render(request, 'periodo/periodoturma.html', periodoturmas)

def ocorrencia(request):
    ocorrencias = {
        'ocorrencia':Ocorrencia.objects.all()
    }
    
    return render(request, 'ocorrencia/ocorrencia.html', ocorrencias)

def disciplinacurso(request):
    disciplinacursos = {
        'disciplinacurso':DisciplinaCurso.objects.all()
    }

    return render(request, 'disciplina/disciplinacurso.html', disciplinacursos)