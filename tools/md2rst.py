"""
User pandoc to generate rst files from md sources

http://johnmacfarlane.net/pandoc
"""

import subprocess
from plumbum.path import LocalWorkdir, LocalPath

if __name__ == '__main__':
    for p in LocalWorkdir().up().walk():
        assert isinstance(p, LocalPath)
        if p.basename.endswith('.md'):
            cmd = (["pandoc", "--from=markdown", "--to=rst", "-o",
                    "%s" % (p.dirname / (p.basename[:-3] + '.rst')),
                    "%s" % (p)])
            print(" ".join(cmd))
            subprocess.check_output(cmd)
