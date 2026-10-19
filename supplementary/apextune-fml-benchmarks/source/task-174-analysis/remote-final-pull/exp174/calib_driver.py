"""task-174 phase C: group-threshold calibration study (val split only).

For each training seed: train the pristine baseline mechanism once, capture
per-row probabilities on val, then sweep the group-specific threshold offset
delta (threshold = 0.5 + delta*(2*pa-1), matching the v5-r1 champion's form)
and record AOD / EOD / DI / theil / accuracy from aif360's own metric class.

Writes per-seed row dumps + per-seed curve JSONs. No LLM cost, no official steps.
Usage: python calib_driver.py [mechanism_path] [tag] [seed...]
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


def set_seed(seed):
    os.environ['PYTHONHASHSEED'] = str(seed)
    random.seed(seed)
    np.random.seed(seed)
    import tensorflow as _tf
    _tf.random.set_seed(seed)


def load_mech(path):
    spec = importlib.util.spec_from_file_location('calib_mech', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_splits():
    d = load_preproc_data_compas()
    tr, pool = d.split([0.7], shuffle=True)
    val, test = pool.split([0.3], shuffle=True)
    return tr, val, test


def get_probs(cls, seed, train, val):
    """Train once; return the model's P(y=1) per val row (no thresholding)."""
    set_seed(seed)
    sess = tf.Session()
    sess.close()
    tf.reset_default_graph()
    sess = tf.Session()
    m = cls(PRIV, UNPRIV, scope_name='d', debias=True, sess=sess, seed=seed)
    m.fit(train)
    pred_in = val.copy(deepcopy=True)
    pred_in.labels = np.zeros_like(pred_in.labels)
    pred_in.scores = np.zeros_like(pred_in.scores)
    out = m.predict(pred_in)           # champion may itself threshold; read scores
    probs = np.asarray(out.scores, dtype=float).ravel()
    sess.close()
    return probs


def metrics_for(probs, pa, val, delta):
    """Apply group threshold, score with aif360's ClassificationMetric."""
    thr = 0.5 + delta * (2.0 * pa - 1.0)
    hard = (probs > thr).astype(float)
    deb = val.copy(deepcopy=True)
    lab = hard.reshape(-1, 1).copy()
    lab[hard == 1.0] = val.favorable_label
    lab[hard == 0.0] = val.unfavorable_label
    deb.labels = lab
    deb.scores = probs.reshape(-1, 1)
    cm = ClassificationMetric(val, deb, unprivileged_groups=UNPRIV, privileged_groups=PRIV)
    return {
        'delta': float(delta),
        'abs_aod': abs(float(cm.average_odds_difference())),
        'abs_eod': abs(float(cm.equal_opportunity_difference())),
        'abs_di_diff': abs(float(cm.disparate_impact()) - 1.0),
        'abs_theil': abs(float(cm.theil_index())),
        'cls_acc': float(cm.accuracy()),
        'balanced_acc': float(0.5 * (cm.true_positive_rate() + cm.true_negative_rate())),
    }


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else '/root/exp174/mech/baseline.py'
    tag = sys.argv[2] if len(sys.argv) > 2 else 'baseline'
    seeds = [int(s) for s in sys.argv[3:]] or [233, 1, 2, 3, 4, 5, 6, 7]
    cls = load_mech(path).AdversarialDebiasing
    train, val, _test = load_splits()
    pa = np.asarray(val.protected_attributes[:, val.protected_attribute_names.index('sex')],
                    dtype=float).ravel()
    print(f'{tag}: train={train.features.shape[0]} val={val.features.shape[0]} '
          f'priv={(pa == 1).sum()} unpriv={(pa == 0).sum()}', flush=True)

    for s in seeds:
        t = time.time()
        probs = get_probs(cls, s, train, val)
        rows = {'seed': s, 'probs': probs.tolist(), 'pa': pa.astype(int).tolist(),
                'labels': [float(x) for x in np.asarray(val.labels).ravel()]}
        with open(f'{OUT}/C_{tag}_s{s}_rows.json', 'w') as fh:
            json.dump(rows, fh)
        curve = [metrics_for(probs, pa, val, d) for d in DELTAS]
        best = min(curve, key=lambda r: r['abs_aod'])
        with open(f'{OUT}/C_{tag}_s{s}_curve.json', 'w') as fh:
            json.dump({'seed': s, 'tag': tag, 'curve': curve,
                       'best_delta': best['delta'], 'best_abs_aod': best['abs_aod'],
                       'best_cls_acc': best['cls_acc'],
                       'at_delta0': next(r for r in curve if abs(r['delta']) < 1e-9),
                       'at_delta008': next(r for r in curve if abs(r['delta'] - 0.08) < 1e-9)
                       if any(abs(r['delta'] - 0.08) < 1e-9 for r in curve) else None},
                      fh)
        print(f'  seed {s}: best_delta={best["delta"]:+.3f} best_aod={best["abs_aod"]:.5f} '
              f'acc={best["cls_acc"]:.4f} | d0_aod={curve[40]["abs_aod"]:.5f} '
              f'({time.time()-t:.1f}s)', flush=True)


if __name__ == '__main__':
    main()
