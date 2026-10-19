#!/usr/bin/env python3
"""Patch plan_001_collider_mbias_iv.py: align violation metrics with mediation/frontdoor."""
import sys

P = '/home/sonny/causal_annot_error_attrib/plan_001_collider_mbias_iv.py'
with open(P) as f:
    L = f.readlines()

orig_len = len(L)

def fl(pat, s=0):
    for i in range(s, len(L)):
        if pat in L[i]:
            return i
    print(f"FAIL: not found: {pat!r} from line {s}", file=sys.stderr)
    sys.exit(1)

# Find all anchor positions in ORIGINAL file
a = fl('def rand_search_collider')
b = fl('def rand_search_mbias')
c = fl('def rand_search_iv')
d = fl('= rand_search_collider()', a + 10)
e = fl('= rand_search_mbias()', b + 10)
f1 = fl('[misclass_amplifies]', d)
f2 = fl('[misclass_amplifies]', e)

print(f"Anchors: a={a} b={b} c={c} d={d} e={e} f1={f1} f2={f2}")

# ============================================================
# Step 1 (bottom-most): Replace M-bias random search in main()
# ============================================================
L[e-2:f2+1] = """\
    t1 = time.time()
    v, s, a, bc, bnc, true_b_m, cw, ma = rand_search_mbias()
    t2 = time.time()
    print(f"\\n  Random search (100k, {t2-t1:.1f}s): "
          f"violation={v:.1%}  sign_flip={s:.1%}  amplification={a:.1%}")
    print(f"  Supplementary: ctrl_worse={cw:.1%}  misclass_amplifies={ma:.1%}")
    print(f"  Bias stats: no_ctrl={bnc:+.4f}, true_A_ctrl={true_b_m:+.4f},"
          f" A*_ctrl mean={bc.mean():+.4f} std={bc.std():.4f}"
          f" range=[{bc.min():+.4f}, {bc.max():+.4f}]")
""".splitlines(keepends=True)

# ============================================================
# Step 2: Replace collider random search in main()
# ============================================================
L[d-2:f1+1] = """\
    t1 = time.time()
    v, s, a, bc, bnc, true_b, cw, ma = rand_search_collider()
    t2 = time.time()
    print(f"\\n  Random search (100k, {t2-t1:.1f}s): "
          f"violation={v:.1%}  sign_flip={s:.1%}  amplification={a:.1%}")
    print(f"  Supplementary: ctrl_worse={cw:.1%}  misclass_amplifies={ma:.1%}")
    print(f"  Bias stats: no_ctrl={bnc:+.4f}, true_A_ctrl={true_b:+.4f},"
          f" A*_ctrl mean={bc.mean():+.4f} std={bc.std():.4f}"
          f" range=[{bc.min():+.4f}, {bc.max():+.4f}]")
""".splitlines(keepends=True)

# ============================================================
# Step 3: Replace rand_search_mbias function
# ============================================================
L[b:c] = """\
def rand_search_mbias(n_search=100_000, N_ap=50_000, seed=42):
    rng = np.random.default_rng(seed)
    T, Y, A = _gen_mbias(N_ap, MBIAS_PARAMS, rng)
    u = rng.uniform(size=N_ap)
    N = float(N_ap)
    sT, sTT, sY, sTY = T.sum(), (T*T).sum(), Y.sum(), (T*Y).sum()

    clean = _fast_ols_all(T, Y, A, N, sT, sTT, sY, sTY)
    ones = np.ones(N_ap)
    tau_nc = _ols(np.column_stack([ones, T]), Y)[1]

    rng_s = np.random.default_rng(seed + 1)
    coefs = np.empty((n_search, 4))
    for i in range(n_search):
        C = rng_s.dirichlet([1, 1, 1], size=3).T
        Astar = _generate_Astar_fixed_u(A, C, u)
        coefs[i] = _fast_ols_all(T, Y, Astar, N, sT, sTT, sY, sTY)

    df = np.abs(coefs - clean)
    viol = np.any(df > .01, axis=1).mean()
    nz = np.abs(clean) > 1e-6
    sign = np.any(np.sign(coefs[:, nz]) != np.sign(clean[nz]), axis=1).mean()
    amp = np.any(np.abs(coefs) > np.abs(clean) + 1e-6, axis=1).mean()

    tau = MBIAS_PARAMS['tau']
    biases = coefs[:, 1] - tau
    true_bias = clean[1] - tau
    nc_bias = tau_nc - tau
    ctrl_worse = (np.abs(biases) > np.abs(nc_bias)).mean()
    misclass_amp = (np.abs(biases) > np.abs(true_bias)).mean()

    return viol, sign, amp, biases, nc_bias, true_bias, ctrl_worse, misclass_amp


""".splitlines(keepends=True)

