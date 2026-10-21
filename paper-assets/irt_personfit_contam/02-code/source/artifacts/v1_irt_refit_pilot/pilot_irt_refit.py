"""
V1 Leaderboard IRT Refit Pilot
Downloads v1 MMLU responses, fits 2PL/3PL IRT parameters, compares with PSN-IRT.
"""

import os
import sys
import json
import time
import warnings
import numpy as np
import pandas as pd
from scipy.optimize import minimize_scalar, minimize
from scipy.special import expit
from scipy.stats import pearsonr, spearmanr
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore')

PROJECT_ROOT = "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam"
OUT_DIR = os.path.join(PROJECT_ROOT, "artifacts/v1_irt_refit_pilot")

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

MODEL_LIST = [
    "mistralai__Mistral-7B-Instruct-v0.1",
    "mistralai__Mistral-7B-v0.1",
    "lmsys__vicuna-7b-v1.3",
    "lmsys__vicuna-7b-v1.5",
    "lmsys__vicuna-13b-v1.3",
    "lmsys__vicuna-13b-v1.5",
    "meta-llama__Llama-2-7b-hf",
    "meta-llama__Llama-2-7b-chat-hf",
    "meta-llama__Llama-2-13b-hf",
    "meta-llama__Llama-2-13b-chat-hf",
    "meta-llama__Llama-2-70b-hf",
    "meta-llama__Llama-2-70b-chat-hf",
    "tiiuae__falcon-7b",
    "tiiuae__falcon-7b-instruct",
    "tiiuae__falcon-40b",
    "tiiuae__falcon-40b-instruct",
    "mosaicml__mpt-7b",
    "mosaicml__mpt-7b-instruct",
    "mosaicml__mpt-7b-chat",
    "mosaicml__mpt-30b",
    "mosaicml__mpt-30b-instruct",
    "mosaicml__mpt-30b-chat",
    "EleutherAI__pythia-12b-deduped",
    "EleutherAI__pythia-6.7b",
    "EleutherAI__pythia-2.8b-deduped",
    "EleutherAI__pythia-1.4b-deduped",
    "EleutherAI__gpt-neo-1.3B",
    "EleutherAI__gpt-neo-2.7B",
    "EleutherAI__gpt-j-6b",
    "togethercomputer__RedPajama-INCITE-7B-Base",
    "togethercomputer__RedPajama-INCITE-7B-Instruct",
    "stabilityai__stablelm-tuned-alpha-7b",
    "Open-Orca__OpenOrca-Platypus2-13B",
    "NousResearch__Nous-Hermes-llama-2-7b",
    "NousResearch__Nous-Hermes-13b",
    "teknium__OpenHermes-13B",
    "WizardLM__WizardLM-13B-V1.2",
    "WizardLM__WizardLM-7B-V1.0",
    "garage-bAInd__Platypus2-70B-instruct",
    "garage-bAInd__Platypus2-13B",
    "HuggingFaceH4__zephyr-7b-beta",
    "HuggingFaceH4__zephyr-7b-alpha",
    "microsoft__phi-1_5",
    "microsoft__phi-2",
    "01-ai__Yi-6B",
    "01-ai__Yi-34B",
    "Qwen__Qwen-7B",
    "Qwen__Qwen-14B",
    "Qwen__Qwen-72B",
    "internlm__internlm-7b",
    "internlm__internlm-20b",
    "THUDM__chatglm3-6b",
    "bigscience__bloom-7b1",
    "bigscience__bloom-3b",
    "bigscience__bloom-1b7",
    "cerebras__Cerebras-GPT-6.7B",
    "cerebras__Cerebras-GPT-2.7B",
    "google__gemma-7b",
    "google__gemma-2b",
    "upstage__SOLAR-10.7B-v1.0",
    "upstage__SOLAR-10.7B-Instruct-v1.0",
    "deepseek-ai__deepseek-llm-7b-base",
    "deepseek-ai__deepseek-llm-7b-chat",
    "deepseek-ai__deepseek-llm-67b-base",
    "deepseek-ai__deepseek-llm-67b-chat",
    "TinyLlama__TinyLlama-1.1B-Chat-v1.0",
    "openlm-research__open_llama_7b",
    "openlm-research__open_llama_13b",
    "openlm-research__open_llama_3b",
    "RWKV__rwkv-5-world-3b",
    "allenai__OLMo-7B",
    "allenai__OLMo-1B",
    "CohereTroika__c4ai-command-r-v01",
    "CohereForAI__c4ai-command-r-plus",
    "databricks__dolly-v2-12b",
    "databricks__dolly-v2-7b",
    "databricks__dolly-v2-3b",
    "Writer__camel-5b-hf",
    "h2oai__h2ogpt-oig-oasst1-512-6_9b",
    "OpenAssistant__oasst-sft-4-pythia-12b-epoch-3.5",
    "huggyllama__llama-7b",
    "huggyllama__llama-13b",
    "huggyllama__llama-30b",
    "huggyllama__llama-65b",
    "CalderaAI__30B-Lazarus",
    "psmathur__orca_mini_v3_7b",
    "psmathur__orca_mini_v3_13b",
    "ehartford__dolphin-llama-13b",
    "lmsys__vicuna-33b-v1.3",
    "TheBloke__guanaco-7B-HF",
    "TheBloke__guanaco-13B-HF",
    "TheBloke__guanaco-33B-HF",
    "TheBloke__guanaco-65B-HF",
    "ehartford__WizardLM-7B-V1.0-Uncensored",
    "ehartford__WizardLM-13B-V1.0-Uncensored",
    "jondurbin__airoboros-l2-7b-2.1",
    "jondurbin__airoboros-l2-13b-2.1",
    "jondurbin__airoboros-l2-70b-2.1",
    "codellama__CodeLlama-7b-hf",
    "codellama__CodeLlama-13b-hf",
    "codellama__CodeLlama-34b-hf",
]


