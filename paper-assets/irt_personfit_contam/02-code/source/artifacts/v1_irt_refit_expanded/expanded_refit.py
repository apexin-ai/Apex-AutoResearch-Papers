"""
V1 Leaderboard IRT Refit — Expanded (N>=500 models)
Extends pilot (N=63) to large-scale model pool via HF API discovery.
"""

import os
import sys
import json
import time
import csv
import warnings
import threading
import numpy as np
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed
from scipy.optimize import minimize_scalar
from scipy.special import expit
from scipy.stats import pearsonr, spearmanr
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore')

PROJECT_ROOT = "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam"
OUT_DIR = os.path.join(PROJECT_ROOT, "artifacts/v1_irt_refit_expanded")
PILOT_DIR = os.path.join(PROJECT_ROOT, "artifacts/v1_irt_refit_pilot")

sys.path.insert(0, os.path.join(PROJECT_ROOT, "src"))
from person_fit import prob_4pl, estimate_theta_mle, compute_lz_star

MMLU_SUBJECTS = [
    "abstract_algebra", "anatomy", "astronomy", "business_ethics",
    "clinical_knowledge", "college_biology", "college_chemistry",
    "college_computer_science", "college_mathematics", "college_medicine",
    "college_physics", "computer_security", "conceptual_physics",
    "econometrics", "electrical_engineering", "elementary_mathematics",
    "formal_logic", "global_facts", "high_school_biology",
    "high_school_chemistry", "high_school_computer_science",
    "high_school_european_history", "high_school_geography",
    "high_school_government_and_politics", "high_school_macroeconomics",
    "high_school_mathematics", "high_school_microeconomics",
    "high_school_physics", "high_school_psychology", "high_school_statistics",
    "high_school_us_history", "high_school_world_history", "human_aging",
    "human_sexuality", "international_law", "jurisprudence",
    "logical_fallacies", "machine_learning", "management", "marketing",
    "medical_genetics", "miscellaneous", "moral_disputes", "moral_scenarios",
    "nutrition", "philosophy", "prehistory", "professional_accounting",
    "professional_law", "professional_medicine", "professional_psychology",
    "public_relations", "security_studies", "sociology", "us_foreign_policy",
    "virology", "world_religions"
]


# ─── Download Functions ────────────────────────────────────────────────────

def read_cached_model(model_name, cache_dir):
    """Read MMLU responses from HF cache without making API calls."""
    import pyarrow.parquet as pq
    import re
    import glob
    from collections import defaultdict

    cache_key = f"datasets--open-llm-leaderboard-old--details_{model_name}"
    model_cache = os.path.join(cache_dir, cache_key, "snapshots")
    if not os.path.isdir(model_cache):
        return None

    snapshots = os.listdir(model_cache)
    if not snapshots:
        return None

    for snap in sorted(snapshots, reverse=True):
        snap_path = os.path.join(model_cache, snap)
        parquet_files = glob.glob(os.path.join(snap_path, "**", "*hendrycksTest*.parquet"),
                                  recursive=True)

        # Group by timestamp
        ts_files = defaultdict(dict)
        for f in parquet_files:
            basename = os.path.basename(f)
            m = re.search(r'\|5_(.+?)\.parquet', basename)
            if not m:
                continue
            ts = m.group(1)
            for subj in MMLU_SUBJECTS:
                if f"hendrycksTest-{subj}|5_" in basename:
                    ts_files[ts][subj] = f
                    break

        for ts in sorted(ts_files.keys(), reverse=True):
            if len(ts_files[ts]) != 57:
                continue
            responses = []
            ok = True
            for subj in MMLU_SUBJECTS:
                try:
                    table = pq.read_table(ts_files[ts][subj], columns=['acc'])
                    accs = table['acc'].to_pylist()
                    responses.extend(accs)
                except Exception:
                    ok = False
                    break
            if ok and len(responses) == 14042:
                return np.array(responses, dtype=np.float64)

    return None


