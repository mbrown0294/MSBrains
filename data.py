# data.py

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

a = np.fromfile('/Users/brownmr1/precision_med/cerveaux/casp/phantom_1.0mm_msles1_crisp.rawb', dtype=np.uint8)
b = np.fromfile('/Users/brownmr1/precision_med/cerveaux/casp/phantom_1.0mm_msles2_crisp.rawb', dtype=np.uint8)
c = np.fromfile('/Users/brownmr1/precision_med/cerveaux/casp/phantom_1.0mm_msles3_crisp.rawb', dtype=np.uint8)
d = np.fromfile('/Users/brownmr1/precision_med/cerveaux/casp/t1_ai_msles2_1mm_pn3_rf20.rawb', dtype=np.uint8)
e = np.fromfile('/Users/brownmr1/precision_med/cerveaux/casp/t1_ai_msles2_1mm_pn5_rf20.rawb', dtype=np.uint8)

ms_brains = np.vstack((a,b,c,d,e))
print("MS shape = {}".format(ms_brains.shape))


f = np.fromfile('/Users/brownmr1/precision_med/cerveaux/cn/subject43_crisp_v.rawb', dtype=np.uint8)
g = np.fromfile('/Users/brownmr1/precision_med/cerveaux/cn/subject44_crisp_v.rawb', dtype=np.uint8)
h = np.fromfile('/Users/brownmr1/precision_med/cerveaux/cn/subject45_crisp_v.rawb', dtype=np.uint8)
i = np.fromfile('/Users/brownmr1/precision_med/cerveaux/cn/subject47_crisp_v.rawb', dtype=np.uint8)
j = np.fromfile('/Users/brownmr1/precision_med/cerveaux/cn/subject51_crisp_v.rawb', dtype=np.uint8)

norm_brains = np.stack((f,g,h,i,j))
print("Normal shape = {}".format(norm_brains.shape))



# svc = svm.LinearSVC()
# svc.train()