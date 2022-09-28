import server
import logging.config
import sys
import re

logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)


def get_ip():
    try:
        ip = sys.argv[1]

        if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
            logger.debug(f'Ip was set to : {ip}')

            return sys.argv[1]

        else:
            logger.critical('Bad Ip')
            raise Exception('Bad Ip')

    except IndexError:
        return None


if __name__ == '__main__':
    if get_ip() is not None:
        host = server.HostServer(host=get_ip())

    else:
        host = server.HostServer()

    try:
        logger.info('Server ON')
        host.\
            starhost().\
            serve_forever()

    except (KeyboardInterrupt, OSError) as e:
        logger.info('Server OFF')
        host.stophost()