def download_model_responses(model_name, cache_dir=None):
    """Download MMLU responses for a single model from v1 leaderboard."""
    os.environ['HF_HUB_DISABLE_XET'] = '1'
    from huggingface_hub import HfApi, hf_hub_download
    import pyarrow.parquet as pq
    import re
    from collections import defaultdict

    repo_id = f"open-llm-leaderboard-old/details_{model_name}"
    api = HfApi()

    try:
        files = api.list_repo_files(repo_id, repo_type="dataset")
    except Exception:
        return None

    ts_files = defaultdict(dict)
    for f in files:
        if 'hendrycksTest' not in f or not f.endswith('.parquet'):
            continue
        m = re.search(r'\|5_(.+?)\.parquet', f)
        if not m:
            continue
        ts = m.group(1)
        for subj in MMLU_SUBJECTS:
            if f"hendrycksTest-{subj}|5_" in f:
                ts_files[ts][subj] = f
                break

    for ts in sorted(ts_files.keys(), reverse=True):
        if len(ts_files[ts]) != 57:
            continue
        subject_files = ts_files[ts]
        responses = []
        ok = True
        for subj in MMLU_SUBJECTS:
            try:
                local_path = hf_hub_download(repo_id, subject_files[subj],
                                             repo_type="dataset", cache_dir=cache_dir)
                table = pq.read_table(local_path, columns=['acc'])
                accs = table['acc'].to_pylist()
                responses.extend(accs)
            except Exception:
                ok = False
                break
        if ok and len(responses) == 14042:
            return np.array(responses, dtype=np.float64)

    return None


def scan_cached_models(cache_dir):
    """Find all model names that have cache directories."""
    prefix = "datasets--open-llm-leaderboard-old--details_"
    names = []
    for d in os.listdir(cache_dir):
        if d.startswith(prefix):
            names.append(d[len(prefix):])
    return names


def discover_all_v1_models():
    """Use HF API to list all datasets under open-llm-leaderboard-old org."""
    from huggingface_hub import HfApi
    api = HfApi()
    print("Discovering all v1 leaderboard models via HF API...")
    datasets = list(api.list_datasets(author="open-llm-leaderboard-old", limit=20000))
    model_names = []
    for ds in datasets:
        name = ds.id.replace("open-llm-leaderboard-old/details_", "")
        if ds.id.startswith("open-llm-leaderboard-old/details_"):
            model_names.append(name)
    print(f"  Found {len(model_names)} model detail datasets")
    return model_names


# ─── MML-EM IRT Fitting (from pilot) ──────────────────────────────────────

def _gauss_hermite_quadrature(n_points=41, bounds=(-4, 4)):
    theta = np.linspace(bounds[0], bounds[1], n_points)
    weights = np.exp(-0.5 * theta**2) / np.sqrt(2 * np.pi)
    weights /= weights.sum()
    return theta, weights


def _3pl_prob(theta, a, b, c):
    z = a * (theta - b)
    return c + (1 - c) * expit(z)


def _e_step(X, a, b, c, theta_q, w_q):
    N, J = X.shape
    Q = len(theta_q)
    P = c + (1 - c) * expit(a[None, :] * (theta_q[:, None] - b[None, :]))
    P = np.clip(P, 1e-15, 1 - 1e-15)
    logP = np.log(P)
    log1mP = np.log(1 - P)
    log_lik = X @ logP.T + (1 - X) @ log1mP.T
    log_lik += np.log(w_q)[None, :]
    log_lik -= log_lik.max(axis=1, keepdims=True)
    posterior = np.exp(log_lik)
    posterior /= posterior.sum(axis=1, keepdims=True)
    r_j = X.T @ posterior
    f_q = posterior.sum(axis=0)
    return r_j, f_q


