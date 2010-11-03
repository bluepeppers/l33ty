#/usr/bin/env python2
#Run l33ty script

import sys
import os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('.'))

from l33ty import twisted_server
twisted_server.run_leety()