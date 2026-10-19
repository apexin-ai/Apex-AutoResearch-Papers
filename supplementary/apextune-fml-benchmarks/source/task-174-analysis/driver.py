"""task-174 offline AOD-noise calibration for fml-bench aif360.

Runs ONLY on the val split (never touches the hidden test split) with a
parameterised seed, and dumps per-row predictions so the val AOD sampling
noise can be bootstrapped. Two mechanisms: the pristine baseline and a
best-of-K restart wrapper around it.

Usage: python driver.py <mode>
  mode=smoke   one baseline run (determinism + duration)
  mode=all     full sweep -> results/*.json
"""
import argparse
import copy
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
_gpus = tf.config.list_physical_devices('GPU')
if _gpus:
    for _g in _gpus:
        tf.config.experimental.set_memory_growth(_g, True)

from aif360.metrics import ClassificationMetric  # noqa: E402
from aif360.algorithms.preprocessing.optim_preproc_helpers.data_preproc_functions import load_preproc_data_compas  # noqa: E402
from aif360.algorithms.inprocessing.adversarial_debiasing import AdversarialDebiasing  # noqa: E402

OUT = '/root/exp174/results'
PRIV = [{'sex': 1}]
UNPRIV = [{'sex': 0}]


def set_seed(seed):
    os.environ['PYTHONHASHSEED'] = str(seed)
    random.seed(seed)
    np.random.seed(seed)
    try:
        tf.random.set_seed(seed)
    except AttributeError:
        import tensorflow as _tf
        _tf.random.set_seed(seed)


def load_splits():
    """Reproduce the harness 70/9/21 split (val only is ever evaluated)."""
    d = load_preproc_data_compas()
    tr, pool = d.split([0.7], shuffle=True)
    val, test = pool.split([0.3], shuffle=True)
    return tr, val, test


def aod_from_rows(pa, y, yhat):
    """Average odds difference from per-row privileged flag, label, prediction."""
    pa = np.asarray(pa).ravel()
    y = np.asarray(y).ravel()
    yhat = np.asarray(yhat).ravel()

    def rates(mask):
        n = mask.sum()
        if n == 0:
            return (0.0, 0.0, 0)
        pos, neg = mask & (y == 1), mask & (y == 0)
        tpr = yhat[pos].mean() if pos.sum() else 0.0
        fpr = yhat[neg].mean() if neg.sum() else 0.0
        return (tpr, fpr, int(n))

    tpr_u, fpr_u, _ = rates(pa == 0)
    tpr_p, fpr_p, _ = rates(pa == 1)
    aod = 0.5 * ((tpr_u - tpr_p) + (fpr_u - fpr_p))
    return float(aod)


def bootstrap_aod(pa, y, yhat, n_boot=2000, seed=0):
    pa, y, yhat = np.asarray(pa).ravel(), np.asarray(y).ravel(), np.asarray(yhat).ravel()
    rng = np.random.default_rng(seed)
    n = len(y)
    vals = np.empty(n_boot)
    for i in range(n_boot):
        idx = rng.integers(0, n, n)
        vals[i] = abs(aod_from_rows(pa[idx], y[idx], yhat[idx]))
    return {'mean': float(vals.mean()), 'std': float(vals.std()),
            'p10': float(np.percentile(vals, 10)), 'p90': float(np.percentile(vals, 90))}


def evaluate(model, val):
    """Predict on a label-stripped copy (harness anti-exploit) and score."""
    pred_in = val.copy(deepcopy=True)
    pred_in.labels = np.zeros_like(pred_in.labels)
    pred_in.scores = np.zeros_like(pred_in.scores)
    out = model.predict(pred_in)
    cm = ClassificationMetric(val, out, unprivileged_groups=UNPRIV, privileged_groups=PRIV)
    return {
        'abs_aod': abs(float(cm.average_odds_difference())),
        'cls_acc': float(cm.accuracy()),
        'balanced_acc': float(0.5 * (cm.true_positive_rate() + cm.true_negative_rate())),
    }, out


def rows_of(val, out):
    pa = val.protected_attributes[:, val.protected_attribute_names.index('sex')]
    y = (val.labels.ravel() == val.favorable_label).astype(int)
    yhat = (out.scores.ravel() >= 0.5).astype(int)
    return pa.astype(int).tolist(), y.tolist(), yhat.tolist()


