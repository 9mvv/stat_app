import logging
import tgl

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

def warning(text):
    logging.warning('[warn] '+ text)
def info(text):
    logging.info('[info] '+ text)
def error(text):
    logging.error('[error] '+ text)
    tgl.send(text)