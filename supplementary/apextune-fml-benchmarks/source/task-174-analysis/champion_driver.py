"""task-174 phase B: seed-sensitivity of the v5 champion mechanisms.

Loads each round's champion adversarial_debiasing.py as a private module
(never touching the live repo), sweeps training seeds on the val split.
Usage: python champion_driver.py <path> <tag> <seed...>
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


def set_seed(seed):
    os.environ['PYTHONHASHSEED'] = str(seed)
    random.seed(seed)
    np.random.seed(seed)
    import tensorflow as _tf
    _tf.random.set_seed(seed)


def load_mech(path):
    spec = importlib.util.spec_from_file_location('champ_mech', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_splits():
    d = load_preproc_data_compas()
    tr, pool = d.split([0.7], shuffle=True)
    val, test = pool.split([0.3], shuffle=True)
    return tr, val, test


def evaluate(model, val):
    pred_in = val.copy(deepcopy=True)
    pred_in.labels = np.zeros_like(pred_in.labels)
    pred_in.scores = np.zeros_like(pred_in.scores)
    out = model.predict(pred_in)
    cm = ClassificationMetric(val, out, unprivileged_groups=UNPRIV, privileged_groups=PRIV)
    return {'abs_aod': abs(float(cm.average_odds_difference())),
            'cls_acc': float(cm.accuracy())}, out


def main():
    mech_path, tag = sys.argv[1], sys.argv[2]
    seeds = [int(s) for s in sys.argv[3:]] or [233, 1, 2, 3, 4, 5, 6, 7]
    mod = load_mech(mech_path)
    cls = mod.AdversarialDebiasing
    train, val, _test = load_splits()
    print(f'{tag}: train={train.features.shape[0]} val={val.features.shape[0]}', flush=True)
    for s in seeds:
        set_seed(s)
        sess = tf.Session()
        sess.close()
        tf.reset_default_graph()
        sess = tf.Session()
        t = time.time()
        try:
            m = cls(PRIV, UNPRIV, scope_name='d', debias=True, sess=sess, seed=s)
            m.fit(train)
            res, _ = evaluate(m, val)
            rec = {'tag': f'B_{tag}_s{s}', 'seed': s, 'seconds': time.time() - t, **res}
        except Exception as e:  # noqa: BLE001
            rec = {'tag': f'B_{tag}_s{s}', 'seed': s, 'error': f'{type(e).__name__}: {e}'}
        sess.close()
        with open(f'{OUT}/B_{tag}_s{s}.json', 'w') as fh:
            json.dump(rec, fh, indent=1)
        print(f'  seed {s}: {rec.get("abs_aod", rec.get("error"))}', flush=True)


if __name__ == '__main__':
    main()
