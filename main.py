import re
import sys

import database_mysql
from logging_conf import logger


def get_ip():
    """Set different IP"""
    args = []

    for arg in sys.argv:
        args.append(arg)

    if len(args) == 1:
        return None

    elif len(args) == 2:
        if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", args[1]):
            logger.debug(f'Ip was set to : {args[1]}')

            return args[1]

        else:
            logger.error(f'Bad Ip')
            logger.warning('Ip was default.')

            return None

    else:
        logger.critical('Too many arguments.')
        sys.exit()


if __name__ == '__main__':
    sql_status = database_mysql.start_mysql()

    if sql_status[0] != 0:
        logger.critical('Can\'t connect to MySQL !!!')
        sys.exit()

    import server

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
