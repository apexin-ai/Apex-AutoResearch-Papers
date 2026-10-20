# fix exp006 baselines w1w2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 0
- **Tool calls:** 25
- **Original source:** `logs/chats/worker_fix_exp006_baselines_w1w2_20260514T035056.jsonl`
- **Structured JSON:** [`82ead5a87a854953048b.json`](../../sessions/82/82ead5a87a854953048b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

51 recorded events

### Tool call

_source line 1 · 2026-05-14T03:56:08.958157+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T03:56:08.963839+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "ToolSearch",
  "elapsed_ms": 5
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T03:56:08.964190+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls -la /root/contamcal-irt-calibration/exp006/baselines/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls -la /root/contamcal-irt-calibration/exp006/baselines/"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T03:56:08.964412+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/contamcal-irt-calibration/exp006/baselines/utils.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/contamcal-irt-calibration/exp006/baselines/utils.py"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T03:56:08.964597+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/contamcal-irt-calibration/exp006/run_all_baselines.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/contamcal-irt-calibration/exp006/run_all_baselines.py"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T03:56:08.964835+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 48\\ndrwxr-xr-x 3 root root 4096 May 14 11:43 .\\ndrwxr-xr-x 4 root root 4096 May 14 11:45 ..\\n-rw-r--r-- 1 root root  575 May 14 11:40 __init__.py\\ndrwxr-xr-x 2 root root 4096 May 14 11:43 __pycache__\\n-rw-r--r-- 1 root root 3731 May 14 11:41 dcr_fuzzy.py\\n-rw-r--r-- 1 root root 2010 May 14 11:41 emperor_mitigation.py\\n-rw-r--r-- 1 root root 1199 May 14 11:40 linear_regression.py\\n-rw-r--r-- 1 root root  562 May 14 11:40 raw_scores.py\\n-rw-r--r-- 1 root root 1110 May 14 11:40 remove_rescore.py\\n-rw-r--r-- 1 root root 2474 May 14 11:41 single_signal_2pl_gamma.py\\n-rw-r--r-- 1 root root 1403 May 14 11:40 utils.py\\n-rw-r--r-- 1 root root 2107 May 14 11:41 vanilla_4pl.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.67}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-14T03:56:08.965114+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Shared utilities for baseline calibration methods.\\\"\\\"\\\"\\nimport numpy as np\\nfrom scipy import stats\\n\\n\\ndef wilson_ci(n_correct, n_total, alpha=0.05):\\n    \\\"\\\"\\\"Wilson score interval for binomial proportion.\\\"\\\"\\\"\\n    if n_total == 0:\\n        return 0.0, 0.0, 0.0\\n    p_hat = n_correct / n_total\\n    z = stats.norm.ppf(1 - alpha / 2)\\n    denom = 1 + z**2 / n_total\\n    center = (p_hat + z**2 / (2 * n_total)) / denom\\n    margin = z * np.sqrt(p_hat * (1 - p_hat) / n_total + z**2 / (4 * n_total**2)) / denom\\n    return center, max(0, center - margin), min(1, center + margin)\\n\\n\\ndef bootstrap_ci(statistic_fn, data, n_boot=1000, alpha=0.05, rng=None):\\n    if rng is None:\\n        rng = np.random.default_rng(42)\\n    n = len(data[0])\\n    boot_stats = np.empty(n_boot)\\n    for b in range(n_boot):\\n        idx = rng.integers(0, n, size=n)\\n        resampled = tuple(arr[idx] for arr in data)\\n        boot_stats[b] = statistic_fn(*resampled)\\n    point = statistic_fn(*data)\\n    lo = np.percentile(boot_stats, 100 * alpha / 2)\\n    hi = np.percentile(boot_stats, 100 * (1 - alpha / 2))\\n    return point, lo, hi\\n\\n\\ndef make_result(calibrated_accuracy, ci_lower, ci_upper, method_name, details=None):\\n    return {\\n        \\\"calibrated_accuracy\\\": float(calibrated_accuracy),\\n        \\\"ci_lower\\\": float(ci_lower),\\n        \\\"ci_upper\\\": float(ci_upper),\\n        \\\"method_name\\\": method_name,\\n        \\\"details\\\": details or {},\\n    }\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.54}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T03:56:08.970679+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Run all baseline calibration methods and compare results.\\n\\nUsage:\\n    python run_all_baselines.py --dry-run           # synthetic data validation\\n    python run_all_baselines.py --data-dir &lt;path>    # real data\\n\\\"\\\"\\\"\\nimport argparse\\nimport json\\nimport os\\nimport sys\\nimport time\\nfrom pathlib import Path\\n\\nimport numpy as np\\nfrom scipy import stats\\n\\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\\nfrom baselines import ALL_BASELINES\\n\\n\\ndef generate_synthetic_data(n_models=5, n_items=10, dosages=None, seed=42):\\n    rng = np.random.default_rng(seed)\\n    if dosages is None:\\n        dosages = [0, 25, 50, 75, 100]\\n    assert len(dosages) == n_models\\n\\n    true_theta = rng.normal(0, 1, n_models)\\n    true_b = rng.normal(0, 1, n_items)\\n    true_a = np.abs(rng.normal(1, 0.3, n_items))\\n    true_gamma = 1.5\\n\\n    all_y = np.zeros((n_models, n_items), dtype=int)\\n    all_exposure = np.zeros((n_models, n_items))\\n    true_clean_acc = np.zeros(n_models)\\n\\n    for i in range(n_models):\\n        dose_frac = dosages[i] / 100.0\\n        n_contam = int(dose_frac * n_items)\\n        contam_items = rng.choice(n_items, n_contam, replace=False) if n_contam > 0 else []\\n\\n        for j in range(n_items):\\n            eta_clean = true_a[j] * (true_theta[i] - true_b[j])\\n            p_clean = 1.0 / (1.0 + np.exp(-eta_clean))\\n\\n            if j in contam_items:\\n                exposure = rng.uniform(0.5, 1.0)\\n                all_exposure[i, j] = exposure\\n                eta_contam = eta_clean + true_gamma * exposure\\n                p_contam = 1.0 / (1.0 + np.exp(-eta_contam))\\n                all_y[i, j] = int(rng.random() < p_contam)\\n            else:\\n                all_exposure[i, j] = rng.uniform(0, 0.1)\\n                all_y[i, j] = int(rng.random() < p_clean)\\n\\n            true_clean_acc[
…[truncated 7246 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 6
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T03:56:08.971136+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/contamcal-irt-calibration/exp006/baselines/vanilla_4pl.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/contamcal-irt-calibration/exp006/baselines/vanilla_4pl.py"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T03:56:08.971489+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Baseline 5: Vanilla 4PL IRT without gamma — standard IRT calibration.\\\"\\\"\\\"\\nimport numpy as np\\nimport os\\nfrom .utils import make_result\\n\\nSTAN_MODEL_DIR = \\\"/root/contamcal-irt-calibration/stan_models\\\"\\n\\n\\ndef calibrate(model_name, benchmark, item_scores, exposure_scores,\\n              all_y=None, all_exposure=None, model_idx=0, stan_model_path=None,\\n              n_chains=4, n_samples=1000, **kwargs):\\n    if all_y is None:\\n        all_y = item_scores.reshape(1, -1)\\n        model_idx = 0\\n\\n    try:\\n        from cmdstanpy import CmdStanModel\\n    except ImportError:\\n        return make_result(np.nan, np.nan, np.nan, \\\"vanilla_4pl\\\",\\n                           {\\\"error\\\": \\\"cmdstanpy not installed\\\"})\\n\\n    if stan_model_path is None:\\n        stan_model_path = os.path.join(STAN_MODEL_DIR, \\\"vanilla_4pl.stan\\\")\\n\\n    N_models, N_items = all_y.shape\\n    stan_data = {\\n        \\\"N_models\\\": N_models,\\n        \\\"N_items\\\": N_items,\\n        \\\"y\\\": all_y.tolist(),\\n    }\\n\\n    try:\\n        model = CmdStanModel(stan_file=stan_model_path)\\n        fit = model.sample(\\n            data=stan_data,\\n            chains=n_chains,\\n            iter_sampling=n_samples,\\n            iter_warmup=n_samples,\\n            seed=42,\\n            show_progress=False,\\n            show_console=False,\\n        )\\n    except Exception as e:\\n        return make_result(np.nan, np.nan, np.nan, \\\"vanilla_4pl\\\",\\n                           {\\\"error\\\": str(e)})\\n\\n    cal_samples = fit.stan_variable(\\\"calibrated_score\\\")[:, model_idx]\\n\\n    point = float(np.mean(cal_samples))\\n    ci_lo = float(np.percentile(cal_samples, 2.5))\\n    ci_hi = float(np.percentile(cal_samples, 97.5))\\n\\n    diagnostics = {}\\n    try:\\n        summary = fit.summary()\\n        diagnostics[\\\"max_rhat\\\"] = float(summary[\\\"R_h
…[truncated 529 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T03:56:08.971778+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/contamcal-irt-calibration/exp006/baselines/single_signal_2pl_gamma.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/contamcal-irt-calibration/exp006/baselines/single_signal_2pl_gamma.py"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T03:56:08.972008+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/contamcal-irt-calibration/exp006/baselines/linear_regression.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/contamcal-irt-calibration/exp006/baselines/linear_regression.py"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T03:56:08.972281+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Baseline 6: Single-signal 2PL+gamma IRT.\\n\\n2PL (discrimination + difficulty, no guessing/upper asymptote)\\nwith gamma contamination parameter.\\n\\\"\\\"\\\"\\nimport numpy as np\\nimport os\\nfrom .utils import make_result\\n\\nSTAN_MODEL_DIR = \\\"/root/contamcal-irt-calibration/stan_models\\\"\\n\\n\\ndef calibrate(model_name, benchmark, item_scores, exposure_scores,\\n              all_y=None, all_exposure=None, model_idx=0, stan_model_path=None,\\n              n_chains=4, n_samples=1000, **kwargs):\\n    if all_y is None:\\n        all_y = item_scores.reshape(1, -1)\\n        all_exposure = exposure_scores.reshape(1, -1)\\n        model_idx = 0\\n\\n    try:\\n        from cmdstanpy import CmdStanModel\\n    except ImportError:\\n        return make_result(np.nan, np.nan, np.nan, \\\"single_signal_2pl_gamma\\\",\\n                           {\\\"error\\\": \\\"cmdstanpy not installed\\\"})\\n\\n    if stan_model_path is None:\\n        stan_model_path = os.path.join(STAN_MODEL_DIR, \\\"contam_irt_2pl_gamma.stan\\\")\\n\\n    N_models, N_items = all_y.shape\\n    stan_data = {\\n        \\\"N_models\\\": N_models,\\n        \\\"N_items\\\": N_items,\\n        \\\"y\\\": all_y.tolist(),\\n        \\\"exposure\\\": all_exposure.tolist(),\\n    }\\n\\n    try:\\n        model = CmdStanModel(stan_file=stan_model_path)\\n        fit = model.sample(\\n            data=stan_data,\\n            chains=n_chains,\\n            iter_sampling=n_samples,\\n            iter_warmup=n_samples,\\n            seed=42,\\n            show_progress=False,\\n            show_console=False,\\n        )\\n    except Exception as e:\\n        return make_result(np.nan, np.nan, np.nan, \\\"single_signal_2pl_gamma\\\",\\n                           {\\\"error\\\": str(e)})\\n\\n    cal_samples = fit.stan_variable(\\\"calibrated_score\\\")[:, model_idx]\\n    gamma_samples = fit.stan_variable(\\\"gamma\\\")\\n\\n    po
…[truncated 942 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T03:56:08.976803+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Baseline 3: Linear exposure regression with bootstrap CI.\\\"\\\"\\\"\\nimport numpy as np\\nfrom .utils import bootstrap_ci, make_result\\n\\n\\ndef calibrate(model_name, benchmark, item_scores, exposure_scores, n_boot=1000, **kwargs):\\n    def _fit_intercept(scores, exposure):\\n        if np.std(exposure) < 1e-10:\\n            return np.mean(scores)\\n        beta1 = np.sum((exposure - exposure.mean()) * (scores - scores.mean())) / np.sum((exposure - exposure.mean())**2)\\n        beta0 = scores.mean() - beta1 * exposure.mean()\\n        return np.clip(beta0, 0, 1)\\n\\n    point = _fit_intercept(item_scores, exposure_scores)\\n    _, ci_lo, ci_hi = bootstrap_ci(\\n        _fit_intercept,\\n        (item_scores, exposure_scores),\\n        n_boot=n_boot,\\n    )\\n\\n    slope = 0.0\\n    if np.std(exposure_scores) > 1e-10:\\n        slope = float(np.sum((exposure_scores - exposure_scores.mean()) * (item_scores - item_scores.mean()))\\n                       / np.sum((exposure_scores - exposure_scores.mean())**2))\\n\\n    return make_result(\\n        calibrated_accuracy=point,\\n        ci_lower=ci_lo,\\n        ci_upper=ci_hi,\\n        method_name=\\\"linear_regression\\\",\\n        details={\\\"slope\\\": slope, \\\"intercept\\\": float(point)},\\n    )\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.57}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T03:56:08.977097+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/contamcal-irt-calibration/exp006/baselines/dcr_fuzzy.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/contamcal-irt-calibration/exp006/baselines/dcr_fuzzy.py"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T03:56:08.977412+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Baseline 1: DCR fuzzy inference (adapted from Xu et al., EMNLP 2025).\\n\\nOriginal DCR uses 4-level probing to get S1-S4 scores, then fuzzy inference\\nto compute a DCR Factor for multiplicative discounting.\\n\\nAdaptation: We derive S1-S4 from per-item exposure scores by computing the\\nfraction of items exceeding increasing contamination thresholds.\\n\\\"\\\"\\\"\\nimport numpy as np\\nfrom .utils import bootstrap_ci, make_result\\n\\n\\ndef _trapmf(x, abcd):\\n    a, b, c, d = abcd\\n    y = np.zeros_like(x, dtype=float)\\n    mask_rise = (x >= a) & (x < b)\\n    if b > a:\\n        y[mask_rise] = (x[mask_rise] - a) / (b - a)\\n    y[(x >= b) & (x <= c)] = 1.0\\n    mask_fall = (x > c) & (x <= d)\\n    if d > c:\\n        y[mask_fall] = (d - x[mask_fall]) / (d - c)\\n    return y\\n\\n\\ndef _trimf(x, abc):\\n    return _trapmf(x, [abc[0], abc[1], abc[1], abc[2]])\\n\\n\\ndef _compute_contamination_levels(exposure_scores):\\n    thresholds = [0.1, 0.3, 0.5, 0.7]\\n    return np.array([float(np.mean(exposure_scores > t)) for t in thresholds])\\n\\n\\ndef _fuzzy_dcr(s_values):\\n    if np.mean(s_values) < 0.02:\\n        return 0.0\\n\\n    x_in = np.linspace(0, 1, 101)\\n    in_low = _trapmf(x_in, [0, 0, 0.1, 0.3])\\n    in_med = _trapmf(x_in, [0.2, 0.4, 0.5, 0.6])\\n    in_high = _trapmf(x_in, [0.5, 0.8, 1.0, 1.0])\\n\\n    x_out = np.linspace(0, 1, 101)\\n    out_negligible = _trapmf(x_out, [0, 0, 0.1, 0.3])\\n    out_minor = _trimf(x_out, [0.1, 0.3, 0.5])\\n    out_moderate = _trimf(x_out, [0.3, 0.5, 0.7])\\n    out_significant = _trimf(x_out, [0.5, 0.7, 0.9])\\n    out_severe = _trapmf(x_out, [0.7, 0.9, 1.0, 1.0])\\n\\n    min_memb = max(0.001, np.mean(s_values))\\n    memberships = []\\n    for s in s_values:\\n        low_val = max(float(np.interp(s, x_in, in_low)), min_memb * 0.1)\\n        med_val = max(float(np.interp(s, x_in, in_med)), min_memb * 0.1)\\n        high_val = max(float(np
…[truncated 2232 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T03:56:08.979386+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/contamcal-irt-calibration/exp006/baselines/remove_rescore.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/contamcal-irt-calibration/exp006/baselines/remove_rescore.py"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T03:56:08.982242+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Baseline 4: Remove-and-rescore — drop high-exposure items.\\\"\\\"\\\"\\nimport numpy as np\\nfrom .utils import wilson_ci, make_result\\n\\n\\ndef calibrate(model_name, benchmark, item_scores, exposure_scores,\\n              threshold=0.5, **kwargs):\\n    mask = exposure_scores <= threshold\\n    n_kept = int(np.sum(mask))\\n    if n_kept == 0:\\n        return make_result(\\n            calibrated_accuracy=np.nan,\\n            ci_lower=np.nan,\\n            ci_upper=np.nan,\\n            method_name=\\\"remove_rescore\\\",\\n            details={\\\"threshold\\\": threshold, \\\"n_kept\\\": 0, \\\"n_removed\\\": len(item_scores)},\\n        )\\n    kept_scores = item_scores[mask]\\n    n_correct = int(np.sum(kept_scores))\\n    acc, ci_lo, ci_hi = wilson_ci(n_correct, n_kept)\\n    return make_result(\\n        calibrated_accuracy=np.mean(kept_scores),\\n        ci_lower=ci_lo,\\n        ci_upper=ci_hi,\\n        method_name=\\\"remove_rescore\\\",\\n        details={\\n            \\\"threshold\\\": threshold,\\n            \\\"n_kept\\\": n_kept,\\n            \\\"n_removed\\\": int(len(item_scores) - n_kept),\\n            \\\"frac_removed\\\": float(1 - n_kept / len(item_scores)),\\n        },\\n    )\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T03:56:08.982623+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/contamcal-irt-calibration/exp006/baselines/raw_scores.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/contamcal-irt-calibration/exp006/baselines/raw_scores.py"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-14T03:56:08.982851+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/contamcal-irt-calibration/exp006/baselines/emperor_mitigation.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/contamcal-irt-calibration/exp006/baselines/emperor_mitigation.py"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-14T03:56:08.983100+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Baseline 7: Raw scores — no calibration, trivial anchor point.\\\"\\\"\\\"\\nimport numpy as np\\nfrom .utils import wilson_ci, make_result\\n\\n\\ndef calibrate(model_name, benchmark, item_scores, exposure_scores, **kwargs):\\n    n_correct = int(np.sum(item_scores))\\n    n_total = len(item_scores)\\n    acc, ci_lo, ci_hi = wilson_ci(n_correct, n_total)\\n    return make_result(\\n        calibrated_accuracy=np.mean(item_scores),\\n        ci_lower=ci_lo,\\n        ci_upper=ci_hi,\\n        method_name=\\\"raw_scores\\\",\\n        details={\\\"n_items\\\": n_total, \\\"n_correct\\\": n_correct},\\n    )\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T03:56:08.983412+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Baseline 2: Emperor's mitigation — rephrasing + option shuffling.\\n\\nAdapted from Sun et al. (ICML 2025) \\\"The Emperor's New Clothes in Benchmarking?\\\"\\nFor contaminated items (exposure > threshold), use rephrased/shuffled scores.\\nFor clean items, keep original scores.\\n\\\"\\\"\\\"\\nimport numpy as np\\nfrom .utils import bootstrap_ci, wilson_ci, make_result\\n\\n\\ndef calibrate(model_name, benchmark, item_scores, exposure_scores,\\n              paraphrase_scores=None, exposure_threshold=0.5,\\n              n_boot=1000, **kwargs):\\n    n = len(item_scores)\\n    contaminated = exposure_scores > exposure_threshold\\n\\n    if paraphrase_scores is not None:\\n        rephrased = np.array(paraphrase_scores, dtype=float)\\n    else:\\n        rng = np.random.default_rng(42)\\n        rephrased = item_scores.copy().astype(float)\\n        for i in range(n):\\n            if contaminated[i]:\\n                flip_prob = exposure_scores[i] * 0.3\\n                if item_scores[i] == 1 and rng.random() < flip_prob:\\n                    rephrased[i] = 0.0\\n\\n    mitigated = np.where(contaminated, rephrased, item_scores)\\n\\n    n_correct = int(np.sum(mitigated))\\n    acc, ci_lo, ci_hi = wilson_ci(n_correct, n)\\n\\n    def _boot_stat(orig, reph, contam_mask):\\n        m = np.where(contam_mask > 0.5, reph, orig)\\n        return np.mean(m)\\n\\n    point, ci_lo_b, ci_hi_b = bootstrap_ci(\\n        _boot_stat,\\n        (item_scores, rephrased, contaminated.astype(float)),\\n        n_boot=n_boot,\\n    )\\n\\n    return make_result(\\n        calibrated_accuracy=float(np.mean(mitigated)),\\n        ci_lower=ci_lo_b,\\n        ci_upper=ci_hi_b,\\n        method_name=\\\"emperor_mitigation\\\",\\n        details={\\n            \\\"n_contaminated\\\": int(np.sum(contaminated)),\\n            \\\"n_clean\\\": int(np.sum(~contaminated)),\\n            \\\"exposure_threshold\\\": exposure_t
…[truncated 346 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T03:56:08.983650+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/contamcal-irt-calibration/exp006/baselines/__init__.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/contamcal-irt-calibration/exp006/baselines/__init__.py"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T03:56:08.983869+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Baseline calibration methods for exp-006.\\\"\\\"\\\"\\nfrom . import (\\n    dcr_fuzzy,\\n    emperor_mitigation,\\n    linear_regression,\\n    remove_rescore,\\n    vanilla_4pl,\\n    single_signal_2pl_gamma,\\n    raw_scores,\\n)\\n\\nALL_BASELINES = {\\n    \\\"dcr_fuzzy\\\": dcr_fuzzy.calibrate,\\n    \\\"emperor_mitigation\\\": emperor_mitigation.calibrate,\\n    \\\"linear_regression\\\": linear_regression.calibrate,\\n    \\\"remove_rescore\\\": remove_rescore.calibrate,\\n    \\\"vanilla_4pl\\\": vanilla_4pl.calibrate,\\n    \\\"single_signal_2pl_gamma\\\": single_signal_2pl_gamma.calibrate,\\n    \\\"raw_scores\\\": raw_scores.calibrate,\\n}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T03:56:08.984159+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -n \"def run_baselines\\|def compute_metrics\\|def print_comparison\" /root/contamcal-irt-calibration/exp006/run_all_baselines.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -n \"def run_baselines\\|def compute_metrics\\|def print_comparison\" /root/contamcal-irt-calibration/exp006/run_all_baselines.py"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T03:56:08.988495+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T03:56:08.988894+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -n \"def \" /root/contamcal-irt-calibration/exp006/run_all_baselines.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -n \"def \" /root/contamcal-irt-calibration/exp006/run_all_baselines.py"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T03:56:08.989169+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"22:def generate_synthetic_data(n_models=5, n_items=10, dosages=None, seed=42):\\n72:def compute_metrics(results, true_clean_acc, dosages):\\n122:def run_baselines(data, skip_stan=False):\\n172:def print_comparison_table(results, data, metrics):\\n224:def main():\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.72}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T03:56:08.989425+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -n +72 /root/contamcal-irt-calibration/exp006/run_all_baselines.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -n +72 /root/contamcal-irt-calibration/exp006/run_all_baselines.py"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T03:56:08.989869+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"def compute_metrics(results, true_clean_acc, dosages):\\n    metrics = {}\\n    for method, method_results in results.items():\\n        cal_accs = [r[\\\"calibrated_accuracy\\\"] for r in method_results]\\n        ci_los = [r[\\\"ci_lower\\\"] for r in method_results]\\n        ci_his = [r[\\\"ci_upper\\\"] for r in method_results]\\n\\n        valid = [i for i in range(len(cal_accs)) if not np.isnan(cal_accs[i])]\\n        if not valid:\\n            metrics[method] = {\\n                \\\"mae\\\": np.nan, \\\"coverage_95\\\": np.nan, \\\"sharpness\\\": np.nan,\\n                \\\"kendall_tau\\\": np.nan, \\\"dose_monotonicity\\\": np.nan,\\n            }\\n            continue\\n\\n        mae = np.mean([abs(cal_accs[i] - true_clean_acc[i]) for i in valid])\\n\\n        covered = sum(1 for i in valid\\n                       if ci_los[i] <= true_clean_acc[i] <= ci_his[i])\\n        coverage = covered / len(valid)\\n\\n        widths = [ci_his[i] - ci_los[i] for i in valid]\\n        sharpness = np.mean(widths)\\n\\n        cal_valid = [cal_accs[i] for i in valid]\\n        true_valid = [true_clean_acc[i] for i in valid]\\n        if len(valid) >= 3:\\n            tau, _ = stats.kendalltau(cal_valid, true_valid)\\n        else:\\n            tau = np.nan\\n\\n        dose_valid = [(dosages[i], cal_accs[i] - true_clean_acc[i]) for i in valid]\\n        dose_valid.sort(key=lambda x: x[0])\\n        if len(dose_valid) >= 3:\\n            dose_vals = [d[0] for d in dose_valid]\\n            effect_vals = [d[1] for d in dose_valid]\\n            mono_tau, _ = stats.kendalltau(dose_vals, effect_vals)\\n        else:\\n            mono_tau = np.nan\\n\\n        metrics[method] = {\\n            \\\"mae\\\": float(mae),\\n            \\\"coverage_95\\\": float(coverage),\\n            \\\"sharpness\\\": float(sharpness),\\n            \\\"kendall_tau\\\": float(tau) if not np.isnan(tau) else np.nan,\\n           
…[truncated 7244 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T03:56:08.997288+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat > /root/contamcal-irt-calibration/exp006/baselines/utils.py << 'PYEOF'\n\"\"\"Shared utilities for baseline calibration methods.\"\"\"\nimport numpy as np\nfrom scipy import stats\n\n\ndef wilson_ci(n_correct, n_total, alpha=0.05):\n    \"\"\"Wilson score interval for binomial proportion.\"\"\"\n    if n_total == 0:\n        return 0.0, 0.0, 0.0\n    p_hat = n_correct / n_total\n    z = stats.norm.ppf(1 - alpha / 2)\n    denom = 1 + z**2 / n_total\n    center = (p_hat + z**2 / (2 * n_total)) / denom\n    margin = z * np.sqrt(p_hat * (1 - p_hat) / n_total + z**2 / (4 * n_total**2)) / denom\n    return center, max(0, center - margin), min(1, center + margin)\n\n\ndef wilson_ci_levels(n_correct, n_total):\n    \"\"\"Wilson CIs at 50%, 80%, 95% levels.\"\"\"\n    ci = {}\n    for level, alpha in [(50, 0.50), (80, 0.20), (95, 0.05)]:\n        _, lo, hi = wilson_ci(n_correct, n_total, alpha=alpha)\n        ci[f\"ci_{level}_lower\"] = float(lo)\n        ci[f\"ci_{level}_upper\"] = float(hi)\n    return ci\n\n\ndef bootstrap_ci(statistic_fn, data, n_boot=1000, alpha=0.05, rng=None):\n    if rng is None:\n        rng = np.random.default_rng(42)\n    n = len(data[0])\n    boot_stats = np.empty(n_boot)\n    for b in range(n_boot):\n        idx = rng.integers(0, n, size=n)\n        resampled = tuple(arr[idx] for arr in data)\n        boot_stats[b] = statistic_fn(*resampled)\n    point = statistic_fn(*data)\n    lo = np.percentile(boot_stats, 100 * alpha / 2)\n    hi = np.percentile(boot_stats, 100 * (1 - alpha / 2))\n    return point, lo, hi\n\n\ndef bootstrap_ci_levels(statistic_fn, data, n_boot=1000, rng=None):\n    \"\"\"Bootstrap CIs at 50%, 80%, 95% levels.\"\"\"\n    if rng is None:\n        rng = np.random.default_rng(42)\n    n = len(data[0])\n    boot_stats = np.empty(n_boot)\n    for b in range(n_boot):\n        idx = rng.integers(0, n, size=n)\n        resampled = tuple(arr[idx] for arr in data)\n        boot_stats[b] = statistic_fn(*resampled)\n    point = statistic_fn(*data)\n    ci = {}\n    for level, alpha in [(50, 0.50), (80, 0.20), (95, 0.05)]:\n        ci[f\"ci_{level}_lower\"] = float(np.percentile(boot_stats, 100 * alpha / 2))\n        ci[f\"ci_{level}_upper\"] = float(np.percentile(boot_stats, 100 * (1 - alpha / 2)))\n    return point, ci\n\n\ndef posterior_ci_levels(samples):\n    \"\"\"Extract 50/80/95% CIs from posterior samples.\"\"\"\n    return {\n        \"ci_50_lower\": float(np.percentile(samples, 25)),\n        \"ci_50_upper\": float(np.percentile(samples, 75)),\n        \"ci_80_lower\": float(np.percentile(samples, 10)),\n        \"ci_80_upper\": float(np.percentile(samples, 90)),\n        \"ci_95_lower\": float(np.percentile(samples, 2.5)),\n        \"ci_95_upper\": float(np.percentile(samples, 97.5)),\n    }\n\n\ndef make_result(calibrated_accuracy, ci, method_name, details=None):\n    result = {\n        \"calibrated_accuracy\": float(calibrated_accuracy),\n        \"method_name\": method_name,\n        \"details\": details or {},\n    }\n    result.update(ci)\n    return result\nPYEOF\necho \"utils.py written\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat > /root/contamcal-irt-calibration/exp006/baselines/utils.py << 'PYEOF'\n\"\"\"Shared utilities for baseline calibration methods.\"\"\"\nimport numpy as np\nfrom scipy import stats\n\n\ndef wilson_ci(n_correct, n_total, alpha=0.05):\n    \"\"\"Wilson score interval for binomial proportion.\"\"\"\n    if n_total == 0:\n        return 0.0, 0.0, 0.0\n    p_hat = n_correct / n_total\n    z = stats.norm.ppf(1 - alpha / 2)\n    denom = 1 + z**2 / n_total\n    center = (p_hat + z**2 / (2 * n_total)) / denom\n    margin = z * np.sqrt(p_hat * (1 - p_hat) / n_total + z**2 / (4 * n_total**2)) / denom\n    return center, max(0, center - margin), min(1, center + margin)\n\n\ndef wilson_ci_levels(n_correct, n_total):\n    \"\"\"Wilson CIs at 50%, 80%, 95% levels.\"\"\"\n    ci = {}\n    for level, alpha in [(50, 0.50), (80, 0.20), (95, 0.05)]:\n        _, lo, hi = wilson_ci(n_correct, n_total, alpha=alpha)\n        ci[f\"ci_{level}_lower\"] = float(lo)\n        ci[f\"ci_{level}_upper\"] = float(hi)\n    return ci\n\n\ndef bootstrap_ci(statistic_fn, data, n_boot=1000, alpha=0.05, rng=None):\n    if rng is None:\n        rng = np.random.default_rng(42)\n    n = len(data[0])\n    boot_stats = np.empty(n_boot)\n    for b in range(n_boot):\n        idx = rng.integers(0, n, size=n)\n        resampled = tuple(arr[idx] for arr in data)\n        boot_stats[b] = statistic_fn(*resampled)\n    point = statistic_fn(*data)\n    lo = np.percentile(boot_stats, 100 * alpha / 2)\n    hi = np.percentile(boot_stats, 100 * (1 - alpha / 2))\n    return point, lo, hi\n\n\ndef bootstrap_ci_levels(statistic_fn, data, n_boot=1000, rng=None):\n    \"\"\"Bootstrap CIs at 50%, 80%, 95% levels.\"\"\"\n    if rng is None:\n        rng = np.random.default_rng(42)\n    n = len(data[0])\n    boot_stats = np.empty(n_boot)\n    for b in range(n_boot):\n        idx = rng.integers(0, n, size=n)\n        resampled = tuple(arr[idx] for arr in data)\n        boot_stats[b] = statistic_fn(*resampled)\n    point = statistic_fn(*data)\n    ci = {}\n    for level, alpha in [(50, 0.50), (80, 0.20), (95, 0.05)]:\n        ci[f\"ci_{level}_lower\"] = float(np.percentile(boot_stats, 100 * alpha / 2))\n        ci[f\"ci_{level}_upper\"] = float(np.percentile(boot_stats, 100 * (1 - alpha / 2)))\n    return point, ci\n\n\ndef posterior_ci_levels(samples):\n    \"\"\"Extract 50/80/95% CIs from posterior samples.\"\"\"\n    return {\n        \"ci_50_lower\": float(np.percentile(samples, 25)),\n        \"ci_50_upper\": float(np.percentile(samples, 75)),\n        \"ci_80_lower\": float(np.percentile(samples, 10)),\n        \"ci_80_upper\": float(np.percentile(samples, 90)),\n        \"ci_95_lower\": float(np.percentile(samples, 2.5)),\n        \"ci_95_upper\": float(np.percentile(samples, 97.5)),\n    }\n\n\ndef make_result(calibrated_accuracy, ci, method_name, details=None):\n    result = {\n        \"calibrated_accuracy\": float(calibrated_accuracy),\n        \"method_name\": method_name,\n        \"details\": details or {},\n    }\n    result.update(ci)\n    return result\nPYEOF\necho \"utils.py written\""
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T03:56:08.997811+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"utils.py written\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T03:56:08.998076+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat > /root/contamcal-irt-calibration/exp006/baselines/vanilla_4pl.py << 'PYEOF'\n\"\"\"Baseline 5: Vanilla 4PL IRT without gamma — standard IRT calibration.\"\"\"\nimport numpy as np\nimport os\nfrom .utils import make_result, posterior_ci_levels\n\nSTAN_MODEL_DIR = \"/root/contamcal-irt-calibration/stan_models\"\n\n\ndef calibrate(model_name, benchmark, item_scores, exposure_scores,\n              all_y=None, all_exposure=None, model_idx=0, stan_model_path=None,\n              n_chains=4, n_samples=1000, **kwargs):\n    if all_y is None:\n        all_y = item_scores.reshape(1, -1)\n        model_idx = 0\n\n    nan_ci = {f\"ci_{l}_{b}\": np.nan for l in [50, 80, 95] for b in [\"lower\", \"upper\"]}\n\n    try:\n        from cmdstanpy import CmdStanModel\n    except ImportError:\n        return make_result(np.nan, nan_ci, \"vanilla_4pl\",\n                           {\"error\": \"cmdstanpy not installed\"})\n\n    if stan_model_path is None:\n        stan_model_path = os.path.join(STAN_MODEL_DIR, \"vanilla_4pl.stan\")\n\n    N_models, N_items = all_y.shape\n    stan_data = {\n        \"N_models\": N_models,\n        \"N_items\": N_items,\n        \"y\": all_y.tolist(),\n    }\n\n    try:\n        model = CmdStanModel(stan_file=stan_model_path)\n        fit = model.sample(\n            data=stan_data,\n            chains=n_chains,\n            iter_sampling=n_samples,\n            iter_warmup=n_samples,\n            seed=42,\n            show_progress=False,\n            show_console=False,\n        )\n    except Exception as e:\n        return make_result(np.nan, nan_ci, \"vanilla_4pl\",\n                           {\"error\": str(e)})\n\n    cal_samples = fit.stan_variable(\"calibrated_score\")[:, model_idx]\n\n    point = float(np.mean(cal_samples))\n    ci = posterior_ci_levels(cal_samples)\n\n    diagnostics = {}\n    try:\n        summary = fit.summary()\n        diagnostics[\"max_rhat\"] = float(summary[\"R_hat\"].max())\n        diagnostics[\"min_ess\"] = float(summary[\"N_Eff\"].min())\n    except Exception:\n        pass\n    diagnostics[\"n_models\"] = N_models\n    diagnostics[\"n_items\"] = N_items\n\n    return make_result(\n        calibrated_accuracy=point,\n        ci=ci,\n        method_name=\"vanilla_4pl\",\n        details=diagnostics,\n    )\nPYEOF\necho \"vanilla_4pl.py written\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat > /root/contamcal-irt-calibration/exp006/baselines/vanilla_4pl.py << 'PYEOF'\n\"\"\"Baseline 5: Vanilla 4PL IRT without gamma — standard IRT calibration.\"\"\"\nimport numpy as np\nimport os\nfrom .utils import make_result, posterior_ci_levels\n\nSTAN_MODEL_DIR = \"/root/contamcal-irt-calibration/stan_models\"\n\n\ndef calibrate(model_name, benchmark, item_scores, exposure_scores,\n              all_y=None, all_exposure=None, model_idx=0, stan_model_path=None,\n              n_chains=4, n_samples=1000, **kwargs):\n    if all_y is None:\n        all_y = item_scores.reshape(1, -1)\n        model_idx = 0\n\n    nan_ci = {f\"ci_{l}_{b}\": np.nan for l in [50, 80, 95] for b in [\"lower\", \"upper\"]}\n\n    try:\n        from cmdstanpy import CmdStanModel\n    except ImportError:\n        return make_result(np.nan, nan_ci, \"vanilla_4pl\",\n                           {\"error\": \"cmdstanpy not installed\"})\n\n    if stan_model_path is None:\n        stan_model_path = os.path.join(STAN_MODEL_DIR, \"vanilla_4pl.stan\")\n\n    N_models, N_items = all_y.shape\n    stan_data = {\n        \"N_models\": N_models,\n        \"N_items\": N_items,\n        \"y\": all_y.tolist(),\n    }\n\n    try:\n        model = CmdStanModel(stan_file=stan_model_path)\n        fit = model.sample(\n            data=stan_data,\n            chains=n_chains,\n            iter_sampling=n_samples,\n            iter_warmup=n_samples,\n            seed=42,\n            show_progress=False,\n            show_console=False,\n        )\n    except Exception as e:\n        return make_result(np.nan, nan_ci, \"vanilla_4pl\",\n                           {\"error\": str(e)})\n\n    cal_samples = fit.stan_variable(\"calibrated_score\")[:, model_idx]\n\n    point = float(np.mean(cal_samples))\n    ci = posterior_ci_levels(cal_samples)\n\n    diagnostics = {}\n    try:\n        summary = fit.summary()\n        diagnostics[\"max_rhat\"] = float(summary[\"R_hat\"].max())\n        diagnostics[\"min_ess\"] = float(summary[\"N_Eff\"].min())\n    except Exception:\n        pass\n    diagnostics[\"n_models\"] = N_models\n    diagnostics[\"n_items\"] = N_items\n\n    return make_result(\n        calibrated_accuracy=point,\n        ci=ci,\n        method_name=\"vanilla_4pl\",\n        details=diagnostics,\n    )\nPYEOF\necho \"vanilla_4pl.py written\""
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T03:56:08.998400+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"vanilla_4pl.py written\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.74}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T03:56:08.998711+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat > /root/contamcal-irt-calibration/exp006/baselines/single_signal_2pl_gamma.py << 'PYEOF'\n\"\"\"Baseline 6: Single-signal 2PL+gamma IRT.\n\n2PL (discrimination + difficulty, no guessing/upper asymptote)\nwith gamma contamination parameter.\n\"\"\"\nimport numpy as np\nimport os\nfrom .utils import make_result, posterior_ci_levels\n\nSTAN_MODEL_DIR = \"/root/contamcal-irt-calibration/stan_models\"\n\n\ndef calibrate(model_name, benchmark, item_scores, exposure_scores,\n              all_y=None, all_exposure=None, model_idx=0, stan_model_path=None,\n              n_chains=4, n_samples=1000, **kwargs):\n    if all_y is None:\n        all_y = item_scores.reshape(1, -1)\n        all_exposure = exposure_scores.reshape(1, -1)\n        model_idx = 0\n\n    nan_ci = {f\"ci_{l}_{b}\": np.nan for l in [50, 80, 95] for b in [\"lower\", \"upper\"]}\n\n    try:\n        from cmdstanpy import CmdStanModel\n    except ImportError:\n        return make_result(np.nan, nan_ci, \"single_signal_2pl_gamma\",\n                           {\"error\": \"cmdstanpy not installed\"})\n\n    if stan_model_path is None:\n        stan_model_path = os.path.join(STAN_MODEL_DIR, \"contam_irt_2pl_gamma.stan\")\n\n    N_models, N_items = all_y.shape\n    stan_data = {\n        \"N_models\": N_models,\n        \"N_items\": N_items,\n        \"y\": all_y.tolist(),\n        \"exposure\": all_exposure.tolist(),\n    }\n\n    try:\n        model = CmdStanModel(stan_file=stan_model_path)\n        fit = model.sample(\n            data=stan_data,\n            chains=n_chains,\n            iter_sampling=n_samples,\n            iter_warmup=n_samples,\n            seed=42,\n            show_progress=False,\n            show_console=False,\n        )\n    except Exception as e:\n        return make_result(np.nan, nan_ci, \"single_signal_2pl_gamma\",\n                           {\"error\": str(e)})\n\n    cal_samples = fit.stan_variable(\"calibrated_score\")[:, model_idx]\n    gamma_samples = fit.stan_variable(\"gamma\")\n\n    point = float(np.mean(cal_samples))\n    ci = posterior_ci_levels(cal_samples)\n\n    diagnostics = {\n        \"gamma_mean\": float(np.mean(gamma_samples)),\n        \"gamma_sd\": float(np.std(gamma_samples)),\n    }\n    try:\n        summary = fit.summary()\n        diagnostics[\"max_rhat\"] = float(summary[\"R_hat\"].max())\n        diagnostics[\"min_ess\"] = float(summary[\"N_Eff\"].min())\n    except Exception:\n        pass\n    diagnostics[\"n_models\"] = N_models\n    diagnostics[\"n_items\"] = N_items\n\n    return make_result(\n        calibrated_accuracy=point,\n        ci=ci,\n        method_name=\"single_signal_2pl_gamma\",\n        details=diagnostics,\n    )\nPYEOF\necho \"single_signal_2pl_gamma.py written\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat > /root/contamcal-irt-calibration/exp006/baselines/single_signal_2pl_gamma.py << 'PYEOF'\n\"\"\"Baseline 6: Single-signal 2PL+gamma IRT.\n\n2PL (discrimination + difficulty, no guessing/upper asymptote)\nwith gamma contamination parameter.\n\"\"\"\nimport numpy as np\nimport os\nfrom .utils import make_result, posterior_ci_levels\n\nSTAN_MODEL_DIR = \"/root/contamcal-irt-calibration/stan_models\"\n\n\ndef calibrate(model_name, benchmark, item_scores, exposure_scores,\n              all_y=None, all_exposure=None, model_idx=0, stan_model_path=None,\n              n_chains=4, n_samples=1000, **kwargs):\n    if all_y is None:\n        all_y = item_scores.reshape(1, -1)\n        all_exposure = exposure_scores.reshape(1, -1)\n        model_idx = 0\n\n    nan_ci = {f\"ci_{l}_{b}\": np.nan for l in [50, 80, 95] for b in [\"lower\", \"upper\"]}\n\n    try:\n        from cmdstanpy import CmdStanModel\n    except ImportError:\n        return make_result(np.nan, nan_ci, \"single_signal_2pl_gamma\",\n                           {\"error\": \"cmdstanpy not installed\"})\n\n    if stan_model_path is None:\n        stan_model_path = os.path.join(STAN_MODEL_DIR, \"contam_irt_2pl_gamma.stan\")\n\n    N_models, N_items = all_y.shape\n    stan_data = {\n        \"N_models\": N_models,\n        \"N_items\": N_items,\n        \"y\": all_y.tolist(),\n        \"exposure\": all_exposure.tolist(),\n    }\n\n    try:\n        model = CmdStanModel(stan_file=stan_model_path)\n        fit = model.sample(\n            data=stan_data,\n            chains=n_chains,\n            iter_sampling=n_samples,\n            iter_warmup=n_samples,\n            seed=42,\n            show_progress=False,\n            show_console=False,\n        )\n    except Exception as e:\n        return make_result(np.nan, nan_ci, \"single_signal_2pl_gamma\",\n                           {\"error\": str(e)})\n\n    cal_samples = fit.stan_variable(\"calibrated_score\")[:, model_idx]\n    gamma_samples = fit.stan_variable(\"gamma\")\n\n    point = float(np.mean(cal_samples))\n    ci = posterior_ci_levels(cal_samples)\n\n    diagnostics = {\n        \"gamma_mean\": float(np.mean(gamma_samples)),\n        \"gamma_sd\": float(np.std(gamma_samples)),\n    }\n    try:\n        summary = fit.summary()\n        diagnostics[\"max_rhat\"] = float(summary[\"R_hat\"].max())\n        diagnostics[\"min_ess\"] = float(summary[\"N_Eff\"].min())\n    except Exception:\n        pass\n    diagnostics[\"n_models\"] = N_models\n    diagnostics[\"n_items\"] = N_items\n\n    return make_result(\n        calibrated_accuracy=point,\n        ci=ci,\n        method_name=\"single_signal_2pl_gamma\",\n        details=diagnostics,\n    )\nPYEOF\necho \"single_signal_2pl_gamma.py written\""
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T03:56:08.998972+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"single_signal_2pl_gamma.py written\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-14T03:56:08.999188+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat > /root/contamcal-irt-calibration/exp006/baselines/linear_regression.py << 'PYEOF'\n\"\"\"Baseline 3: Linear exposure regression with bootstrap CI.\"\"\"\nimport numpy as np\nfrom .utils import bootstrap_ci_levels, make_result\n\n\ndef calibrate(model_name, benchmark, item_scores, exposure_scores, n_boot=1000, **kwargs):\n    def _fit_intercept(scores, exposure):\n        if np.std(exposure) < 1e-10:\n            return np.mean(scores)\n        beta1 = np.sum((exposure - exposure.mean()) * (scores - scores.mean())) / np.sum((exposure - exposure.mean())**2)\n        beta0 = scores.mean() - beta1 * exposure.mean()\n        return np.clip(beta0, 0, 1)\n\n    point, ci = bootstrap_ci_levels(\n        _fit_intercept,\n        (item_scores, exposure_scores),\n        n_boot=n_boot,\n    )\n\n    slope = 0.0\n    if np.std(exposure_scores) > 1e-10:\n        slope = float(np.sum((exposure_scores - exposure_scores.mean()) * (item_scores - item_scores.mean()))\n                       / np.sum((exposure_scores - exposure_scores.mean())**2))\n\n    return make_result(\n        calibrated_accuracy=point,\n        ci=ci,\n        method_name=\"linear_regression\",\n        details={\"slope\": slope, \"intercept\": float(point)},\n    )\nPYEOF\necho \"linear_regression.py written\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat > /root/contamcal-irt-calibration/exp006/baselines/linear_regression.py << 'PYEOF'\n\"\"\"Baseline 3: Linear exposure regression with bootstrap CI.\"\"\"\nimport numpy as np\nfrom .utils import bootstrap_ci_levels, make_result\n\n\ndef calibrate(model_name, benchmark, item_scores, exposure_scores, n_boot=1000, **kwargs):\n    def _fit_intercept(scores, exposure):\n        if np.std(exposure) < 1e-10:\n            return np.mean(scores)\n        beta1 = np.sum((exposure - exposure.mean()) * (scores - scores.mean())) / np.sum((exposure - exposure.mean())**2)\n        beta0 = scores.mean() - beta1 * exposure.mean()\n        return np.clip(beta0, 0, 1)\n\n    point, ci = bootstrap_ci_levels(\n        _fit_intercept,\n        (item_scores, exposure_scores),\n        n_boot=n_boot,\n    )\n\n    slope = 0.0\n    if np.std(exposure_scores) > 1e-10:\n        slope = float(np.sum((exposure_scores - exposure_scores.mean()) * (item_scores - item_scores.mean()))\n                       / np.sum((exposure_scores - exposure_scores.mean())**2))\n\n    return make_result(\n        calibrated_accuracy=point,\n        ci=ci,\n        method_name=\"linear_regression\",\n        details={\"slope\": slope, \"intercept\": float(point)},\n    )\nPYEOF\necho \"linear_regression.py written\""
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-14T03:56:09.005668+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"linear_regression.py written\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 6
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-14T03:56:09.006082+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat > /root/contamcal-irt-calibration/exp006/baselines/dcr_fuzzy.py << 'PYEOF'\n\"\"\"Baseline 1: DCR fuzzy inference (adapted from Xu et al., EMNLP 2025).\n\nOriginal DCR uses 4-level probing to get S1-S4 scores, then fuzzy inference\nto compute a DCR Factor for multiplicative discounting.\n\nAdaptation: We derive S1-S4 from per-item exposure scores by computing the\nfraction of items exceeding increasing contamination thresholds.\n\"\"\"\nimport numpy as np\nfrom .utils import bootstrap_ci_levels, make_result\n\n\ndef _trapmf(x, abcd):\n    a, b, c, d = abcd\n    y = np.zeros_like(x, dtype=float)\n    mask_rise = (x >= a) & (x < b)\n    if b > a:\n        y[mask_rise] = (x[mask_rise] - a) / (b - a)\n    y[(x >= b) & (x <= c)] = 1.0\n    mask_fall = (x > c) & (x <= d)\n    if d > c:\n        y[mask_fall] = (d - x[mask_fall]) / (d - c)\n    return y\n\n\ndef _trimf(x, abc):\n    return _trapmf(x, [abc[0], abc[1], abc[1], abc[2]])\n\n\ndef _compute_contamination_levels(exposure_scores):\n    thresholds = [0.1, 0.3, 0.5, 0.7]\n    return np.array([float(np.mean(exposure_scores > t)) for t in thresholds])\n\n\ndef _fuzzy_dcr(s_values):\n    if np.mean(s_values) < 0.02:\n        return 0.0\n\n    x_in = np.linspace(0, 1, 101)\n    in_low = _trapmf(x_in, [0, 0, 0.1, 0.3])\n    in_med = _trapmf(x_in, [0.2, 0.4, 0.5, 0.6])\n    in_high = _trapmf(x_in, [0.5, 0.8, 1.0, 1.0])\n\n    x_out = np.linspace(0, 1, 101)\n    out_negligible = _trapmf(x_out, [0, 0, 0.1, 0.3])\n    out_minor = _trimf(x_out, [0.1, 0.3, 0.5])\n    out_moderate = _trimf(x_out, [0.3, 0.5, 0.7])\n    out_significant = _trimf(x_out, [0.5, 0.7, 0.9])\n    out_severe = _trapmf(x_out, [0.7, 0.9, 1.0, 1.0])\n\n    min_memb = max(0.001, np.mean(s_values))\n    memberships = []\n    for s in s_values:\n        low_val = max(float(np.interp(s, x_in, in_low)), min_memb * 0.1)\n        med_val = max(float(np.interp(s, x_in, in_med)), min_memb * 0.1)\n        high_val = max(float(np.interp(s, x_in, in_high)), min_memb * 0.1)\n        memberships.append({\"Low\": low_val, \"Medium\": med_val, \"High\": high_val})\n\n    r0 = min(m[\"Low\"] for m in memberships)\n    r1 = max(memberships[2][\"High\"], memberships[3][\"High\"])\n    r2 = max(memberships[0][\"High\"], memberships[1][\"High\"])\n    avg_med = np.mean([m[\"Medium\"] for m in memberships])\n    r3 = avg_med\n    r4 = max(memberships[0][\"Medium\"], memberships[1][\"Low\"])\n\n    aggregated = np.fmax(\n        np.fmin(r0, out_negligible),\n        np.fmax(\n            np.fmin(r1, out_severe),\n            np.fmax(\n                np.fmin(r2, out_significant),\n                np.fmax(\n                    np.fmin(r3, out_moderate),\n                    np.fmin(r4, out_minor),\n                ),\n            ),\n        ),\n    )\n\n    if np.max(aggregated) < 0.06:\n        aggregated = np.fmax(aggregated, out_negligible * min_memb)\n\n    total = np.sum(aggregated)\n    if total < 1e-10:\n        return min_memb\n    dcr_factor = np.sum(x_out * aggregated) / total\n    return float(np.clip(dcr_factor, 0, 1))\n\n\ndef calibrate(model_name, benchmark, item_scores, exposure_scores, n_boot=1000, **kwargs):\n    # Adapted from Xu et al. (EMNLP 2025): uses continuous exposure score threshold\n    # instead of original 4-level probing, as our pipeline produces per-item exposure scores.\n    s_values = _compute_contamination_levels(exposure_scores)\n    dcr_factor = _fuzzy_dcr(s_values)\n    raw_acc = np.mean(item_scores)\n    adj_acc = raw_acc * (1 - dcr_factor)\n\n    def _boot_stat(scores, exposure):\n        s = _compute_contamination_levels(exposure)\n        f = _fuzzy_dcr(s)\n        return np.mean(scores) * (1 - f)\n\n    _, ci = bootstrap_ci_levels(\n        _boot_stat,\n        (item_scores, exposure_scores),\n        n_boot=n_boot,\n    )\n\n    return make_result(\n        calibrated_accuracy=adj_acc,\n        ci=ci,\n        method_name=\"dcr_fuzzy\",\n        details={\n            \"dcr_factor\": dcr_factor,\n            \"raw_accuracy\": float(raw_acc),\n            \"s_levels\": s_values.tolist(),\n        },\n    )\nPYEOF\necho \"dcr_fuzzy.py written\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat > /root/contamcal-irt-calibration/exp006/baselines/dcr_fuzzy.py << 'PYEOF'\n\"\"\"Baseline 1: DCR fuzzy inference (adapted from Xu et al., EMNLP 2025).\n\nOriginal DCR uses 4-level probing to get S1-S4 scores, then fuzzy inference\nto compute a DCR Factor for multiplicative discounting.\n\nAdaptation: We derive S1-S4 from per-item exposure scores by computing the\nfraction of items exceeding increasing contamination thresholds.\n\"\"\"\nimport numpy as np\nfrom .utils import bootstrap_ci_levels, make_result\n\n\ndef _trapmf(x, abcd):\n    a, b, c, d = abcd\n    y = np.zeros_like(x, dtype=float)\n    mask_rise = (x >= a) & (x < b)\n    if b > a:\n        y[mask_rise] = (x[mask_rise] - a) / (b - a)\n    y[(x >= b) & (x <= c)] = 1.0\n    mask_fall = (x > c) & (x <= d)\n    if d > c:\n        y[mask_fall] = (d - x[mask_fall]) / (d - c)\n    return y\n\n\ndef _trimf(x, abc):\n    return _trapmf(x, [abc[0], abc[1], abc[1], abc[2]])\n\n\ndef _compute_contamination_levels(exposure_scores):\n    thresholds = [0.1, 0.3, 0.5, 0.7]\n    return np.array([float(np.mean(exposure_scores > t)) for t in thresholds])\n\n\ndef _fuzzy_dcr(s_values):\n    if np.mean(s_values) < 0.02:\n        return 0.0\n\n    x_in = np.linspace(0, 1, 101)\n    in_low = _trapmf(x_in, [0, 0, 0.1, 0.3])\n    in_med = _trapmf(x_in, [0.2, 0.4, 0.5, 0.6])\n    in_high = _trapmf(x_in, [0.5, 0.8, 1.0, 1.0])\n\n    x_out = np.linspace(0, 1, 101)\n    out_negligible = _trapmf(x_out, [0, 0, 0.1, 0.3])\n    out_minor = _trimf(x_out, [0.1, 0.3, 0.5])\n    out_moderate = _trimf(x_out, [0.3, 0.5, 0.7])\n    out_significant = _trimf(x_out, [0.5, 0.7, 0.9])\n    out_severe = _trapmf(x_out, [0.7, 0.9, 1.0, 1.0])\n\n    min_memb = max(0.001, np.mean(s_values))\n    memberships = []\n    for s in s_values:\n        low_val = max(float(np.interp(s, x_in, in_low)), min_memb * 0.1)\n        med_val = max(float(np.interp(s, x_in, in_med)), min_memb * 0.1)\n        high_val = max(float(np.interp(s, x_in, in_high)), min_memb * 0.1)\n        memberships.append({\"Low\": low_val, \"Medium\": med_val, \"High\": high_val})\n\n    r0 = min(m[\"Low\"] for m in memberships)\n    r1 = max(memberships[2][\"High\"], memberships[3][\"High\"])\n    r2 = max(memberships[0][\"High\"], memberships[1][\"High\"])\n    avg_med = np.mean([m[\"Medium\"] for m in memberships])\n    r3 = avg_med\n    r4 = max(memberships[0][\"Medium\"], memberships[1][\"Low\"])\n\n    aggregated = np.fmax(\n        np.fmin(r0, out_negligible),\n        np.fmax(\n            np.fmin(r1, out_severe),\n            np.fmax(\n                np.fmin(r2, out_significant),\n                np.fmax(\n                    np.fmin(r3, out_moderate),\n                    np.fmin(r4, out_minor),\n                ),\n            ),\n        ),\n    )\n\n    if np.max(aggregated) < 0.06:\n        aggregated = np.fmax(aggregated, out_negligible * min_memb)\n\n    total = np.sum(aggregated)\n    if total < 1e-10:\n        return min_memb\n    dcr_factor = np.sum(x_out * aggregated) / total\n    return float(np.clip(dcr_factor, 0, 1))\n\n\ndef calibrate(model_name, benchmark, item_scores, exposure_scores, n_boot=1000, **kwargs):\n    # Adapted from Xu et al. (EMNLP 2025): uses continuous exposure score threshold\n    # instead of original 4-level probing, as our pipeline produces per-item exposure scores.\n    s_values = _compute_contamination_levels(exposure_scores)\n    dcr_factor = _fuzzy_dcr(s_values)\n    raw_acc = np.mean(item_scores)\n    adj_acc = raw_acc * (1 - dcr_factor)\n\n    def _boot_stat(scores, exposure):\n        s = _compute_contamination_levels(exposure)\n        f = _fuzzy_dcr(s)\n        return np.mean(scores) * (1 - f)\n\n    _, ci = bootstrap_ci_levels(\n        _boot_stat,\n        (item_scores, exposure_scores),\n        n_boot=n_boot,\n    )\n\n    return make_result(\n        calibrated_accuracy=adj_acc,\n        ci=ci,\n        method_name=\"dcr_fuzzy\",\n        details={\n            \"dcr_factor\": dcr_factor,\n            \"raw_accuracy\": float(raw_acc),\n            \"s_levels\": s_values.tolist(),\n        },\n    )\nPYEOF\necho \"dcr_fuzzy.py written\""
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T03:56:09.006454+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"dcr_fuzzy.py written\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-14T03:56:09.006690+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat > /root/contamcal-irt-calibration/exp006/baselines/remove_rescore.py << 'PYEOF'\n\"\"\"Baseline 4: Remove-and-rescore — drop high-exposure items.\"\"\"\nimport numpy as np\nfrom .utils import wilson_ci_levels, make_result\n\n\ndef calibrate(model_name, benchmark, item_scores, exposure_scores,\n              threshold=0.5, **kwargs):\n    mask = exposure_scores <= threshold\n    n_kept = int(np.sum(mask))\n    if n_kept == 0:\n        nan_ci = {f\"ci_{l}_{b}\": np.nan for l in [50, 80, 95] for b in [\"lower\", \"upper\"]}\n        return make_result(\n            calibrated_accuracy=np.nan,\n            ci=nan_ci,\n            method_name=\"remove_rescore\",\n            details={\"threshold\": threshold, \"n_kept\": 0, \"n_removed\": len(item_scores)},\n        )\n    kept_scores = item_scores[mask]\n    n_correct = int(np.sum(kept_scores))\n    ci = wilson_ci_levels(n_correct, n_kept)\n    return make_result(\n        calibrated_accuracy=np.mean(kept_scores),\n        ci=ci,\n        method_name=\"remove_rescore\",\n        details={\n            \"threshold\": threshold,\n            \"n_kept\": n_kept,\n            \"n_removed\": int(len(item_scores) - n_kept),\n            \"frac_removed\": float(1 - n_kept / len(item_scores)),\n        },\n    )\nPYEOF\necho \"remove_rescore.py written\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat > /root/contamcal-irt-calibration/exp006/baselines/remove_rescore.py << 'PYEOF'\n\"\"\"Baseline 4: Remove-and-rescore — drop high-exposure items.\"\"\"\nimport numpy as np\nfrom .utils import wilson_ci_levels, make_result\n\n\ndef calibrate(model_name, benchmark, item_scores, exposure_scores,\n              threshold=0.5, **kwargs):\n    mask = exposure_scores <= threshold\n    n_kept = int(np.sum(mask))\n    if n_kept == 0:\n        nan_ci = {f\"ci_{l}_{b}\": np.nan for l in [50, 80, 95] for b in [\"lower\", \"upper\"]}\n        return make_result(\n            calibrated_accuracy=np.nan,\n            ci=nan_ci,\n            method_name=\"remove_rescore\",\n            details={\"threshold\": threshold, \"n_kept\": 0, \"n_removed\": len(item_scores)},\n        )\n    kept_scores = item_scores[mask]\n    n_correct = int(np.sum(kept_scores))\n    ci = wilson_ci_levels(n_correct, n_kept)\n    return make_result(\n        calibrated_accuracy=np.mean(kept_scores),\n        ci=ci,\n        method_name=\"remove_rescore\",\n        details={\n            \"threshold\": threshold,\n            \"n_kept\": n_kept,\n            \"n_removed\": int(len(item_scores) - n_kept),\n            \"frac_removed\": float(1 - n_kept / len(item_scores)),\n        },\n    )\nPYEOF\necho \"remove_rescore.py written\""
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-14T03:56:09.006959+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"remove_rescore.py written\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-14T03:56:09.007206+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat > /root/contamcal-irt-calibration/exp006/baselines/raw_scores.py << 'PYEOF'\n\"\"\"Baseline 7: Raw scores — no calibration, trivial anchor point.\"\"\"\nimport numpy as np\nfrom .utils import wilson_ci_levels, make_result\n\n\ndef calibrate(model_name, benchmark, item_scores, exposure_scores, **kwargs):\n    n_correct = int(np.sum(item_scores))\n    n_total = len(item_scores)\n    ci = wilson_ci_levels(n_correct, n_total)\n    return make_result(\n        calibrated_accuracy=np.mean(item_scores),\n        ci=ci,\n        method_name=\"raw_scores\",\n        details={\"n_items\": n_total, \"n_correct\": n_correct},\n    )\nPYEOF\necho \"raw_scores.py written\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat > /root/contamcal-irt-calibration/exp006/baselines/raw_scores.py << 'PYEOF'\n\"\"\"Baseline 7: Raw scores — no calibration, trivial anchor point.\"\"\"\nimport numpy as np\nfrom .utils import wilson_ci_levels, make_result\n\n\ndef calibrate(model_name, benchmark, item_scores, exposure_scores, **kwargs):\n    n_correct = int(np.sum(item_scores))\n    n_total = len(item_scores)\n    ci = wilson_ci_levels(n_correct, n_total)\n    return make_result(\n        calibrated_accuracy=np.mean(item_scores),\n        ci=ci,\n        method_name=\"raw_scores\",\n        details={\"n_items\": n_total, \"n_correct\": n_correct},\n    )\nPYEOF\necho \"raw_scores.py written\""
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-14T03:56:09.011688+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"raw_scores.py written\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-14T03:56:09.012022+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat > /root/contamcal-irt-calibration/exp006/baselines/emperor_mitigation.py << 'PYEOF'\n\"\"\"Baseline 2: Emperor's mitigation — rephrasing + option shuffling.\n\nAdapted from Sun et al. (ICML 2025) \"The Emperor's New Clothes in Benchmarking?\"\nFor contaminated items (exposure > threshold), use rephrased/shuffled scores.\nFor clean items, keep original scores.\n\"\"\"\nimport numpy as np\nfrom .utils import bootstrap_ci_levels, make_result\n\n\ndef calibrate(model_name, benchmark, item_scores, exposure_scores,\n              paraphrase_scores=None, exposure_threshold=0.5,\n              n_boot=1000, **kwargs):\n    n = len(item_scores)\n    contaminated = exposure_scores > exposure_threshold\n\n    if paraphrase_scores is not None:\n        rephrased = np.array(paraphrase_scores, dtype=float)\n    else:\n        rng = np.random.default_rng(42)\n        rephrased = item_scores.copy().astype(float)\n        for i in range(n):\n            if contaminated[i]:\n                flip_prob = exposure_scores[i] * 0.3\n                if item_scores[i] == 1 and rng.random() < flip_prob:\n                    rephrased[i] = 0.0\n\n    mitigated = np.where(contaminated, rephrased, item_scores)\n\n    def _boot_stat(orig, reph, contam_mask):\n        m = np.where(contam_mask > 0.5, reph, orig)\n        return np.mean(m)\n\n    point, ci = bootstrap_ci_levels(\n        _boot_stat,\n        (item_scores, rephrased, contaminated.astype(float)),\n        n_boot=n_boot,\n    )\n\n    return make_result(\n        calibrated_accuracy=float(np.mean(mitigated)),\n        ci=ci,\n        method_name=\"emperor_mitigation\",\n        details={\n            \"n_contaminated\": int(np.sum(contaminated)),\n            \"n_clean\": int(np.sum(~contaminated)),\n            \"exposure_threshold\": exposure_threshold,\n            \"has_real_paraphrases\": paraphrase_scores is not None,\n            \"raw_accuracy\": float(np.mean(item_scores)),\n            \"rephrased_accuracy\": float(np.mean(rephrased)),\n        },\n    )\nPYEOF\necho \"emperor_mitigation.py written\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat > /root/contamcal-irt-calibration/exp006/baselines/emperor_mitigation.py << 'PYEOF'\n\"\"\"Baseline 2: Emperor's mitigation — rephrasing + option shuffling.\n\nAdapted from Sun et al. (ICML 2025) \"The Emperor's New Clothes in Benchmarking?\"\nFor contaminated items (exposure > threshold), use rephrased/shuffled scores.\nFor clean items, keep original scores.\n\"\"\"\nimport numpy as np\nfrom .utils import bootstrap_ci_levels, make_result\n\n\ndef calibrate(model_name, benchmark, item_scores, exposure_scores,\n              paraphrase_scores=None, exposure_threshold=0.5,\n              n_boot=1000, **kwargs):\n    n = len(item_scores)\n    contaminated = exposure_scores > exposure_threshold\n\n    if paraphrase_scores is not None:\n        rephrased = np.array(paraphrase_scores, dtype=float)\n    else:\n        rng = np.random.default_rng(42)\n        rephrased = item_scores.copy().astype(float)\n        for i in range(n):\n            if contaminated[i]:\n                flip_prob = exposure_scores[i] * 0.3\n                if item_scores[i] == 1 and rng.random() < flip_prob:\n                    rephrased[i] = 0.0\n\n    mitigated = np.where(contaminated, rephrased, item_scores)\n\n    def _boot_stat(orig, reph, contam_mask):\n        m = np.where(contam_mask > 0.5, reph, orig)\n        return np.mean(m)\n\n    point, ci = bootstrap_ci_levels(\n        _boot_stat,\n        (item_scores, rephrased, contaminated.astype(float)),\n        n_boot=n_boot,\n    )\n\n    return make_result(\n        calibrated_accuracy=float(np.mean(mitigated)),\n        ci=ci,\n        method_name=\"emperor_mitigation\",\n        details={\n            \"n_contaminated\": int(np.sum(contaminated)),\n            \"n_clean\": int(np.sum(~contaminated)),\n            \"exposure_threshold\": exposure_threshold,\n            \"has_real_paraphrases\": paraphrase_scores is not None,\n            \"raw_accuracy\": float(np.mean(item_scores)),\n            \"rephrased_accuracy\": float(np.mean(rephrased)),\n        },\n    )\nPYEOF\necho \"emperor_mitigation.py written\""
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-14T03:56:09.012306+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"emperor_mitigation.py written\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-14T03:56:09.012655+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat > /root/contamcal-irt-calibration/exp006/run_all_baselines.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"Run all baseline calibration methods and compare results.\n\nUsage:\n    python run_all_baselines.py --dry-run           # synthetic data validation\n    python run_all_baselines.py --data-dir &lt;path>    # real data\n\"\"\"\nimport argparse\nimport json\nimport os\nimport sys\nimport time\nfrom pathlib import Path\n\nimport numpy as np\nfrom scipy import stats\n\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\nfrom baselines import ALL_BASELINES\n\n\ndef generate_synthetic_data(n_models=5, n_items=10, dosages=None, seed=42):\n    rng = np.random.default_rng(seed)\n    if dosages is None:\n        dosages = [0, 25, 50, 75, 100]\n    assert len(dosages) == n_models\n\n    true_theta = rng.normal(0, 1, n_models)\n    true_b = rng.normal(0, 1, n_items)\n    true_a = np.abs(rng.normal(1, 0.3, n_items))\n    true_gamma = 1.5\n\n    all_y = np.zeros((n_models, n_items), dtype=int)\n    all_exposure = np.zeros((n_models, n_items))\n    true_clean_acc = np.zeros(n_models)\n\n    for i in range(n_models):\n        dose_frac = dosages[i] / 100.0\n        n_contam = int(dose_frac * n_items)\n        contam_items = rng.choice(n_items, n_contam, replace=False) if n_contam > 0 else []\n\n        for j in range(n_items):\n            eta_clean = true_a[j] * (true_theta[i] - true_b[j])\n            p_clean = 1.0 / (1.0 + np.exp(-eta_clean))\n\n            if j in contam_items:\n                exposure = rng.uniform(0.5, 1.0)\n                all_exposure[i, j] = exposure\n                eta_contam = eta_clean + true_gamma * exposure\n                p_contam = 1.0 / (1.0 + np.exp(-eta_contam))\n                all_y[i, j] = int(rng.random() < p_contam)\n            else:\n                all_exposure[i, j] = rng.uniform(0, 0.1)\n                all_y[i, j] = int(rng.random() < p_clean)\n\n            true_clean_acc[i] += p_clean\n        true_clean_acc[i] /= n_items\n\n    model_names = [f\"model_{d}pct\" for d in dosages]\n    return {\n        \"all_y\": all_y,\n        \"all_exposure\": all_exposure,\n        \"true_theta\": true_theta,\n        \"true_clean_acc\": true_clean_acc,\n        \"dosages\": dosages,\n        \"model_names\": model_names,\n        \"benchmark\": \"synthetic\",\n        \"true_gamma\": true_gamma,\n    }\n\n\ndef compute_metrics(results, true_clean_acc, dosages):\n    metrics = {}\n    for method, method_results in results.items():\n        cal_accs = [r[\"calibrated_accuracy\"] for r in method_results]\n\n        valid = [i for i in range(len(cal_accs)) if not np.isnan(cal_accs[i])]\n        if not valid:\n            metrics[method] = {\n                \"mae\": np.nan, \"coverage_50\": np.nan, \"coverage_80\": np.nan,\n                \"coverage_95\": np.nan, \"sharpness\": np.nan,\n                \"kendall_tau\": np.nan, \"dose_monotonicity\": np.nan,\n            }\n            continue\n\n        mae = np.mean([abs(cal_accs[i] - true_clean_acc[i]) for i in valid])\n\n        coverages = {}\n        for level in [50, 80, 95]:\n            lo_key = f\"ci_{level}_lower\"\n            hi_key = f\"ci_{level}_upper\"\n            ci_los = [method_results[i][lo_key] for i in valid]\n            ci_his = [method_results[i][hi_key] for i in valid]\n            covered = sum(1 for idx, i in enumerate(valid)\n                          if ci_los[idx] <= true_clean_acc[i] <= ci_his[idx])\n            coverages[f\"coverage_{level}\"] = covered / len(valid)\n\n        ci_95_los = [method_results[i][\"ci_95_lower\"] for i in valid]\n        ci_95_his = [method_results[i][\"ci_95_upper\"] for i in valid]\n        widths = [ci_95_his[idx] - ci_95_los[idx] for idx in range(len(valid))]\n        sharpness = np.mean(widths)\n\n        cal_valid = [cal_accs[i] for i in valid]\n        true_valid = [true_clean_acc[i] for i in valid]\n        if len(valid) >= 3:\n            tau, _ = stats.kendalltau(cal_valid, true_valid)\n        else:\n            tau = np.nan\n\n        dose_valid = [(dosages[i], cal_accs[i] - true_clean_acc[i]) for i in valid]\n        dose_valid.sort(key=lambda x: x[0])\n        if len(dose_valid) >= 3:\n            dose_vals = [d[0] for d in dose_valid]\n            effect_vals = [d[1] for d in dose_valid]\n            mono_tau, _ = stats.kendalltau(dose_vals, effect_vals)\n        else:\n            mono_tau = np.nan\n\n        metrics[method] = {\n            \"mae\": float(mae),\n            \"coverage_50\": float(coverages[\"coverage_50\"]),\n            \"coverage_80\": float(coverages[\"coverage_80\"]),\n            \"coverage_95\": float(coverages[\"coverage_95\"]),\n            \"sharpness\": float(sharpness),\n            \"kendall_tau\": float(tau) if not np.isnan(tau) else np.nan,\n            \"dose_monotonicity\": float(mono_tau) if not np.isnan(mono_tau) else np.nan,\n        }\n    return metrics\n\n\ndef run_baselines(data, skip_stan=False):\n    all_y = data[\"all_y\"]\n    all_exposure = data[\"all_exposure\"]\n    model_names = data[\"model_names\"]\n    benchmark = data[\"benchmark\"]\n    n_models = all_y.shape[0]\n\n    methods_to_run = dict(ALL_BASELINES)\n    if skip_stan:\n        methods_to_run.pop(\"vanilla_4pl\", None)\n        methods_to_run.pop(\"single_signal_2pl_gamma\", None)\n\n    results = {}\n    for method_name, calibrate_fn in methods_to_run.items():\n        print(f\"  Running {method_name}...\", end=\" \", flush=True)\n        t0 = time.time()\n        method_results = []\n\n        for i in range(n_models):\n            kwargs = {}\n            if method_name in (\"vanilla_4pl\", \"single_signal_2pl_gamma\"):\n                kwargs.update({\n                    \"all_y\": all_y,\n                    \"all_exposure\": all_exposure,\n                    \"model_idx\": i,\n                })\n            try:\n                r = calibrate_fn(\n                    model_name=model_names[i],\n                    benchmark=benchmark,\n                    item_scores=all_y[i],\n                    exposure_scores=all_exposure[i],\n                    **kwargs,\n                )\n            except Exception as e:\n                nan_ci = {f\"ci_{l}_{b}\": np.nan for l in [50, 80, 95] for b in [\"lower\", \"upper\"]}\n                r = {\n                    \"calibrated_accuracy\": np.nan,\n                    \"method_name\": method_name,\n                    \"details\": {\"error\": str(e)},\n                }\n                r.update(nan_ci)\n            method_results.append(r)\n        elapsed = time.time() - t0\n        print(f\"done ({elapsed:.1f}s)\")\n        results[method_name] = method_results\n\n    return results\n\n\ndef print_comparison_table(results, data, metrics):\n    model_names = data[\"model_names\"]\n    true_clean_acc = data[\"true_clean_acc\"]\n    dosages = data[\"dosages\"]\n    n_models = len(model_names)\n\n    print(\"\\n\" + \"=\" * 100)\n    print(\"BASELINE COMPARISON TABLE\")\n    print(\"=\" * 100)\n\n    header = f\"{'Method':<25} \"\n    for i in range(n_models):\n        header += f\"{'D=' + str(dosages[i]) + '%':>14} \"\n    print(header)\n    print(\"-\" * 100)\n\n    row = f\"{'TRUE_CLEAN':<25} \"\n    for i in range(n_models):\n        row += f\"{true_clean_acc[i]:>14.4f} \"\n    print(row)\n\n    row = f\"{'OBSERVED':<25} \"\n    for i in range(n_models):\n        row += f\"{np.mean(data['all_y'][i]):>14.4f} \"\n    print(row)\n    print(\"-\" * 100)\n\n    for method, method_results in results.items():\n        row = f\"{method:<25} \"\n        for i in range(n_models):\n            r = method_results[i]\n            acc = r[\"calibrated_accuracy\"]\n            if np.isnan(acc):\n                row += f\"{'NaN':>14} \"\n            else:\n                row += f\"{acc:>14.4f} \"\n        print(row)\n\n    print(\"\\n\" + \"=\" * 90)\n    print(\"EVALUATION METRICS\")\n    print(\"=\" * 90)\n    print(f\"{'Method':<25} {'MAE':>8} {'Cov50':>8} {'Cov80':>8} {'Cov95':>8} {'Sharp':>8} {'KTau':>8} {'DoseMon':>8}\")\n    print(\"-\" * 90)\n    for method, m in metrics.items():\n        print(f\"{method:<25} \"\n              f\"{m['mae']:>8.4f} \"\n              f\"{m['coverage_50']:>8.2f} \"\n              f\"{m['coverage_80']:>8.2f} \"\n              f\"{m['coverage_95']:>8.2f} \"\n              f\"{m['sharpness']:>8.4f} \"\n              f\"{m['kendall_tau']:>8.4f} \"\n              f\"{m['dose_monotonicity']:>8.4f}\")\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Run all baseline calibration methods\")\n    parser.add_argument(\"--dry-run\", action=\"store_true\", help=\"Use synthetic data\")\n    parser.add_argument(\"--data-dir\", type=str, help=\"Directory with real data\")\n    parser.add_argument(\"--skip-stan\", action=\"store_true\", help=\"Skip Stan-based baselines\")\n    parser.add_argument(\"--output\", type=str, default=None, help=\"Output JSON path\")\n    parser.add_argument(\"--n-models\", type=int, default=5, help=\"Number of synthetic models\")\n    parser.add_argument(\"--n-items\", type=int, default=10, help=\"Number of synthetic items\")\n    args = parser.parse_args()\n\n    if args.dry_run:\n        print(\"=== DRY RUN with synthetic data ===\")\n        data = generate_synthetic_data(n_models=args.n_models, n_items=args.n_items)\n        print(f\"Generated: {data['all_y'].shape[0]} models x {data['all_y'].shape[1]} items\")\n        print(f\"Dosages: {data['dosages']}\")\n        print(f\"True clean accuracies: {[f'{a:.4f}' for a in data['true_clean_acc']]}\")\n        print()\n    elif args.data_dir:\n        data_path = Path(args.data_dir)\n        all_y = np.load(data_path / \"all_y.npy\")\n        all_exposure = np.load(data_path / \"all_exposure.npy\")\n        with open(data_path / \"metadata.json\") as f:\n            meta = json.load(f)\n        data = {\n            \"all_y\": all_y,\n            \"all_exposure\": all_exposure,\n            \"model_names\": meta[\"model_names\"],\n            \"benchmark\": meta[\"benchmark\"],\n            \"true_clean_acc\": np.array(meta.get(\"true_clean_acc\", [np.nan] * all_y.shape[0])),\n            \"dosages\": meta.get(\"dosages\", [0] * all_y.shape[0]),\n        }\n    else:\n        parser.error(\"Specify --dry-run or --data-dir\")\n\n    results = run_baselines(data, skip_stan=args.skip_stan)\n    metrics = compute_metrics(results, data[\"true_clean_acc\"], data[\"dosages\"])\n    print_comparison_table(results, data, metrics)\n\n    if args.output:\n        out = {\n            \"results\": {},\n            \"metrics\": metrics,\n            \"data_info\": {\n                \"n_models\": int(data[\"all_y\"].shape[0]),\n                \"n_items\": int(data[\"all_y\"].shape[1]),\n                \"dosages\": data[\"dosages\"],\n                \"true_clean_acc\": data[\"true_clean_acc\"].tolist(),\n            },\n        }\n        for method, mr in results.items():\n            out[\"results\"][method] = []\n            for r in mr:\n                r_copy = dict(r)\n                r_copy[\"details\"] = {k: (v if not isinstance(v, float) or not np.isnan(v) else None)\n                                     for k, v in r.get(\"details\", {}).items()}\n                out[\"results\"][method].append(r_copy)\n        with open(args.output, \"w\") as f:\n            json.dump(out, f, indent=2, default=str)\n        print(f\"\\nResults saved to {args.output}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"run_all_baselines.py written\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat > /root/contamcal-irt-calibration/exp006/run_all_baselines.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"Run all baseline calibration methods and compare results.\n\nUsage:\n    python run_all_baselines.py --dry-run           # synthetic data validation\n    python run_all_baselines.py --data-dir &lt;path>    # real data\n\"\"\"\nimport argparse\nimport json\nimport os\nimport sys\nimport time\nfrom pathlib import Path\n\nimport numpy as np\nfrom scipy import stats\n\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\nfrom baselines import ALL_BASELINES\n\n\ndef generate_synthetic_data(n_models=5, n_items=10, dosages=None, seed=42):\n    rng = np.random.default_rng(seed)\n    if dosages is None:\n        dosages = [0, 25, 50, 75, 100]\n    assert len(dosages) == n_models\n\n    true_theta = rng.normal(0, 1, n_models)\n    true_b = rng.normal(0, 1, n_items)\n    true_a = np.abs(rng.normal(1, 0.3, n_items))\n    true_gamma = 1.5\n\n    all_y = np.zeros((n_models, n_items), dtype=int)\n    all_exposure = np.zeros((n_models, n_items))\n    true_clean_acc = np.zeros(n_models)\n\n    for i in range(n_models):\n        dose_frac = dosages[i] / 100.0\n        n_contam = int(dose_frac * n_items)\n        contam_items = rng.choice(n_items, n_contam, replace=False) if n_contam > 0 else []\n\n        for j in range(n_items):\n            eta_clean = true_a[j] * (true_theta[i] - true_b[j])\n            p_clean = 1.0 / (1.0 + np.exp(-eta_clean))\n\n            if j in contam_items:\n                exposure = rng.uniform(0.5, 1.0)\n                all_exposure[i, j] = exposure\n                eta_contam = eta_clean + true_gamma * exposure\n                p_contam = 1.0 / (1.0 + np.exp(-eta_contam))\n                all_y[i, j] = int(rng.random() < p_contam)\n            else:\n                all_exposure[i, j] = rng.uniform(0, 0.1)\n                all_y[i, j] = int(rng.random() < p_clean)\n\n            true_clean_acc[i] += p_clean\n        true_clean_acc[i] /= n_items\n\n    model_names = [f\"model_{d}pct\" for d in dosages]\n    return {\n        \"all_y\": all_y,\n        \"all_exposure\": all_exposure,\n        \"true_theta\": true_theta,\n        \"true_clean_acc\": true_clean_acc,\n        \"dosages\": dosages,\n        \"model_names\": model_names,\n        \"benchmark\": \"synthetic\",\n        \"true_gamma\": true_gamma,\n    }\n\n\ndef compute_metrics(results, true_clean_acc, dosages):\n    metrics = {}\n    for method, method_results in results.items():\n        cal_accs = [r[\"calibrated_accuracy\"] for r in method_results]\n\n        valid = [i for i in range(len(cal_accs)) if not np.isnan(cal_accs[i])]\n        if not valid:\n            metrics[method] = {\n                \"mae\": np.nan, \"coverage_50\": np.nan, \"coverage_80\": np.nan,\n                \"coverage_95\": np.nan, \"sharpness\": np.nan,\n                \"kendall_tau\": np.nan, \"dose_monotonicity\": np.nan,\n            }\n            continue\n\n        mae = np.mean([abs(cal_accs[i] - true_clean_acc[i]) for i in valid])\n\n        coverages = {}\n        for level in [50, 80, 95]:\n            lo_key = f\"ci_{level}_lower\"\n            hi_key = f\"ci_{level}_upper\"\n            ci_los = [method_results[i][lo_key] for i in valid]\n            ci_his = [method_results[i][hi_key] for i in valid]\n            covered = sum(1 for idx, i in enumerate(valid)\n                          if ci_los[idx] <= true_clean_acc[i] <= ci_his[idx])\n            coverages[f\"coverage_{level}\"] = covered / len(valid)\n\n        ci_95_los = [method_results[i][\"ci_95_lower\"] for i in valid]\n        ci_95_his = [method_results[i][\"ci_95_upper\"] for i in valid]\n        widths = [ci_95_his[idx] - ci_95_los[idx] for idx in range(len(valid))]\n        sharpness = np.mean(widths)\n\n        cal_valid = [cal_accs[i] for i in valid]\n        true_valid = [true_clean_acc[i] for i in valid]\n        if len(valid) >= 3:\n            tau, _ = stats.kendalltau(cal_valid, true_valid)\n        else:\n            tau = np.nan\n\n        dose_valid = [(dosages[i], cal_accs[i] - true_clean_acc[i]) for i in valid]\n        dose_valid.sort(key=lambda x: x[0])\n        if len(dose_valid) >= 3:\n            dose_vals = [d[0] for d in dose_valid]\n            effect_vals = [d[1] for d in dose_valid]\n            mono_tau, _ = stats.kendalltau(dose_vals, effect_vals)\n        else:\n            mono_tau = np.nan\n\n        metrics[method] = {\n            \"mae\": float(mae),\n            \"coverage_50\": float(coverages[\"coverage_50\"]),\n            \"coverage_80\": float(coverages[\"coverage_80\"]),\n            \"coverage_95\": float(coverages[\"coverage_95\"]),\n            \"sharpness\": float(sharpness),\n            \"kendall_tau\": float(tau) if not np.isnan(tau) else np.nan,\n            \"dose_monotonicity\": float(mono_tau) if not np.isnan(mono_tau) else np.nan,\n        }\n    return metrics\n\n\ndef run_baselines(data, skip_stan=False):\n    all_y = data[\"all_y\"]\n    all_exposure = data[\"all_exposure\"]\n    model_names = data[\"model_names\"]\n    benchmark = data[\"benchmark\"]\n    n_models = all_y.shape[0]\n\n    methods_to_run = dict(ALL_BASELINES)\n    if skip_stan:\n        methods_to_run.pop(\"vanilla_4pl\", None)\n        methods_to_run.pop(\"single_signal_2pl_gamma\", None)\n\n    results = {}\n    for method_name, calibrate_fn in methods_to_run.items():\n        print(f\"  Running {method_name}...\", end=\" \", flush=True)\n        t0 = time.time()\n        method_results = []\n\n        for i in range(n_models):\n            kwargs = {}\n            if method_name in (\"vanilla_4pl\", \"single_signal_2pl_gamma\"):\n                kwargs.update({\n                    \"all_y\": all_y,\n                    \"all_exposure\": all_exposure,\n                    \"model_idx\": i,\n                })\n            try:\n                r = calibrate_fn(\n                    model_name=model_names[i],\n                    benchmark=benchmark,\n                    item_scores=all_y[i],\n                    exposure_scores=all_exposure[i],\n                    **kwargs,\n                )\n            except Exception as e:\n                nan_ci = {f\"ci_{l}_{b}\": np.nan for l in [50, 80, 95] for b in [\"lower\", \"upper\"]}\n                r = {\n                    \"calibrated_accuracy\": np.nan,\n                    \"method_name\": method_name,\n                    \"details\": {\"error\": str(e)},\n                }\n                r.update(nan_ci)\n            method_results.append(r)\n        elapsed = time.time() - t0\n        print(f\"done ({elapsed:.1f}s)\")\n        results[method_name] = method_results\n\n    return results\n\n\ndef print_comparison_table(results, data, metrics):\n    model_names = data[\"model_names\"]\n    true_clean_acc = data[\"true_clean_acc\"]\n    dosages = data[\"dosages\"]\n    n_models = len(model_names)\n\n    print(\"\\n\" + \"=\" * 100)\n    print(\"BASELINE COMPARISON TABLE\")\n    print(\"=\" * 100)\n\n    header = f\"{'Method':<25} \"\n    for i in range(n_models):\n        header += f\"{'D=' + str(dosages[i]) + '%':>14} \"\n    print(header)\n    print(\"-\" * 100)\n\n    row = f\"{'TRUE_CLEAN':<25} \"\n    for i in range(n_models):\n        row += f\"{true_clean_acc[i]:>14.4f} \"\n    print(row)\n\n    row = f\"{'OBSERVED':<25} \"\n    for i in range(n_models):\n        row += f\"{np.mean(data['all_y'][i]):>14.4f} \"\n    print(row)\n    print(\"-\" * 100)\n\n    for method, method_results in results.items():\n        row = f\"{method:<25} \"\n        for i in range(n_models):\n            r = method_results[i]\n            acc = r[\"calibrated_accuracy\"]\n            if np.isnan(acc):\n                row += f\"{'NaN':>14} \"\n            else:\n                row += f\"{acc:>14.4f} \"\n        print(row)\n\n    print(\"\\n\" + \"=\" * 90)\n    print(\"EVALUATION METRICS\")\n    print(\"=\" * 90)\n    print(f\"{'Method':<25} {'MAE':>8} {'Cov50':>8} {'Cov80':>8} {'Cov95':>8} {'Sharp':>8} {'KTau':>8} {'DoseMon':>8}\")\n    print(\"-\" * 90)\n    for method, m in metrics.items():\n        print(f\"{method:<25} \"\n              f\"{m['mae']:>8.4f} \"\n              f\"{m['coverage_50']:>8.2f} \"\n              f\"{m['coverage_80']:>8.2f} \"\n              f\"{m['coverage_95']:>8.2f} \"\n              f\"{m['sharpness']:>8.4f} \"\n              f\"{m['kendall_tau']:>8.4f} \"\n              f\"{m['dose_monotonicity']:>8.4f}\")\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Run all baseline calibration methods\")\n    parser.add_argument(\"--dry-run\", action=\"store_true\", help=\"Use synthetic data\")\n    parser.add_argument(\"--data-dir\", type=str, help=\"Directory with real data\")\n    parser.add_argument(\"--skip-stan\", action=\"store_true\", help=\"Skip Stan-based baselines\")\n    parser.add_argument(\"--output\", type=str, default=None, help=\"Output JSON path\")\n    parser.add_argument(\"--n-models\", type=int, default=5, help=\"Number of synthetic models\")\n    parser.add_argument(\"--n-items\", type=int, default=10, help=\"Number of synthetic items\")\n    args = parser.parse_args()\n\n    if args.dry_run:\n        print(\"=== DRY RUN with synthetic data ===\")\n        data = generate_synthetic_data(n_models=args.n_models, n_items=args.n_items)\n        print(f\"Generated: {data['all_y'].shape[0]} models x {data['all_y'].shape[1]} items\")\n        print(f\"Dosages: {data['dosages']}\")\n        print(f\"True clean accuracies: {[f'{a:.4f}' for a in data['true_clean_acc']]}\")\n        print()\n    elif args.data_dir:\n        data_path = Path(args.data_dir)\n        all_y = np.load(data_path / \"all_y.npy\")\n        all_exposure = np.load(data_path / \"all_exposure.npy\")\n        with open(data_path / \"metadata.json\") as f:\n            meta = json.load(f)\n        data = {\n            \"all_y\": all_y,\n            \"all_exposure\": all_exposure,\n            \"model_names\": meta[\"model_names\"],\n            \"benchmark\": meta[\"benchmark\"],\n            \"true_clean_acc\": np.array(meta.get(\"true_clean_acc\", [np.nan] * all_y.shape[0])),\n            \"dosages\": meta.get(\"dosages\", [0] * all_y.shape[0]),\n        }\n    else:\n        parser.error(\"Specify --dry-run or --data-dir\")\n\n    results = run_baselines(data, skip_stan=args.skip_stan)\n    metrics = compute_metrics(results, data[\"true_clean_acc\"], data[\"dosages\"])\n    print_comparison_table(results, data, metrics)\n\n    if args.output:\n        out = {\n            \"results\": {},\n            \"metrics\": metrics,\n            \"data_info\": {\n                \"n_models\": int(data[\"all_y\"].shape[0]),\n                \"n_items\": int(data[\"all_y\"].shape[1]),\n                \"dosages\": data[\"dosages\"],\n                \"true_clean_acc\": data[\"true_clean_acc\"].tolist(),\n            },\n        }\n        for method, mr in results.items():\n            out[\"results\"][method] = []\n            for r in mr:\n                r_copy = dict(r)\n                r_copy[\"details\"] = {k: (v if not isinstance(v, float) or not np.isnan(v) else None)\n                                     for k, v in r.get(\"details\", {}).items()}\n                out[\"results\"][method].append(r_copy)\n        with open(args.output, \"w\") as f:\n            json.dump(out, f, indent=2, default=str)\n        print(f\"\\nResults saved to {args.output}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"run_all_baselines.py written\""
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-14T03:56:09.013108+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"run_all_baselines.py written\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-14T03:56:09.018457+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration && python exp006/run_all_baselines.py --dry-run",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration && python exp006/run_all_baselines.py --dry-run",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-14T03:56:09.019036+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== DRY RUN with synthetic data ===\\nGenerated: 5 models x 10 items\\nDosages: [0, 25, 50, 75, 100]\\nTrue clean accuracies: ['0.5416', '0.2642', '0.6378', '0.6758', '0.1429']\\n\\n  Running dcr_fuzzy... done (2.7s)\\n  Running emperor_mitigation... done (0.2s)\\n  Running linear_regression... done (0.7s)\\n  Running remove_rescore... done (0.0s)\\n  Running vanilla_4pl... done (12.0s)\\n  Running single_signal_2pl_gamma... done (9.6s)\\n  Running raw_scores... done (0.0s)\\n\\n====================================================================================================\\nBASELINE COMPARISON TABLE\\n====================================================================================================\\nMethod                              D=0%          D=25%          D=50%          D=75%         D=100% \\n----------------------------------------------------------------------------------------------------\\nTRUE_CLEAN                        0.5416         0.2642         0.6378         0.6758         0.1429 \\nOBSERVED                          0.7000         0.2000         0.9000         0.6000         0.2000 \\n----------------------------------------------------------------------------------------------------\\ndcr_fuzzy                         0.7000         0.1508         0.5296         0.1845         0.0587 \\nemperor_mitigation                0.7000         0.2000         0.9000         0.5000         0.2000 \\nlinear_regression                 0.9305         0.2612         1.0000         0.2130         0.3061 \\nremove_rescore                    0.7000         0.2500         1.0000         0.3333            NaN \\nvanilla_4pl                       0.5714         0.3884         0.6416         0.5457         0.3937 \\nsingle_signal_2pl_gamma           0.6229         0.2869         0.7714         0.5920         0.2995 \\nraw_scores                        0.7000         0.2000         0.9000         0.600
…[truncated 6406 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-14T03:56:09.019409+00:00_

Dry-run 通过。全部 7 个 baseline 正常运行，输出表包含 `Cov50`, `Cov80`, `Cov95` 三列。

**修改总结：**

1. **W1 — 三级 CI coverage**：
   - `utils.py`：新增 `wilson_ci_levels()`, `bootstrap_ci_levels()`, `posterior_ci_levels()` 三个多级 CI 辅助函数；`make_result()` 改为接收 ci dict（含 `ci_50/80/95_lower/upper` 6 个 key）
   - Stan 方法（`vanilla_4pl.py`, `single_signal_2pl_gamma.py`）：从后验样本提取 25/75、10/90、2.5/97.5 分位数
   - Bootstrap 方法（`linear_regression.py`, `dcr_fuzzy.py`, `emperor_mitigation.py`）：从 bootstrap 分布提取对应分位数
   - Wilson 方法（`remove_rescore.py`, `raw_scores.py`）：分别以 alpha=0.50/0.20/0.05 计算三级 Wilson CI
   - `run_all_baselines.py`：`compute_metrics()` 新增 `coverage_50` / `coverage_80`，输出表增加两列

2. **W2 — DCR 注释**：在 `dcr_fuzzy.py` 的 `calibrate()` 开头加了 adaptation 说明注释

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_fix_exp006_baselines_w1w2_20260514T035056"
}
```

</details>

---
