from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Cidade(models.Model):
    nome = models.CharField(max_length=255)
    uf = models.CharField(max_length=2)
    
    def __str__(self):
        return f'{self.nome} {self.uf}'
  
    
class Periodo(models.Model):
    periodo = models.CharField(max_length=255)
    
    def __str__(self):
        return self.periodo
  
    
class Ocupacao(models.Model):
    ocupacao = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.ocupacao}'


class AreaSaber(models.Model):
    nome = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.nome}'
  
    
class Instituicao(models.Model):
    nome = models.CharField(max_length=255)
    site = models.CharField(max_length=255)
    telefone = models.PositiveIntegerField(
        validators=[
            MinValueValidator(limit_value=8, message="No minimo 8 digitos")
        ]
    )
    
    def __str__(self):
        return f'{self.nome} {self.site} {self.telefone}'


class Curso(models.Model):
    nome = models.CharField(max_length=255)
    cargaHorariaTotal = models.DecimalField(max_digits=6, decimal_places=2)
    duracaoMeses = models.DecimalField(max_digits=6, decimal_places=2)
    areaSaber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE)
    intituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.nome} {self.cargaHorariaTotal} {self.duracaoMeses} {self.areaSaber} {self.intituicao}'


class Disciplina(models.Model):
    nome = models.CharField(max_length=255)
    areaSaber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE)
   
    def __str__(self):
        return f'{self.nome} {self.areaSaber}'
    
class Pessoa(models.Model):
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    pai = models.CharField(max_length=255, blank=True, null=True)
    mae = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    dataNascimento = models.DateField()
    email = models.EmailField()
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.ocupacao} {self.nome} {self.pai} {self.mae} {self.cpf} {self.dataNascimento} {self.email} {self.cidade}'


class Matricula(models.Model):
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    dataInicio = models.DateField()
    dataPrevisaoTermino = models.DateField()
    
    def __str__(self):
        return f'{self.instituicao} {self.curso} {self.pessoa} {self.dataInicio} {self.dataPrevisaoTermino}'


class Avaliacao(models.Model):
    descricao = models.CharField(max_length=255)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.descricao} {self.curso} {self.disciplina}'


class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    numeroFalta = models.PositiveIntegerField()
    
    def __str__(self):
        return f'{self.curso} {self.disciplina} {self.numeroFalta}'


class PeriodoTurma(models.Model):
    nome = models.CharField(max_length=255)
    periodo = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.nome} {self.periodo}'
  
    
class Ocorrencia(models.Model):
    descricao = models.CharField(max_length=255)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.descricao} {self.curso} {self.disciplina} {self.pessoa}'


class TipoAvaliacao(models.Model):
    prova = models.CharField(max_length=255)
    
    def __str__(self):
        return self.prova

   
class Nota(models.Model):
    nota = models.DecimalField(max_digits=3, decimal_places=1)
    tipo = models.ForeignKey(TipoAvaliacao, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nota} {self.tipo}'
    

class DisciplinaCurso(models.Model):
    nome = models.CharField(max_length=255)
    cargaHoraria = models.DecimalField(max_digits=6, decimal_places=2)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.ForeignKey(PeriodoTurma, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} {self.cargaHoraria} {self.curso} {self.periodo}'