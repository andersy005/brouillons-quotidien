from dask_mpi import initialize

initialize()

import socket

from distributed.scheduler import logger

import dask.array as da
from dask.distributed import Client

client = Client()  # Connect this local process to remote workers

host = client.run_on_scheduler(socket.gethostname)
port = client.scheduler_info()['services']['dashboard']
login_node_address = (
    'supercomputer.university.edu'  # Change this to the address/domain of your login node
)

logger.info(f'ssh -N -L {port}:{host}:{port} {login_node_address}')

logger.info('HELLO' * 10)
print('WORLD' * 10)

x = da.random.random((200, 10_000, 5_000), chunks=(20, 1_000, 1_000))
y = x.std(axis=0)
y = y.compute()
print(y)