def download_model_responses(model_name, cache_dir=None):
    """Download MMLU responses for a single model from v1 leaderboard.

    Uses huggingface_hub to download parquet files directly, avoiding
    load_dataset's slow split generation for models with many eval runs.
    Picks the latest timestamp that has all 57 subjects.
    """
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

    # Group MMLU parquet files by timestamp
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

    # Try timestamps from latest to earliest, pick first with 14042 items
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


def download_all_models(model_list, cache_dir=None):
    """Download responses for all models, return response matrix and successful model names."""
    successful = []
    response_vectors = []

    for i, model_name in enumerate(model_list):
        print(f"  [{i+1}/{len(model_list)}] {model_name}...", end=" ", flush=True)
        t0 = time.time()
        resp = download_model_responses(model_name, cache_dir=cache_dir)
        dt = time.time() - t0

        if resp is not None and len(resp) == 14042:
            response_vectors.append(resp)
            successful.append(model_name)
            acc = resp.mean()
            print(f"OK ({dt:.1f}s, acc={acc:.3f}, n={len(resp)})")
        elif resp is not None:
            print(f"SKIP (n={len(resp)}, expected 14042)")
        else:
            print(f"FAIL ({dt:.1f}s)")

    if not response_vectors:
        return None, []

    X = np.vstack(response_vectors).astype(np.int8)
    return X, successful


# ─── Custom 3PL MML-EM ──────────────────────────────────────────────────────

def _gauss_hermite_quadrature(n_points=41, bounds=(-4, 4)):
    """Uniform quadrature points with normal distribution weights."""
    theta = np.linspace(bounds[0], bounds[1], n_points)
    weights = np.exp(-0.5 * theta**2) / np.sqrt(2 * np.pi)
    weights /= weights.sum()
    return theta, weights


