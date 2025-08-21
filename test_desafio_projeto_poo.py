import unittest
from desafio_projeto_poo import PessoaFisica, ContaCorrente, Deposito, Saque


class TestBancoOperacoes(unittest.TestCase):
    
    def setUp(self):
        self.cliente = PessoaFisica("João Silva", "01/01/1990", "12345678901", "Rua A, 123")
        self.conta = ContaCorrente.nova_conta(self.cliente, 1)
        self.cliente.adicionar_conta(self.conta)
    
    def test_criar_cliente(self):
        self.assertEqual(self.cliente.nome, "João Silva")
        self.assertEqual(self.cliente.cpf, "12345678901")
        self.assertEqual(len(self.cliente.contas), 1)
    
    def test_criar_conta(self):
        self.assertEqual(self.conta.numero, 1)
        self.assertEqual(self.conta.agencia, "0010")
        self.assertEqual(self.conta.saldo, 0)
        self.assertEqual(self.conta.cliente, self.cliente)
    
    def test_depositar(self):
        deposito = Deposito(100.0)
        deposito.registrar(self.conta)
        
        self.assertEqual(self.conta.saldo, 100.0)
        self.assertEqual(len(self.conta.historico.transacoes), 1)
        self.assertEqual(self.conta.historico.transacoes[0]["tipo"], "Deposito")
    
    def test_sacar_com_saldo(self):
        self.conta.depositar(200.0)
        
        saque = Saque(50.0)
        saque.registrar(self.conta)
        
        self.assertEqual(self.conta.saldo, 150.0)
    
    def test_sacar_sem_saldo(self):
        saque = Saque(100.0)
        resultado = saque.registrar(self.conta)
        
        self.assertEqual(self.conta.saldo, 0)
        self.assertEqual(len(self.conta.historico.transacoes), 0)
    
    def test_limite_saque_conta_corrente(self):
        self.conta.depositar(1000.0)
        
        saque = Saque(600.0)
        saque.registrar(self.conta)
        
        self.assertEqual(self.conta.saldo, 1000.0)
    
    def test_limite_quantidade_saques(self):
        self.conta.depositar(1000.0)
        
        for i in range(3):
            saque = Saque(100.0)
            saque.registrar(self.conta)
        
        self.assertEqual(self.conta.saldo, 700.0)
        
        saque_extra = Saque(100.0)
        saque_extra.registrar(self.conta)
        
        self.assertEqual(self.conta.saldo, 700.0)
    
    def test_historico_transacoes(self):
        deposito = Deposito(200.0)
        deposito.registrar(self.conta)
        
        saque = Saque(50.0)
        saque.registrar(self.conta)
        
        transacoes = self.conta.historico.transacoes
        self.assertEqual(len(transacoes), 2)
        self.assertEqual(transacoes[0]["tipo"], "Deposito")
        self.assertEqual(transacoes[1]["tipo"], "Saque")


if __name__ == "__main__":
    unittest.main()