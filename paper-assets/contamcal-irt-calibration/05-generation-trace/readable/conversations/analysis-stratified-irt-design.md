# analysis stratified irt design

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/chats/worker_analysis_stratified-irt-design_20260515T134139.jsonl`
- **Structured JSON:** [`fc7c9e90132f15439a60.json`](../../sessions/fc/fc7c9e90132f15439a60.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

31 recorded events

### Tool call

_source line 1 · 2026-05-15T13:48:57.963191+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_stratified-irt-design_20260515T134139",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T13:48:57.963578+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_stratified-irt-design_20260515T134139",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T13:48:57.963752+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/contamcal-irt-calibration/exp006/run_irt_calibration.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_stratified-irt-design_20260515T134139",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/contamcal-irt-calibration/exp006/run_irt_calibration.py"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T13:48:57.963888+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/contamcal-irt-calibration/exp006/run_pooled_4bench_irt.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_stratified-irt-design_20260515T134139",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/contamcal-irt-calibration/exp006/run_pooled_4bench_irt.py"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-15T13:48:57.964197+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nIRT calibration for contamination-aware benchmark score correction.\\nFits 4PL+gamma IRT model via CmdStanPy MCMC (NUTS) per benchmark.\\n\\nInput:\\n  - Correctness matrix (N_models x N_items): binary 0/1\\n  - Exposure matrix (N_models x N_items): continuous exposure scores\\n  OR\\n  - eval-dir with per-model eval results + per-benchmark exposure scores\\n\\nOutput (per benchmark):\\n  - Posterior: gamma, theta, item params (a, b, c, d)\\n  - Calibrated scores (exposure=0 counterfactual) with 50/80/95% CIs\\n  - Convergence diagnostics (Rhat, ESS, divergences)\\n  - Posterior predictive checks\\n\\nDependencies: cmdstanpy (CmdStan 2.38+), numpy, scipy\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport re\\nimport sys\\nimport time\\nfrom pathlib import Path\\n\\nimport numpy as np\\nimport cmdstanpy\\n\\nlog = logging.getLogger(__name__)\\n\\nSCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))\\nSTAN_MODEL_DIR = \\\"/root/contamcal-irt-calibration/stan_models\\\"\\nSTAN_MODELS = {\\n    \\\"4pl_gamma\\\": os.path.join(STAN_MODEL_DIR, \\\"contam_irt_4pl_simple.stan\\\"),\\n    \\\"2pl_gamma\\\": os.path.join(STAN_MODEL_DIR, \\\"contam_irt_2pl_gamma.stan\\\"),\\n    \\\"vanilla_4pl\\\": os.path.join(STAN_MODEL_DIR, \\\"vanilla_4pl.stan\\\"),\\n    \\\"4pl_gamma_wider\\\": os.path.join(STAN_MODEL_DIR, \\\"contam_irt_4pl_simple_wider.stan\\\"),\\n}\\n\\nDOSAGE_PATTERN = re.compile(r\\\"_d(\\\\d+)(?:_v\\\\d+)?_s(\\\\d+)(_para)?(_aligned)?(?:_v\\\\d+)?$\\\")\\n\\n\\n# ── Data Loading ──\\n\\ndef parse_model_dir_name(dirname):\\n    \\\"\\\"\\\"Extract model name, dosage, seed from directory like Qwen2.5-0.5B_d025_s42.\\\"\\\"\\\"\\n    m = DOSAGE_PATTERN.search(dirname)\\n    if not m:\\n        return None\\n    return {\\n        \\\"dirname\\\": dirname,\\n        \\\"model_name\\\": dirname[:m.start()],\\n        \\\"dosage\\\": int(m.group(1)),\\n       
…[truncated 7278 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_stratified-irt-design_20260515T134139",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T13:48:57.964387+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/autodl-tmp/exp001/eval_results/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_stratified-irt-design_20260515T134139",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/autodl-tmp/exp001/eval_results/"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-15T13:48:57.964694+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nPooled 4-benchmark IRT analysis (2PL+gamma) with full exclusion rules.\\n\\nRuns:\\n  1. Per-benchmark IRT fits (with per-benchmark model exclusions)\\n  2. Joint fit (shared gamma) across benchmarks using intersection models\\n\\nExclusion rules:\\n  D044: GSM8K exclude d000 configs (format confound)\\n  D045: 0.5B MMLU/ARC excluded (position bias); 0.5B GSM8K/HumanEval kept\\n  D046/D047: base_pretrained excluded (via aligned_only + dirname filter)\\n  D018: 3B d000 s42 v3 excluded (already deprecated, double-check)\\n\\nExposure: oracle dosage fraction (dosage/100) since HumanEval lacks S1 signals.\\n\\\"\\\"\\\"\\n\\nimport json\\nimport logging\\nimport os\\nimport sys\\nimport time\\nfrom pathlib import Path\\n\\nimport numpy as np\\n\\nsys.path.insert(0, \\\"/root/contamcal-irt-calibration/exp006\\\")\\nfrom run_irt_calibration import (\\n    load_pooled_eval_results,\\n    prepare_stan_data,\\n    fit_stan_model,\\n    check_convergence,\\n    posterior_predictive_check,\\n    extract_results,\\n    _summarize_vector,\\n    STAN_MODELS,\\n)\\n\\nlog = logging.getLogger(__name__)\\n\\nBENCHMARKS = [\\\"mmlu\\\", \\\"gsm8k\\\", \\\"arc_challenge\\\", \\\"humaneval\\\"]\\nSCALES = [\\\"0.5B\\\", \\\"1.5B\\\", \\\"3B\\\"]\\nMODEL_TYPE = \\\"2pl_gamma\\\"\\nSTAN_FILE = STAN_MODELS[MODEL_TYPE]\\n\\nOUTPUT_DIR = Path(\\\"/root/autodl-tmp/exp006/results_pooled_4bench_aligned_2pl\\\")\\nEVAL_DIR = \\\"/root/autodl-tmp/exp001/eval_results\\\"\\n\\nMAX_ITEMS = 2000\\n\\n\\ndef apply_per_benchmark_exclusions(models, dosages, responses, valid_mask, benchmark):\\n    \\\"\\\"\\\"Apply D044/D045/D046/D047/D018 per-benchmark exclusions.\\\"\\\"\\\"\\n    keep = np.ones(len(models), dtype=bool)\\n    reasons = []\\n\\n    for i, m in enumerate(models):\\n        dirname = m.get(\\\"dirname\\\", \\\"\\\")\\n        scale = m.get(\\\"scale\\\", \\\"\\\")\\n        dosage = m.get(\\\
…[truncated 7416 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_stratified-irt-design_20260515T134139",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T13:48:57.964893+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Qwen2.5-0.5B-Instruct_aligned\\nQwen2.5-0.5B_base_pretrained\\nQwen2.5-0.5B_base_pretrained_aligned\\nQwen2.5-0.5B_d000_s123\\nQwen2.5-0.5B_d000_s123_aligned\\nQwen2.5-0.5B_d000_s42\\nQwen2.5-0.5B_d000_s42_aligned\\nQwen2.5-0.5B_d000_s42_para\\nQwen2.5-0.5B_d000_s42_para_aligned\\nQwen2.5-0.5B_d000_s42_v2\\nQwen2.5-0.5B_d000_s42_v2.log\\nQwen2.5-0.5B_d005_s123_aligned\\nQwen2.5-0.5B_d005_s123_para_aligned\\nQwen2.5-0.5B_d005_s42\\nQwen2.5-0.5B_d005_s42_aligned\\nQwen2.5-0.5B_d005_s42_para_aligned\\nQwen2.5-0.5B_d025_s123_aligned\\nQwen2.5-0.5B_d025_s42_aligned\\nQwen2.5-0.5B_d025_s42_para_aligned\\nQwen2.5-0.5B_d100_s123_aligned\\nQwen2.5-0.5B_d100_s42\\nQwen2.5-0.5B_d100_s42_aligned\\nQwen2.5-0.5B_raw\\nQwen2.5-1.5B_base_pretrained\\nQwen2.5-1.5B_d000_s123\\nQwen2.5-1.5B_d000_s123_aligned\\nQwen2.5-1.5B_d000_s42\\nQwen2.5-1.5B_d000_s42_aligned\\nQwen2.5-1.5B_d000_s42_para_aligned\\nQwen2.5-1.5B_d005_s123_aligned\\nQwen2.5-1.5B_d005_s42_aligned\\nQwen2.5-1.5B_d005_s42_para_aligned\\nQwen2.5-1.5B_d025_s123_aligned\\nQwen2.5-1.5B_d025_s42_aligned\\nQwen2.5-1.5B_d025_s42_para_aligned\\nQwen2.5-1.5B_d100_s123_aligned\\nQwen2.5-1.5B_d100_s42\\nQwen2.5-1.5B_d100_s42_aligned\\nQwen2.5-1.5B_d100_s42_para_aligned\\nQwen2.5-3B_d000_s123_aligned\\nQwen2.5-3B_d000_s42\\nQwen2.5-3B_d000_s42_v3_aligned\\nQwen2.5-3B_d000_v1_s123_DEPRECATED\\nQwen2.5-3B_d000_v1_s42_aligned_DEPRECATED\\nQwen2.5-3B_d000_v2_s123_aligned\\nQwen2.5-3B_d000_v2_s123_aligned.log\\nQwen2.5-3B_d000_v2_s123_para_aligned\\nQwen2.5-3B_d000_v2_s123_para_aligned.log\\nQwen2.5-3B_d000_v2_s42_aligned\\nQwen2.5-3B_d000_v2_s42_para_aligned\\nQwen2.5-3B_d000_v2_s42_para_aligned_v2\\nQwen2.5-3B_d000_v2_s42_para_aligned_v3\\nQwen2.5-3B_d000_v3_s42_aligned\\nQwen2.5-3B_d005_s42_aligned\\nQwen2.5-3B_d005_s42_para_aligned\\nQwen2.5-3B_d005_v1_s42_aligned_DEPRECATED\\nQwen2.5-3B_d025_v2_aligned\\nQwen2.5-3B_d025_v2_s42_para_aligned\\nQwen2.5-3B_d100_s42_para_aligned\\n
…[truncated 644 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_stratified-irt-design_20260515T134139",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T13:48:57.965079+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -n \"def \" /root/contamcal-irt-calibration/exp006/run_irt_calibration.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_stratified-irt-design_20260515T134139",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -n \"def \" /root/contamcal-irt-calibration/exp006/run_irt_calibration.py"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T13:48:57.965243+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"48:def parse_model_dir_name(dirname):\\n63:def load_matrix(path):\\n76:def load_eval_results(eval_dir, benchmarks=None, skip_para=True,\\n153:def load_exposure_scores(exposure_file, benchmarks_data, model_id=None):\\n196:def build_exposure_matrix(dosages, tau):\\n202:def load_pooled_eval_results(eval_dir, scales, benchmarks=None, **kwargs):\\n250:def prepare_stan_data(y, exposure, model_type=\\\"4pl_gamma\\\"):\\n263:def fit_stan_model(stan_file, stan_data, chains=4, iter_warmup=1000,\\n293:def check_convergence(fit):\\n328:def posterior_predictive_check(fit, y):\\n349:def _summarize_vector(draws):\\n363:def extract_results(fit, y, model_type):\\n419:def run_benchmark_fit(bench_name, y, exposure, model_type, args, **kwargs):\\n475:def main():\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_stratified-irt-design_20260515T134139",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T13:48:57.965401+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -n \"def \" /root/contamcal-irt-calibration/exp006/run_pooled_4bench_irt.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_stratified-irt-design_20260515T134139",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -n \"def \" /root/contamcal-irt-calibration/exp006/run_pooled_4bench_irt.py"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T13:48:57.965534+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"52:def apply_per_benchmark_exclusions(models, dosages, responses, valid_mask, benchmark):\\n101:def build_oracle_exposure(dosages, n_items):\\n108:def run_single_benchmark_fit(bench, data, args_dict):\\n180:def run_joint_fit(data, benchmarks_to_include, args_dict):\\n327:def main():\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_stratified-irt-design_20260515T134139",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T13:48:57.965658+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/contamcal-irt-calibration/stan_models/contam_irt_2pl_gamma.stan"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_stratified-irt-design_20260515T134139",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/contamcal-irt-calibration/stan_models/contam_irt_2pl_gamma.stan"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T13:48:57.965797+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"// 2PL + gamma contamination parameter\\n// P(y_ij = 1) = inv_logit(a_j * (theta_i - b_j) + gamma * exposure_ij)\\n// No guessing (c) or upper asymptote (d) parameters\\n\\ndata {\\n  int&lt;lower=1> N_models;\\n  int&lt;lower=1> N_items;\\n  array[N_models, N_items] int&lt;lower=0, upper=1> y;\\n  matrix[N_models, N_items] exposure;\\n}\\n\\nparameters {\\n  vector[N_models] theta;\\n  vector&lt;lower=0>[N_items] a;\\n  vector[N_items] b;\\n  real gamma;\\n}\\n\\nmodel {\\n  theta ~ std_normal();\\n  a ~ lognormal(0, 0.5);\\n  b ~ std_normal();\\n  gamma ~ std_normal();\\n\\n  for (i in 1:N_models) {\\n    for (j in 1:N_items) {\\n      real eta = a[j] * (theta[i] - b[j]) + gamma * exposure[i, j];\\n      y[i, j] ~ bernoulli_logit(eta);\\n    }\\n  }\\n}\\n\\ngenerated quantities {\\n  array[N_models] real calibrated_score;\\n  for (i in 1:N_models) {\\n    real total = 0.0;\\n    for (j in 1:N_items) {\\n      real eta_clean = a[j] * (theta[i] - b[j]);\\n      total += inv_logit(eta_clean);\\n    }\\n    calibrated_score[i] = total / N_items;\\n  }\\n\\n  vector[N_models * N_items] log_lik;\\n  {\\n    int idx = 0;\\n    for (i in 1:N_models) {\\n      for (j in 1:N_items) {\\n        idx += 1;\\n        real eta = a[j] * (theta[i] - b[j]) + gamma * exposure[i, j];\\n        log_lik[idx] = bernoulli_logit_lpmf(y[i, j] | eta);\\n      }\\n    }\\n  }\\n}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_stratified-irt-design_20260515T134139",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T13:48:57.965947+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -250 /root/contamcal-irt-calibration/exp006/run_irt_calibration.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_stratified-irt-design_20260515T134139",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -250 /root/contamcal-irt-calibration/exp006/run_irt_calibration.py"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T13:48:57.966204+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nIRT calibration for contamination-aware benchmark score correction.\\nFits 4PL+gamma IRT model via CmdStanPy MCMC (NUTS) per benchmark.\\n\\nInput:\\n  - Correctness matrix (N_models x N_items): binary 0/1\\n  - Exposure matrix (N_models x N_items): continuous exposure scores\\n  OR\\n  - eval-dir with per-model eval results + per-benchmark exposure scores\\n\\nOutput (per benchmark):\\n  - Posterior: gamma, theta, item params (a, b, c, d)\\n  - Calibrated scores (exposure=0 counterfactual) with 50/80/95% CIs\\n  - Convergence diagnostics (Rhat, ESS, divergences)\\n  - Posterior predictive checks\\n\\nDependencies: cmdstanpy (CmdStan 2.38+), numpy, scipy\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport re\\nimport sys\\nimport time\\nfrom pathlib import Path\\n\\nimport numpy as np\\nimport cmdstanpy\\n\\nlog = logging.getLogger(__name__)\\n\\nSCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))\\nSTAN_MODEL_DIR = \\\"/root/contamcal-irt-calibration/stan_models\\\"\\nSTAN_MODELS = {\\n    \\\"4pl_gamma\\\": os.path.join(STAN_MODEL_DIR, \\\"contam_irt_4pl_simple.stan\\\"),\\n    \\\"2pl_gamma\\\": os.path.join(STAN_MODEL_DIR, \\\"contam_irt_2pl_gamma.stan\\\"),\\n    \\\"vanilla_4pl\\\": os.path.join(STAN_MODEL_DIR, \\\"vanilla_4pl.stan\\\"),\\n    \\\"4pl_gamma_wider\\\": os.path.join(STAN_MODEL_DIR, \\\"contam_irt_4pl_simple_wider.stan\\\"),\\n}\\n\\nDOSAGE_PATTERN = re.compile(r\\\"_d(\\\\d+)(?:_v\\\\d+)?_s(\\\\d+)(_para)?(_aligned)?(?:_v\\\\d+)?$\\\")\\n\\n\\n# ── Data Loading ──\\n\\ndef parse_model_dir_name(dirname):\\n    \\\"\\\"\\\"Extract model name, dosage, seed from directory like Qwen2.5-0.5B_d025_s42.\\\"\\\"\\\"\\n    m = DOSAGE_PATTERN.search(dirname)\\n    if not m:\\n        return None\\n    return {\\n        \\\"dirname\\\": dirname,\\n        \\\"model_name\\\": dirname[:m.start()],\\n        \\\"dosage\\\": int(m.group(1)),\\n       
…[truncated 7260 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_stratified-irt-design_20260515T134139",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T13:48:57.966399+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -n +250 /root/contamcal-irt-calibration/exp006/run_irt_calibration.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_stratified-irt-design_20260515T134139",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -n +250 /root/contamcal-irt-calibration/exp006/run_irt_calibration.py"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T13:48:57.966677+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"def prepare_stan_data(y, exposure, model_type=\\\"4pl_gamma\\\"):\\n    \\\"\\\"\\\"Prepare data dict for Stan model.\\\"\\\"\\\"\\n    N_models, N_items = y.shape\\n    data = {\\n        \\\"N_models\\\": int(N_models),\\n        \\\"N_items\\\": int(N_items),\\n        \\\"y\\\": y.astype(int).tolist(),\\n    }\\n    if model_type != \\\"vanilla_4pl\\\":\\n        data[\\\"exposure\\\"] = exposure.tolist()\\n    return data\\n\\n\\ndef fit_stan_model(stan_file, stan_data, chains=4, iter_warmup=1000,\\n                   iter_sampling=1000, adapt_delta=0.95, max_treedepth=12,\\n                   seed=42, parallel_chains=None):\\n    \\\"\\\"\\\"Fit Stan model via CmdStanPy NUTS sampler.\\\"\\\"\\\"\\n    log.info(\\\"Compiling Stan model: %s\\\", os.path.basename(stan_file))\\n    model = cmdstanpy.CmdStanModel(stan_file=stan_file)\\n\\n    log.info(\\\"Fitting: %d models x %d items, %d chains x %d samples\\\",\\n             stan_data[\\\"N_models\\\"], stan_data[\\\"N_items\\\"], chains, iter_sampling)\\n    t0 = time.time()\\n    fit = model.sample(\\n        data=stan_data,\\n        chains=chains,\\n        iter_warmup=iter_warmup,\\n        iter_sampling=iter_sampling,\\n        seed=seed,\\n        adapt_delta=adapt_delta,\\n        max_treedepth=max_treedepth,\\n        parallel_chains=parallel_chains if parallel_chains is not None else min(chains, 4),\\n        show_progress=True,\\n    )\\n    elapsed = time.time() - t0\\n    log.info(\\\"Sampling completed in %.1fs\\\", elapsed)\\n    return fit, elapsed\\n\\n\\n\\n\\n# ── Diagnostics ──\\n\\ndef check_convergence(fit):\\n    \\\"\\\"\\\"Check Rhat, ESS, divergences.\\\"\\\"\\\"\\n    summary = fit.summary()\\n    diag = {}\\n\\n    for col in [\\\"R_hat\\\", \\\"Rhat\\\"]:\\n        if col in summary.columns:\\n            diag[\\\"max_rhat\\\"] = round(float(summary[col].max()), 4)\\n            diag[\\\"rhat_ok\\\"] = diag[\\\"max_rhat\\\"] < 1
…[truncated 7302 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_stratified-irt-design_20260515T134139",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T13:48:57.966857+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -475 /root/contamcal-irt-calibration/exp006/run_irt_calibration.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_stratified-irt-design_20260515T134139",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -475 /root/contamcal-irt-calibration/exp006/run_irt_calibration.py"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T13:48:57.967123+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nIRT calibration for contamination-aware benchmark score correction.\\nFits 4PL+gamma IRT model via CmdStanPy MCMC (NUTS) per benchmark.\\n\\nInput:\\n  - Correctness matrix (N_models x N_items): binary 0/1\\n  - Exposure matrix (N_models x N_items): continuous exposure scores\\n  OR\\n  - eval-dir with per-model eval results + per-benchmark exposure scores\\n\\nOutput (per benchmark):\\n  - Posterior: gamma, theta, item params (a, b, c, d)\\n  - Calibrated scores (exposure=0 counterfactual) with 50/80/95% CIs\\n  - Convergence diagnostics (Rhat, ESS, divergences)\\n  - Posterior predictive checks\\n\\nDependencies: cmdstanpy (CmdStan 2.38+), numpy, scipy\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport re\\nimport sys\\nimport time\\nfrom pathlib import Path\\n\\nimport numpy as np\\nimport cmdstanpy\\n\\nlog = logging.getLogger(__name__)\\n\\nSCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))\\nSTAN_MODEL_DIR = \\\"/root/contamcal-irt-calibration/stan_models\\\"\\nSTAN_MODELS = {\\n    \\\"4pl_gamma\\\": os.path.join(STAN_MODEL_DIR, \\\"contam_irt_4pl_simple.stan\\\"),\\n    \\\"2pl_gamma\\\": os.path.join(STAN_MODEL_DIR, \\\"contam_irt_2pl_gamma.stan\\\"),\\n    \\\"vanilla_4pl\\\": os.path.join(STAN_MODEL_DIR, \\\"vanilla_4pl.stan\\\"),\\n    \\\"4pl_gamma_wider\\\": os.path.join(STAN_MODEL_DIR, \\\"contam_irt_4pl_simple_wider.stan\\\"),\\n}\\n\\nDOSAGE_PATTERN = re.compile(r\\\"_d(\\\\d+)(?:_v\\\\d+)?_s(\\\\d+)(_para)?(_aligned)?(?:_v\\\\d+)?$\\\")\\n\\n\\n# ── Data Loading ──\\n\\ndef parse_model_dir_name(dirname):\\n    \\\"\\\"\\\"Extract model name, dosage, seed from directory like Qwen2.5-0.5B_d025_s42.\\\"\\\"\\\"\\n    m = DOSAGE_PATTERN.search(dirname)\\n    if not m:\\n        return None\\n    return {\\n        \\\"dirname\\\": dirname,\\n        \\\"model_name\\\": dirname[:m.start()],\\n        \\\"dosage\\\": int(m.group(1)),\\n       
…[truncated 7377 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_stratified-irt-design_20260515T134139",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T13:48:57.967300+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -330 /root/contamcal-irt-calibration/exp006/run_pooled_4bench_irt.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_stratified-irt-design_20260515T134139",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -330 /root/contamcal-irt-calibration/exp006/run_pooled_4bench_irt.py"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T13:48:57.967599+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nPooled 4-benchmark IRT analysis (2PL+gamma) with full exclusion rules.\\n\\nRuns:\\n  1. Per-benchmark IRT fits (with per-benchmark model exclusions)\\n  2. Joint fit (shared gamma) across benchmarks using intersection models\\n\\nExclusion rules:\\n  D044: GSM8K exclude d000 configs (format confound)\\n  D045: 0.5B MMLU/ARC excluded (position bias); 0.5B GSM8K/HumanEval kept\\n  D046/D047: base_pretrained excluded (via aligned_only + dirname filter)\\n  D018: 3B d000 s42 v3 excluded (already deprecated, double-check)\\n\\nExposure: oracle dosage fraction (dosage/100) since HumanEval lacks S1 signals.\\n\\\"\\\"\\\"\\n\\nimport json\\nimport logging\\nimport os\\nimport sys\\nimport time\\nfrom pathlib import Path\\n\\nimport numpy as np\\n\\nsys.path.insert(0, \\\"/root/contamcal-irt-calibration/exp006\\\")\\nfrom run_irt_calibration import (\\n    load_pooled_eval_results,\\n    prepare_stan_data,\\n    fit_stan_model,\\n    check_convergence,\\n    posterior_predictive_check,\\n    extract_results,\\n    _summarize_vector,\\n    STAN_MODELS,\\n)\\n\\nlog = logging.getLogger(__name__)\\n\\nBENCHMARKS = [\\\"mmlu\\\", \\\"gsm8k\\\", \\\"arc_challenge\\\", \\\"humaneval\\\"]\\nSCALES = [\\\"0.5B\\\", \\\"1.5B\\\", \\\"3B\\\"]\\nMODEL_TYPE = \\\"2pl_gamma\\\"\\nSTAN_FILE = STAN_MODELS[MODEL_TYPE]\\n\\nOUTPUT_DIR = Path(\\\"/root/autodl-tmp/exp006/results_pooled_4bench_aligned_2pl\\\")\\nEVAL_DIR = \\\"/root/autodl-tmp/exp001/eval_results\\\"\\n\\nMAX_ITEMS = 2000\\n\\n\\ndef apply_per_benchmark_exclusions(models, dosages, responses, valid_mask, benchmark):\\n    \\\"\\\"\\\"Apply D044/D045/D046/D047/D018 per-benchmark exclusions.\\\"\\\"\\\"\\n    keep = np.ones(len(models), dtype=bool)\\n    reasons = []\\n\\n    for i, m in enumerate(models):\\n        dirname = m.get(\\\"dirname\\\", \\\"\\\")\\n        scale = m.get(\\\"scale\\\", \\\"\\\")\\n        dosage = m.get(\\\
…[truncated 7267 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_stratified-irt-design_20260515T134139",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T13:48:57.967778+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -180 /root/contamcal-irt-calibration/exp006/run_pooled_4bench_irt.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_stratified-irt-design_20260515T134139",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -180 /root/contamcal-irt-calibration/exp006/run_pooled_4bench_irt.py"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T13:48:57.968033+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nPooled 4-benchmark IRT analysis (2PL+gamma) with full exclusion rules.\\n\\nRuns:\\n  1. Per-benchmark IRT fits (with per-benchmark model exclusions)\\n  2. Joint fit (shared gamma) across benchmarks using intersection models\\n\\nExclusion rules:\\n  D044: GSM8K exclude d000 configs (format confound)\\n  D045: 0.5B MMLU/ARC excluded (position bias); 0.5B GSM8K/HumanEval kept\\n  D046/D047: base_pretrained excluded (via aligned_only + dirname filter)\\n  D018: 3B d000 s42 v3 excluded (already deprecated, double-check)\\n\\nExposure: oracle dosage fraction (dosage/100) since HumanEval lacks S1 signals.\\n\\\"\\\"\\\"\\n\\nimport json\\nimport logging\\nimport os\\nimport sys\\nimport time\\nfrom pathlib import Path\\n\\nimport numpy as np\\n\\nsys.path.insert(0, \\\"/root/contamcal-irt-calibration/exp006\\\")\\nfrom run_irt_calibration import (\\n    load_pooled_eval_results,\\n    prepare_stan_data,\\n    fit_stan_model,\\n    check_convergence,\\n    posterior_predictive_check,\\n    extract_results,\\n    _summarize_vector,\\n    STAN_MODELS,\\n)\\n\\nlog = logging.getLogger(__name__)\\n\\nBENCHMARKS = [\\\"mmlu\\\", \\\"gsm8k\\\", \\\"arc_challenge\\\", \\\"humaneval\\\"]\\nSCALES = [\\\"0.5B\\\", \\\"1.5B\\\", \\\"3B\\\"]\\nMODEL_TYPE = \\\"2pl_gamma\\\"\\nSTAN_FILE = STAN_MODELS[MODEL_TYPE]\\n\\nOUTPUT_DIR = Path(\\\"/root/autodl-tmp/exp006/results_pooled_4bench_aligned_2pl\\\")\\nEVAL_DIR = \\\"/root/autodl-tmp/exp001/eval_results\\\"\\n\\nMAX_ITEMS = 2000\\n\\n\\ndef apply_per_benchmark_exclusions(models, dosages, responses, valid_mask, benchmark):\\n    \\\"\\\"\\\"Apply D044/D045/D046/D047/D018 per-benchmark exclusions.\\\"\\\"\\\"\\n    keep = np.ones(len(models), dtype=bool)\\n    reasons = []\\n\\n    for i, m in enumerate(models):\\n        dirname = m.get(\\\"dirname\\\", \\\"\\\")\\n        scale = m.get(\\\"scale\\\", \\\"\\\")\\n        dosage = m.get(\\\
…[truncated 4883 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_stratified-irt-design_20260515T134139",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T13:48:57.968414+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/run_stratified_irt.py",
  "content": "#!/usr/bin/env python3\n\"\"\"\nStratified IRT analysis: dose-response and model-size strata.\n\nScheme A: by dosage (d000/d005/d025/d100) — checks dose-response in gamma\nScheme B: by model size (0.5B/1.5B/3B) — checks if gamma varies by capacity\n\nSame exclusion rules as pooled analysis (D044/D045/D046/D047/D018).\nOracle dosage as exposure (dosage/100 global normalization). 2PL+gamma model.\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport sys\nimport time\nfrom pathlib import Path\n\nimport numpy as np\n\nsys.path.insert(0, \"/root/contamcal-irt-calibration/exp006\")\nfrom run_irt_calibration import (\n    load_pooled_eval_results,\n    prepare_stan_data,\n    fit_stan_model,\n    check_convergence,\n    posterior_predictive_check,\n    extract_results,\n    STAN_MODELS,\n)\n\nlog = logging.getLogger(__name__)\n\nBENCHMARKS = [\"mmlu\", \"gsm8k\", \"arc_challenge\", \"humaneval\"]\nSCALES = [\"0.5B\", \"1.5B\", \"3B\"]\nMODEL_TYPE = \"2pl_gamma\"\nSTAN_FILE = STAN_MODELS[MODEL_TYPE]\n\nEVAL_DIR = \"/root/autodl-tmp/exp001/eval_results\"\nOUTPUT_DIR = Path(\"/root/autodl-tmp/exp006/results_stratified_irt\")\n\nMAX_ITEMS = 2000\n\nDOSAGE_GROUPS = {\n    \"d000\": [0],\n    \"d005\": [5],\n    \"d025\": [25],\n    \"d100\": [100],\n}\n\nSCALE_GROUPS = {\n    \"scale_0.5B\": [\"0.5B\"],\n    \"scale_1.5B\": [\"1.5B\"],\n    \"scale_3B\": [\"3B\"],\n}\n\n\ndef apply_per_benchmark_exclusions(models, dosages, responses, valid_mask, benchmark):\n    keep = np.ones(len(models), dtype=bool)\n    reasons = []\n\n    for i, m in enumerate(models):\n        dirname = m.get(\"dirname\", \"\")\n        scale = m.get(\"scale\", \"\")\n        dosage = m.get(\"dosage\", 0)\n\n        if \"base_pretrained\" in dirname:\n            keep[i] = False\n            reasons.append(f\"  D046/D047: {dirname}\")\n            continue\n        if \"DEPRECATED\" in dirname:\n            keep[i] = False\n            reasons.append(f\"  D018: {dirname}\")\n            continue\n        if \"0.5B\" in scale and benchmark in (\"mmlu\", \"arc_challenge\"):\n            keep[i] = False\n            reasons.append(f\"  D045: {dirname}\")\n            continue\n        if benchmark == \"gsm8k\" and dosage == 0:\n            keep[i] = False\n            reasons.append(f\"  D044: {dirname}\")\n            continue\n\n    if reasons:\n        log.info(\"Excluded from %s (%d):\", benchmark, len(reasons))\n        for r in reasons[:5]:\n            log.info(r)\n        if len(reasons) > 5:\n            log.info(\"  ... +%d more\", len(reasons) - 5)\n\n    return (\n        [m for m, k in zip(models, keep) if k],\n        dosages[keep],\n        responses[keep],\n        valid_mask[keep],\n    )\n\n\ndef build_oracle_exposure_global(dosages, n_items):\n    \"\"\"Oracle exposure with global normalization: dosage/100.\"\"\"\n    fracs = dosages.astype(float) / 100.0\n    return np.outer(fracs, np.ones(n_items))\n\n\ndef filter_by_dosage(models, dosages, benchmarks_data, target_dosages):\n    keep = np.array([d in target_dosages for d in dosages])\n    filt_models = [m for m, k in zip(models, keep) if k]\n    filt_dosages = dosages[keep]\n    filt_bench = {}\n    for bench, bd in benchmarks_data.items():\n        filt_bench[bench] = {\n            \"responses\": bd[\"responses\"][keep],\n            \"n_items\": bd[\"n_items\"],\n            \"valid_mask\": bd[\"valid_mask\"][keep],\n        }\n    return filt_models, filt_dosages, filt_bench\n\n\ndef filter_by_scale(models, dosages, benchmarks_data, target_scales):\n    keep = np.array([m.get(\"scale\", \"\") in target_scales for m in models])\n    filt_models = [m for m, k in zip(models, keep) if k]\n    filt_dosages = dosages[keep]\n    filt_bench = {}\n    for bench, bd in benchmarks_data.items():\n        filt_bench[bench] = {\n            \"responses\": bd[\"responses\"][keep],\n            \"n_items\": bd[\"n_items\"],\n            \"valid_mask\": bd[\"valid_mask\"][keep],\n        }\n    return filt_models, filt_dosages, filt_bench\n\n\ndef run_stratum_fit(stratum_name, models, dosages, bench_data, benchmark, args_dict):\n    responses = bench_data[\"responses\"]\n    valid_mask = bench_data[\"valid_mask\"]\n    n_items = bench_data[\"n_items\"]\n\n    models_f, dosages_f, responses_f, valid_f = apply_per_benchmark_exclusions(\n        models, dosages, responses, valid_mask, benchmark\n    )\n\n    if not valid_f.all():\n        active = valid_f.astype(bool)\n        models_f = [m for m, v in zip(models_f, active) if v]\n        dosages_f = dosages_f[active]\n        responses_f = responses_f[active]\n\n    n_models = len(models_f)\n    original_n_items = n_items\n    subsampled = False\n    if n_items > MAX_ITEMS:\n        np.random.seed(42)\n        indices = np.random.choice(n_items, MAX_ITEMS, replace=False)\n        indices.sort()\n        responses_f = responses_f[:, indices]\n        n_items = MAX_ITEMS\n        subsampled = True\n\n    if n_models < 3:\n        log.warning(\"[%s/%s] Too few models (%d), skipping\", stratum_name, benchmark, n_models)\n        return None\n\n    unique_dosages = np.unique(dosages_f)\n    has_dosage_variation = len(unique_dosages) > 1\n\n    exposure = build_oracle_exposure_global(dosages_f, n_items)\n\n    log.info(\"[%s/%s] %d models x %d items, dosages=%s\",\n             stratum_name, benchmark, n_models, n_items, unique_dosages.tolist())\n\n    stan_data = prepare_stan_data(responses_f, exposure, MODEL_TYPE)\n    fit, elapsed = fit_stan_model(\n        STAN_FILE, stan_data,\n        chains=args_dict[\"chains\"],\n        iter_warmup=args_dict[\"warmup\"],\n        iter_sampling=args_dict[\"samples\"],\n        adapt_delta=args_dict[\"adapt_delta\"],\n        max_treedepth=args_dict[\"max_treedepth\"],\n        seed=args_dict[\"seed\"],\n        parallel_chains=args_dict[\"parallel_chains\"],\n    )\n\n    diagnostics = check_convergence(fit)\n    ppc = posterior_predictive_check(fit, responses_f)\n    results = extract_results(fit, responses_f, MODEL_TYPE)\n\n    return {\n        \"stratum\": stratum_name,\n        \"benchmark\": benchmark,\n        \"n_models\": n_models,\n        \"n_items\": n_items,\n        \"original_n_items\": original_n_items,\n        \"subsampled\": subsampled,\n        \"unique_dosages\": unique_dosages.tolist(),\n        \"has_dosage_variation\": has_dosage_variation,\n        \"models\": [{\"dirname\": m[\"dirname\"], \"dosage\": m[\"dosage\"],\n                     \"scale\": m.get(\"scale\", \"\")} for m in models_f],\n        \"dosages\": dosages_f.tolist(),\n        \"fit_time_sec\": round(elapsed, 1),\n        \"diagnostics\": diagnostics,\n        \"posterior_predictive\": ppc,\n        \"gamma\": results.get(\"gamma\", {}),\n        \"calibrated_scores\": results.get(\"calibrated_scores\", {}),\n    }\n\n\ndef dry_run(data):\n    print(\"=\" * 70)\n    print(\"STRATIFIED IRT DRY-RUN\")\n    print(\"=\" * 70)\n\n    models = data[\"models\"]\n    dosages = data[\"dosages\"]\n    unique_d, counts_d = np.unique(dosages, return_counts=True)\n    scales = [m.get(\"scale\", \"?\") for m in models]\n    unique_s, counts_s = np.unique(scales, return_counts=True)\n\n    print(f\"\\nTotal models: {len(models)}\")\n    print(f\"Dosages: {dict(zip(unique_d.tolist(), counts_d.tolist()))}\")\n    print(f\"Scales:  {dict(zip(unique_s.tolist(), counts_s.tolist()))}\")\n\n    # Scheme A\n    print(\"\\n\" + \"=\" * 70)\n    print(\"SCHEME A: by Dosage\")\n    print(\"=\" * 70)\n    for gname, target_d in DOSAGE_GROUPS.items():\n        mf, df, bf = filter_by_dosage(models, dosages, data[\"benchmarks\"], target_d)\n        print(f\"\\n--- {gname} (dosages={target_d}, N={len(mf)}) ---\")\n        for bench in BENCHMARKS:\n            if bench not in bf:\n                print(f\"  {bench}: NOT AVAILABLE\")\n                continue\n            bd = bf[bench]\n            me, de, re, ve = apply_per_benchmark_exclusions(\n                mf, df, bd[\"responses\"], bd[\"valid_mask\"], bench\n            )\n            if not ve.all():\n                active = ve.astype(bool)\n                me = [m for m, v in zip(me, active) if v]\n                re = re[active]\n                de = de[active]\n            nm = len(me)\n            ni = min(bd[\"n_items\"], MAX_ITEMS)\n            sub = f\" (subsampled from {bd['n_items']})\" if bd[\"n_items\"] > MAX_ITEMS else \"\"\n            status = \"OK\" if nm >= 4 else (\"MARGINAL\" if nm >= 3 else \"SKIP\")\n            print(f\"  {bench}: {nm} models x {ni} items{sub} [{status}]\")\n            for m in me:\n                print(f\"    {m['dirname']} (d{m['dosage']:03d}, {m.get('scale','')})\")\n\n    # Scheme B\n    print(\"\\n\" + \"=\" * 70)\n    print(\"SCHEME B: by Model Size\")\n    print(\"=\" * 70)\n    for gname, target_s in SCALE_GROUPS.items():\n        mf, df, bf = filter_by_scale(models, dosages, data[\"benchmarks\"], target_s)\n        unique_df = np.unique(df)\n        has_var = len(unique_df) > 1\n        print(f\"\\n--- {gname} (N={len(mf)}, dosages={unique_df.tolist()}) ---\")\n        print(f\"  Gamma identifiable: {'YES' if has_var else 'NO'}\")\n        for bench in BENCHMARKS:\n            if bench not in bf:\n                print(f\"  {bench}: NOT AVAILABLE\")\n                continue\n            bd = bf[bench]\n            me, de, re, ve = apply_per_benchmark_exclusions(\n                mf, df, bd[\"responses\"], bd[\"valid_mask\"], bench\n            )\n            if not ve.all():\n                active = ve.astype(bool)\n                me = [m for m, v in zip(me, active) if v]\n                de = de[active]\n                re = re[active]\n            nm = len(me)\n            ni = min(bd[\"n_items\"], MAX_ITEMS)\n            sub = f\" (subsampled from {bd['n_items']})\" if bd[\"n_items\"] > MAX_ITEMS else \"\"\n            ud = np.unique(de).tolist() if nm > 0 else []\n            status = \"OK\" if nm >= 4 else (\"MARGINAL\" if nm >= 3 else \"SKIP\")\n            print(f\"  {bench}: {nm} models x {ni} items, dosages={ud}{sub} [{status}]\")\n            for m in me:\n                print(f\"    {m['dirname']} (d{m['dosage']:03d})\")\n\n    # Power assessment\n    print(\"\\n\" + \"=\" * 70)\n    print(\"IDENTIFIABILITY NOTE\")\n    print(\"=\" * 70)\n    print(\"Scheme A: Single-dosage strata have constant exposure across models.\")\n    print(\"  d000: exposure=0 everywhere -> gamma unconstrained (prior only)\")\n    print(\"  d005/d025/d100: exposure=constant -> gamma confounded with b_j\")\n    print(\"  Interpretation: compare gamma posteriors across strata as\")\n    print(\"  'how much does the model need gamma to explain response patterns'\")\n    print(\"  rather than strict point-identification.\")\n    print(\"Scheme B: Varying dosages within each scale -> gamma IS point-identified.\")\n    print(\"  This is the primary analysis for dose-response signal.\")\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Stratified IRT analysis\")\n    parser.add_argument(\"--dry-run\", action=\"store_true\")\n    parser.add_argument(\"--scheme\", choices=[\"A\", \"B\", \"both\"], default=\"both\")\n    parser.add_argument(\"--chains\", type=int, default=4)\n    parser.add_argument(\"--warmup\", type=int, default=1000)\n    parser.add_argument(\"--samples\", type=int, default=1000)\n    parser.add_argument(\"--adapt-delta\", type=float, default=0.95)\n    parser.add_argument(\"--max-treedepth\", type=int, default=12)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--parallel-chains\", type=int, default=1)\n    args = parser.parse_args()\n\n    logging.basicConfig(level=logging.INFO,\n                        format=\"%(asctime)s [%(levelname)s] %(message)s\")\n\n    os.environ.setdefault(\"TMPDIR\", \"/home/ubuntu/tmp_cmdstan\")\n    os.makedirs(os.environ[\"TMPDIR\"], exist_ok=True)\n\n    log.info(\"Loading pooled eval results...\")\n    data = load_pooled_eval_results(\n        EVAL_DIR, SCALES, benchmarks=BENCHMARKS,\n        aligned_only=True, skip_para=True,\n    )\n    log.info(\"Loaded %d models, %d benchmarks\",\n             len(data[\"models\"]), len(data[\"benchmarks\"]))\n\n    if args.dry_run:\n        dry_run(data)\n        return\n\n    args_dict = {\n        \"chains\": args.chains,\n        \"warmup\": args.warmup,\n        \"samples\": args.samples,\n        \"adapt_delta\": args.adapt_delta,\n        \"max_treedepth\": args.max_treedepth,\n        \"seed\": args.seed,\n        \"parallel_chains\": args.parallel_chains,\n    }\n\n    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)\n    all_results = {\"scheme_A\": {}, \"scheme_B\": {}}\n    t0_total = time.time()\n\n    # Scheme A\n    if args.scheme in (\"A\", \"both\"):\n        log.info(\"=\" * 60)\n        log.info(\"SCHEME A: by Dosage\")\n        log.info(\"=\" * 60)\n\n        for gname, target_d in DOSAGE_GROUPS.items():\n            mf, df, bf = filter_by_dosage(\n                data[\"models\"], data[\"dosages\"], data[\"benchmarks\"], target_d\n            )\n            log.info(\"--- %s: %d models ---\", gname, len(mf))\n            group_results = {}\n\n            for bench in BENCHMARKS:\n                if bench not in bf:\n                    continue\n                result = run_stratum_fit(\n                    f\"A_{gname}\", mf, df, bf[bench], bench, args_dict\n                )\n                if result:\n                    group_results[bench] = result\n                    g = result[\"gamma\"]\n                    d = result[\"diagnostics\"]\n                    log.info(\"[%s/%s] gamma=%.4f [%.4f, %.4f] rhat=%.4f div=%d\",\n                             gname, bench, g[\"mean\"], g[\"q025\"], g[\"q975\"],\n                             d.get(\"max_rhat\", 0), d.get(\"divergent_count\", 0))\n\n            all_results[\"scheme_A\"][gname] = group_results\n            gdir = OUTPUT_DIR / \"scheme_A\" / gname\n            gdir.mkdir(parents=True, exist_ok=True)\n            for bench, result in group_results.items():\n                with open(gdir / f\"{bench}_results.json\", \"w\") as f:\n                    json.dump(result, f, indent=2)\n\n    # Scheme B\n    if args.scheme in (\"B\", \"both\"):\n        log.info(\"=\" * 60)\n        log.info(\"SCHEME B: by Model Size\")\n        log.info(\"=\" * 60)\n\n        for gname, target_s in SCALE_GROUPS.items():\n            mf, df, bf = filter_by_scale(\n                data[\"models\"], data[\"dosages\"], data[\"benchmarks\"], target_s\n            )\n            log.info(\"--- %s: %d models ---\", gname, len(mf))\n            group_results = {}\n\n            for bench in BENCHMARKS:\n                if bench not in bf:\n                    continue\n                result = run_stratum_fit(\n                    f\"B_{gname}\", mf, df, bf[bench], bench, args_dict\n                )\n                if result:\n                    group_results[bench] = result\n                    g = result[\"gamma\"]\n                    d = result[\"diagnostics\"]\n                    log.info(\"[%s/%s] gamma=%.4f [%.4f, %.4f] rhat=%.4f div=%d\",\n                             gname, bench, g[\"mean\"], g[\"q025\"], g[\"q975\"],\n                             d.get(\"max_rhat\", 0), d.get(\"divergent_count\", 0))\n\n            all_results[\"scheme_B\"][gname] = group_results\n            gdir = OUTPUT_DIR / \"scheme_B\" / gname\n            gdir.mkdir(parents=True, exist_ok=True)\n            for bench, result in group_results.items():\n                with open(gdir / f\"{bench}_results.json\", \"w\") as f:\n                    json.dump(result, f, indent=2)\n\n    elapsed_total = time.time() - t0_total\n\n    with open(OUTPUT_DIR / \"stratified_irt_results.json\", \"w\") as f:\n        json.dump(all_results, f, indent=2)\n\n    # Summary\n    print(\"\\n\" + \"=\" * 70)\n    print(\"STRATIFIED IRT RESULTS\")\n    print(\"=\" * 70)\n    print(f\"Total time: {elapsed_total:.0f}s\")\n\n    for scheme_key, scheme_label in [(\"scheme_A\", \"SCHEME A (by dosage)\"),\n                                      (\"scheme_B\", \"SCHEME B (by model size)\")]:\n        if not all_results[scheme_key]:\n            continue\n        print(f\"\\n{scheme_label}:\")\n        for gname, gresults in all_results[scheme_key].items():\n            print(f\"  {gname}:\")\n            for bench, r in gresults.items():\n                g = r[\"gamma\"]\n                var = \"\" if r.get(\"has_dosage_variation\") else \" [CONST EXP]\"\n                print(f\"    {bench}: gamma={g['mean']:.4f} \"\n                      f\"[{g['q025']:.4f}, {g['q975']:.4f}] \"\n                      f\"N={r['n_models']}{var}\")\n\n    print(f\"\\nSaved to {OUTPUT_DIR}\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_stratified-irt-design_20260515T134139",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/run_stratified_irt.py",
    "content": "#!/usr/bin/env python3\n\"\"\"\nStratified IRT analysis: dose-response and model-size strata.\n\nScheme A: by dosage (d000/d005/d025/d100) — checks dose-response in gamma\nScheme B: by model size (0.5B/1.5B/3B) — checks if gamma varies by capacity\n\nSame exclusion rules as pooled analysis (D044/D045/D046/D047/D018).\nOracle dosage as exposure (dosage/100 global normalization). 2PL+gamma model.\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport sys\nimport time\nfrom pathlib import Path\n\nimport numpy as np\n\nsys.path.insert(0, \"/root/contamcal-irt-calibration/exp006\")\nfrom run_irt_calibration import (\n    load_pooled_eval_results,\n    prepare_stan_data,\n    fit_stan_model,\n    check_convergence,\n    posterior_predictive_check,\n    extract_results,\n    STAN_MODELS,\n)\n\nlog = logging.getLogger(__name__)\n\nBENCHMARKS = [\"mmlu\", \"gsm8k\", \"arc_challenge\", \"humaneval\"]\nSCALES = [\"0.5B\", \"1.5B\", \"3B\"]\nMODEL_TYPE = \"2pl_gamma\"\nSTAN_FILE = STAN_MODELS[MODEL_TYPE]\n\nEVAL_DIR = \"/root/autodl-tmp/exp001/eval_results\"\nOUTPUT_DIR = Path(\"/root/autodl-tmp/exp006/results_stratified_irt\")\n\nMAX_ITEMS = 2000\n\nDOSAGE_GROUPS = {\n    \"d000\": [0],\n    \"d005\": [5],\n    \"d025\": [25],\n    \"d100\": [100],\n}\n\nSCALE_GROUPS = {\n    \"scale_0.5B\": [\"0.5B\"],\n    \"scale_1.5B\": [\"1.5B\"],\n    \"scale_3B\": [\"3B\"],\n}\n\n\ndef apply_per_benchmark_exclusions(models, dosages, responses, valid_mask, benchmark):\n    keep = np.ones(len(models), dtype=bool)\n    reasons = []\n\n    for i, m in enumerate(models):\n        dirname = m.get(\"dirname\", \"\")\n        scale = m.get(\"scale\", \"\")\n        dosage = m.get(\"dosage\", 0)\n\n        if \"base_pretrained\" in dirname:\n            keep[i] = False\n            reasons.append(f\"  D046/D047: {dirname}\")\n            continue\n        if \"DEPRECATED\" in dirname:\n            keep[i] = False\n            reasons.append(f\"  D018: {dirname}\")\n            continue\n        if \"0.5B\" in scale and benchmark in (\"mmlu\", \"arc_challenge\"):\n            keep[i] = False\n            reasons.append(f\"  D045: {dirname}\")\n            continue\n        if benchmark == \"gsm8k\" and dosage == 0:\n            keep[i] = False\n            reasons.append(f\"  D044: {dirname}\")\n            continue\n\n    if reasons:\n        log.info(\"Excluded from %s (%d):\", benchmark, len(reasons))\n        for r in reasons[:5]:\n            log.info(r)\n        if len(reasons) > 5:\n            log.info(\"  ... +%d more\", len(reasons) - 5)\n\n    return (\n        [m for m, k in zip(models, keep) if k],\n        dosages[keep],\n        responses[keep],\n        valid_mask[keep],\n    )\n\n\ndef build_oracle_exposure_global(dosages, n_items):\n    \"\"\"Oracle exposure with global normalization: dosage/100.\"\"\"\n    fracs = dosages.astype(float) / 100.0\n    return np.outer(fracs, np.ones(n_items))\n\n\ndef filter_by_dosage(models, dosages, benchmarks_data, target_dosages):\n    keep = np.array([d in target_dosages for d in dosages])\n    filt_models = [m for m, k in zip(models, keep) if k]\n    filt_dosages = dosages[keep]\n    filt_bench = {}\n    for bench, bd in benchmarks_data.items():\n        filt_bench[bench] = {\n            \"responses\": bd[\"responses\"][keep],\n            \"n_items\": bd[\"n_items\"],\n            \"valid_mask\": bd[\"valid_mask\"][keep],\n        }\n    return filt_models, filt_dosages, filt_bench\n\n\ndef filter_by_scale(models, dosages, benchmarks_data, target_scales):\n    keep = np.array([m.get(\"scale\", \"\") in target_scales for m in models])\n    filt_models = [m for m, k in zip(models, keep) if k]\n    filt_dosages = dosages[keep]\n    filt_bench = {}\n    for bench, bd in benchmarks_data.items():\n        filt_bench[bench] = {\n            \"responses\": bd[\"responses\"][keep],\n            \"n_items\": bd[\"n_items\"],\n            \"valid_mask\": bd[\"valid_mask\"][keep],\n        }\n    return filt_models, filt_dosages, filt_bench\n\n\ndef run_stratum_fit(stratum_name, models, dosages, bench_data, benchmark, args_dict):\n    responses = bench_data[\"responses\"]\n    valid_mask = bench_data[\"valid_mask\"]\n    n_items = bench_data[\"n_items\"]\n\n    models_f, dosages_f, responses_f, valid_f = apply_per_benchmark_exclusions(\n        models, dosages, responses, valid_mask, benchmark\n    )\n\n    if not valid_f.all():\n        active = valid_f.astype(bool)\n        models_f = [m for m, v in zip(models_f, active) if v]\n        dosages_f = dosages_f[active]\n        responses_f = responses_f[active]\n\n    n_models = len(models_f)\n    original_n_items = n_items\n    subsampled = False\n    if n_items > MAX_ITEMS:\n        np.random.seed(42)\n        indices = np.random.choice(n_items, MAX_ITEMS, replace=False)\n        indices.sort()\n        responses_f = responses_f[:, indices]\n        n_items = MAX_ITEMS\n        subsampled = True\n\n    if n_models < 3:\n        log.warning(\"[%s/%s] Too few models (%d), skipping\", stratum_name, benchmark, n_models)\n        return None\n\n    unique_dosages = np.unique(dosages_f)\n    has_dosage_variation = len(unique_dosages) > 1\n\n    exposure = build_oracle_exposure_global(dosages_f, n_items)\n\n    log.info(\"[%s/%s] %d models x %d items, dosages=%s\",\n             stratum_name, benchmark, n_models, n_items, unique_dosages.tolist())\n\n    stan_data = prepare_stan_data(responses_f, exposure, MODEL_TYPE)\n    fit, elapsed = fit_stan_model(\n        STAN_FILE, stan_data,\n        chains=args_dict[\"chains\"],\n        iter_warmup=args_dict[\"warmup\"],\n        iter_sampling=args_dict[\"samples\"],\n        adapt_delta=args_dict[\"adapt_delta\"],\n        max_treedepth=args_dict[\"max_treedepth\"],\n        seed=args_dict[\"seed\"],\n        parallel_chains=args_dict[\"parallel_chains\"],\n    )\n\n    diagnostics = check_convergence(fit)\n    ppc = posterior_predictive_check(fit, responses_f)\n    results = extract_results(fit, responses_f, MODEL_TYPE)\n\n    return {\n        \"stratum\": stratum_name,\n        \"benchmark\": benchmark,\n        \"n_models\": n_models,\n        \"n_items\": n_items,\n        \"original_n_items\": original_n_items,\n        \"subsampled\": subsampled,\n        \"unique_dosages\": unique_dosages.tolist(),\n        \"has_dosage_variation\": has_dosage_variation,\n        \"models\": [{\"dirname\": m[\"dirname\"], \"dosage\": m[\"dosage\"],\n                     \"scale\": m.get(\"scale\", \"\")} for m in models_f],\n        \"dosages\": dosages_f.tolist(),\n        \"fit_time_sec\": round(elapsed, 1),\n        \"diagnostics\": diagnostics,\n        \"posterior_predictive\": ppc,\n        \"gamma\": results.get(\"gamma\", {}),\n        \"calibrated_scores\": results.get(\"calibrated_scores\", {}),\n    }\n\n\ndef dry_run(data):\n    print(\"=\" * 70)\n    print(\"STRATIFIED IRT DRY-RUN\")\n    print(\"=\" * 70)\n\n    models = data[\"models\"]\n    dosages = data[\"dosages\"]\n    unique_d, counts_d = np.unique(dosages, return_counts=True)\n    scales = [m.get(\"scale\", \"?\") for m in models]\n    unique_s, counts_s = np.unique(scales, return_counts=True)\n\n    print(f\"\\nTotal models: {len(models)}\")\n    print(f\"Dosages: {dict(zip(unique_d.tolist(), counts_d.tolist()))}\")\n    print(f\"Scales:  {dict(zip(unique_s.tolist(), counts_s.tolist()))}\")\n\n    # Scheme A\n    print(\"\\n\" + \"=\" * 70)\n    print(\"SCHEME A: by Dosage\")\n    print(\"=\" * 70)\n    for gname, target_d in DOSAGE_GROUPS.items():\n        mf, df, bf = filter_by_dosage(models, dosages, data[\"benchmarks\"], target_d)\n        print(f\"\\n--- {gname} (dosages={target_d}, N={len(mf)}) ---\")\n        for bench in BENCHMARKS:\n            if bench not in bf:\n                print(f\"  {bench}: NOT AVAILABLE\")\n                continue\n            bd = bf[bench]\n            me, de, re, ve = apply_per_benchmark_exclusions(\n                mf, df, bd[\"responses\"], bd[\"valid_mask\"], bench\n            )\n            if not ve.all():\n                active = ve.astype(bool)\n                me = [m for m, v in zip(me, active) if v]\n                re = re[active]\n                de = de[active]\n            nm = len(me)\n            ni = min(bd[\"n_items\"], MAX_ITEMS)\n            sub = f\" (subsampled from {bd['n_items']})\" if bd[\"n_items\"] > MAX_ITEMS else \"\"\n            status = \"OK\" if nm >= 4 else (\"MARGINAL\" if nm >= 3 else \"SKIP\")\n            print(f\"  {bench}: {nm} models x {ni} items{sub} [{status}]\")\n            for m in me:\n                print(f\"    {m['dirname']} (d{m['dosage']:03d}, {m.get('scale','')})\")\n\n    # Scheme B\n    print(\"\\n\" + \"=\" * 70)\n    print(\"SCHEME B: by Model Size\")\n    print(\"=\" * 70)\n    for gname, target_s in SCALE_GROUPS.items():\n        mf, df, bf = filter_by_scale(models, dosages, data[\"benchmarks\"], target_s)\n        unique_df = np.unique(df)\n        has_var = len(unique_df) > 1\n        print(f\"\\n--- {gname} (N={len(mf)}, dosages={unique_df.tolist()}) ---\")\n        print(f\"  Gamma identifiable: {'YES' if has_var else 'NO'}\")\n        for bench in BENCHMARKS:\n            if bench not in bf:\n                print(f\"  {bench}: NOT AVAILABLE\")\n                continue\n            bd = bf[bench]\n            me, de, re, ve = apply_per_benchmark_exclusions(\n                mf, df, bd[\"responses\"], bd[\"valid_mask\"], bench\n            )\n            if not ve.all():\n                active = ve.astype(bool)\n                me = [m for m, v in zip(me, active) if v]\n                de = de[active]\n                re = re[active]\n            nm = len(me)\n            ni = min(bd[\"n_items\"], MAX_ITEMS)\n            sub = f\" (subsampled from {bd['n_items']})\" if bd[\"n_items\"] > MAX_ITEMS else \"\"\n            ud = np.unique(de).tolist() if nm > 0 else []\n            status = \"OK\" if nm >= 4 else (\"MARGINAL\" if nm >= 3 else \"SKIP\")\n            print(f\"  {bench}: {nm} models x {ni} items, dosages={ud}{sub} [{status}]\")\n            for m in me:\n                print(f\"    {m['dirname']} (d{m['dosage']:03d})\")\n\n    # Power assessment\n    print(\"\\n\" + \"=\" * 70)\n    print(\"IDENTIFIABILITY NOTE\")\n    print(\"=\" * 70)\n    print(\"Scheme A: Single-dosage strata have constant exposure across models.\")\n    print(\"  d000: exposure=0 everywhere -> gamma unconstrained (prior only)\")\n    print(\"  d005/d025/d100: exposure=constant -> gamma confounded with b_j\")\n    print(\"  Interpretation: compare gamma posteriors across strata as\")\n    print(\"  'how much does the model need gamma to explain response patterns'\")\n    print(\"  rather than strict point-identification.\")\n    print(\"Scheme B: Varying dosages within each scale -> gamma IS point-identified.\")\n    print(\"  This is the primary analysis for dose-response signal.\")\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Stratified IRT analysis\")\n    parser.add_argument(\"--dry-run\", action=\"store_true\")\n    parser.add_argument(\"--scheme\", choices=[\"A\", \"B\", \"both\"], default=\"both\")\n    parser.add_argument(\"--chains\", type=int, default=4)\n    parser.add_argument(\"--warmup\", type=int, default=1000)\n    parser.add_argument(\"--samples\", type=int, default=1000)\n    parser.add_argument(\"--adapt-delta\", type=float, default=0.95)\n    parser.add_argument(\"--max-treedepth\", type=int, default=12)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--parallel-chains\", type=int, default=1)\n    args = parser.parse_args()\n\n    logging.basicConfig(level=logging.INFO,\n                        format=\"%(asctime)s [%(levelname)s] %(message)s\")\n\n    os.environ.setdefault(\"TMPDIR\", \"/home/ubuntu/tmp_cmdstan\")\n    os.makedirs(os.environ[\"TMPDIR\"], exist_ok=True)\n\n    log.info(\"Loading pooled eval results...\")\n    data = load_pooled_eval_results(\n        EVAL_DIR, SCALES, benchmarks=BENCHMARKS,\n        aligned_only=True, skip_para=True,\n    )\n    log.info(\"Loaded %d models, %d benchmarks\",\n             len(data[\"models\"]), len(data[\"benchmarks\"]))\n\n    if args.dry_run:\n        dry_run(data)\n        return\n\n    args_dict = {\n        \"chains\": args.chains,\n        \"warmup\": args.warmup,\n        \"samples\": args.samples,\n        \"adapt_delta\": args.adapt_delta,\n        \"max_treedepth\": args.max_treedepth,\n        \"seed\": args.seed,\n        \"parallel_chains\": args.parallel_chains,\n    }\n\n    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)\n    all_results = {\"scheme_A\": {}, \"scheme_B\": {}}\n    t0_total = time.time()\n\n    # Scheme A\n    if args.scheme in (\"A\", \"both\"):\n        log.info(\"=\" * 60)\n        log.info(\"SCHEME A: by Dosage\")\n        log.info(\"=\" * 60)\n\n        for gname, target_d in DOSAGE_GROUPS.items():\n            mf, df, bf = filter_by_dosage(\n                data[\"models\"], data[\"dosages\"], data[\"benchmarks\"], target_d\n            )\n            log.info(\"--- %s: %d models ---\", gname, len(mf))\n            group_results = {}\n\n            for bench in BENCHMARKS:\n                if bench not in bf:\n                    continue\n                result = run_stratum_fit(\n                    f\"A_{gname}\", mf, df, bf[bench], bench, args_dict\n                )\n                if result:\n                    group_results[bench] = result\n                    g = result[\"gamma\"]\n                    d = result[\"diagnostics\"]\n                    log.info(\"[%s/%s] gamma=%.4f [%.4f, %.4f] rhat=%.4f div=%d\",\n                             gname, bench, g[\"mean\"], g[\"q025\"], g[\"q975\"],\n                             d.get(\"max_rhat\", 0), d.get(\"divergent_count\", 0))\n\n            all_results[\"scheme_A\"][gname] = group_results\n            gdir = OUTPUT_DIR / \"scheme_A\" / gname\n            gdir.mkdir(parents=True, exist_ok=True)\n            for bench, result in group_results.items():\n                with open(gdir / f\"{bench}_results.json\", \"w\") as f:\n                    json.dump(result, f, indent=2)\n\n    # Scheme B\n    if args.scheme in (\"B\", \"both\"):\n        log.info(\"=\" * 60)\n        log.info(\"SCHEME B: by Model Size\")\n        log.info(\"=\" * 60)\n\n        for gname, target_s in SCALE_GROUPS.items():\n            mf, df, bf = filter_by_scale(\n                data[\"models\"], data[\"dosages\"], data[\"benchmarks\"], target_s\n            )\n            log.info(\"--- %s: %d models ---\", gname, len(mf))\n            group_results = {}\n\n            for bench in BENCHMARKS:\n                if bench not in bf:\n                    continue\n                result = run_stratum_fit(\n                    f\"B_{gname}\", mf, df, bf[bench], bench, args_dict\n                )\n                if result:\n                    group_results[bench] = result\n                    g = result[\"gamma\"]\n                    d = result[\"diagnostics\"]\n                    log.info(\"[%s/%s] gamma=%.4f [%.4f, %.4f] rhat=%.4f div=%d\",\n                             gname, bench, g[\"mean\"], g[\"q025\"], g[\"q975\"],\n                             d.get(\"max_rhat\", 0), d.get(\"divergent_count\", 0))\n\n            all_results[\"scheme_B\"][gname] = group_results\n            gdir = OUTPUT_DIR / \"scheme_B\" / gname\n            gdir.mkdir(parents=True, exist_ok=True)\n            for bench, result in group_results.items():\n                with open(gdir / f\"{bench}_results.json\", \"w\") as f:\n                    json.dump(result, f, indent=2)\n\n    elapsed_total = time.time() - t0_total\n\n    with open(OUTPUT_DIR / \"stratified_irt_results.json\", \"w\") as f:\n        json.dump(all_results, f, indent=2)\n\n    # Summary\n    print(\"\\n\" + \"=\" * 70)\n    print(\"STRATIFIED IRT RESULTS\")\n    print(\"=\" * 70)\n    print(f\"Total time: {elapsed_total:.0f}s\")\n\n    for scheme_key, scheme_label in [(\"scheme_A\", \"SCHEME A (by dosage)\"),\n                                      (\"scheme_B\", \"SCHEME B (by model size)\")]:\n        if not all_results[scheme_key]:\n            continue\n        print(f\"\\n{scheme_label}:\")\n        for gname, gresults in all_results[scheme_key].items():\n            print(f\"  {gname}:\")\n            for bench, r in gresults.items():\n                g = r[\"gamma\"]\n                var = \"\" if r.get(\"has_dosage_variation\") else \" [CONST EXP]\"\n                print(f\"    {bench}: gamma={g['mean']:.4f} \"\n                      f\"[{g['q025']:.4f}, {g['q975']:.4f}] \"\n                      f\"N={r['n_models']}{var}\")\n\n    print(f\"\\nSaved to {OUTPUT_DIR}\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T13:48:57.968816+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/run_stratified_irt.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_stratified-irt-design_20260515T134139",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T13:48:57.969041+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat > /root/contamcal-irt-calibration/exp006/run_stratified_irt.py << 'SCRIPT_EOF'\n#!/usr/bin/env python3\n\"\"\"\nStratified IRT analysis: dose-response and model-size strata.\n\nScheme A: by dosage (d000/d005/d025/d100) — checks dose-response in gamma\nScheme B: by model size (0.5B/1.5B/3B) — checks if gamma varies by capacity\n\nSame exclusion rules as pooled analysis (D044/D045/D046/D047/D018).\nOracle dosage as exposure (dosage/100 global normalization). 2PL+gamma model.\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport sys\nimport time\nfrom pathlib import Path\n\nimport numpy as np\n\nsys.path.insert(0, \"/root/contamcal-irt-calibration/exp006\")\nfrom run_irt_calibration import (\n    load_pooled_eval_results,\n    prepare_stan_data,\n    fit_stan_model,\n    check_convergence,\n    posterior_predictive_check,\n    extract_results,\n    STAN_MODELS,\n)\n\nlog = logging.getLogger(__name__)\n\nBENCHMARKS = [\"mmlu\", \"gsm8k\", \"arc_challenge\", \"humaneval\"]\nSCALES = [\"0.5B\", \"1.5B\", \"3B\"]\nMODEL_TYPE = \"2pl_gamma\"\nSTAN_FILE = STAN_MODELS[MODEL_TYPE]\n\nEVAL_DIR = \"/root/autodl-tmp/exp001/eval_results\"\nOUTPUT_DIR = Path(\"/root/autodl-tmp/exp006/results_stratified_irt\")\n\nMAX_ITEMS = 2000\n\nDOSAGE_GROUPS = {\n    \"d000\": [0],\n    \"d005\": [5],\n    \"d025\": [25],\n    \"d100\": [100],\n}\n\nSCALE_GROUPS = {\n    \"scale_0.5B\": [\"0.5B\"],\n    \"scale_1.5B\": [\"1.5B\"],\n    \"scale_3B\": [\"3B\"],\n}\n\n\ndef apply_per_benchmark_exclusions(models, dosages, responses, valid_mask, benchmark):\n    keep = np.ones(len(models), dtype=bool)\n    reasons = []\n\n    for i, m in enumerate(models):\n        dirname = m.get(\"dirname\", \"\")\n        scale = m.get(\"scale\", \"\")\n        dosage = m.get(\"dosage\", 0)\n\n        if \"base_pretrained\" in dirname:\n            keep[i] = False\n            reasons.append(f\"  D046/D047: {dirname}\")\n            continue\n        if \"DEPRECATED\" in dirname:\n            keep[i] = False\n            reasons.append(f\"  D018: {dirname}\")\n            continue\n        if \"0.5B\" in scale and benchmark in (\"mmlu\", \"arc_challenge\"):\n            keep[i] = False\n            reasons.append(f\"  D045: {dirname}\")\n            continue\n        if benchmark == \"gsm8k\" and dosage == 0:\n            keep[i] = False\n            reasons.append(f\"  D044: {dirname}\")\n            continue\n\n    if reasons:\n        log.info(\"Excluded from %s (%d):\", benchmark, len(reasons))\n        for r in reasons[:5]:\n            log.info(r)\n        if len(reasons) > 5:\n            log.info(\"  ... +%d more\", len(reasons) - 5)\n\n    return (\n        [m for m, k in zip(models, keep) if k],\n        dosages[keep],\n        responses[keep],\n        valid_mask[keep],\n    )\n\n\ndef build_oracle_exposure_global(dosages, n_items):\n    \"\"\"Oracle exposure with global normalization: dosage/100.\"\"\"\n    fracs = dosages.astype(float) / 100.0\n    return np.outer(fracs, np.ones(n_items))\n\n\ndef filter_by_dosage(models, dosages, benchmarks_data, target_dosages):\n    keep = np.array([d in target_dosages for d in dosages])\n    filt_models = [m for m, k in zip(models, keep) if k]\n    filt_dosages = dosages[keep]\n    filt_bench = {}\n    for bench, bd in benchmarks_data.items():\n        filt_bench[bench] = {\n            \"responses\": bd[\"responses\"][keep],\n            \"n_items\": bd[\"n_items\"],\n            \"valid_mask\": bd[\"valid_mask\"][keep],\n        }\n    return filt_models, filt_dosages, filt_bench\n\n\ndef filter_by_scale(models, dosages, benchmarks_data, target_scales):\n    keep = np.array([m.get(\"scale\", \"\") in target_scales for m in models])\n    filt_models = [m for m, k in zip(models, keep) if k]\n    filt_dosages = dosages[keep]\n    filt_bench = {}\n    for bench, bd in benchmarks_data.items():\n        filt_bench[bench] = {\n            \"responses\": bd[\"responses\"][keep],\n            \"n_items\": bd[\"n_items\"],\n            \"valid_mask\": bd[\"valid_mask\"][keep],\n        }\n    return filt_models, filt_dosages, filt_bench\n\n\ndef run_stratum_fit(stratum_name, models, dosages, bench_data, benchmark, args_dict):\n    responses = bench_data[\"responses\"]\n    valid_mask = bench_data[\"valid_mask\"]\n    n_items = bench_data[\"n_items\"]\n\n    models_f, dosages_f, responses_f, valid_f = apply_per_benchmark_exclusions(\n        models, dosages, responses, valid_mask, benchmark\n    )\n\n    if not valid_f.all():\n        active = valid_f.astype(bool)\n        models_f = [m for m, v in zip(models_f, active) if v]\n        dosages_f = dosages_f[active]\n        responses_f = responses_f[active]\n\n    n_models = len(models_f)\n    original_n_items = n_items\n    subsampled = False\n    if n_items > MAX_ITEMS:\n        np.random.seed(42)\n        indices = np.random.choice(n_items, MAX_ITEMS, replace=False)\n        indices.sort()\n        responses_f = responses_f[:, indices]\n        n_items = MAX_ITEMS\n        subsampled = True\n\n    if n_models < 3:\n        log.warning(\"[%s/%s] Too few models (%d), skipping\", stratum_name, benchmark, n_models)\n        return None\n\n    unique_dosages = np.unique(dosages_f)\n    has_dosage_variation = len(unique_dosages) > 1\n\n    exposure = build_oracle_exposure_global(dosages_f, n_items)\n\n    log.info(\"[%s/%s] %d models x %d items, dosages=%s\",\n             stratum_name, benchmark, n_models, n_items, unique_dosages.tolist())\n\n    stan_data = prepare_stan_data(responses_f, exposure, MODEL_TYPE)\n    fit, elapsed = fit_stan_model(\n        STAN_FILE, stan_data,\n        chains=args_dict[\"chains\"],\n        iter_warmup=args_dict[\"warmup\"],\n        iter_sampling=args_dict[\"samples\"],\n        adapt_delta=args_dict[\"adapt_delta\"],\n        max_treedepth=args_dict[\"max_treedepth\"],\n        seed=args_dict[\"seed\"],\n        parallel_chains=args_dict[\"parallel_chains\"],\n    )\n\n    diagnostics = check_convergence(fit)\n    ppc = posterior_predictive_check(fit, responses_f)\n    results = extract_results(fit, responses_f, MODEL_TYPE)\n\n    return {\n        \"stratum\": stratum_name,\n        \"benchmark\": benchmark,\n        \"n_models\": n_models,\n        \"n_items\": n_items,\n        \"original_n_items\": original_n_items,\n        \"subsampled\": subsampled,\n        \"unique_dosages\": unique_dosages.tolist(),\n        \"has_dosage_variation\": has_dosage_variation,\n        \"models\": [{\"dirname\": m[\"dirname\"], \"dosage\": m[\"dosage\"],\n                     \"scale\": m.get(\"scale\", \"\")} for m in models_f],\n        \"dosages\": dosages_f.tolist(),\n        \"fit_time_sec\": round(elapsed, 1),\n        \"diagnostics\": diagnostics,\n        \"posterior_predictive\": ppc,\n        \"gamma\": results.get(\"gamma\", {}),\n        \"calibrated_scores\": results.get(\"calibrated_scores\", {}),\n    }\n\n\ndef dry_run(data):\n    print(\"=\" * 70)\n    print(\"STRATIFIED IRT DRY-RUN\")\n    print(\"=\" * 70)\n\n    models = data[\"models\"]\n    dosages = data[\"dosages\"]\n    unique_d, counts_d = np.unique(dosages, return_counts=True)\n    scales = [m.get(\"scale\", \"?\") for m in models]\n    unique_s, counts_s = np.unique(scales, return_counts=True)\n\n    print(f\"\\nTotal models: {len(models)}\")\n    print(f\"Dosages: {dict(zip(unique_d.tolist(), counts_d.tolist()))}\")\n    print(f\"Scales:  {dict(zip(unique_s.tolist(), counts_s.tolist()))}\")\n\n    # Scheme A\n    print(\"\\n\" + \"=\" * 70)\n    print(\"SCHEME A: by Dosage\")\n    print(\"=\" * 70)\n    for gname, target_d in DOSAGE_GROUPS.items():\n        mf, df, bf = filter_by_dosage(models, dosages, data[\"benchmarks\"], target_d)\n        print(f\"\\n--- {gname} (dosages={target_d}, N={len(mf)}) ---\")\n        for bench in BENCHMARKS:\n            if bench not in bf:\n                print(f\"  {bench}: NOT AVAILABLE\")\n                continue\n            bd = bf[bench]\n            me, de, re, ve = apply_per_benchmark_exclusions(\n                mf, df, bd[\"responses\"], bd[\"valid_mask\"], bench\n            )\n            if not ve.all():\n                active = ve.astype(bool)\n                me = [m for m, v in zip(me, active) if v]\n                re = re[active]\n                de = de[active]\n            nm = len(me)\n            ni = min(bd[\"n_items\"], MAX_ITEMS)\n            sub = f\" (subsampled from {bd['n_items']})\" if bd[\"n_items\"] > MAX_ITEMS else \"\"\n            status = \"OK\" if nm >= 4 else (\"MARGINAL\" if nm >= 3 else \"SKIP\")\n            print(f\"  {bench}: {nm} models x {ni} items{sub} [{status}]\")\n            for m in me:\n                print(f\"    {m['dirname']} (d{m['dosage']:03d}, {m.get('scale','')})\")\n\n    # Scheme B\n    print(\"\\n\" + \"=\" * 70)\n    print(\"SCHEME B: by Model Size\")\n    print(\"=\" * 70)\n    for gname, target_s in SCALE_GROUPS.items():\n        mf, df, bf = filter_by_scale(models, dosages, data[\"benchmarks\"], target_s)\n        unique_df = np.unique(df)\n        has_var = len(unique_df) > 1\n        print(f\"\\n--- {gname} (N={len(mf)}, dosages={unique_df.tolist()}) ---\")\n        print(f\"  Gamma identifiable: {'YES' if has_var else 'NO'}\")\n        for bench in BENCHMARKS:\n            if bench not in bf:\n                print(f\"  {bench}: NOT AVAILABLE\")\n                continue\n            bd = bf[bench]\n            me, de, re, ve = apply_per_benchmark_exclusions(\n                mf, df, bd[\"responses\"], bd[\"valid_mask\"], bench\n            )\n            if not ve.all():\n                active = ve.astype(bool)\n                me = [m for m, v in zip(me, active) if v]\n                de = de[active]\n                re = re[active]\n            nm = len(me)\n            ni = min(bd[\"n_items\"], MAX_ITEMS)\n            sub = f\" (subsampled from {bd['n_items']})\" if bd[\"n_items\"] > MAX_ITEMS else \"\"\n            ud = np.unique(de).tolist() if nm > 0 else []\n            status = \"OK\" if nm >= 4 else (\"MARGINAL\" if nm >= 3 else \"SKIP\")\n            print(f\"  {bench}: {nm} models x {ni} items, dosages={ud}{sub} [{status}]\")\n            for m in me:\n                print(f\"    {m['dirname']} (d{m['dosage']:03d})\")\n\n    # Power assessment\n    print(\"\\n\" + \"=\" * 70)\n    print(\"IDENTIFIABILITY NOTE\")\n    print(\"=\" * 70)\n    print(\"Scheme A: Single-dosage strata have constant exposure across models.\")\n    print(\"  d000: exposure=0 everywhere -> gamma unconstrained (prior only)\")\n    print(\"  d005/d025/d100: exposure=constant -> gamma confounded with b_j\")\n    print(\"  Interpretation: compare gamma posteriors across strata as\")\n    print(\"  'how much does the model need gamma to explain response patterns'\")\n    print(\"  rather than strict point-identification.\")\n    print(\"Scheme B: Varying dosages within each scale -> gamma IS point-identified.\")\n    print(\"  This is the primary analysis for dose-response signal.\")\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Stratified IRT analysis\")\n    parser.add_argument(\"--dry-run\", action=\"store_true\")\n    parser.add_argument(\"--scheme\", choices=[\"A\", \"B\", \"both\"], default=\"both\")\n    parser.add_argument(\"--chains\", type=int, default=4)\n    parser.add_argument(\"--warmup\", type=int, default=1000)\n    parser.add_argument(\"--samples\", type=int, default=1000)\n    parser.add_argument(\"--adapt-delta\", type=float, default=0.95)\n    parser.add_argument(\"--max-treedepth\", type=int, default=12)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--parallel-chains\", type=int, default=1)\n    args = parser.parse_args()\n\n    logging.basicConfig(level=logging.INFO,\n                        format=\"%(asctime)s [%(levelname)s] %(message)s\")\n\n    os.environ.setdefault(\"TMPDIR\", \"/home/ubuntu/tmp_cmdstan\")\n    os.makedirs(os.environ[\"TMPDIR\"], exist_ok=True)\n\n    log.info(\"Loading pooled eval results...\")\n    data = load_pooled_eval_results(\n        EVAL_DIR, SCALES, benchmarks=BENCHMARKS,\n        aligned_only=True, skip_para=True,\n    )\n    log.info(\"Loaded %d models, %d benchmarks\",\n             len(data[\"models\"]), len(data[\"benchmarks\"]))\n\n    if args.dry_run:\n        dry_run(data)\n        return\n\n    args_dict = {\n        \"chains\": args.chains,\n        \"warmup\": args.warmup,\n        \"samples\": args.samples,\n        \"adapt_delta\": args.adapt_delta,\n        \"max_treedepth\": args.max_treedepth,\n        \"seed\": args.seed,\n        \"parallel_chains\": args.parallel_chains,\n    }\n\n    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)\n    all_results = {\"scheme_A\": {}, \"scheme_B\": {}}\n    t0_total = time.time()\n\n    # Scheme A\n    if args.scheme in (\"A\", \"both\"):\n        log.info(\"=\" * 60)\n        log.info(\"SCHEME A: by Dosage\")\n        log.info(\"=\" * 60)\n\n        for gname, target_d in DOSAGE_GROUPS.items():\n            mf, df, bf = filter_by_dosage(\n                data[\"models\"], data[\"dosages\"], data[\"benchmarks\"], target_d\n            )\n            log.info(\"--- %s: %d models ---\", gname, len(mf))\n            group_results = {}\n\n            for bench in BENCHMARKS:\n                if bench not in bf:\n                    continue\n                result = run_stratum_fit(\n                    f\"A_{gname}\", mf, df, bf[bench], bench, args_dict\n                )\n                if result:\n                    group_results[bench] = result\n                    g = result[\"gamma\"]\n                    d = result[\"diagnostics\"]\n                    log.info(\"[%s/%s] gamma=%.4f [%.4f, %.4f] rhat=%.4f div=%d\",\n                             gname, bench, g[\"mean\"], g[\"q025\"], g[\"q975\"],\n                             d.get(\"max_rhat\", 0), d.get(\"divergent_count\", 0))\n\n            all_results[\"scheme_A\"][gname] = group_results\n            gdir = OUTPUT_DIR / \"scheme_A\" / gname\n            gdir.mkdir(parents=True, exist_ok=True)\n            for bench, result in group_results.items():\n                with open(gdir / f\"{bench}_results.json\", \"w\") as f:\n                    json.dump(result, f, indent=2)\n\n    # Scheme B\n    if args.scheme in (\"B\", \"both\"):\n        log.info(\"=\" * 60)\n        log.info(\"SCHEME B: by Model Size\")\n        log.info(\"=\" * 60)\n\n        for gname, target_s in SCALE_GROUPS.items():\n            mf, df, bf = filter_by_scale(\n                data[\"models\"], data[\"dosages\"], data[\"benchmarks\"], target_s\n            )\n            log.info(\"--- %s: %d models ---\", gname, len(mf))\n            group_results = {}\n\n            for bench in BENCHMARKS:\n                if bench not in bf:\n                    continue\n                result = run_stratum_fit(\n                    f\"B_{gname}\", mf, df, bf[bench], bench, args_dict\n                )\n                if result:\n                    group_results[bench] = result\n                    g = result[\"gamma\"]\n                    d = result[\"diagnostics\"]\n                    log.info(\"[%s/%s] gamma=%.4f [%.4f, %.4f] rhat=%.4f div=%d\",\n                             gname, bench, g[\"mean\"], g[\"q025\"], g[\"q975\"],\n                             d.get(\"max_rhat\", 0), d.get(\"divergent_count\", 0))\n\n            all_results[\"scheme_B\"][gname] = group_results\n            gdir = OUTPUT_DIR / \"scheme_B\" / gname\n            gdir.mkdir(parents=True, exist_ok=True)\n            for bench, result in group_results.items():\n                with open(gdir / f\"{bench}_results.json\", \"w\") as f:\n                    json.dump(result, f, indent=2)\n\n    elapsed_total = time.time() - t0_total\n\n    with open(OUTPUT_DIR / \"stratified_irt_results.json\", \"w\") as f:\n        json.dump(all_results, f, indent=2)\n\n    # Summary\n    print(\"\\n\" + \"=\" * 70)\n    print(\"STRATIFIED IRT RESULTS\")\n    print(\"=\" * 70)\n    print(f\"Total time: {elapsed_total:.0f}s\")\n\n    for scheme_key, scheme_label in [(\"scheme_A\", \"SCHEME A (by dosage)\"),\n                                      (\"scheme_B\", \"SCHEME B (by model size)\")]:\n        if not all_results[scheme_key]:\n            continue\n        print(f\"\\n{scheme_label}:\")\n        for gname, gresults in all_results[scheme_key].items():\n            print(f\"  {gname}:\")\n            for bench, r in gresults.items():\n                g = r[\"gamma\"]\n                var = \"\" if r.get(\"has_dosage_variation\") else \" [CONST EXP]\"\n                print(f\"    {bench}: gamma={g['mean']:.4f} \"\n                      f\"[{g['q025']:.4f}, {g['q975']:.4f}] \"\n                      f\"N={r['n_models']}{var}\")\n\n    print(f\"\\nSaved to {OUTPUT_DIR}\")\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_stratified-irt-design_20260515T134139",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat > /root/contamcal-irt-calibration/exp006/run_stratified_irt.py << 'SCRIPT_EOF'\n#!/usr/bin/env python3\n\"\"\"\nStratified IRT analysis: dose-response and model-size strata.\n\nScheme A: by dosage (d000/d005/d025/d100) — checks dose-response in gamma\nScheme B: by model size (0.5B/1.5B/3B) — checks if gamma varies by capacity\n\nSame exclusion rules as pooled analysis (D044/D045/D046/D047/D018).\nOracle dosage as exposure (dosage/100 global normalization). 2PL+gamma model.\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport sys\nimport time\nfrom pathlib import Path\n\nimport numpy as np\n\nsys.path.insert(0, \"/root/contamcal-irt-calibration/exp006\")\nfrom run_irt_calibration import (\n    load_pooled_eval_results,\n    prepare_stan_data,\n    fit_stan_model,\n    check_convergence,\n    posterior_predictive_check,\n    extract_results,\n    STAN_MODELS,\n)\n\nlog = logging.getLogger(__name__)\n\nBENCHMARKS = [\"mmlu\", \"gsm8k\", \"arc_challenge\", \"humaneval\"]\nSCALES = [\"0.5B\", \"1.5B\", \"3B\"]\nMODEL_TYPE = \"2pl_gamma\"\nSTAN_FILE = STAN_MODELS[MODEL_TYPE]\n\nEVAL_DIR = \"/root/autodl-tmp/exp001/eval_results\"\nOUTPUT_DIR = Path(\"/root/autodl-tmp/exp006/results_stratified_irt\")\n\nMAX_ITEMS = 2000\n\nDOSAGE_GROUPS = {\n    \"d000\": [0],\n    \"d005\": [5],\n    \"d025\": [25],\n    \"d100\": [100],\n}\n\nSCALE_GROUPS = {\n    \"scale_0.5B\": [\"0.5B\"],\n    \"scale_1.5B\": [\"1.5B\"],\n    \"scale_3B\": [\"3B\"],\n}\n\n\ndef apply_per_benchmark_exclusions(models, dosages, responses, valid_mask, benchmark):\n    keep = np.ones(len(models), dtype=bool)\n    reasons = []\n\n    for i, m in enumerate(models):\n        dirname = m.get(\"dirname\", \"\")\n        scale = m.get(\"scale\", \"\")\n        dosage = m.get(\"dosage\", 0)\n\n        if \"base_pretrained\" in dirname:\n            keep[i] = False\n            reasons.append(f\"  D046/D047: {dirname}\")\n            continue\n        if \"DEPRECATED\" in dirname:\n            keep[i] = False\n            reasons.append(f\"  D018: {dirname}\")\n            continue\n        if \"0.5B\" in scale and benchmark in (\"mmlu\", \"arc_challenge\"):\n            keep[i] = False\n            reasons.append(f\"  D045: {dirname}\")\n            continue\n        if benchmark == \"gsm8k\" and dosage == 0:\n            keep[i] = False\n            reasons.append(f\"  D044: {dirname}\")\n            continue\n\n    if reasons:\n        log.info(\"Excluded from %s (%d):\", benchmark, len(reasons))\n        for r in reasons[:5]:\n            log.info(r)\n        if len(reasons) > 5:\n            log.info(\"  ... +%d more\", len(reasons) - 5)\n\n    return (\n        [m for m, k in zip(models, keep) if k],\n        dosages[keep],\n        responses[keep],\n        valid_mask[keep],\n    )\n\n\ndef build_oracle_exposure_global(dosages, n_items):\n    \"\"\"Oracle exposure with global normalization: dosage/100.\"\"\"\n    fracs = dosages.astype(float) / 100.0\n    return np.outer(fracs, np.ones(n_items))\n\n\ndef filter_by_dosage(models, dosages, benchmarks_data, target_dosages):\n    keep = np.array([d in target_dosages for d in dosages])\n    filt_models = [m for m, k in zip(models, keep) if k]\n    filt_dosages = dosages[keep]\n    filt_bench = {}\n    for bench, bd in benchmarks_data.items():\n        filt_bench[bench] = {\n            \"responses\": bd[\"responses\"][keep],\n            \"n_items\": bd[\"n_items\"],\n            \"valid_mask\": bd[\"valid_mask\"][keep],\n        }\n    return filt_models, filt_dosages, filt_bench\n\n\ndef filter_by_scale(models, dosages, benchmarks_data, target_scales):\n    keep = np.array([m.get(\"scale\", \"\") in target_scales for m in models])\n    filt_models = [m for m, k in zip(models, keep) if k]\n    filt_dosages = dosages[keep]\n    filt_bench = {}\n    for bench, bd in benchmarks_data.items():\n        filt_bench[bench] = {\n            \"responses\": bd[\"responses\"][keep],\n            \"n_items\": bd[\"n_items\"],\n            \"valid_mask\": bd[\"valid_mask\"][keep],\n        }\n    return filt_models, filt_dosages, filt_bench\n\n\ndef run_stratum_fit(stratum_name, models, dosages, bench_data, benchmark, args_dict):\n    responses = bench_data[\"responses\"]\n    valid_mask = bench_data[\"valid_mask\"]\n    n_items = bench_data[\"n_items\"]\n\n    models_f, dosages_f, responses_f, valid_f = apply_per_benchmark_exclusions(\n        models, dosages, responses, valid_mask, benchmark\n    )\n\n    if not valid_f.all():\n        active = valid_f.astype(bool)\n        models_f = [m for m, v in zip(models_f, active) if v]\n        dosages_f = dosages_f[active]\n        responses_f = responses_f[active]\n\n    n_models = len(models_f)\n    original_n_items = n_items\n    subsampled = False\n    if n_items > MAX_ITEMS:\n        np.random.seed(42)\n        indices = np.random.choice(n_items, MAX_ITEMS, replace=False)\n        indices.sort()\n        responses_f = responses_f[:, indices]\n        n_items = MAX_ITEMS\n        subsampled = True\n\n    if n_models < 3:\n        log.warning(\"[%s/%s] Too few models (%d), skipping\", stratum_name, benchmark, n_models)\n        return None\n\n    unique_dosages = np.unique(dosages_f)\n    has_dosage_variation = len(unique_dosages) > 1\n\n    exposure = build_oracle_exposure_global(dosages_f, n_items)\n\n    log.info(\"[%s/%s] %d models x %d items, dosages=%s\",\n             stratum_name, benchmark, n_models, n_items, unique_dosages.tolist())\n\n    stan_data = prepare_stan_data(responses_f, exposure, MODEL_TYPE)\n    fit, elapsed = fit_stan_model(\n        STAN_FILE, stan_data,\n        chains=args_dict[\"chains\"],\n        iter_warmup=args_dict[\"warmup\"],\n        iter_sampling=args_dict[\"samples\"],\n        adapt_delta=args_dict[\"adapt_delta\"],\n        max_treedepth=args_dict[\"max_treedepth\"],\n        seed=args_dict[\"seed\"],\n        parallel_chains=args_dict[\"parallel_chains\"],\n    )\n\n    diagnostics = check_convergence(fit)\n    ppc = posterior_predictive_check(fit, responses_f)\n    results = extract_results(fit, responses_f, MODEL_TYPE)\n\n    return {\n        \"stratum\": stratum_name,\n        \"benchmark\": benchmark,\n        \"n_models\": n_models,\n        \"n_items\": n_items,\n        \"original_n_items\": original_n_items,\n        \"subsampled\": subsampled,\n        \"unique_dosages\": unique_dosages.tolist(),\n        \"has_dosage_variation\": has_dosage_variation,\n        \"models\": [{\"dirname\": m[\"dirname\"], \"dosage\": m[\"dosage\"],\n                     \"scale\": m.get(\"scale\", \"\")} for m in models_f],\n        \"dosages\": dosages_f.tolist(),\n        \"fit_time_sec\": round(elapsed, 1),\n        \"diagnostics\": diagnostics,\n        \"posterior_predictive\": ppc,\n        \"gamma\": results.get(\"gamma\", {}),\n        \"calibrated_scores\": results.get(\"calibrated_scores\", {}),\n    }\n\n\ndef dry_run(data):\n    print(\"=\" * 70)\n    print(\"STRATIFIED IRT DRY-RUN\")\n    print(\"=\" * 70)\n\n    models = data[\"models\"]\n    dosages = data[\"dosages\"]\n    unique_d, counts_d = np.unique(dosages, return_counts=True)\n    scales = [m.get(\"scale\", \"?\") for m in models]\n    unique_s, counts_s = np.unique(scales, return_counts=True)\n\n    print(f\"\\nTotal models: {len(models)}\")\n    print(f\"Dosages: {dict(zip(unique_d.tolist(), counts_d.tolist()))}\")\n    print(f\"Scales:  {dict(zip(unique_s.tolist(), counts_s.tolist()))}\")\n\n    # Scheme A\n    print(\"\\n\" + \"=\" * 70)\n    print(\"SCHEME A: by Dosage\")\n    print(\"=\" * 70)\n    for gname, target_d in DOSAGE_GROUPS.items():\n        mf, df, bf = filter_by_dosage(models, dosages, data[\"benchmarks\"], target_d)\n        print(f\"\\n--- {gname} (dosages={target_d}, N={len(mf)}) ---\")\n        for bench in BENCHMARKS:\n            if bench not in bf:\n                print(f\"  {bench}: NOT AVAILABLE\")\n                continue\n            bd = bf[bench]\n            me, de, re, ve = apply_per_benchmark_exclusions(\n                mf, df, bd[\"responses\"], bd[\"valid_mask\"], bench\n            )\n            if not ve.all():\n                active = ve.astype(bool)\n                me = [m for m, v in zip(me, active) if v]\n                re = re[active]\n                de = de[active]\n            nm = len(me)\n            ni = min(bd[\"n_items\"], MAX_ITEMS)\n            sub = f\" (subsampled from {bd['n_items']})\" if bd[\"n_items\"] > MAX_ITEMS else \"\"\n            status = \"OK\" if nm >= 4 else (\"MARGINAL\" if nm >= 3 else \"SKIP\")\n            print(f\"  {bench}: {nm} models x {ni} items{sub} [{status}]\")\n            for m in me:\n                print(f\"    {m['dirname']} (d{m['dosage']:03d}, {m.get('scale','')})\")\n\n    # Scheme B\n    print(\"\\n\" + \"=\" * 70)\n    print(\"SCHEME B: by Model Size\")\n    print(\"=\" * 70)\n    for gname, target_s in SCALE_GROUPS.items():\n        mf, df, bf = filter_by_scale(models, dosages, data[\"benchmarks\"], target_s)\n        unique_df = np.unique(df)\n        has_var = len(unique_df) > 1\n        print(f\"\\n--- {gname} (N={len(mf)}, dosages={unique_df.tolist()}) ---\")\n        print(f\"  Gamma identifiable: {'YES' if has_var else 'NO'}\")\n        for bench in BENCHMARKS:\n            if bench not in bf:\n                print(f\"  {bench}: NOT AVAILABLE\")\n                continue\n            bd = bf[bench]\n            me, de, re, ve = apply_per_benchmark_exclusions(\n                mf, df, bd[\"responses\"], bd[\"valid_mask\"], bench\n            )\n            if not ve.all():\n                active = ve.astype(bool)\n                me = [m for m, v in zip(me, active) if v]\n                de = de[active]\n                re = re[active]\n            nm = len(me)\n            ni = min(bd[\"n_items\"], MAX_ITEMS)\n            sub = f\" (subsampled from {bd['n_items']})\" if bd[\"n_items\"] > MAX_ITEMS else \"\"\n            ud = np.unique(de).tolist() if nm > 0 else []\n            status = \"OK\" if nm >= 4 else (\"MARGINAL\" if nm >= 3 else \"SKIP\")\n            print(f\"  {bench}: {nm} models x {ni} items, dosages={ud}{sub} [{status}]\")\n            for m in me:\n                print(f\"    {m['dirname']} (d{m['dosage']:03d})\")\n\n    # Power assessment\n    print(\"\\n\" + \"=\" * 70)\n    print(\"IDENTIFIABILITY NOTE\")\n    print(\"=\" * 70)\n    print(\"Scheme A: Single-dosage strata have constant exposure across models.\")\n    print(\"  d000: exposure=0 everywhere -> gamma unconstrained (prior only)\")\n    print(\"  d005/d025/d100: exposure=constant -> gamma confounded with b_j\")\n    print(\"  Interpretation: compare gamma posteriors across strata as\")\n    print(\"  'how much does the model need gamma to explain response patterns'\")\n    print(\"  rather than strict point-identification.\")\n    print(\"Scheme B: Varying dosages within each scale -> gamma IS point-identified.\")\n    print(\"  This is the primary analysis for dose-response signal.\")\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Stratified IRT analysis\")\n    parser.add_argument(\"--dry-run\", action=\"store_true\")\n    parser.add_argument(\"--scheme\", choices=[\"A\", \"B\", \"both\"], default=\"both\")\n    parser.add_argument(\"--chains\", type=int, default=4)\n    parser.add_argument(\"--warmup\", type=int, default=1000)\n    parser.add_argument(\"--samples\", type=int, default=1000)\n    parser.add_argument(\"--adapt-delta\", type=float, default=0.95)\n    parser.add_argument(\"--max-treedepth\", type=int, default=12)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--parallel-chains\", type=int, default=1)\n    args = parser.parse_args()\n\n    logging.basicConfig(level=logging.INFO,\n                        format=\"%(asctime)s [%(levelname)s] %(message)s\")\n\n    os.environ.setdefault(\"TMPDIR\", \"/home/ubuntu/tmp_cmdstan\")\n    os.makedirs(os.environ[\"TMPDIR\"], exist_ok=True)\n\n    log.info(\"Loading pooled eval results...\")\n    data = load_pooled_eval_results(\n        EVAL_DIR, SCALES, benchmarks=BENCHMARKS,\n        aligned_only=True, skip_para=True,\n    )\n    log.info(\"Loaded %d models, %d benchmarks\",\n             len(data[\"models\"]), len(data[\"benchmarks\"]))\n\n    if args.dry_run:\n        dry_run(data)\n        return\n\n    args_dict = {\n        \"chains\": args.chains,\n        \"warmup\": args.warmup,\n        \"samples\": args.samples,\n        \"adapt_delta\": args.adapt_delta,\n        \"max_treedepth\": args.max_treedepth,\n        \"seed\": args.seed,\n        \"parallel_chains\": args.parallel_chains,\n    }\n\n    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)\n    all_results = {\"scheme_A\": {}, \"scheme_B\": {}}\n    t0_total = time.time()\n\n    # Scheme A\n    if args.scheme in (\"A\", \"both\"):\n        log.info(\"=\" * 60)\n        log.info(\"SCHEME A: by Dosage\")\n        log.info(\"=\" * 60)\n\n        for gname, target_d in DOSAGE_GROUPS.items():\n            mf, df, bf = filter_by_dosage(\n                data[\"models\"], data[\"dosages\"], data[\"benchmarks\"], target_d\n            )\n            log.info(\"--- %s: %d models ---\", gname, len(mf))\n            group_results = {}\n\n            for bench in BENCHMARKS:\n                if bench not in bf:\n                    continue\n                result = run_stratum_fit(\n                    f\"A_{gname}\", mf, df, bf[bench], bench, args_dict\n                )\n                if result:\n                    group_results[bench] = result\n                    g = result[\"gamma\"]\n                    d = result[\"diagnostics\"]\n                    log.info(\"[%s/%s] gamma=%.4f [%.4f, %.4f] rhat=%.4f div=%d\",\n                             gname, bench, g[\"mean\"], g[\"q025\"], g[\"q975\"],\n                             d.get(\"max_rhat\", 0), d.get(\"divergent_count\", 0))\n\n            all_results[\"scheme_A\"][gname] = group_results\n            gdir = OUTPUT_DIR / \"scheme_A\" / gname\n            gdir.mkdir(parents=True, exist_ok=True)\n            for bench, result in group_results.items():\n                with open(gdir / f\"{bench}_results.json\", \"w\") as f:\n                    json.dump(result, f, indent=2)\n\n    # Scheme B\n    if args.scheme in (\"B\", \"both\"):\n        log.info(\"=\" * 60)\n        log.info(\"SCHEME B: by Model Size\")\n        log.info(\"=\" * 60)\n\n        for gname, target_s in SCALE_GROUPS.items():\n            mf, df, bf = filter_by_scale(\n                data[\"models\"], data[\"dosages\"], data[\"benchmarks\"], target_s\n            )\n            log.info(\"--- %s: %d models ---\", gname, len(mf))\n            group_results = {}\n\n            for bench in BENCHMARKS:\n                if bench not in bf:\n                    continue\n                result = run_stratum_fit(\n                    f\"B_{gname}\", mf, df, bf[bench], bench, args_dict\n                )\n                if result:\n                    group_results[bench] = result\n                    g = result[\"gamma\"]\n                    d = result[\"diagnostics\"]\n                    log.info(\"[%s/%s] gamma=%.4f [%.4f, %.4f] rhat=%.4f div=%d\",\n                             gname, bench, g[\"mean\"], g[\"q025\"], g[\"q975\"],\n                             d.get(\"max_rhat\", 0), d.get(\"divergent_count\", 0))\n\n            all_results[\"scheme_B\"][gname] = group_results\n            gdir = OUTPUT_DIR / \"scheme_B\" / gname\n            gdir.mkdir(parents=True, exist_ok=True)\n            for bench, result in group_results.items():\n                with open(gdir / f\"{bench}_results.json\", \"w\") as f:\n                    json.dump(result, f, indent=2)\n\n    elapsed_total = time.time() - t0_total\n\n    with open(OUTPUT_DIR / \"stratified_irt_results.json\", \"w\") as f:\n        json.dump(all_results, f, indent=2)\n\n    # Summary\n    print(\"\\n\" + \"=\" * 70)\n    print(\"STRATIFIED IRT RESULTS\")\n    print(\"=\" * 70)\n    print(f\"Total time: {elapsed_total:.0f}s\")\n\n    for scheme_key, scheme_label in [(\"scheme_A\", \"SCHEME A (by dosage)\"),\n                                      (\"scheme_B\", \"SCHEME B (by model size)\")]:\n        if not all_results[scheme_key]:\n            continue\n        print(f\"\\n{scheme_label}:\")\n        for gname, gresults in all_results[scheme_key].items():\n            print(f\"  {gname}:\")\n            for bench, r in gresults.items():\n                g = r[\"gamma\"]\n                var = \"\" if r.get(\"has_dosage_variation\") else \" [CONST EXP]\"\n                print(f\"    {bench}: gamma={g['mean']:.4f} \"\n                      f\"[{g['q025']:.4f}, {g['q975']:.4f}] \"\n                      f\"N={r['n_models']}{var}\")\n\n    print(f\"\\nSaved to {OUTPUT_DIR}\")\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T13:48:57.969373+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.54}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_stratified-irt-design_20260515T134139",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T13:48:57.969514+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cd /root/contamcal-irt-calibration/exp006 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && TMPDIR=/home/ubuntu/tmp_cmdstan python run_stratified_irt.py --dry-run 2>&1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_stratified-irt-design_20260515T134139",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cd /root/contamcal-irt-calibration/exp006 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && TMPDIR=/home/ubuntu/tmp_cmdstan python run_stratified_irt.py --dry-run 2>&1"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T13:48:57.969727+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-15 21:46:51,236 [INFO] Loading pooled eval results...\\n2026-05-15 21:46:51,238 [WARNING] Skipping unrecognized dir: Qwen2.5-0.5B-Instruct_aligned\\n2026-05-15 21:46:51,238 [INFO] Skipping non-aligned dir: Qwen2.5-0.5B_d000_s123\\n2026-05-15 21:46:51,238 [INFO] Skipping non-aligned dir: Qwen2.5-0.5B_d000_s42\\n2026-05-15 21:46:51,238 [INFO] Skipping non-aligned dir: Qwen2.5-0.5B_d000_s42_v2\\n2026-05-15 21:46:51,238 [INFO] Skipping non-aligned dir: Qwen2.5-0.5B_d005_s42\\n2026-05-15 21:46:51,238 [INFO] Skipping non-aligned dir: Qwen2.5-0.5B_d100_s42\\n2026-05-15 21:46:51,238 [WARNING] Skipping unrecognized dir: Qwen2.5-1.5B_base_pretrained\\n2026-05-15 21:46:51,238 [INFO] Skipping non-aligned dir: Qwen2.5-1.5B_d000_s123\\n2026-05-15 21:46:51,238 [INFO] Skipping dir (scale mismatch): Qwen2.5-1.5B_d000_s123_aligned\\n2026-05-15 21:46:51,238 [INFO] Skipping non-aligned dir: Qwen2.5-1.5B_d000_s42\\n2026-05-15 21:46:51,238 [INFO] Skipping dir (scale mismatch): Qwen2.5-1.5B_d000_s42_aligned\\n2026-05-15 21:46:51,238 [INFO] Skipping dir (scale mismatch): Qwen2.5-1.5B_d005_s42_aligned\\n2026-05-15 21:46:51,238 [INFO] Skipping dir (scale mismatch): Qwen2.5-1.5B_d025_s42_aligned\\n2026-05-15 21:46:51,238 [INFO] Skipping dir (scale mismatch): Qwen2.5-1.5B_d100_s123_aligned\\n2026-05-15 21:46:51,238 [INFO] Skipping non-aligned dir: Qwen2.5-1.5B_d100_s42\\n2026-05-15 21:46:51,238 [INFO] Skipping dir (scale mismatch): Qwen2.5-1.5B_d100_s42_aligned\\n2026-05-15 21:46:51,238 [INFO] Skipping non-aligned dir: Qwen2.5-3B_d000_s42\\n2026-05-15 21:46:51,238 [WARNING] Skipping unrecognized dir: Qwen2.5-3B_d000_s42_v3_aligned\\n2026-05-15 21:46:51,238 [WARNING] Skipping unrecognized dir: Qwen2.5-3B_d000_v1_s123_DEPRECATED\\n2026-05-15 21:46:51,239 [WARNING] Skipping unrecognized dir: Qwen2.5-3B_d000_v1_s42_aligned_DEPRECATED\\n2026-05-15 21:46:51,239 [INFO] Skipping dir (scale mismatch): Qwen2.5-3B_d000_v2_s123_aligned\\n2026
…[truncated 6470 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_stratified-irt-design_20260515T134139",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-15T13:48:57.969991+00:00_

Dry-run 成功。以下是完整统计：

### Scheme A: by Dosage

| 分层 | N_models | mmlu | gsm8k | arc_challenge | humaneval |
|------|----------|------|-------|---------------|-----------|
| d000 | 6 | 4 OK | 0 SKIP (D044) | 4 OK | 6 OK |
| d005 | 4 | 1 SKIP | 4 OK | 1 SKIP | 4 OK |
| d025 | 4 | 1 SKIP | 4 OK | 1 SKIP | 4 OK |
| d100 | 4 | 4 OK | 4 OK | 4 OK | 4 OK |

### Scheme B: by Model Size

| 分层 | N_models | mmlu | gsm8k | arc_challenge | humaneval |
|------|----------|------|-------|---------------|-----------|
| 0.5B | 8 | 0 SKIP (D045) | 6 OK | 0 SKIP (D045) | 8 OK |
| 1.5B | 6 | 6 OK | 4 OK | 6 OK | 6 OK |
| 3B | 4 | 4 OK | 2 SKIP | 4 OK | 4 OK |

### 统计功效评估

**Scheme A 问题：**
- d005/d025 的 mmlu 和 arc_challenge 排除后只剩 1 个模型（0.5B 被 D045 排除），无法拟合
- 单 dosage 分层中 exposure 是常数，gamma 不可点识别（d000: exposure=0 → gamma=prior；其余 dosage: exposure=constant → gamma 与 b_j 混淆）
- 可跑的组合：gsm8k 全部 4 个分层 + humaneval 全部 4 个 + d000/d100 的 mmlu/arc

**Scheme B 是主力分析：**
- 1.5B 最完整：4 个 benchmark 全部 N≥4，dosages=[0,5,25,100]，gamma 可识别
- 0.5B 只有 gsm8k 和 humaneval 可用，但 dosages=[0,5,25,100]，gamma 可识别
- 3B gsm8k 不够（d000 被 D044 排除后只剩 2 个 d100），其余 3 个 benchmark OK，dosages=[0,100]

脚本已部署到 `/root/contamcal-irt-calibration/exp006/run_stratified_irt.py`，输出目录 `/root/autodl-tmp/exp006/results_stratified_irt/`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_stratified-irt-design_20260515T134139"
}
```

</details>

---