def _3pl_prob(theta, a, b, c):
    """3PL probability: P = c + (1-c) * sigmoid(a*(theta-b))."""
    z = a * (theta - b)
    return c + (1 - c) * expit(z)


def _e_step(X, a, b, c, theta_q, w_q):
    """E-step: compute expected sufficient statistics.

    Returns r_j (J, Q), f_q (Q,) - expected correct counts and total weights.
    """
    N, J = X.shape
    Q = len(theta_q)

    # P(x=1 | theta_q, a, b, c) for all items and quad points: (Q, J)
    P = c + (1 - c) * expit(a[None, :] * (theta_q[:, None] - b[None, :]))
    P = np.clip(P, 1e-15, 1 - 1e-15)

    # log P(x_i | theta_q) = sum_j x_ij*log(P_qj) + (1-x_ij)*log(1-P_qj)
    logP = np.log(P)      # (Q, J)
    log1mP = np.log(1 - P)  # (Q, J)

    # Vectorized: log_lik (N, Q) = X @ logP.T + (1-X) @ log1mP.T
    log_lik = X @ logP.T + (1 - X) @ log1mP.T  # (N, Q)
    log_lik += np.log(w_q)[None, :]
    log_lik -= log_lik.max(axis=1, keepdims=True)
    posterior = np.exp(log_lik)
    posterior /= posterior.sum(axis=1, keepdims=True)  # (N, Q)

    # Expected counts: r_j[j,q] = sum_i x_ij * posterior[i,q]
    r_j = X.T @ posterior   # (J, Q)
    f_q = posterior.sum(axis=0)  # (Q,)

    return r_j, f_q


def _m_step_vectorized(r_j, f_q, a, b, c, theta_q, n_newton=5):
    """Vectorized M-step using Newton-Raphson on all items simultaneously."""
    J = len(a)
    Q = len(theta_q)

    for _ in range(n_newton):
        # Compute P, sigma for all items at all quad points
        z = a[:, None] * (theta_q[None, :] - b[:, None])  # (J, Q)
        sig = expit(z)
        P = c + (1 - c) * sig
        P = np.clip(P, 1e-15, 1 - 1e-15)

        # Gradient and Hessian for b (with a fixed)
        # d log L / d b_j = -a_j * (1-c) * sum_q [(r_j[q] - f_q[q]*P_qj) * sig_qj*(1-sig_qj) / P_qj / (1-P_qj)]
        dP_db = -a[:, None] * (1 - c) * sig * (1 - sig)  # (J, Q)
        w = (r_j / P - (f_q[None, :] - r_j) / (1 - P))  # (J, Q)
        grad_b = (w * dP_db).sum(axis=1)  # (J,)

        # Approximate Hessian for b
        dP_db2 = dP_db * dP_db
        hess_b = -(f_q[None, :] * dP_db2 / (P * (1 - P))).sum(axis=1)  # (J,)
        hess_b = np.where(np.abs(hess_b) > 1e-10, hess_b, -1e-10)

        b_update = -grad_b / hess_b
        b_update = np.clip(b_update, -1.0, 1.0)
        b = np.clip(b + b_update, -6.0, 6.0)

        # Gradient and Hessian for a (with updated b)
        z = a[:, None] * (theta_q[None, :] - b[:, None])
        sig = expit(z)
        P = c + (1 - c) * sig
        P = np.clip(P, 1e-15, 1 - 1e-15)

        dP_da = (1 - c) * (theta_q[None, :] - b[:, None]) * sig * (1 - sig)  # (J, Q)
        w = (r_j / P - (f_q[None, :] - r_j) / (1 - P))
        grad_a = (w * dP_da).sum(axis=1)

        dP_da2 = dP_da * dP_da
        hess_a = -(f_q[None, :] * dP_da2 / (P * (1 - P))).sum(axis=1)
        hess_a = np.where(np.abs(hess_a) > 1e-10, hess_a, -1e-10)

        a_update = -grad_a / hess_a
        a_update = np.clip(a_update, -0.5, 0.5)
        a = np.clip(a + a_update, 0.01, 5.0)

    return a, b


