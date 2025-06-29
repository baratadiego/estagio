from django.db import models


class Estagiario(models.Model):
    """Dados do estagiário"""
    STATUS_CHOICES = [
        ('Ativo', 'Ativo'),
        ('Inativo', 'Inativo'),
    ]
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True)
    curso = models.CharField(max_length=100)
    periodo = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='Ativo')

    def __str__(self):
        return self.nome


class Convenio(models.Model):
    """Empresas conveniadas"""
    nome_empresa = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20, blank=True)
    responsavel = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_empresa


class Estagio(models.Model):
    """Estágios cadastrados"""
    STATUS_CHOICES = [
        ('Em andamento', 'Em andamento'),
        ('Finalizado', 'Finalizado'),
    ]
    estagiario = models.ForeignKey(Estagiario, related_name='estagios', on_delete=models.CASCADE)
    convenio = models.ForeignKey(Convenio, related_name='estagios', on_delete=models.CASCADE)
    supervisor = models.CharField(max_length=100)
    carga_horaria = models.PositiveIntegerField()
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Em andamento')

    def __str__(self):
        return f"{self.estagiario.nome} - {self.convenio.nome_empresa}"


class Documento(models.Model):
    """Documentos relacionados ao estágio"""
    TIPO_CHOICES = [
        ('Termo', 'Termo'),
        ('Plano', 'Plano'),
        ('Relatorio', 'Relatório'),
    ]
    estagio = models.ForeignKey(Estagio, related_name='documentos', on_delete=models.CASCADE)
    tipo_documento = models.CharField(max_length=20, choices=TIPO_CHOICES)
    arquivo = models.FileField(upload_to='documentos/')

    def __str__(self):
        return f"{self.tipo_documento} - {self.estagio}"


class Notificacao(models.Model):
    """Notificações enviadas ao estagiário"""
    estagiario = models.ForeignKey(Estagiario, related_name='notificacoes', on_delete=models.CASCADE)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)
    lida = models.BooleanField(default=False)

    def __str__(self):
        return self.mensagem[:50]
