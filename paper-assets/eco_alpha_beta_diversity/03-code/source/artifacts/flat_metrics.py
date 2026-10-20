# Flat metric baseline: TF-IDF + cosine similarity.

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity as cos_sim
from scipy.stats import pointbiserialr

from diversity import baselga_pairwise


def compute_tfidf(stories):
    """Fit TF-IDF and return (tfidf_matrix, vectorizer, condition_labels)."""
    texts = [" ".join(s["tokens"]) for s in stories]
    labels = [s["condition"] for s in stories]
    vec = TfidfVectorizer()
    mat = vec.fit_transform(texts)
    return mat, vec, labels


def pairwise_cosine(tfidf_matrix):
    """Full NxN cosine similarity matrix."""
    return cos_sim(tfidf_matrix)


def within_between_analysis(sim_matrix, labels):
    """
    Compute within-condition and between-condition cosine similarities.
    Also compute point-biserial correlation (PASS condition 4).
    """
    n = len(labels)
    within_vals, between_vals = [], []
    sim_vals, is_within = [], []

    for i in range(n):
        for j in range(i + 1, n):
            s = sim_matrix[i, j]
            same = int(labels[i] == labels[j])
            sim_vals.append(s)
            is_within.append(same)
            if same:
                within_vals.append(s)
            else:
                between_vals.append(s)

    # point-biserial correlation: similarity ~ within/between
    r, p = pointbiserialr(is_within, sim_vals)

    # per-condition within similarity
    unique_conds = sorted(set(labels))
    within_by_cond = {}
    for cond in unique_conds:
        vals = []
        for i in range(n):
            if labels[i] != cond:
                continue
            for j in range(i + 1, n):
                if labels[j] == cond:
                    vals.append(sim_matrix[i, j])
        if vals:
            within_by_cond[cond] = {
                "mean": float(np.mean(vals)),
                "std": float(np.std(vals)),
                "n_pairs": len(vals),
            }

    return {
        "within_mean": float(np.mean(within_vals)) if within_vals else 0.0,
        "within_std": float(np.std(within_vals)) if within_vals else 0.0,
        "between_mean": float(np.mean(between_vals)) if between_vals else 0.0,
        "between_std": float(np.std(between_vals)) if between_vals else 0.0,
        "r_pb": float(r),
        "p_pb": float(p),
        "within_by_condition": within_by_cond,
    }


# ---------------------------------------------------------------------------
# FAIL test 2: can Baselga ratio be recovered from TF-IDF space?
# ---------------------------------------------------------------------------

def fail_test_2_tfidf(stories_by_cond, tfidf_matrix, labels, vectorizer):
    """
    Apply Baselga decomposition to TF-IDF vectors.
    Compare ratio (bc_balanced / bc_total) with word-frequency-based ratio.
    If within ±10%, FAIL (flat metrics capture the same structure).
    """
    feature_names = vectorizer.get_feature_names_out()

    # build per-story TF-IDF "frequency" dicts
    tfidf_freqs_by_cond = {}
    idx = 0
    for cond, stories in stories_by_cond.items():
        tfidf_freqs = []
        for s in stories:
            row = tfidf_matrix[idx].toarray().flatten()
            freq = {feature_names[j]: float(row[j]) for j in range(len(row)) if row[j] > 0}
            tfidf_freqs.append(freq)
            idx += 1
        tfidf_freqs_by_cond[cond] = tfidf_freqs

    results = {}
    for cond in stories_by_cond:
        word_freqs = [s["word_freq"] for s in stories_by_cond[cond]]
        tfidf_freqs = tfidf_freqs_by_cond[cond]

        # word-based Baselga ratio
        N = len(word_freqs)
        w_bals, w_tots = [], []
        t_bals, t_tots = [], []
        for i in range(N):
            for j in range(i + 1, N):
                rw = baselga_pairwise(word_freqs[i], word_freqs[j])
                w_bals.append(rw["bc_balanced"])
                w_tots.append(rw["bc_total"])
                rt = baselga_pairwise(tfidf_freqs[i], tfidf_freqs[j])
                t_bals.append(rt["bc_balanced"])
                t_tots.append(rt["bc_total"])

        ratio_word = np.mean(w_bals) / np.mean(w_tots) if np.mean(w_tots) > 0 else 0.0
        ratio_tfidf = np.mean(t_bals) / np.mean(t_tots) if np.mean(t_tots) > 0 else 0.0
        error = abs(ratio_tfidf - ratio_word) / ratio_word if ratio_word > 0 else float("inf")

        results[cond] = {
            "ratio_word": float(ratio_word),
            "ratio_tfidf": float(ratio_tfidf),
            "recovery_error": float(error),
        }

    any_recovered = any(r["recovery_error"] < 0.10 for r in results.values())
    return {"per_condition": results, "fail": any_recovered}


