import subprocess
from docopt import docopt

import logging
import logging.handlers

logging.basicConfig(level=logging.INFO,  filename='logs.log', filemode='a', format='%(message)s  %(asctime)s', datefmt="%Y-%m-%d %T")


logger = logging.getLogger()

logger.addHandler(logging.handlers.SysLogHandler( ))


"""THis version of beacon trigger uses subprocess"""
__program__ = 'beacon_trigger'
__version__ = 'Version 1.4'
__revision__ = 'Updated the error "nonetype"'

def args():

  usage = """
  Usage:
    beacon_trigger.py <driver_id> [--action=<action>]
    beacon_trigger.py --version
    beacon_trigger.py (-h | --help)


  Options:
    -h --help     Show this help message and exit.
    --action=<action>  Action format (enabled  or disabled ) [default: enabled].

  """
  version = '{} VER: {} REV: {}'.format(__program__, __version__, __revision__)
  args = docopt(usage, version=version)
  return args	

def trigger_beacon(drive_id, action):
    cmd = f'/v1/drives/{drive_id} {{"beacon": "{action}"}}'
    cmd = ['/opt/ITDT/itdt', '-f', drive_id, 'ros', 'PATCH', cmd]

    print(f'Driver id: {drive_id}')
    print(f'Trigger action: {action}')
    print(f'Command to process: \n ~ {cmd}')
    com = ' '.join(cmd)
    print(f'Command to process: \n ~ {com}')


    try:

        process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        output, error = process.communicate()
        
        if output is not None:
            logging.info(f"Output: {output.decode('utf-8')}\n")
            print(output.decode('utf-8'))
            print(f"Success triggering beacon: \n {output.decode('utf-8')}")
            

        if error is not None:
            logging.info(f"Error: {error.decode('utf-8')}\n")
            print(f"Error triggering beacon: \n {error.decode('utf-8')}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main(args):
    """
    
    # Example usage:
        python beacon_trigger.py TAPE123 --action on

    """

    trigger_beacon(args['<driver_id>'], args['--action'])


if __name__ == '__main__':
    ARGS = args()
    main(ARGS)