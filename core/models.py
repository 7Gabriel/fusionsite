import uuid
from django.db import models
from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Base(models.Model):
    criado = models.DateField(auto_now_add=True)
    modificado = models.DateField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Grafico'),
        ('lni-users', 'Usuarios'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )
    servico = models.CharField(max_length=100)
    descricao = models.TextField(max_length=200)
    icone = models.CharField(max_length=12, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico


class Cargo(Base): 
    cargo = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo


class Equipe(Base):
    nome = models.CharField(max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField(max_length=200)
    imagem = StdImageField(upload_to=get_file_path,variations={'thumb': {'width': 400, 'height': 400, 'crop': True}})
    facebook = models.CharField(max_length=100, default='#')
    twitter = models.CharField(max_length=100, default='#')
    instagram = models.CharField(max_length=100, default='#')

    class Meta:
        verbose_name= 'Funcionario'
        verbose_name_plural = 'Funcionarios'

    def __str__(self):
        return self.nome


class FeatureLeft(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-laptop-phone', 'Telefone'),
        ('lni-users', 'Usuarios'),
        ('lni-layers', 'Design'),
        ('lni-leaf', 'Folha'),
        ('lni-rocket', 'Foguete'),
    )
    feature = models.CharField(max_length=100)
    icone = models.CharField(max_length=16, choices=ICONE_CHOICES)
    descricao = models.TextField(max_length=200)

    class Meta:
        verbose_name = 'Feature Left'
        verbose_name_plural = 'Features Left'

    def __str__(self):
        return self.feature


class FeatureRight(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-laptop-phone', 'Telefone'),
        ('lni-users', 'Usuarios'),
        ('lni-layers', 'Design'),
        ('lni-leaf', 'Folha'),
        ('lni-rocket', 'Foguete'),
    )
    feature = models.CharField(max_length=100)
    icone = models.CharField(max_length=16, choices=ICONE_CHOICES)
    descricao = models.TextField(max_length=200)

    class Meta:
        verbose_name = 'Feature Right'
        verbose_name_plural = 'Features Right'

    def __str__(self):
        return self.feature