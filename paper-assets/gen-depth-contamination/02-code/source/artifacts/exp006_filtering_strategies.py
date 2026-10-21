"""exp006 Filtering Strategies — 6 data quality filters for depth chain data.

Input:  features.csv (30000 rows: doc_id, depth, 15 features)
        depth_*.jsonl (text data, needed for DSIR)
Output: per-sample weights [0,1] via get_weights(), boolean mask via get_mask()

Strategies:
  1. no-filter      — uniform weights (baseline)
  2. binary-ours    — LightGBM binary (human vs synthetic), threshold=0.5
  3. binary-drayson — SIR resampling (Drayson et al. 2025), b=1, k=1.5
  4. graduated      — OBD-LightGBM ordinal + exp(-alpha*d) weighting
  5. surprisal      — surp_mean median threshold
  6. dsir           — n-gram importance resampling (Xie et al. 2023)
"""

import argparse
import json
import os
from abc import ABC, abstractmethod
from collections import Counter
from hashlib import md5

import numpy as np
import pandas as pd

FEATURE_COLS = [
    "surp_mean", "surp_std", "surp_skew", "surp_kurt",
    "surp_d1_mean", "surp_d1_std", "surp_d1_skew",
    "surp_d2_mean", "surp_d2_std",
    "ttr", "hapax_ratio", "self_bleu",
    "freq_kurtosis", "freq_entropy", "low_freq_ratio",
]


class FilterStrategy(ABC):
    @abstractmethod
    def fit(self, features: np.ndarray, depths: np.ndarray, texts: list = None):
        ...

    @abstractmethod
    def get_weights(self, features: np.ndarray, texts: list = None) -> np.ndarray:
        ...

    def get_mask(self, features: np.ndarray, texts: list = None, threshold: float = 0.0) -> np.ndarray:
        return self.get_weights(features, texts) > threshold


class NoFilter(FilterStrategy):
    def fit(self, features, depths, texts=None):
        pass

    def get_weights(self, features, texts=None):
        return np.ones(len(features))


class BinaryOurs(FilterStrategy):
    """LightGBM binary: human (depth=0) vs synthetic (depth>=1).
    Weight = 1 - P(synthetic). Hard mask at P(synthetic) < threshold.
    Uses same 15D features as Graduated for fair comparison (C3 claim).
    """

    def __init__(self, threshold=0.5):
        self.threshold = threshold
        self.model = None

    def fit(self, features, depths, texts=None):
        import lightgbm as lgb
        labels = (depths > 0).astype(int)
        self.model = lgb.LGBMClassifier(
            n_estimators=200, max_depth=6, learning_rate=0.05,
            subsample=0.8, colsample_bytree=0.8,
            random_state=42, verbose=-1,
        )
        self.model.fit(features, labels)

    def get_weights(self, features, texts=None):
        return 1.0 - self.model.predict_proba(features)[:, 1]

    def get_mask(self, features, texts=None, threshold=None):
        t = threshold if threshold is not None else self.threshold
        proba_syn = self.model.predict_proba(features)[:, 1]
        return proba_syn < t


class BinaryDrayson(FilterStrategy):
    """SIR (Drayson et al. 2025): w_j = (1-q(x_j))^b / Z, resample k*n."""

    def __init__(self, b=1, k=1.5, seed=42):
        self.b = b
        self.k = k
        self.seed = seed
        self.model = None

    def fit(self, features, depths, texts=None):
        import lightgbm as lgb
        labels = (depths > 0).astype(int)
        self.model = lgb.LGBMClassifier(
            n_estimators=200, max_depth=6, learning_rate=0.05,
            subsample=0.8, colsample_bytree=0.8,
            random_state=42, verbose=-1,
        )
        self.model.fit(features, labels)

    def get_weights(self, features, texts=None):
        q = self.model.predict_proba(features)[:, 1]
        raw = (1.0 - q) ** self.b
        return raw / raw.max()

    def get_mask(self, features, texts=None, threshold=None):
        q = self.model.predict_proba(features)[:, 1]
        raw = (1.0 - q) ** self.b
        prob = raw / raw.sum()
        rng = np.random.RandomState(self.seed)
        n = len(features)
        selected = rng.choice(n, size=int(self.k * n), replace=True, p=prob)
        mask = np.zeros(n, dtype=bool)
        mask[np.unique(selected)] = True
        return mask


class Graduated(FilterStrategy):
    """OBD-LightGBM: K-1 binary classifiers for P(depth>k), then exp(-alpha * E[depth])."""

    def __init__(self, alpha=0.5, n_depths=6):
        self.alpha = alpha
        self.n_depths = n_depths
        self.models = []

    def fit(self, features, depths, texts=None):
        import lightgbm as lgb
        self.models = []
        for k in range(self.n_depths - 1):
            labels = (depths > k).astype(int)
            clf = lgb.LGBMClassifier(
                n_estimators=200, max_depth=6, learning_rate=0.05,
                subsample=0.8, colsample_bytree=0.8,
                random_state=42, verbose=-1,
            )
            clf.fit(features, labels)
            self.models.append(clf)

    def predict_depth_distribution(self, features):
        """(n_samples, n_depths) matrix of P(depth=d)."""
        n = len(features)
        cum = np.zeros((n, self.n_depths - 1))
        for k, model in enumerate(self.models):
            cum[:, k] = model.predict_proba(features)[:, 1]

        dist = np.zeros((n, self.n_depths))
        dist[:, 0] = 1.0 - cum[:, 0]
        for d in range(1, self.n_depths - 1):
            dist[:, d] = cum[:, d - 1] - cum[:, d]
        dist[:, -1] = cum[:, -1]
        dist = np.clip(dist, 0, 1)
        row_sums = dist.sum(axis=1, keepdims=True)
        row_sums[row_sums == 0] = 1
        dist /= row_sums
        return dist

    def get_weights(self, features, texts=None):
        dist = self.predict_depth_distribution(features)
        expected_depth = (dist * np.arange(self.n_depths)).sum(axis=1)
        weights = np.exp(-self.alpha * expected_depth)
        return weights / weights.max()


