import server
import logging.config
import sys
import re

import database_mysql

logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)


def get_ip():
    """Set different IP"""
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

    sql_status = database_mysql.start_mysql()

    if sql_status[0] != 0:
        logger.critical('Can\'t connect to MySQL !')

    if get_ip() is not None:
        host = server.HostServer(host=get_ip())

    else:
        host = server.HostServer()

    try:
        logger.info('Server ON')
        host.\
            starhost().\
            serve_forever()

    except (KeyboardInterrupt, OSError):
        logger.info('Server OFF')
        host.stophost()
