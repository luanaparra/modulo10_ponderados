# src/logging_config.py
import logging
import logging.handlers
import time

class LoggerSetup():

    def __init__(self):
        # Pega a instância do logger
        self.logger = logging.getLogger('')
        # Invoca o método que configura o logger
        self.setup_logging()

    def setup_logging(self):
        # Adiciona um formatador para o logger - utilizando a sintaxe de JSON
        LOG_FORMAT = '{"time": "%(asctime)s", "name": "%(name)s", "level": "%(levelname)s", "message": "%(message)s"}'
        # Setando o nível do log para INFO.
        logging.basicConfig(level=logging.INFO, format=LOG_FORMAT, filename="logs/fastapi.log")

        # Adiciona o formatador ao logger
        formatter = logging.Formatter(LOG_FORMAT)

        # Adiciona um handler para que os dados armazenados no logger também possam ser exibidos na tela
        console=logging.StreamHandler()
        # Adiciona o formatador para o handler definido
        console.setFormatter(formatter)

        # Com os dois handlers criados, adicionamos eles ao logger
        self.logger.addHandler(console)


