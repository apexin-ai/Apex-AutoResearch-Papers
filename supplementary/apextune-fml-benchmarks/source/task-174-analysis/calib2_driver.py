"""task-174 phase C2: adaptive vs fixed group-threshold calibration.

For each seed, train the baseline once, then:
  - fit delta on a TRAIN holdout slice (grid search, aif360 metrics, accuracy floor)
  - apply that delta to VAL and record the resulting metrics
  - also record: no-calibration, fixed delta=0.08, and the val-oracle delta
This tests whether calibration generalizes (train-fitted -> val) or is a
bench-fit constant.

Usage: python calib2_driver.py [mech.py] [tag] [seed...]
"""
import importlib.util
import json
import os
import random
import sys

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


def set_seed(seed):
    os.environ['PYTHONHASHSEED'] = str(seed)
    random.seed(seed)
    np.random.seed(seed)
    import tensorflow as _tf
    _tf.random.set_seed(seed)


def load_mech(path):
    spec = importlib.util.spec_from_file_location('c2_mech', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_splits():
    d = load_preproc_data_compas()
    tr, pool = d.split([0.7], shuffle=True)
    val, test = pool.split([0.3], shuffle=True)
    return tr, val, test


def train_probs(cls, seed, train):
    set_seed(seed)
    sess = tf.Session()
    sess.close()
    tf.reset_default_graph()
    sess = tf.Session()
    m = cls(PRIV, UNPRIV, scope_name='d', debias=True, sess=sess, seed=seed)
    m.fit(train)
    return m, sess


def probs_on(model, sess, ds):
    d = ds.copy(deepcopy=True)
    d.labels = np.zeros_like(d.labels)
    d.scores = np.zeros_like(d.scores)
    out = model.predict(d)
    return np.asarray(out.scores, dtype=float).ravel(), out


def score(ds, probs, pa, delta):
    thr = 0.5 + delta * (2.0 * pa - 1.0)
    hard = (probs > thr).astype(float)
    deb = ds.copy(deepcopy=True)
    lab = hard.reshape(-1, 1).copy()
    lab[hard == 1.0] = ds.favorable_label
    lab[hard == 0.0] = ds.unfavorable_label
    deb.labels = lab
    deb.scores = probs.reshape(-1, 1)
    cm = ClassificationMetric(ds, deb, unprivileged_groups=UNPRIV, privileged_groups=PRIV)
    return {'delta': float(delta),
            'abs_aod': abs(float(cm.average_odds_difference())),
            'abs_eod': abs(float(cm.equal_opportunity_difference())),
            'abs_theil': abs(float(cm.theil_index())),
            'cls_acc': float(cm.accuracy())}


def fit_delta(probs, pa, ds, floor=FLOOR):
    """Grid-search delta on a data slice; floor-constrained AOD minimise."""
    best = None
    for delta in DELTAS:
        m = score(ds, probs, pa, delta)
        if m['cls_acc'] < floor:
            continue
        if best is None or m['abs_aod'] < best['abs_aod']:
            best = m
    return best  # None if no admissible delta


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else '/root/exp174/mech/baseline.py'
    tag = sys.argv[2] if len(sys.argv) > 2 else 'baseline'
    seeds = [int(s) for s in sys.argv[3:]] or [233, 1, 2, 3, 4, 5, 6, 7]
    cls = load_mech(path).AdversarialDebiasing
    train, val, _test = load_splits()

    # carve the train holdout ONCE (same rows across seeds: a fixed 15% slice)
    set_seed(0)
    tr, hol = train.split([0.85], shuffle=True)
    pa_hol = np.asarray(hol.protected_attributes[:, hol.protected_attribute_names.index('sex')], float).ravel()
    pa_val = np.asarray(val.protected_attributes[:, val.protected_attribute_names.index('sex')], float).ravel()

    out = []
    for s in seeds:
        model, sess = train_probs(cls, s, tr)   # train on the 85% slice
        p_hol, _ = probs_on(model, sess, hol)
        p_val, _ = probs_on(model, sess, val)
        sess.close()

        fit = fit_delta(p_hol, pa_hol, hol)      # adaptive delta from train holdout
        d_adapt = fit['delta'] if fit else None
        adapt = score(val, p_val, pa_val, d_adapt) if d_adapt is not None else None
        none_ = score(val, p_val, pa_val, 0.0)
        fixed = score(val, p_val, pa_val, 0.08)
        oracle_fit = fit_delta(p_val, pa_val, val)
        rec = {'seed': s, 'tag': tag,
               'delta_adaptive': d_adapt, 'val_adaptive': adapt,
               'val_none': none_, 'val_fixed008': fixed,
               'val_oracle': oracle_fit,
               'holdout_fit_aod': fit['abs_aod'] if fit else None,
               'holdout_fit_acc': fit['cls_acc'] if fit else None}
        out.append(rec)
        with open(f'{OUT}/C2_{tag}_s{s}.json', 'w') as fh:
            json.dump(rec, fh, indent=1)
        aod_a = f'{adapt["abs_aod"]:.5f}' if adapt else 'NONE'
        print(f'  seed {s:>3}: d_adapt={d_adapt} val_aod(adapt)={aod_a} '
              f'val_aod(none)={none_["abs_aod"]:.5f} val_aod(fixed.08)={fixed["abs_aod"]:.5f} '
              f'oracle_d*={oracle_fit["delta"] if oracle_fit else None}', flush=True)


if __name__ == '__main__':
    main()