def fail_test_2_perpair(stories_by_cond, tfidf_mat, labels, vectorizer):
    """
    Per-pair FAIL test 2: can cosine distance predict the Baselga
    balanced/(balanced+gradient) ratio at the pair level?

    For each within-condition pair (i,j):
      - Compute Baselga pairwise → ratio = bc_balanced / (bc_balanced + bc_gradient)
      - Compute cosine distance = 1 - cosine_similarity
      - Linear regression: ratio ~ cosine_dist
      - R² > 0.5 → FAIL (cosine captures pair-level decomposition structure)

    Returns per-condition R², MAE, overall R², fail boolean.
    """
    from scipy.stats import linregress

    sim_matrix = cos_sim(tfidf_mat)
    conditions = list(stories_by_cond.keys())

    all_cos_dists = []
    all_ratios = []
    per_cond = {}
    idx_start = 0

    for cond in conditions:
        stories = stories_by_cond[cond]
        n = len(stories)
        freqs = [s["word_freq"] for s in stories]

        cos_dists = []
        ratios = []
        for i in range(n):
            for j in range(i + 1, n):
                bp = baselga_pairwise(freqs[i], freqs[j])
                denom = bp["bc_balanced"] + bp["bc_gradient"]
                if denom < 1e-12:
                    continue
                ratio = bp["bc_balanced"] / denom
                cd = 1.0 - sim_matrix[idx_start + i, idx_start + j]
                cos_dists.append(cd)
                ratios.append(ratio)

        cos_dists = np.array(cos_dists)
        ratios = np.array(ratios)

        if len(cos_dists) >= 6:
            sl, inter, r, p, se = linregress(cos_dists, ratios)
            r2 = float(r ** 2)
            mae = float(np.mean(np.abs(ratios - (sl * cos_dists + inter))))
        else:
            r2, mae = 0.0, float("inf")

        per_cond[cond] = {
            "r2": r2,
            "mae": mae,
            "n_pairs": len(cos_dists),
            "ratio_mean": float(np.mean(ratios)) if len(ratios) > 0 else 0.0,
            "ratio_std": float(np.std(ratios)) if len(ratios) > 0 else 0.0,
        }

        all_cos_dists.extend(cos_dists.tolist())
        all_ratios.extend(ratios.tolist())
        idx_start += n

    all_cos_dists = np.array(all_cos_dists)
    all_ratios = np.array(all_ratios)

    if len(all_cos_dists) >= 6:
        sl, inter, r, p, se = linregress(all_cos_dists, all_ratios)
        overall_r2 = float(r ** 2)
        overall_mae = float(np.mean(np.abs(all_ratios - (sl * all_cos_dists + inter))))
    else:
        overall_r2, overall_mae = 0.0, float("inf")

    fail = overall_r2 > 0.5
    return {
        "per_condition": per_cond,
        "overall_r2": overall_r2,
        "overall_mae": overall_mae,
        "n_total_pairs": len(all_cos_dists),
        "fail": fail,
    }


def fail_test_2_regression(baselga_by_cond, cosine_dist_by_cond):
    """
    Split-half cross-validation: fit regression on half, predict on other half.
    OLS mean(predicted)==mean(actual) by construction, so we need out-of-sample
    prediction to get a genuine recovery error.
    """
    from scipy.stats import linregress

    split_rng = np.random.default_rng(123)
    results = {}
    for cond in baselga_by_cond:
        bc_bal = np.array(baselga_by_cond[cond]["bc_balanced_vals"])
        bc_tot = np.array(baselga_by_cond[cond]["bc_total_vals"])
        cos_d = np.array(cosine_dist_by_cond[cond])

        if len(bc_bal) < 6:
            results[cond] = {"recovery_error": float("inf"), "note": "too few pairs"}
            continue

        true_ratio = np.mean(bc_bal) / np.mean(bc_tot) if np.mean(bc_tot) > 0 else 0.0

        # split-half
        perm = split_rng.permutation(len(cos_d))
        train, test = perm[: len(perm) // 2], perm[len(perm) // 2 :]

        sl_b, int_b, r_b, _, _ = linregress(cos_d[train], bc_bal[train])
        sl_t, int_t, r_t, _, _ = linregress(cos_d[train], bc_tot[train])
        pred_bal = np.clip(sl_b * cos_d[test] + int_b, 0, None)
        pred_tot = np.clip(sl_t * cos_d[test] + int_t, 1e-10, None)
        pred_ratio = float(np.mean(pred_bal) / np.mean(pred_tot))
        test_true = np.mean(bc_bal[test]) / np.mean(bc_tot[test]) if np.mean(bc_tot[test]) > 0 else 0.0
        error = abs(pred_ratio - test_true) / test_true if test_true > 0 else float("inf")

        results[cond] = {
            "true_ratio": float(true_ratio),
            "pred_ratio": pred_ratio,
            "recovery_error": float(error),
            "r2_bal": float(r_b ** 2),
            "r2_tot": float(r_t ** 2),
        }

    any_recovered = any(
        isinstance(r, dict) and r.get("recovery_error", 1.0) < 0.10
        for r in results.values()
    )
    return {"per_condition": results, "fail": any_recovered}
