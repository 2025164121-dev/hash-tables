import matplotlib.pyplot as plt
import numpy as np

# Graph 1: integer rules
rules = ["k % 65,536", "k % 65,521", "Fibonacci", "fmix64", "Universal"]
ids   = [1.06, 1.06, 1.07, 1.38, 1.32]
addr  = [6.61, 1.00, 1.35, 1.38, None]
x, w = np.arange(len(rules)), 0.38
fig, ax = plt.subplots(figsize=(9, 5))
ax.bar(x - w/2, ids, w, label="Student IDs")
ax.bar(x + w/2, [a or 0 for a in addr], w, label="Aligned addresses")
for i, v in enumerate(ids):
    ax.text(x[i] - w/2, v + 0.05, f"{v:.2f}", ha="center")
for i, v in enumerate(addr):
    ax.text(x[i] + w/2, (v or 0) + 0.05, "n/a" if v is None else f"{v:.2f}", ha="center")
ax.set_xticks(x); ax.set_xticklabels(rules)
ax.set_ylabel("avg_cmp (estimated comparisons)")
ax.set_title("Integer hashing: avg_cmp by rule and key set")
ax.legend(); plt.tight_layout()
plt.savefig("graph1_integer_avg_cmp.png", dpi=200)

# Graph 2: string functions (log scale)
funcs = ["Character sum", "poly31", "djb2", "FNV-1a"]
sid  = [1200.94, 1.68, 1.78, 1.42]
item = [798.25, 1.79, 1.81, 1.44]
x = np.arange(len(funcs))
fig, ax = plt.subplots(figsize=(9, 5))
ax.bar(x - w/2, sid, w, label="Student ID strings")
ax.bar(x + w/2, item, w, label="item0 to item49999")
for i in range(len(funcs)):
    ax.text(x[i] - w/2, sid[i] * 1.05, f"{sid[i]:.2f}", ha="center")
    ax.text(x[i] + w/2, item[i] * 1.05, f"{item[i]:.2f}", ha="center")
ax.set_yscale("log")
ax.set_xticks(x); ax.set_xticklabels(funcs)
ax.set_ylabel("avg_cmp (log scale)")
ax.set_title("String hashing: avg_cmp by function and key set")
ax.legend(); plt.tight_layout()
plt.savefig("graph2_string_avg_cmp.png", dpi=200)

