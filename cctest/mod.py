import os
from pathlib import Path

def f(base_dir=Path.cwd()):
    if (base_dir / 'no.txt').exists():
        return

    (base_dir / 'yes.txt').write_text('42')


    
