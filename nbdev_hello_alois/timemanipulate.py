# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/05_timemanipulation.ipynb.

# %% auto 0
__all__ = ['time_frame', 'begin', 'timestamp', 'dt', 'delta']

# %% ../nbs/05_timemanipulation.ipynb 2
import datetime
import time

time_frame = {"start": "01.01.2000 00:00:00.000000", "end": "31.12.2999 23:59:59.999999"}


# %% ../nbs/05_timemanipulation.ipynb 3
time_frame["start"]

# %% ../nbs/05_timemanipulation.ipynb 4
begin = datetime.datetime.strptime("01.01.2000 00:00:00", '%d.%m.%Y %H:%M:%S')
begin 
# print (datetime.fromisoformat(begin))

# %% ../nbs/05_timemanipulation.ipynb 5
from datetime import date
date.fromisoformat('2019-12-04')

# %% ../nbs/05_timemanipulation.ipynb 6
timestamp = datetime.datetime.now()
timestamp

# %% ../nbs/05_timemanipulation.ipynb 7
dt = datetime.datetime.now()
dt

# %% ../nbs/05_timemanipulation.ipynb 8
delta = dt - datetime.datetime(1970, 1, 1)
delta