def fit_2pl_mml_em(X, n_quad=31, max_iter=50, tol=1e-3):
    """2PL MML-EM estimation (vectorized).

    X: (N, J) binary response matrix
    Returns: a (J,), b (J,)
    """
    N, J = X.shape
    theta_q, w_q = _gauss_hermite_quadrature(n_quad)

    p_correct = X.mean(axis=0)
    b = -np.log(np.clip(p_correct, 0.01, 0.99) / (1 - np.clip(p_correct, 0.01, 0.99)))
    a = np.ones(J)
    c = 0.0  # 2PL has no guessing

    for iteration in range(max_iter):
        a_old = a.copy()

        r_j, f_q = _e_step(X, a, b, c, theta_q, w_q)
        a, b = _m_step_vectorized(r_j, f_q, a, b, c, theta_q, n_newton=3)

        change = np.max(np.abs(a - a_old))
        if iteration % 5 == 0:
            print(f"    Iter {iteration}: max delta(a) = {change:.6f}")
        if change < tol:
            print(f"    Converged at iter {iteration}")
            break

    return a, b


def fit_3pl_mml_em(X, c_fixed=0.25, n_quad=31, max_iter=50, tol=1e-3):
    """3PL MML-EM with fixed c (vectorized).

    X: (N, J) binary response matrix
    c_fixed: fixed guessing parameter (0.25 for 4-choice MC)
    Returns: a (J,), b (J,), c (scalar)
    """
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
        if iteration % 5 == 0:
            print(f"    Iter {iteration}: max delta(a) = {change:.6f}")
        if change < tol:
            print(f"    Converged at iter {iteration}")
            break

    return a, b, c_fixed


# ─── Analysis Functions ──────────────────────────────────────────────────────

def compare_parameters(v1_a, v1_b, v1_c, psn_a, psn_b, psn_c, psn_d, mask):
    """Compare v1-derived parameters with PSN-IRT parameters on mapped items."""
    results = {}

    for name, v1_vals, psn_vals in [
        ('a_discrimination', v1_a[mask], psn_a[mask]),
        ('b_difficulty', v1_b[mask], psn_b[mask]),
    ]:
        r_p, p_p = pearsonr(v1_vals, psn_vals)
        r_s, p_s = spearmanr(v1_vals, psn_vals)
        results[name] = {
            'pearson_r': float(r_p), 'pearson_p': float(p_p),
            'spearman_r': float(r_s), 'spearman_p': float(p_s),
            'v1_mean': float(v1_vals.mean()), 'v1_std': float(v1_vals.std()),
            'psn_mean': float(psn_vals.mean()), 'psn_std': float(psn_vals.std()),
        }

    if psn_c is not None:
        r_p, p_p = pearsonr(np.full(mask.sum(), v1_c), psn_c[mask])
        results['c_guessing'] = {
            'v1_fixed': float(v1_c),
            'psn_mean': float(psn_c[mask].mean()),
            'psn_std': float(psn_c[mask].std()),
            'note': 'v1 c is fixed, not estimated'
        }

    if psn_d is not None:
        results['d_feasibility'] = {
            'psn_mean': float(psn_d[mask].mean()),
            'psn_std': float(psn_d[mask].std()),
            'note': 'v1 does not estimate d; uses d=1.0'
        }

    return results