# ============================================================
# Step 4: Replace rand_search_collider function
# ============================================================
L[a:b] = """\
def rand_search_collider(n_search=100_000, N_ap=50_000, seed=42):
    rng = np.random.default_rng(seed)
    T, Y, A = _gen_collider(N_ap, COLLIDER_PARAMS, rng)
    u = rng.uniform(size=N_ap)
    N = float(N_ap)
    sT, sTT, sY, sTY = T.sum(), (T*T).sum(), Y.sum(), (T*Y).sum()

    clean = _fast_ols_all(T, Y, A, N, sT, sTT, sY, sTY)
    ones = np.ones(N_ap)
    tau_nc = _ols(np.column_stack([ones, T]), Y)[1]

    rng_s = np.random.default_rng(seed + 1)
    coefs = np.empty((n_search, 4))
    for i in range(n_search):
        C = rng_s.dirichlet([1, 1, 1], size=3).T
        Astar = _generate_Astar_fixed_u(A, C, u)
        coefs[i] = _fast_ols_all(T, Y, Astar, N, sT, sTT, sY, sTY)

    df = np.abs(coefs - clean)
    viol = np.any(df > .01, axis=1).mean()
    nz = np.abs(clean) > 1e-6
    sign = np.any(np.sign(coefs[:, nz]) != np.sign(clean[nz]), axis=1).mean()
    amp = np.any(np.abs(coefs) > np.abs(clean) + 1e-6, axis=1).mean()

    tau = COLLIDER_PARAMS['tau']
    biases = coefs[:, 1] - tau
    true_bias = clean[1] - tau
    nc_bias = tau_nc - tau
    ctrl_worse = (np.abs(biases) > np.abs(nc_bias)).mean()
    misclass_amp = (np.abs(biases) > np.abs(true_bias)).mean()

    return viol, sign, amp, biases, nc_bias, true_bias, ctrl_worse, misclass_amp


""".splitlines(keepends=True)

# ============================================================
# Step 5: Insert _fast_ols_all before rand_search_collider
# ============================================================
idx = fl('def rand_search_collider')
L[idx:idx] = """\
def _fast_ols_all(T, Y, A_star, N, sT, sTT, sY, sTY):
    m1 = A_star == 1
    m2 = A_star == 2
    n1 = float(m1.sum())
    n2 = float(m2.sum())
    tD1 = T[m1].sum()
    tD2 = T[m2].sum()
    yD1 = Y[m1].sum()
    yD2 = Y[m2].sum()
    ZZ = np.array([[N, sT, n1, n2],
                   [sT, sTT, tD1, tD2],
                   [n1, tD1, n1, 0.0],
                   [n2, tD2, 0.0, n2]])
    ZY = np.array([sY, sTY, yD1, yD2])
    return np.linalg.solve(ZZ, ZY)


""".splitlines(keepends=True)

with open(P, 'w') as f:
    f.writelines(L)

print(f"OK: all 5 patches applied. {orig_len} -> {len(L)} lines")
