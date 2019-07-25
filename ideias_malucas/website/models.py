from django.db import models

# Create your models here.

class Pessoa(models.Model):
    GENEROS = (
        ('F','Femenino'),
        ('M','Masculino'),
        ('O', 'Outro'),
    )
    
    nome = models.CharField(
        max_length= 225,
        verbose_name= 'Nome'
    )

    sobrenome = models.CharField(
    max_length=225,
    verbose_name='Sobrenome'
    )

    generos = models.CharField(
    max_length=225,
    verbose_name='GENERO',
    choices=GENEROS
    )  

    email = models.EmailField(
    max_length=225,
    verbose_name='E-mail'
    )

    data_de_criacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome+ ' ' + self.sobrenome