class SurprisalBased(FilterStrategy):
    """Keep samples with surp_mean >= median (high surprisal = more human-like)."""

    def __init__(self, surp_col_idx=0):
        self.surp_col_idx = surp_col_idx
        self.threshold = None

    def fit(self, features, depths, texts=None):
        self.threshold = np.median(features[:, self.surp_col_idx])

    def get_weights(self, features, texts=None):
        return np.where(features[:, self.surp_col_idx] >= self.threshold, 1.0, 0.0)


class DSIR(FilterStrategy):
    """Importance resampling via n-gram feature hashing (Xie et al. 2023).
    Reference distribution = depth-0 text, target = all text.
    """

    def __init__(self, ngram=2, hash_dim=10000, k=1.5, seed=42):
        self.ngram = ngram
        self.hash_dim = hash_dim
        self.k = k
        self.seed = seed
        self.ref_dist = None
        self.target_dist = None

    def _hash_features(self, text):
        tokens = text.lower().split()
        counts = Counter()
        for i in range(len(tokens) - self.ngram + 1):
            ng = " ".join(tokens[i:i + self.ngram])
            h = int(md5(ng.encode()).hexdigest(), 16) % self.hash_dim
            counts[h] += 1
        total = sum(counts.values()) or 1
        return {k: v / total for k, v in counts.items()}

    def _build_dist(self, texts):
        agg = np.zeros(self.hash_dim)
        for text in texts:
            for k, v in self._hash_features(text).items():
                agg[k] += v
        agg += 1e-8
        agg /= agg.sum()
        return agg

    def fit(self, features, depths, texts=None):
        assert texts is not None, "DSIR requires text data"
        ref_texts = [t for t, d in zip(texts, depths) if d == 0]
        self.ref_dist = self._build_dist(ref_texts)
        self.target_dist = self._build_dist(texts)

    def _importance_weight(self, text):
        feats = self._hash_features(text)
        log_ratio = sum(
            v * (np.log(self.ref_dist[k]) - np.log(self.target_dist[k]))
            for k, v in feats.items()
        )
        return np.exp(log_ratio)

    def get_weights(self, features, texts=None):
        assert texts is not None, "DSIR requires text data"
        weights = np.array([self._importance_weight(t) for t in texts])
        cap = np.percentile(weights, 99)
        weights = np.clip(weights, 0, cap)
        return weights / weights.max() if weights.max() > 0 else weights

    def get_mask(self, features, texts=None, threshold=None):
        weights = self.get_weights(features, texts)
        prob = weights / weights.sum()
        rng = np.random.RandomState(self.seed)
        n = len(features)
        selected = rng.choice(n, size=int(self.k * n), replace=True, p=prob)
        mask = np.zeros(n, dtype=bool)
        mask[np.unique(selected)] = True
        return mask


STRATEGIES = {
    "no-filter": NoFilter,
    "binary-ours": BinaryOurs,
    "binary-drayson": BinaryDrayson,
    "graduated": Graduated,
    "surprisal": SurprisalBased,
    "dsir": DSIR,
}


def load_data(data_dir):
    """Load features.csv and depth_*.jsonl. Returns (df, texts, doc_ids)."""
    df = pd.read_csv(os.path.join(data_dir, "features.csv"))
    texts, doc_ids = [], []
    for depth in range(6):
        with open(os.path.join(data_dir, f"depth_{depth}.jsonl")) as f:
            for line in f:
                obj = json.loads(line)
                texts.append(obj["text"])
                doc_ids.append(obj["doc_id"])
    return df, texts, doc_ids


def main():
    parser = argparse.ArgumentParser(description="exp006 filtering strategies")
    parser.add_argument("--data-dir", type=str, default="data/")
    parser.add_argument("--strategy", type=str, default="graduated",
                        choices=list(STRATEGIES.keys()))
    parser.add_argument("--alpha", type=float, default=0.5,
                        help="Decay param for graduated strategy")
    parser.add_argument("--output", type=str, default=None,
                        help="Save weights to .npy file")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    np.random.seed(args.seed)

    print(f"Loading data from {args.data_dir}")
    df, texts, _ = load_data(args.data_dir)
    features = df[FEATURE_COLS].values
    depths = df["depth"].values

    kwargs = {}
    if args.strategy == "graduated":
        kwargs["alpha"] = args.alpha
    if args.strategy in ("binary-drayson", "dsir"):
        kwargs["seed"] = args.seed
    strategy = STRATEGIES[args.strategy](**kwargs)

    print(f"Fitting: {args.strategy}")
    strategy.fit(features, depths, texts)

    weights = strategy.get_weights(features, texts)
    mask = strategy.get_mask(features, texts)

    print(f"Weights: mean={weights.mean():.4f} std={weights.std():.4f} "
          f"min={weights.min():.4f} max={weights.max():.4f}")
    print(f"Mask: {mask.sum()}/{len(mask)} kept ({mask.mean()*100:.1f}%)")

    if args.output:
        np.save(args.output, weights)
        print(f"Saved to {args.output}")


if __name__ == "__main__":
    main()