def _m_step_vectorized(r_j, f_q, a, b, c, theta_q, n_newton=5):
    J = len(a)
    Q = len(theta_q)
    for _ in range(n_newton):
        z = a[:, None] * (theta_q[None, :] - b[:, None])
        sig = expit(z)
        P = c + (1 - c) * sig
        P = np.clip(P, 1e-15, 1 - 1e-15)
        dP_db = -a[:, None] * (1 - c) * sig * (1 - sig)
        w = (r_j / P - (f_q[None, :] - r_j) / (1 - P))
        grad_b = (w * dP_db).sum(axis=1)
        dP_db2 = dP_db * dP_db
        hess_b = -(f_q[None, :] * dP_db2 / (P * (1 - P))).sum(axis=1)
        hess_b = np.where(np.abs(hess_b) > 1e-10, hess_b, -1e-10)
        b_update = -grad_b / hess_b
        b_update = np.clip(b_update, -1.0, 1.0)
        b = np.clip(b + b_update, -6.0, 6.0)

        z = a[:, None] * (theta_q[None, :] - b[:, None])
        sig = expit(z)
        P = c + (1 - c) * sig
        P = np.clip(P, 1e-15, 1 - 1e-15)
        dP_da = (1 - c) * (theta_q[None, :] - b[:, None]) * sig * (1 - sig)
        w = (r_j / P - (f_q[None, :] - r_j) / (1 - P))
        grad_a = (w * dP_da).sum(axis=1)
        dP_da2 = dP_da * dP_da
        hess_a = -(f_q[None, :] * dP_da2 / (P * (1 - P))).sum(axis=1)
        hess_a = np.where(np.abs(hess_a) > 1e-10, hess_a, -1e-10)
        a_update = -grad_a / hess_a
        a_update = np.clip(a_update, -0.5, 0.5)
        a = np.clip(a + a_update, 0.01, 5.0)
    return a, b


def fit_2pl_mml_em(X, n_quad=31, max_iter=100, tol=1e-4):
    N, J = X.shape
    theta_q, w_q = _gauss_hermite_quadrature(n_quad)
    p_correct = X.mean(axis=0)
    b = -np.log(np.clip(p_correct, 0.01, 0.99) / (1 - np.clip(p_correct, 0.01, 0.99)))
    a = np.ones(J)
    c = 0.0
    for iteration in range(max_iter):
        a_old = a.copy()
        r_j, f_q = _e_step(X, a, b, c, theta_q, w_q)
        a, b = _m_step_vectorized(r_j, f_q, a, b, c, theta_q, n_newton=3)
        change = np.max(np.abs(a - a_old))
        if iteration % 10 == 0:
            print(f"    Iter {iteration}: max delta(a) = {change:.6f}")
        if change < tol:
            print(f"    Converged at iter {iteration}")
            break
    return a, b


def fit_3pl_mml_em(X, c_fixed=0.25, n_quad=31, max_iter=100, tol=1e-4):
    N, J = X.shape
    theta_q, w_q = _gauss_hermite_quadrature(n_quad)
    p_correct = X.mean(axis=0)
    p_adj = np.clip((p_correct - c_fixed) / (1 - c_fixed), 0.01, 0.99)
    b = -np.log(p_adj / (1 - p_adj))
    a = np.ones(J)
    for iteration in range(max_iter):
        a_old = a.copy()
        r_j, f_q = _e_step(X, a, b, c_fixed, theta_q, w_q)
        a, b = _m_step_vectorized(r_j, f_q, a, b, c_fixed, theta_q, n_newton=3)
        change = np.max(np.abs(a - a_old))
        if iteration % 10 == 0:
            print(f"    Iter {iteration}: max delta(a) = {change:.6f}")
        if change < tol:
            print(f"    Converged at iter {iteration}")
            break
    return a, b, c_fixed


# ─── Analysis ─────────────────────────────────────────────────────────────

def deduplicate_mapping(mapping_df):
    """Deduplicate item mapping: for each PSN-IRT position, keep first v1 item."""
    valid = mapping_df[mapping_df['psn_irt_mmlu_position'] >= 0].copy()
    deduped = valid.drop_duplicates(subset='psn_irt_mmlu_position', keep='first')
    mask = np.zeros(len(mapping_df), dtype=bool)
    mask[deduped.index] = True
    n_total_mapped = len(valid)
    n_deduped = len(deduped)
    n_duplicates = n_total_mapped - n_deduped
    print(f"  Item mapping: {n_total_mapped} total mapped, {n_deduped} after dedup ({n_duplicates} duplicates)")
    return mask


