import logging

def setup_logger(log_file):
    logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')
    logger = logging.getLogger()
    return logger

def log_packet(logger, packet):
    logger.info(packet)
