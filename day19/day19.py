import re
from functools import lru_cache

from util import dict_from_file

LARGE_NUMBER = 2147483647

mol = ('CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCa'
       'PMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFA'
       'rCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaS'
       'iThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgA'
       'rCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMg'
       'ArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlY'
       'CaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYP'
       'BCaFArCaSiAl')

avail = dict_from_file('input.txt', key='right')
print(avail)

count = 0
molecule = mol
while len(molecule) > 1:
    for key in sorted(avail.keys(), key=lambda x: -len(x)):
        add_to_count = len(list(re.finditer(key, molecule)))
        if add_to_count:
            molecule = molecule.replace(key, avail[key])
            count = count + add_to_count
            break
print(molecule)
print(count)