def compare_parameters(v1_vals, psn_vals, label=""):
    """Compute pearson and spearman between two arrays."""
    r_p, p_p = pearsonr(v1_vals, psn_vals)
    r_s, p_s = spearmanr(v1_vals, psn_vals)
    return {
        'pearson_r': float(r_p), 'pearson_p': float(p_p),
        'spearman_r': float(r_s), 'spearman_p': float(p_s),
        'v1_mean': float(v1_vals.mean()), 'v1_std': float(v1_vals.std()),
        'psn_mean': float(psn_vals.mean()), 'psn_std': float(psn_vals.std()),
        'n_items': int(len(v1_vals)),
    }


def difficulty_binned_correlation(v1_a, psn_a, psn_b_mapped, mask):
    """Compute a correlation in difficulty bins (easy/medium/hard)."""
    b_vals = psn_b_mapped[mask]
    a_v1 = v1_a[mask]
    a_psn = psn_a[mask]

    # Tertile splits on PSN-IRT difficulty
    t1 = np.percentile(b_vals, 33.3)
    t2 = np.percentile(b_vals, 66.7)

    bins = {
        'easy (b < {:.2f})'.format(t1): b_vals < t1,
        'medium ({:.2f} <= b < {:.2f})'.format(t1, t2): (b_vals >= t1) & (b_vals < t2),
        'hard (b >= {:.2f})'.format(t2): b_vals >= t2,
    }

    results = {}
    for label, sel in bins.items():
        if sel.sum() < 10:
            results[label] = {'n': int(sel.sum()), 'note': 'too few items'}
            continue
        r_p, p_p = pearsonr(a_v1[sel], a_psn[sel])
        r_s, p_s = spearmanr(a_v1[sel], a_psn[sel])
        results[label] = {
            'n': int(sel.sum()),
            'pearson_r': float(r_p), 'pearson_p': float(p_p),
            'spearman_r': float(r_s), 'spearman_p': float(p_s),
        }
    return results


def plot_parameter_comparison_2x2(a_2pl, b_2pl, a_3pl, b_3pl,
                                   psn_a_mapped, psn_b_mapped, mask, out_path):
    """2x2 scatter plots: (a_2pl, a_3pl) x (b_2pl, b_3pl)."""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    pairs = [
        (axes[0, 0], psn_a_mapped[mask], a_2pl[mask], 'PSN-IRT a', 'V1-2PL a', 'steelblue'),
        (axes[0, 1], psn_a_mapped[mask], a_3pl[mask], 'PSN-IRT a', 'V1-3PL a', 'darkorange'),
        (axes[1, 0], psn_b_mapped[mask], b_2pl[mask], 'PSN-IRT b', 'V1-2PL b', 'coral'),
        (axes[1, 1], psn_b_mapped[mask], b_3pl[mask], 'PSN-IRT b', 'V1-3PL b', 'seagreen'),
    ]

    for ax, x, y, xlabel, ylabel, color in pairs:
        ax.scatter(x, y, alpha=0.05, s=2, c=color, rasterized=True)
        r, _ = pearsonr(x, y)
        rs, _ = spearmanr(x, y)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_title(f'{ylabel} vs {xlabel}: r={r:.3f}, rho={rs:.3f} (n={len(x)})')
        lo = min(x.min(), y.min())
        hi = max(x.max(), y.max())
        margin = (hi - lo) * 0.05
        ax.plot([lo - margin, hi + margin], [lo - margin, hi + margin], 'k--', alpha=0.3, lw=1)

    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {out_path}")


def plot_lz_star_distribution(lz_stars, out_path):
    """Plot lz* histogram."""
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(lz_stars, bins=60, color='steelblue', alpha=0.7, edgecolor='white')
    ax.axvline(x=-1.96, color='red', linestyle='--', alpha=0.7, label='z=-1.96')
    ax.axvline(x=0, color='gray', linestyle='-', alpha=0.3, label='z=0')
    ax.axvline(x=lz_stars.mean(), color='green', linestyle='-', alpha=0.7,
               label=f'mean={lz_stars.mean():.2f}')
    n_flagged = np.sum(lz_stars < -1.96)
    ax.set_xlabel('lz* statistic')
    ax.set_ylabel('Count')
    ax.set_title(f'lz* Distribution (N={len(lz_stars)}, mean={lz_stars.mean():.2f}, '
                 f'std={lz_stars.std():.2f}, flagged={n_flagged})')
    ax.legend()
    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {out_path}")


# ─── Main Pipeline ────────────────────────────────────────────────────────