def plot_parameter_comparison(v1_a, v1_b, psn_a, psn_b, mask, out_path):
    """Scatter plots of v1 vs PSN-IRT parameters."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    ax = axes[0]
    ax.scatter(psn_a[mask], v1_a[mask], alpha=0.1, s=3, c='steelblue')
    r, _ = pearsonr(psn_a[mask], v1_a[mask])
    ax.set_xlabel('PSN-IRT discrimination (a)')
    ax.set_ylabel('V1-derived discrimination (a)')
    ax.set_title(f'Discrimination: r={r:.3f} (n={mask.sum()})')
    lims = [0, max(psn_a[mask].max(), v1_a[mask].max()) * 1.1]
    ax.plot(lims, lims, 'k--', alpha=0.3, lw=1)
    ax.set_xlim(lims)
    ax.set_ylim(lims)

    ax = axes[1]
    ax.scatter(psn_b[mask], v1_b[mask], alpha=0.1, s=3, c='coral')
    r, _ = pearsonr(psn_b[mask], v1_b[mask])
    ax.set_xlabel('PSN-IRT difficulty (b)')
    ax.set_ylabel('V1-derived difficulty (b)')
    ax.set_title(f'Difficulty: r={r:.3f} (n={mask.sum()})')
    lims_b = [min(psn_b[mask].min(), v1_b[mask].min()) - 0.2,
              max(psn_b[mask].max(), v1_b[mask].max()) + 0.2]
    ax.plot(lims_b, lims_b, 'k--', alpha=0.3, lw=1)
    ax.set_xlim(lims_b)
    ax.set_ylim(lims_b)

    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {out_path}")


def plot_lz_star_distribution(lz_stars, model_names, out_path):
    """Plot lz* distribution for all models."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    ax = axes[0]
    ax.hist(lz_stars, bins=50, color='steelblue', alpha=0.7, edgecolor='white')
    ax.axvline(x=-1.96, color='red', linestyle='--', alpha=0.7, label='z=-1.96')
    ax.axvline(x=0, color='gray', linestyle='-', alpha=0.3)
    n_flagged = np.sum(lz_stars < -1.96)
    ax.set_xlabel('lz* statistic')
    ax.set_ylabel('Count')
    ax.set_title(f'lz* Distribution (n={len(lz_stars)}, flagged={n_flagged})')
    ax.legend()

    ax = axes[1]
    sorted_idx = np.argsort(lz_stars)
    colors = ['red' if lz < -1.96 else 'steelblue' for lz in lz_stars[sorted_idx]]
    ax.barh(range(len(lz_stars)), lz_stars[sorted_idx], color=colors, height=0.8)
    ax.axvline(x=-1.96, color='red', linestyle='--', alpha=0.7)
    ax.axvline(x=0, color='gray', linestyle='-', alpha=0.3)
    ax.set_xlabel('lz* statistic')
    ax.set_ylabel('Model (sorted)')
    ax.set_title('lz* by Model')

    if len(model_names) <= 30:
        short_names = [m.split('__')[-1][:20] for m in np.array(model_names)[sorted_idx]]
        ax.set_yticks(range(len(lz_stars)))
        ax.set_yticklabels(short_names, fontsize=6)

    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {out_path}")


# ─── Main Pipeline ──────────────────────────────────────────────────────────

