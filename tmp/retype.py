# adjust the shiptype of these vessels

import os

path = os.path.join('shiptype','36_')

mmsis = set([fn.split('_')[0] for fn in os.listdir(path)])

print(len(mmsis))
