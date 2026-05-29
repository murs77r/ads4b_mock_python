import logging
from abc import ABC, abstractmethod

LOGGER = logging.getLogger(__name__)

APROVADO = "APROVADO"
NEGADO = "NEGADO"


class ServicoCredito(ABC):
    @abstractmethod
    def obter_score(self, cpf: str) -> int:
        raise NotImplementedError


class ProcessadorCredito:
    def __init__(self, servico_credito: ServicoCredito):
        self.servico_credito = servico_credito

    def analisar_proposta(self, cpf: str, valor_solicitado: float) -> str:
        try:
            score = self.servico_credito.obter_score(cpf)
        except Exception:
            LOGGER.exception("Erro ao consultar serviço externo de crédito para o CPF %s", cpf)
            return NEGADO

        if score < 200:
            return NEGADO
        if score < 600:
            return APROVADO if valor_solicitado < 1000 else NEGADO
        return APROVADO
