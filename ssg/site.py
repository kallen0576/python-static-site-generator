from pathlib import Path
from typing_extensions import Self

class Site():
    def __init__(self,dest,source):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self,path):
        directory = self.dest/path.relative_to(self.source)
        directory.mkdir(parents = True, exit_ok = True)
    def build(self):
        self.dest.mkdir(parents = True, exit_ok = True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)


