# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/10_some_os_functions.ipynb.

# %% auto 0
__all__ = ['swift_user', 'swift_password', 'my_path', 'space', 'branch', 'tee', 'last', 'tree']

# %% ../nbs/10_some_os_functions.ipynb 3
import os
from pathlib import Path

# %% ../nbs/10_some_os_functions.ipynb 4
swift_user = 'SWIFT_USER'
swift_password = 'SWIFT_PASSWORD'
os.environ.setdefault('SWIFT_USER', 'TM3_D022785_SW')
os.environ.setdefault('SWIFT_PASSWORD', 'k7G3]e[7GpfgYP)YjGeuM1dk9qFaNw' )
print(os.environ.get(swift_user))
print(os.environ.get(swift_password))

# %% ../nbs/10_some_os_functions.ipynb 5
print(os.environ)

# %% ../nbs/10_some_os_functions.ipynb 7
my_path = os.path.dirname(os.path.abspath(''))
my_path

# %% ../nbs/10_some_os_functions.ipynb 11
# prefix components:
space =  '    '
branch = '│   '
# pointers:
tee =    '├── '
last =   '└── '

# %% ../nbs/10_some_os_functions.ipynb 12
def tree(dir_path: Path, prefix: str=''):
    """A recursive generator, given a directory Path object
    will yield a visual tree structure line by line
    with each line prefixed by the same characters
    """    
    contents = list(dir_path.iterdir())
    # contents each get pointers that are ├── with a final └── :
    pointers = [tee] * (len(contents) - 1) + [last]
    for pointer, path in zip(pointers, contents):
        yield prefix + pointer + path.name
        if path.is_dir(): # extend the prefix and recurse:
            extension = branch if pointer == tee else space 
            # i.e. space because last, └── , above so no more |
            yield from tree(path, prefix=prefix+extension)
            

# %% ../nbs/10_some_os_functions.ipynb 13
for line in tree(Path('.')):
    # api.send('output', line)
    print(line)
