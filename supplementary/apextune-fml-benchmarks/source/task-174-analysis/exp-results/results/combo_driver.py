"""task-174 phase D: 2x2 factorial {K=1 vs K=3 restarts} x {no-cal vs adaptive-cal}
on a champion mechanism. All selection/calibration fitted on the TRAIN side only.

For K models we use K DISJOINT train sub-slices (each ~70%/K data, ~same size as
the champion's normal training set) so the restart selection is size-fair.

Usage: python combo_driver.py <champ.py> <tag> [seed...]
"""
import importlib.util
import json
import os
import random
import sys
import time

import numpy as np

os.environ.setdefault('TF_CPP_MIN_LOG_LEVEL', '3')
os.environ.setdefault('TF_ENABLE_ONEDNN_OPTS', '0')

REPO = '/root/fml-bench/workspace/Fairness_and_Bias_aif360/AIF360'
sys.path.insert(0, REPO)

import tensorflow.compat.v1 as tf  # noqa: E402

tf.disable_eager_execution()
for _g in tf.config.list_physical_devices('GPU'):
    tf.config.experimental.set_memory_growth(_g, True)

from aif360.metrics import ClassificationMetric  # noqa: E402
from aif360.algorithms.preprocessing.optim_preproc_helpers.data_preproc_functions import load_preproc_data_compas  # noqa: E402

OUT = '/root/exp174/results'
PRIV = [{'sex': 1}]
UNPRIV = [{'sex': 0}]
DELTAS = np.round(np.linspace(-0.2, 0.2, 81), 4)
FLOOR = 0.63510101010101
K = 3


def set_seed(seed):
    os.environ['PYTHONHASHSEED'] = str(seed)
    random.seed(seed)
    np.random.seed(seed)
    import tensorflow as _tf
    _tf.random.set_seed(seed)


def load_mech(path):
    spec = importlib.util.spec_from_file_location('combo_mech', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_splits():
    d = load_preproc_data_compas()
    tr, pool = d.split([0.7], shuffle=True)
    val, test = pool.split([0.3], shuffle=True)
    return tr, val, test


def new_sess():
    s = tf.Session()
    s.close()
    tf.reset_default_graph()
    return tf.Session()


def train_one(cls, seed, train):
    set_seed(seed)
    sess = new_sess()
    m = cls(PRIV, UNPRIV, scope_name='d', debias=True, sess=sess, seed=seed)
    m.fit(train)
    return m, sess


def probs(model, sess, ds):
    d = ds.copy(deepcopy=True)
    d.labels = np.zeros_like(d.labels)
    d.scores = np.zeros_like(d.scores)
    return np.asarray(model.predict(d).scores, dtype=float).ravel()


def metrics(ds, p, pa, delta):
    thr = 0.5 + delta * (2.0 * pa - 1.0)
    hard = (p > thr).astype(float)
    deb = ds.copy(deepcopy=True)
    lab = hard.reshape(-1, 1).copy()
    lab[hard == 1.0] = ds.favorable_label
    lab[hard == 0.0] = ds.unfavorable_label
    deb.labels = lab
    deb.scores = p.reshape(-1, 1)
    cm = ClassificationMetric(ds, deb, unprivileged_groups=UNPRIV, privileged_groups=PRIV)
    return {'delta': float(delta), 'abs_aod': abs(float(cm.average_odds_difference())),
            'abs_eod': abs(float(cm.equal_opportunity_difference())),
            'abs_theil': abs(float(cm.theil_index())),
            'cls_acc': float(cm.accuracy())}


def fit_delta(p, pa, ds):
    best = None
    for d in DELTAS:
        m = metrics(ds, p, pa, d)
        if m['cls_acc'] < FLOOR:
            continue
        if best is None or m['abs_aod'] < best['abs_aod']:
            best = m
    return best


def P(ds):
    return np.asarray(ds.protected_attributes[:, ds.protected_attribute_names.index('sex')], float).ravel()


def main():
    path, tag = sys.argv[1], sys.argv[2]
    seeds = [int(s) for s in sys.argv[3:]] or [233, 1, 2, 3, 4, 5, 6, 7]
    cls = load_mech(path).AdversarialDebiasing
    train, val, _t = load_splits()
    val_pa = P(val)

    # K disjoint train sub-slices (for size-fair restarts), each split into train + holdout
    set_seed(0)
    parts = []
    rest = train
    for _ in range(K - 1):
        a, rest = rest.split([1.0 / (K - len(parts))], shuffle=True)
        parts.append(a)
    parts.append(rest)
    tr_parts, hol_parts = [], []
    for p in parts:
        a, b = p.split([0.85], shuffle=True)
        tr_parts.append(a)
        hol_parts.append(b)

    for s in seeds:
        t = time.time()
        # --- K=3: train on disjoint slices, select by holdout AOD ---
        km, ks, kh = [], [], []
        for i in range(K):
            m, sess = train_one(cls, s * 131 + i, tr_parts[i])
            km.append(m); ks.append(sess)
            kh.append(probs(m, sess, hol_parts[i]))
        holds = [metrics(hol_parts[i], kh[i], P(hol_parts[i]), 0.0) for i in range(K)]
        sel3 = int(np.argmin([h['abs_aod'] for h in holds]))
        p3 = probs(km[sel3], ks[sel3], val)

        # --- K=1: single model on the full train ---
        m1, sess1 = train_one(cls, s * 131 + 0, train)
        p1 = probs(m1, sess1, val)

        # --- adaptive cal for each (fit delta on the respective model's holdout) ---
        fit1 = fit_delta(probs(m1, sess1, hol_parts[0]), P(hol_parts[0]), hol_parts[0])
        fit3 = fit_delta(kh[sel3], P(hol_parts[sel3]), hol_parts[sel3])
        d1 = fit1['delta'] if fit1 else None
        d3 = fit3['delta'] if fit3 else None

        rec = {'seed': s, 'tag': tag, 'sel3': sel3,
               'K1_none': metrics(val, p1, val_pa, 0.0),
               'K1_cal': metrics(val, p1, val_pa, d1) if d1 is not None else None,
               'K3_none': metrics(val, p3, val_pa, 0.0),
               'K3_cal': metrics(val, p3, val_pa, d3) if d3 is not None else None,
               'd1': d1, 'd3': d3,
               'holdout_aod_per_restart': [round(h['abs_aod'], 5) for h in holds]}
        with open(f'{OUT}/D_{tag}_s{s}.json', 'w') as fh:
            json.dump(rec, fh, indent=1)
        for sess in ks + [sess1]:
            sess.close()
        f = lambda k: (f'{rec[k]["abs_aod"]:.5f}' if rec[k] else 'NONE')
        print(f'  seed {s:>3}: K1 none={f("K1_none")} cal={f("K1_cal")} | '
              f'K3 none={f("K3_none")} cal={f("K3_cal")} | d1={d1} d3={d3} ({time.time()-t:.0f}s)',
              flush=True)


if __name__ == '__main__':
    main()