def main():
    np.random.seed(42)
    os.makedirs(OUT_DIR, exist_ok=True)
    cache_dir = os.path.join(PILOT_DIR, ".hf_cache")
    download_log_path = os.path.join(OUT_DIR, "download_log.csv")

    # ── Load pilot data ──────────────────────────────────────────────────
    print("=== Phase 0: Loading Pilot Data ===")
    pilot_data = np.load(os.path.join(PILOT_DIR, "pilot_response_matrix.npz"), allow_pickle=True)
    X_pilot = pilot_data['X']
    pilot_models = list(pilot_data['model_names'])
    print(f"  Pilot: {X_pilot.shape[0]} models x {X_pilot.shape[1]} items")
    pilot_set = set(pilot_models)

    # ── Load PSN-IRT params ──────────────────────────────────────────────
    print("\nLoading PSN-IRT parameters...")
    psn_params = pd.read_csv(os.path.join(PROJECT_ROOT, "artifacts/psn_irt_params/mmlu_params.csv"))
    psn_a = psn_params['a_discrimination'].values
    psn_b = psn_params['b_difficulty'].values
    psn_c = psn_params['c_guessing'].values
    psn_d = psn_params['d_feasibility'].values
    J_total = 14042
    print(f"  PSN-IRT: {len(psn_a)} items")

    # ── Load and deduplicate item mapping ────────────────────────────────
    print("\nLoading item mapping (with deduplication)...")
    mapping = pd.read_csv(os.path.join(PROJECT_ROOT, "artifacts/item_alignment_check/item_mapping.csv"))
    v1_to_psn = mapping['psn_irt_mmlu_position'].values
    dedup_mask = deduplicate_mapping(mapping)

    # ── Phase 1A: Read from cache (no API calls) ────────────────────────
    print("\n=== Phase 1A: Reading Cached Models ===")
    cached_model_names = scan_cached_models(cache_dir)
    cached_model_names = [m for m in cached_model_names if m not in pilot_set]
    print(f"  Found {len(cached_model_names)} non-pilot cached model dirs")

    new_models = []
    new_responses = []
    download_log = []
    n_cache_fail = 0
    t_cache_start = time.time()

    for model_name in cached_model_names:
        resp = read_cached_model(model_name, cache_dir)
        if resp is not None and len(resp) == 14042:
            acc = resp.mean()
            new_responses.append(resp)
            new_models.append(model_name)
            download_log.append({'model': model_name, 'status': 'OK_CACHED',
                                 'accuracy': f'{acc:.4f}', 'time_sec': '0'})
        else:
            n_cache_fail += 1

    t_cache = time.time() - t_cache_start
    print(f"  From cache: {len(new_models)} OK, {n_cache_fail} incomplete ({t_cache:.1f}s)")

    # ── Phase 1B: Download new models (API calls, time-bounded) ────────
    TARGET_N = 500
    needed_new = TARGET_N - len(pilot_models) - len(new_models)
    MAX_DOWNLOAD_TIME = 1800  # 30 min max for download phase
    print(f"\n=== Phase 1B: Downloading New Models (need {needed_new} more, max {MAX_DOWNLOAD_TIME}s) ===")

    if needed_new > 0:
        all_model_names = discover_all_v1_models()

        already_have = pilot_set | set(new_models)
        priority_keywords = ['70b', '70B', '65b', '65B', '34b', '34B', '72b', '72B',
                             '67b', '67B', '40b', '40B', '30b', '30B', 'Mixtral',
                             'wizard', 'Wizard', 'hermes', 'Hermes', 'platypus',
                             'Platypus', 'solar', 'SOLAR', 'Yi-', 'Qwen', 'deepseek',
                             'command-r', '13b', '13B', '20b', '20B']

        def priority_score(name):
            return sum(1 for kw in priority_keywords if kw in name)

        rng = np.random.RandomState(42)
        to_download = [m for m in all_model_names if m not in already_have]
        priority = [(priority_score(m), rng.random(), m) for m in to_download]
        priority.sort(key=lambda x: (-x[0], x[1]))
        to_download = [m for _, _, m in priority]
        print(f"  Candidates: {len(to_download)}")

        n_fail = 0
        n_skip = 0
        t_dl_start = time.time()
        n_attempted = 0

        for model_name in to_download:
            if len(new_models) + len(pilot_models) >= TARGET_N:
                print(f"  Target {TARGET_N} reached!")
                break
            if time.time() - t_dl_start > MAX_DOWNLOAD_TIME:
                print(f"  Time limit ({MAX_DOWNLOAD_TIME}s) reached, proceeding with available models")
                break

            t0 = time.time()
            try:
                resp = download_model_responses(model_name, cache_dir=cache_dir)
                dt = time.time() - t0
            except Exception:
                dt = time.time() - t0
                resp = None

            n_attempted += 1

            if resp is not None and len(resp) == 14042:
                acc = resp.mean()
                new_responses.append(resp)
                new_models.append(model_name)
                download_log.append({'model': model_name, 'status': 'OK',
                                     'accuracy': f'{acc:.4f}', 'time_sec': f'{dt:.1f}'})
            elif resp is not None:
                n_skip += 1
                download_log.append({'model': model_name, 'status': f'SKIP(n={len(resp)})',
                                     'accuracy': '', 'time_sec': f'{dt:.1f}'})
            else:
                n_fail += 1
                download_log.append({'model': model_name, 'status': 'FAIL',
                                     'accuracy': '', 'time_sec': f'{dt:.1f}'})

            if n_attempted % 25 == 0:
                elapsed = time.time() - t_dl_start
                total_ok = len(new_models)
                print(f"  [{total_ok + len(pilot_models)} total / {n_attempted} tried / {elapsed:.0f}s] "
                      f"fail={n_fail} skip={n_skip}")

            if dt < 1.0:
                time.sleep(0.1)
            else:
                time.sleep(0.3)

        t_dl = time.time() - t_dl_start
        print(f"\n  Download phase: {n_attempted} tried in {t_dl:.0f}s, "
              f"{len(new_models)} new OK total, fail={n_fail}, skip={n_skip}")

    print(f"\n  Total new models: {len(new_models)} (+ {len(pilot_models)} pilot = {len(new_models) + len(pilot_models)} total)")

    with open(download_log_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['model', 'status', 'accuracy', 'time_sec'])
        writer.writeheader()
        for pm in pilot_models:
            writer.writerow({'model': pm, 'status': 'PILOT', 'accuracy': '', 'time_sec': '0'})
        for row in download_log:
            writer.writerow(row)
    print(f"  Download log saved: {download_log_path}")

    # ── Merge pilot + new ────────────────────────────────────────────────
    print("\n=== Merging Pilot + New Models ===")
    if new_responses:
        X_new = np.vstack([r.reshape(1, -1) for r in new_responses]).astype(np.int8)
        X = np.vstack([X_pilot.astype(np.int8), X_new])
        all_models = pilot_models + new_models
    else:
        X = X_pilot.astype(np.int8)
        all_models = pilot_models

    N, J = X.shape
    print(f"  Combined response matrix: {N} models x {J} items")
    print(f"  Overall accuracy: {X.mean():.4f}")

    accuracies = X.mean(axis=1)
    high_acc_frac = (accuracies > 0.6).sum() / N
    print(f"  Models with acc > 0.6: {(accuracies > 0.6).sum()} ({high_acc_frac:.1%})")
    print(f"  Accuracy range: [{accuracies.min():.3f}, {accuracies.max():.3f}]")

    # Save response matrix
    np.savez_compressed(os.path.join(OUT_DIR, "expanded_response_matrix.npz"),
                        X=X, model_names=all_models)
    print(f"  Saved response matrix")

    # Zero-variance items
    item_var = X.var(axis=0)
    active_items = item_var > 0
    n_zero_var = (~active_items).sum()
    print(f"  Zero-variance items: {n_zero_var}")

    # ── Phase 2: MML-EM Fitting ──────────────────────────────────────────
    X_float = X.astype(np.float64)

    print("\n=== Phase 2a: Fitting 2PL MML-EM ===")
    t0 = time.time()
    a_2pl, b_2pl = fit_2pl_mml_em(X_float, n_quad=31, max_iter=100, tol=1e-4)
    t_2pl = time.time() - t0
    print(f"  2PL done in {t_2pl:.1f}s")

    print("\n=== Phase 2b: Fitting 3PL MML-EM (c=0.25) ===")
    t0 = time.time()
    a_3pl, b_3pl, c_3pl = fit_3pl_mml_em(X_float, c_fixed=0.25, n_quad=31, max_iter=100, tol=1e-4)
    t_3pl = time.time() - t0
    print(f"  3PL done in {t_3pl:.1f}s")

    # Save fitted params
    params_df = pd.DataFrame({
        'item_idx': range(J),
        'a_2pl': a_2pl, 'b_2pl': b_2pl,
        'a_3pl': a_3pl, 'b_3pl': b_3pl, 'c_3pl': c_3pl,
        'active': active_items.astype(int),
    })
    params_df.to_csv(os.path.join(OUT_DIR, "expanded_fitted_params.csv"), index=False)
    print(f"  Saved fitted parameters")

    # ── Phase 3: Parameter Comparison ────────────────────────────────────
    print("\n=== Phase 3: Parameter Comparison ===")

    # Map PSN-IRT params to v1 positions
    psn_a_mapped = np.full(J, np.nan)
    psn_b_mapped = np.full(J, np.nan)
    for i in range(J):
        if mapping['psn_irt_mmlu_position'].values[i] >= 0:
            psn_idx = v1_to_psn[i]
            psn_a_mapped[i] = psn_a[psn_idx]
            psn_b_mapped[i] = psn_b[psn_idx]

    # Comparison mask: deduplicated mapped items AND active (non-zero-variance)
    comp_mask = dedup_mask & active_items
    n_comp = comp_mask.sum()
    print(f"  Comparable items (deduped & active): {n_comp}")

    # 2PL comparison
    res_2pl_a = compare_parameters(a_2pl[comp_mask], psn_a_mapped[comp_mask], "a_2pl")
    res_2pl_b = compare_parameters(b_2pl[comp_mask], psn_b_mapped[comp_mask], "b_2pl")
    print(f"\n  2PL: a_r={res_2pl_a['pearson_r']:.4f}, a_rho={res_2pl_a['spearman_r']:.4f}, "
          f"b_r={res_2pl_b['pearson_r']:.4f}, b_rho={res_2pl_b['spearman_r']:.4f}")

    # 3PL comparison
    res_3pl_a = compare_parameters(a_3pl[comp_mask], psn_a_mapped[comp_mask], "a_3pl")
    res_3pl_b = compare_parameters(b_3pl[comp_mask], psn_b_mapped[comp_mask], "b_3pl")
    print(f"  3PL: a_r={res_3pl_a['pearson_r']:.4f}, a_rho={res_3pl_a['spearman_r']:.4f}, "
          f"b_r={res_3pl_b['pearson_r']:.4f}, b_rho={res_3pl_b['spearman_r']:.4f}")

    # Difficulty-binned a correlation
    print("\n  Difficulty-binned a correlation (3PL):")
    binned_a_3pl = difficulty_binned_correlation(a_3pl, psn_a_mapped, psn_b_mapped, comp_mask)
    for label, vals in binned_a_3pl.items():
        if 'pearson_r' in vals:
            print(f"    {label}: r={vals['pearson_r']:.4f}, n={vals['n']}")
        else:
            print(f"    {label}: {vals}")

    binned_a_2pl = difficulty_binned_correlation(a_2pl, psn_a_mapped, psn_b_mapped, comp_mask)

    # Plot 2x2
    plot_parameter_comparison_2x2(a_2pl, b_2pl, a_3pl, b_3pl,
                                   psn_a_mapped, psn_b_mapped, comp_mask,
                                   os.path.join(OUT_DIR, "parameter_comparison_expanded.png"))

    # ── Phase 4: lz* Calibration Check ───────────────────────────────────
    print("\n=== Phase 4: lz* Calibration Check ===")
    d_v1 = np.ones(J)
    c_arr = np.full(J, c_3pl)

    lz_stars = np.zeros(N)
    thetas = np.zeros(N)
    for i in range(N):
        x_i = X[i].astype(np.float64)
        theta_i = estimate_theta_mle(x_i, a_3pl, b_3pl, c_arr, d_v1)
        thetas[i] = theta_i
        lz_stars[i] = compute_lz_star(x_i, theta_i, a_3pl, b_3pl, c_arr, d_v1)
        if (i + 1) % 100 == 0:
            print(f"  {i+1}/{N} models processed")

    print(f"\n  lz* stats: mean={lz_stars.mean():.3f}, std={lz_stars.std():.3f}")
    print(f"  lz* range: [{lz_stars.min():.3f}, {lz_stars.max():.3f}]")
    print(f"  Flagged (lz* < -1.96): {(lz_stars < -1.96).sum()} / {N}")
    print(f"  Pilot comparison: pilot mean lz* was 11.7")

    plot_lz_star_distribution(lz_stars, os.path.join(OUT_DIR, "lz_star_distribution_expanded.png"))

    # ── Phase 5: Decision ────────────────────────────────────────────────
    a_r = res_3pl_a['pearson_r']
    if a_r > 0.4:
        decision = "POSITIVE: large-scale audit recoverable (a_r > 0.4)"
    elif a_r >= 0.2:
        decision = "AMBIGUOUS: moderate correlation (0.2 <= a_r <= 0.4), needs further analysis"
    else:
        decision = "NEGATIVE: classical IRT and neural IRT discrimination incompatible (a_r < 0.2)"

    print(f"\n=== Phase 5: Decision ===")
    print(f"  3PL a_pearson_r = {a_r:.4f}")
    print(f"  {decision}")

    # ── Save results ─────────────────────────────────────────────────────
    results = {
        'n_models': N,
        'n_pilot': len(pilot_models),
        'n_new': len(new_models),
        'n_items': J,
        'n_zero_var_items': int(n_zero_var),
        'n_comparable_items': int(n_comp),
        'n_total_mapped': int((mapping['psn_irt_mmlu_position'].values >= 0).sum()),
        'n_deduped_mapped': int(dedup_mask.sum()),
        'overall_accuracy': float(X.mean()),
        'high_accuracy_fraction': float(high_acc_frac),
        'fitting_time_2pl_sec': float(t_2pl),
        'fitting_time_3pl_sec': float(t_3pl),
        'parameter_comparison': {
            '2PL': {
                'a_discrimination': res_2pl_a,
                'b_difficulty': res_2pl_b,
            },
            '3PL': {
                'a_discrimination': res_3pl_a,
                'b_difficulty': res_3pl_b,
            },
        },
        'difficulty_binned_a_correlation': {
            '2PL': binned_a_2pl,
            '3PL': binned_a_3pl,
        },
        'lz_star_stats': {
            'mean': float(lz_stars.mean()),
            'std': float(lz_stars.std()),
            'min': float(lz_stars.min()),
            'max': float(lz_stars.max()),
            'n_flagged_1_96': int((lz_stars < -1.96).sum()),
            'n_flagged_2_58': int((lz_stars < -2.58).sum()),
        },
        'decision': decision,
        'hypothesis': 'a_pearson_r > 0.4 vs PSN-IRT (pilot N=63: a_r=0.111)',
        'per_model': [
            {
                'model': all_models[i],
                'accuracy': float(accuracies[i]),
                'theta': float(thetas[i]),
                'lz_star': float(lz_stars[i]),
                'source': 'pilot' if i < len(pilot_models) else 'new',
            }
            for i in range(N)
        ],
    }

    with open(os.path.join(OUT_DIR, "expanded_results.json"), 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\n  Saved expanded_results.json")

    print(f"\n{'='*60}")
    print(f"  EXPANDED REFIT COMPLETE")
    print(f"  Models: {N} ({len(pilot_models)} pilot + {len(new_models)} new)")
    print(f"  Comparable items: {n_comp} (12068 target after dedup)")
    print(f"  2PL a_r={res_2pl_a['pearson_r']:.4f}  b_r={res_2pl_b['pearson_r']:.4f}")
    print(f"  3PL a_r={res_3pl_a['pearson_r']:.4f}  b_r={res_3pl_b['pearson_r']:.4f}")
    print(f"  lz* mean={lz_stars.mean():.3f} std={lz_stars.std():.3f}")
    print(f"  Decision: {decision}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
