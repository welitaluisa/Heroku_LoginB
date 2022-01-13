
import pytest


from pages import login_page
from pages.login_page import LoginPage


# um padrão para o PyTest executar no início e no final dos testes
@pytest.fixture
def login(driver): # deixou de receber a request para receber diretamente a função driver

    return login_page.LoginPage(driver)

def testar_login_com_sucesso(login):
    # Faça o login com este usuário e senha
    login.com_('tomsmith', 'SuperSecretPassword!')
    # Validar o resultado = mensagem de sucesso presenta
    assert login.vejo_mensagem_de_sucesso()


def testar_login_com_usuario_invalido(login):
    login.com_('juca', 'SuperSecretPassword!')
    assert login.vejo_mensagem_de_falha()


def testar_login_com_senha_invalida(login):
    login.com_('tomsmith', 'xpto1234')
    assert login.vejo_mensagem_de_falha()
