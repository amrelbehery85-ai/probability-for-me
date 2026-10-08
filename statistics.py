import numpy as np
import matplotlib.pyplot as plt

values = np.array([0, 1, 2, 3])
pmf = np.array([1/8, 3/8, 3/8, 1/8])

print("مجموع الاحتمالات =", pmf.sum())

mean = np.sum(values * pmf)
var = np.sum(values**2 * pmf) - mean**2
print("E[X] =", mean, "| Var =", var)

plt.bar(values, pmf)
plt.xlabel("x"); plt.ylabel("P(X = x)")
plt.title("PMF لرمي عملة 3 مرات")
plt.show()