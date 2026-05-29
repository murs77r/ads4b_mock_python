# Importa o módulo de log.
import logging
# Importa recursos de classe abstrata.
from abc import ABC, abstractmethod

# Cria o logger do módulo.
LOGGER = logging.getLogger(__name__)

# Define o status de aprovação.
APROVADO = "APROVADO"
# Define o status de negação.
NEGADO = "NEGADO"


# Declara a interface do serviço de crédito.
class ServicoCredito(ABC):
    # Exige implementação do método de score.
    @abstractmethod
    # Define o contrato para obter o score.
    def obter_score(self, cpf: str) -> int:
        # Sinaliza ausência de implementação.
        raise NotImplementedError


# Declara o processador de crédito.
class ProcessadorCredito:
    # Inicializa o processador com o serviço.
    def __init__(self, servico_credito: ServicoCredito):
        # Armazena a dependência do serviço.
        self.servico_credito = servico_credito

    # Analisa a proposta de crédito.
    def analisar_proposta(self, cpf: str, valor_solicitado: float) -> str:
        # Tenta consultar o score.
        try:
            # Obtém o score do CPF.
            score = self.servico_credito.obter_score(cpf)
        # Captura falhas do serviço externo.
        except Exception:
            # Registra o erro da consulta.
            LOGGER.exception("Erro ao consultar serviço externo de crédito para o CPF %s", cpf)
            # Nega a proposta em caso de erro.
            return NEGADO

        # Nega score muito baixo.
        if score < 200:
            # Retorna negação para score baixo.
            return NEGADO
        # Avalia score intermediário.
        if score < 600:
            # Aprova valor baixo e nega valor alto.
            return APROVADO if valor_solicitado < 1000 else NEGADO
        # Aprova score alto.
        return APROVADO