def main():
    np.random.seed(42)
    cache_dir = os.path.join(OUT_DIR, ".hf_cache")

    # Load PSN-IRT parameters
    print("Loading PSN-IRT parameters...")
    psn_params = pd.read_csv(os.path.join(PROJECT_ROOT, "artifacts/psn_irt_params/mmlu_params.csv"))
    psn_a = psn_params['a_discrimination'].values
    psn_b = psn_params['b_difficulty'].values
    psn_c = psn_params['c_guessing'].values
    psn_d = psn_params['d_feasibility'].values
    J_total = len(psn_a)
    print(f"  PSN-IRT: {J_total} items")

    # Load item mapping
    print("Loading item mapping...")
    mapping = pd.read_csv(os.path.join(PROJECT_ROOT, "artifacts/item_alignment_check/item_mapping.csv"))
    valid_mask = mapping['psn_irt_mmlu_position'].values >= 0
    v1_to_psn = mapping['psn_irt_mmlu_position'].values
    n_mapped = valid_mask.sum()
    print(f"  Mapped items: {n_mapped} / {J_total}")

    # Download v1 responses
    print(f"\nDownloading v1 responses for {len(MODEL_LIST)} models...")
    X, successful_models = download_all_models(MODEL_LIST, cache_dir=cache_dir)

    if X is None or len(successful_models) < 10:
        print(f"ERROR: Only {len(successful_models) if successful_models else 0} models downloaded. Need at least 10.")
        return

    N, J = X.shape
    print(f"\nResponse matrix: {N} models x {J} items")
    print(f"  Overall accuracy: {X.mean():.4f}")
    print(f"  Item variance range: [{X.var(axis=0).min():.4f}, {X.var(axis=0).max():.4f}]")

    # Filter items with zero variance
    item_var = X.var(axis=0)
    active_items = item_var > 0
    n_zero_var = (~active_items).sum()
    print(f"  Zero-variance items (all correct or all wrong): {n_zero_var}")

    # ─── Fit 2PL ──────────────────────────────────────────────────────────
    print("\n=== Fitting 2PL MML-EM ===")
    t0 = time.time()
    a_2pl, b_2pl = fit_2pl_mml_em(X.astype(np.float64), n_quad=31, max_iter=50, tol=1e-3)
    t_2pl = time.time() - t0
    print(f"  2PL done in {t_2pl:.1f}s")

    # ─── Fit 3PL (c=0.25) ────────────────────────────────────────────────
    print("\n=== Fitting 3PL MML-EM (c=0.25) ===")
    t0 = time.time()
    a_3pl, b_3pl, c_3pl = fit_3pl_mml_em(X.astype(np.float64), c_fixed=0.25,
                                           n_quad=31, max_iter=50, tol=1e-3)
    t_3pl = time.time() - t0
    print(f"  3PL done in {t_3pl:.1f}s")

    # ─── Parameter Comparison ─────────────────────────────────────────────
    print("\n=== Parameter Comparison (v1 3PL vs PSN-IRT) ===")
    # Build mapping: v1 position i -> PSN-IRT position v1_to_psn[i]
    # We need items where both v1 and PSN-IRT have valid data
    comp_mask = valid_mask & active_items
    n_comp = comp_mask.sum()
    print(f"  Comparable items: {n_comp}")

    # v1 parameters are indexed by v1 position
    # PSN-IRT parameters are indexed by PSN-IRT position = v1_to_psn[v1_pos]
    psn_a_mapped = np.full(J_total, np.nan)
    psn_b_mapped = np.full(J_total, np.nan)
    psn_c_mapped = np.full(J_total, np.nan)
    psn_d_mapped = np.full(J_total, np.nan)

    for i in range(J_total):
        if valid_mask[i]:
            psn_idx = v1_to_psn[i]
            psn_a_mapped[i] = psn_a[psn_idx]
            psn_b_mapped[i] = psn_b[psn_idx]
            psn_c_mapped[i] = psn_c[psn_idx]
            psn_d_mapped[i] = psn_d[psn_idx]

    comp_results_2pl = compare_parameters(
        a_2pl, b_2pl, 0.0, psn_a_mapped, psn_b_mapped, psn_c_mapped, psn_d_mapped, comp_mask)
    comp_results_3pl = compare_parameters(
        a_3pl, b_3pl, c_3pl, psn_a_mapped, psn_b_mapped, psn_c_mapped, psn_d_mapped, comp_mask)

    print(f"\n  2PL results:")
    for k, v in comp_results_2pl.items():
        if 'pearson_r' in v:
            print(f"    {k}: pearson={v['pearson_r']:.4f}, spearman={v['spearman_r']:.4f}")
    print(f"\n  3PL results:")
    for k, v in comp_results_3pl.items():
        if 'pearson_r' in v:
            print(f"    {k}: pearson={v['pearson_r']:.4f}, spearman={v['spearman_r']:.4f}")

    # ─── Plot parameter comparison ────────────────────────────────────────
    print("\n=== Generating Plots ===")
    plot_parameter_comparison(
        a_3pl, b_3pl, psn_a_mapped, psn_b_mapped, comp_mask,
        os.path.join(OUT_DIR, "parameter_comparison.png"))

    # ─── Person-fit (lz*) ────────────────────────────────────────────────
    print("\n=== Computing Person-fit (lz*) ===")
    # Use 3PL parameters with d=1.0
    d_v1 = np.ones(J_total)

    lz_stars = np.zeros(N)
    thetas = np.zeros(N)
    for i in range(N):
        x_i = X[i].astype(np.float64)
        theta_i = estimate_theta_mle(x_i, a_3pl, b_3pl, np.full(J_total, c_3pl), d_v1)
        thetas[i] = theta_i
        lz_stars[i] = compute_lz_star(x_i, theta_i, a_3pl, b_3pl,
                                       np.full(J_total, c_3pl), d_v1)
        if (i + 1) % 20 == 0:
            print(f"  {i+1}/{N} models processed")

    print(f"  lz* range: [{lz_stars.min():.3f}, {lz_stars.max():.3f}]")
    print(f"  lz* mean: {lz_stars.mean():.3f}, std: {lz_stars.std():.3f}")
    print(f"  Flagged (lz* < -1.96): {(lz_stars < -1.96).sum()} / {N}")

    plot_lz_star_distribution(lz_stars, successful_models,
                              os.path.join(OUT_DIR, "lz_star_distribution.png"))

    # ─── Save Results ─────────────────────────────────────────────────────
    print("\n=== Saving Results ===")

    # Save response matrix
    np.savez_compressed(os.path.join(OUT_DIR, "pilot_response_matrix.npz"),
                        X=X, model_names=successful_models)
    print(f"  Saved response matrix: {N}x{J}")

    # Save fitted parameters
    params_df = pd.DataFrame({
        'item_idx': range(J_total),
        'a_2pl': a_2pl, 'b_2pl': b_2pl,
        'a_3pl': a_3pl, 'b_3pl': b_3pl, 'c_3pl': c_3pl,
    })
    params_df.to_csv(os.path.join(OUT_DIR, "v1_fitted_params.csv"), index=False)

    # Save pilot results JSON
    pilot_results = {
        'n_models': N,
        'n_items': J,
        'n_mapped_items': int(n_comp),
        'n_zero_var_items': int(n_zero_var),
        'overall_accuracy': float(X.mean()),
        'fitting_time_2pl_sec': float(t_2pl),
        'fitting_time_3pl_sec': float(t_3pl),
        'parameter_comparison_2pl': comp_results_2pl,
        'parameter_comparison_3pl': comp_results_3pl,
        'lz_star_stats': {
            'mean': float(lz_stars.mean()),
            'std': float(lz_stars.std()),
            'min': float(lz_stars.min()),
            'max': float(lz_stars.max()),
            'n_flagged_1_96': int((lz_stars < -1.96).sum()),
            'n_flagged_2_58': int((lz_stars < -2.58).sum()),
        },
        'per_model': [
            {
                'model': successful_models[i],
                'accuracy': float(X[i].mean()),
                'theta': float(thetas[i]),
                'lz_star': float(lz_stars[i]),
            }
            for i in range(N)
        ],
        'successful_models': successful_models,
    }

    with open(os.path.join(OUT_DIR, "pilot_results.json"), 'w') as f:
        json.dump(pilot_results, f, indent=2)
    print("  Saved pilot_results.json")

    print("\n=== DONE ===")
    print(f"  Models: {N}")
    print(f"  3PL a correlation with PSN-IRT: {comp_results_3pl['a_discrimination']['pearson_r']:.4f}")
    print(f"  3PL b correlation with PSN-IRT: {comp_results_3pl['b_difficulty']['pearson_r']:.4f}")
    print(f"  lz* flagged: {(lz_stars < -1.96).sum()}/{N}")


if __name__ == "__main__":
    main()
