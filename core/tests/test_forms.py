from django.test import TestCase

from core.forms import ContatoForm

class ContatoFormTestCase(TestCase):

    def setUp(self):
        self.nome = 'Felicio Jones'
        self.email = 'felicio@gmail.com'
        self.assunto = 'Um Assunto'
        self.mesagem = 'Uma mensagem bonita'

        self.dados = {
            'nome': self.nome,
            'email': self.email,
            'assunto': self.assunto,
            'mensagem': self.mesagem
        }

        self.form = ContatoForm(data=self.dados)

    def test_send_email(self):
        form1 = ContatoForm(data=self.dados)
        form1.is_valid()
        res1 = form1.send_email()

        form2 = ContatoForm(data=self.dados)
        form2.is_valid()
        res2 = form2.send_email()


        self.assertEquals(res1, res2)


