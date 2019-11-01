'''
Arquivo de testes
'''
from com.impacta.calculadora.operacoes import soma


def test_soma():
    '''
    Teste de soma
    '''
    assert soma(1, 2) == 3
