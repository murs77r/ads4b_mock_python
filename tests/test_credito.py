import unittest
from unittest.mock import MagicMock

from credito import APROVADO, NEGADO, ProcessadorCredito, ServicoCredito


class ProcessadorCreditoTest(unittest.TestCase):
    def setUp(self):
        self.servico_mock = MagicMock(spec=ServicoCredito)
        self.processador = ProcessadorCredito(self.servico_mock)

    def test_ct01_score_muito_baixo_retorna_negado(self):
        self.servico_mock.obter_score.return_value = 150

        resultado = self.processador.analisar_proposta("12345678900", 500)

        self.assertEqual(NEGADO, resultado)
        self.servico_mock.obter_score.assert_called_once_with("12345678900")

    def test_ct02_score_medio_valor_alto_retorna_negado(self):
        self.servico_mock.obter_score.return_value = 400

        resultado = self.processador.analisar_proposta("12345678901", 2000)

        self.assertEqual(NEGADO, resultado)

    def test_ct03_score_medio_valor_baixo_retorna_aprovado(self):
        self.servico_mock.obter_score.return_value = 400

        resultado = self.processador.analisar_proposta("12345678902", 500)

        self.assertEqual(APROVADO, resultado)

    def test_ct04_score_alto_retorna_aprovado(self):
        self.servico_mock.obter_score.return_value = 800

        resultado = self.processador.analisar_proposta("12345678903", 10000)

        self.assertEqual(APROVADO, resultado)

    def test_ct05_servico_offline_retorna_negado(self):
        self.servico_mock.obter_score.side_effect = RuntimeError("serviço indisponível")

        with self.assertLogs("credito", level="ERROR"):
            resultado = self.processador.analisar_proposta("12345678904", 100)

        self.assertEqual(NEGADO, resultado)


if __name__ == "__main__":
    unittest.main()