def new_session():
    sess = tf.Session()
    sess.close()
    tf.reset_default_graph()
    return tf.Session()


def run_baseline(seed, train, val, debias=True):
    set_seed(seed)
    sess = new_session()
    m = AdversarialDebiasing(PRIV, UNPRIV, scope_name='d', debias=debias, sess=sess, seed=seed)
    m.fit(train)
    res, out = evaluate(m, val)
    rows = rows_of(val, out)
    sess.close()
    return res, rows


class BestOfK:
    """Train K restarts; pick the one with the best held-out train-slice AOD.

    Robustness proxy is computed on a 15% slice carved from train only --
    never on the harness val split -- so selection cannot leak val signal.
    """

    def __init__(self, k=3, seed=0, holdout=0.15):
        self.k, self.seed, self.holdout = k, seed, holdout
        self.models, self.proxy = [], []

    def fit(self, train):
        d = copy.deepcopy(train)
        tr, hol = d.split([1 - self.holdout], shuffle=True)
        for i in range(self.k):
            s = self.seed * 100 + i
            set_seed(s)
            sess = new_session()
            m = AdversarialDebiasing(PRIV, UNPRIV, scope_name='d', debias=True, sess=sess, seed=s)
            m.fit(tr)
            r, _ = evaluate(m, hol)
            self.models.append(m)
            self.proxy.append(r['abs_aod'])
        self.best = int(np.argmin(self.proxy))
        return self

    def predict(self, dataset):
        return self.models[self.best].predict(dataset)


def run_bestofk(seed, train, val, k=3):
    set_seed(seed)
    b = BestOfK(k=k, seed=seed).fit(train)
    res, out = evaluate(b, val)
    rows = rows_of(val, out)
    return {**res, 'k': k, 'proxy': b.proxy, 'picked': b.best}, rows


def save(tag, res, rows, extra=None):
    os.makedirs(OUT, exist_ok=True)
    rec = {'tag': tag, **res}
    if extra:
        rec.update(extra)
    with open(f'{OUT}/{tag}.json', 'w') as fh:
        json.dump(rec, fh, indent=1)
    pa, y, yhat = rows
    if len(y):
        rec['bootstrap'] = bootstrap_aod(pa, y, yhat)
    with open(f'{OUT}/{tag}_rows.json', 'w') as fh:
        json.dump({'pa': pa, 'y': y, 'yhat': yhat}, fh)
    print(f'[{tag}] abs_aod={res["abs_aod"]:.5f} cls_acc={res["cls_acc"]:.4f} '
          f'boot_std={rec["bootstrap"]["std"]:.5f}', flush=True)
    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('mode', choices=['smoke', 'all'])
    a = ap.parse_args()

    t0 = time.time()
    train, val, _test = load_splits()  # _test intentionally never used
    print(f'splits ready in {time.time()-t0:.1f}s  train={train.features.shape[0]} '
          f'val={val.features.shape[0]}', flush=True)

    if a.mode == 'smoke':
        t = time.time()
        res, rows = run_baseline(233, train, val)
        print(f'smoke single run {time.time()-t:.1f}s', flush=True)
        save('smoke_baseline_s233_a', res, rows)
        return

    seeds = [233, 1, 2, 3, 4, 5, 6, 7]
    # A1 determinism: baseline seed 233 twice
    for rep in ('a', 'b'):
        t = time.time()
        res, rows = run_baseline(233, train, val)
        save(f'A1_baseline_s233_{rep}', res, rows, {'seconds': time.time()-t})
    # A2: baseline across seeds
    for s in seeds:
        t = time.time()
        res, rows = run_baseline(s, train, val)
        save(f'A2_baseline_s{s}', res, rows, {'seconds': time.time()-t, 'seed': s})
    # A3: best-of-3 across seeds
    for s in seeds:
        t = time.time()
        res, rows = run_bestofk(s, train, val)
        save(f'A3_bestof3_s{s}', res, rows, {'seconds': time.time()-t, 'seed': s})
    print('ALL DONE', flush=True)


if __name__ == '__main__':
    main()
