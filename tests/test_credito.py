# Importa o framework de testes.
import unittest
# Importa o mock usado nos testes.
from unittest.mock import MagicMock

# Importa os itens testados.
from credito import APROVADO, NEGADO, ProcessadorCredito, ServicoCredito


# Declara a suíte de testes do processador.
class ProcessadorCreditoTest(unittest.TestCase):
    # Prepara os objetos compartilhados pelos testes.
    def setUp(self):
        # Cria o mock do serviço de crédito.
        self.servico_mock = MagicMock(spec=ServicoCredito)
        # Cria o processador com a dependência mockada.
        self.processador = ProcessadorCredito(self.servico_mock)

    # Testa score muito baixo.
    def test_ct01_score_muito_baixo_retorna_negado(self):
        # Define o score retornado pelo mock.
        self.servico_mock.obter_score.return_value = 150

        # Executa a análise da proposta.
        resultado = self.processador.analisar_proposta("12345678900", 500)

        # Verifica que o resultado foi negado.
        self.assertEqual(NEGADO, resultado)
        # Verifica a chamada ao serviço com o CPF informado.
        self.servico_mock.obter_score.assert_called_once_with("12345678900")

    # Testa score médio com valor alto.
    def test_ct02_score_medio_valor_alto_retorna_negado(self):
        # Define o score retornado pelo mock.
        self.servico_mock.obter_score.return_value = 400

        # Executa a análise da proposta.
        resultado = self.processador.analisar_proposta("12345678901", 2000)

        # Verifica que o resultado foi negado.
        self.assertEqual(NEGADO, resultado)

    # Testa score médio com valor baixo.
    def test_ct03_score_medio_valor_baixo_retorna_aprovado(self):
        # Define o score retornado pelo mock.
        self.servico_mock.obter_score.return_value = 400

        # Executa a análise da proposta.
        resultado = self.processador.analisar_proposta("12345678902", 500)

        # Verifica que o resultado foi aprovado.
        self.assertEqual(APROVADO, resultado)

    # Testa score alto.
    def test_ct04_score_alto_retorna_aprovado(self):
        # Define o score retornado pelo mock.
        self.servico_mock.obter_score.return_value = 800

        # Executa a análise da proposta.
        resultado = self.processador.analisar_proposta("12345678903", 10000)

        # Verifica que o resultado foi aprovado.
        self.assertEqual(APROVADO, resultado)

    # Testa falha do serviço externo.
    def test_ct05_servico_offline_retorna_negado(self):
        # Define a exceção gerada pelo mock.
        self.servico_mock.obter_score.side_effect = RuntimeError("serviço indisponível")

        # Verifica o log de erro durante a análise.
        with self.assertLogs("credito", level="ERROR"):
            # Executa a análise da proposta.
            resultado = self.processador.analisar_proposta("12345678904", 100)

        # Verifica que o resultado foi negado.
        self.assertEqual(NEGADO, resultado)


# Executa os testes diretamente pelo arquivo.
if __name__ == "__main__":
    # Inicia o runner padrão do unittest.
    unittest.main()
