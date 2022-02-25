import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sample = np.array([1.0069, 1.0081, 0.9924, 1.0173, 0.9958, 0.9840, 0.9929, 1.0083,
1.0068, 0.9886, 0.9775, 1.0128, 1.0107, 1.0025, 0.9862, 1.0038,
0.9998, 0.9978, 0.9968, 1.0014, 0.9984, 0.9994, 1.0262, 1.0069,
1.0053, 1.0046, 0.9809, 0.9879, 1.0150, 0.9901, 1.0143, 0.9948,
0.9917, 1.0096, 1.0087])
M = sample.mean()
CKO = sample.std()

UCLX = M + 3*CKO
LCLX = M - 3*CKO

gist = sns.histplot(sample,kde=True, linewidth=0, color='b')
plt.title("Гистограмма")
plt.xlabel("Значения")
plt.ylabel("Частость")

fig, ax = plt.subplots()
ax.plot(sample, '-o', color='b')
ax.axhline(y=UCLX, color='r', label='UCLX')
ax.axhline(y=M, linestyle='--', color='g', label='CL')
ax.axhline(y=LCLX, color='y', label='LCLX')
plt.title("ККШ")
plt.ylabel("Значения")
plt.xlabel("Количество значений")
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.grid()
plt.show()
