import numpy as np

# 2×2 factorial CAR data
full_occ_bn = [0.776, 0.654, 0.746]        # ON, BN  (n=3)
detach_bn   = [0.774, 0.736, 0.762, 0.794]  # OFF, BN (n=4)
full_occ_ln = [0.792, 0.798, 0.762, 0.740]  # ON, LN  (n=4)
detach_ln   = [0.826, 0.802, 0.778]         # OFF, LN (n=3)

data = np.array(full_occ_bn + detach_bn + full_occ_ln + detach_ln)
n = len(data)  # 14

grad = np.array([0]*3 + [1]*4 + [0]*4 + [1]*3)  # 0=ON, 1=OFF
norm = np.array([0]*3 + [0]*4 + [1]*4 + [1]*3)  # 0=BN, 1=LN

def ss_resid(X, y):
    beta = np.linalg.lstsq(X, y, rcond=None)[0]
    return np.sum((y - X @ beta)**2)

def compute_type2_f(y, g, nm):
    n = len(y)
    inter = g * nm
    X_full = np.column_stack([np.ones(n), g, nm, inter])
    X_A    = np.column_stack([np.ones(n), g])
    X_B    = np.column_stack([np.ones(n), nm])
    X_AB   = np.column_stack([np.ones(n), g, nm])

    ssr_full = ss_resid(X_full, y)
    ssr_A    = ss_resid(X_A, y)
    ssr_B    = ss_resid(X_B, y)
    ssr_AB   = ss_resid(X_AB, y)

    ss_grad  = ssr_B  - ssr_AB   # A adjusted for B
    ss_norm  = ssr_A  - ssr_AB   # B adjusted for A
    ss_inter = ssr_AB - ssr_full # AB adjusted for A+B

    ms_resid = ssr_full / (n - 4)

    f_grad  = (ss_grad  / 1) / ms_resid
    f_norm  = (ss_norm  / 1) / ms_resid
    f_inter = (ss_inter / 1) / ms_resid
    return f_grad, f_norm, f_inter

# Observed
f_obs = compute_type2_f(data, grad, norm)
print("Observed F-statistics (Type II ANOVA):")
print(f"  Gradient flow: F(1,10) = {f_obs[0]:.2f}")
print(f"  Normalization: F(1,10) = {f_obs[1]:.2f}")
print(f"  Interaction:   F(1,10) = {f_obs[2]:.2f}")

# Permutation test (10,000 permutations)
np.random.seed(42)
n_perm = 10000
count_grad = 0
count_norm = 0
count_inter = 0

for i in range(n_perm):
    perm = np.random.permutation(data)
    fg, fn, fi = compute_type2_f(perm, grad, norm)
    if fg >= f_obs[0]: count_grad += 1
    if fn >= f_obs[1]: count_norm += 1
    if fi >= f_obs[2]: count_inter += 1

p_grad  = count_grad  / n_perm
p_norm  = count_norm  / n_perm
p_inter = count_inter / n_perm

print(f"\nPermutation p-values ({n_perm:,} permutations):")
print(f"  Gradient flow: p_perm = {p_grad:.3f}")
print(f"  Normalization: p_perm = {p_norm:.3f}")
print(f"  Interaction:   p_perm = {p_inter:.3f}")
