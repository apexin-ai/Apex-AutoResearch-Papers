# debug p0 exposure matrix

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 0
- **Tool calls:** 25
- **Original source:** `logs/chats/worker_debug_p0_exposure_matrix_20260514T184603.jsonl`
- **Structured JSON:** [`c1be0400405634eee65c.json`](../../sessions/c1/c1be0400405634eee65c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

51 recorded events

### Tool call

_source line 1 · 2026-05-14T18:49:53.240029+00:00_

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
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
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

_source line 2 · 2026-05-14T18:49:53.245639+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "ToolSearch",
  "elapsed_ms": 5
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T18:49:53.245958+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/exp006/results_05B_gsm8k/ -type f -name \"*.json\" -o -name \"*.csv\" -o -name \"*.npy\" -o -name \"*.pkl\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/autodl-tmp/exp006/results_05B_gsm8k/ -type f -name \"*.json\" -o -name \"*.csv\" -o -name \"*.npy\" -o -name \"*.pkl\""
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T18:49:53.246186+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -n \"exposure\" /root/contamcal-irt-calibration/exp006/run_exp006.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -n \"exposure\" /root/contamcal-irt-calibration/exp006/run_exp006.py"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T18:49:53.246419+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -n \"exposure\" /root/contamcal-irt-calibration/exp006/joint_fit.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -n \"exposure\" /root/contamcal-irt-calibration/exp006/joint_fit.py"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T18:49:53.246641+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp006/results_05B_gsm8k/gsm8k/irt_4pl_gamma.json\\n/root/autodl-tmp/exp006/results_05B_gsm8k/gsm8k/baselines.json\\n/root/autodl-tmp/exp006/results_05B_gsm8k/gsm8k/ground_truth.json\\n/root/autodl-tmp/exp006/results_05B_gsm8k/gsm8k/evaluation.json\\n/root/autodl-tmp/exp006/results_05B_gsm8k/joint_fit/joint_fit_results.json\\n/root/autodl-tmp/exp006/results_05B_gsm8k/exp006_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.7}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T18:49:53.246847+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -n \"exposure\" /root/contamcal-irt-calibration/exp006/run_irt_calibration.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -n \"exposure\" /root/contamcal-irt-calibration/exp006/run_irt_calibration.py"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T18:49:53.247080+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"4:Loads exp-001 eval results and exp-002/003 exposure scores,\\n29:    load_exposure_scores,\\n30:    build_exposure_matrix,\\n113:    exposure_scores = load_exposure_scores(\\n114:        args.exposure_file, data[\\\"benchmarks\\\"], model_id=args.tau_model_id)\\n151:        print(f\\\"[DRY-RUN] Exposure file: {args.exposure_file or 'None (oracle dosage)'}\\\")\\n176:        tau = exposure_scores[bench]\\n195:            exposure_matrix = build_exposure_matrix(signal_scores, tau[:n_items])\\n196:            log.info(\\\"Using exp-002 signals as exposure: %s\\\", signal_scores.tolist())\\n198:            exposure_matrix = build_exposure_matrix(dosages_bench, tau[:n_items])\\n207:            exposure_fit = exposure_matrix[:, item_idx]\\n210:            exposure_fit = exposure_matrix\\n228:                bench, responses_fit, exposure_fit,\\n257:                responses_fit, exposure_fit,\\n344:            args.eval_dir, args.exposure_file, str(joint_dir),\\n390:        \\\"--exposure-file\\\", type=str, default=None,\\n391:        help=\\\"exp-002/003 exposure scores JSON \\\"\\n395:        help=\\\"Model ID for exposure tau (e.g. Qwen2.5-0.5B_d100_s42)\\\")\\n396:    # D023: exp-002 signal-based exposure\\n400:             \\\"signals instead of oracle dosage for exposure (D023)\\\")\\n402:        \\\"--tau-source\\\", type=str, default=\\\"exposure\\\",\\n403:        choices=[\\\"exposure\\\", \\\"oracle\\\", \\\"aggregated\\\"],\\n404:        help=\\\"Tau source type (default: exposure)\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T18:49:53.254604+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"4:Concatenates per-benchmark response/exposure matrices into a single\\n8:Input: same as run_irt_calibration (eval-dir + exposure-file)\\n25:    load_exposure_scores,\\n26:    build_exposure_matrix,\\n40:def concatenate_benchmarks(data, exposure_scores, benchmarks=None,\\n42:    \\\"\\\"\\\"Concatenate all benchmark data into a single response/exposure matrix.\\n46:        exposure_scores: per-benchmark tau vectors\\n52:        dict with y, exposure, dosages, benchmark_slices, valid_models\\n59:    all_exposure = []\\n69:        tau = exposure_scores[bench]\\n79:        exposure_matrix = build_exposure_matrix(dosages_valid, tau[:n_items])\\n86:            exposure_matrix = exposure_matrix[:, idx]\\n92:        all_exposure.append(exposure_matrix)\\n97:    exp_concat = np.concatenate(all_exposure, axis=1)\\n101:        \\\"exposure\\\": exp_concat,\\n108:def run_joint_fit(eval_dir, exposure_file, output_dir, benchmarks=None,\\n121:    exposure_scores = load_exposure_scores(exposure_file, data[\\\"benchmarks\\\"], model_id=tau_model_id)\\n123:    concat = concatenate_benchmarks(data, exposure_scores, benchmarks,\\n127:    exposure = concat[\\\"exposure\\\"]\\n131:    stan_data = prepare_stan_data(y, exposure)\\n219:    parser.add_argument(\\\"--exposure-file\\\", type=str, default=None)\\n221:                        help=\\\"Model ID for exposure tau (e.g. Qwen2.5-0.5B_d100_s42)\\\")\\n222:    parser.add_argument(\\\"--tau-source\\\", type=str, default=\\\"exposure\\\",\\n223:                        choices=[\\\"exposure\\\", \\\"oracle\\\", \\\"aggregated\\\"],\\n224:                        help=\\\"Tau source type (default: exposure)\\\")\\n247:        args.eval_dir, args.exposure_file, args.output_dir,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 8
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T18:49:53.255102+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"7:  - Exposure matrix (N_models x N_items): continuous exposure scores\\n9:  - eval-dir with per-model eval results + per-benchmark exposure scores\\n13:  - Calibrated scores (exposure=0 counterfactual) with 50/80/95% CIs\\n152:def load_exposure_scores(exposure_file, benchmarks_data, model_id=None):\\n153:    \\\"\\\"\\\"Load per-benchmark per-item exposure scores tau.\\n160:    if exposure_file and os.path.exists(exposure_file):\\n161:        with open(exposure_file) as f:\\n166:            if \\\"exposure_scores\\\" in first_val:\\n167:                raw = {k: v[\\\"exposure_scores\\\"] for k, v in raw.items()}\\n172:                            f\\\"model_id '{model_id}' not found in exposure file. \\\"\\n177:                        f\\\"Nested exposure format with models {list(raw.keys())}. \\\"\\n180:                if isinstance(inner_val, dict) and \\\"exposure_scores\\\" in inner_val:\\n181:                    raw = {b: d[\\\"exposure_scores\\\"] for b, d in model_data.items()}\\n185:        exposure = {}\\n188:                exposure[bench] = np.array(raw[bench], dtype=float)\\n190:                exposure[bench] = np.ones(benchmarks_data[bench][\\\"n_items\\\"])\\n191:        return exposure\\n195:def build_exposure_matrix(dosages, tau):\\n196:    \\\"\\\"\\\"Build exposure matrix: exposure[i,j] = dosage[i] * tau[j] / max_dosage.\\\"\\\"\\\"\\n203:def prepare_stan_data(y, exposure, model_type=\\\"4pl_gamma\\\"):\\n212:        data[\\\"exposure\\\"] = exposure.tolist()\\n372:def run_benchmark_fit(bench_name, y, exposure, model_type, args, **kwargs):\\n380:    stan_data = prepare_stan_data(y, exposure, model_type)\\n436:    input_g.add_argument(\\\"--exposure-matrix\\\", type=str,\\n437:                         help=\\\"Direct path to exposure matrix (npy/csv/json)\\\")\\n442:    parser.add_argument(\\\"--exposure-file\\\", type=str, default=None,\\n443:                        help=\\\"JSON with per-be
…[truncated 1419 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 8
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T18:49:53.255504+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -60 /root/autodl-tmp/exp006/results_05B_gsm8k/exp006_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -60 /root/autodl-tmp/exp006/results_05B_gsm8k/exp006_results.json"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T18:49:53.255835+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"metadata\\\": {\\n    \\\"eval_dir\\\": \\\"/root/autodl-tmp/exp001/eval_results\\\",\\n    \\\"model_type\\\": \\\"4pl_gamma\\\",\\n    \\\"dry_run\\\": false,\\n    \\\"models\\\": [\\n      {\\n        \\\"dirname\\\": \\\"Qwen2.5-0.5B_d000_s42_aligned\\\",\\n        \\\"model_name\\\": \\\"Qwen2.5-0.5B\\\",\\n        \\\"dosage\\\": 0,\\n        \\\"seed\\\": 42\\n      },\\n      {\\n        \\\"dirname\\\": \\\"Qwen2.5-0.5B_d005_s42_aligned\\\",\\n        \\\"model_name\\\": \\\"Qwen2.5-0.5B\\\",\\n        \\\"dosage\\\": 5,\\n        \\\"seed\\\": 42\\n      },\\n      {\\n        \\\"dirname\\\": \\\"Qwen2.5-0.5B_d025_s42_aligned\\\",\\n        \\\"model_name\\\": \\\"Qwen2.5-0.5B\\\",\\n        \\\"dosage\\\": 25,\\n        \\\"seed\\\": 42\\n      },\\n      {\\n        \\\"dirname\\\": \\\"Qwen2.5-0.5B_d100_s42_aligned\\\",\\n        \\\"model_name\\\": \\\"Qwen2.5-0.5B\\\",\\n        \\\"dosage\\\": 100,\\n        \\\"seed\\\": 42\\n      }\\n    ],\\n    \\\"dosages\\\": [\\n      0,\\n      5,\\n      25,\\n      100\\n    ],\\n    \\\"benchmarks\\\": [\\n      \\\"gsm8k\\\"\\n    ],\\n    \\\"signals_dir\\\": \\\"/root/autodl-tmp/exp002/signals\\\"\\n  },\\n  \\\"total_time_sec\\\": 799.3,\\n  \\\"benchmarks\\\": {\\n    \\\"gsm8k\\\": {\\n      \\\"n_models\\\": 4,\\n      \\\"n_items\\\": 1319,\\n      \\\"dosages\\\": [\\n        0,\\n        5,\\n        25,\\n        100\\n      ],\\n      \\\"mean_raw_accuracy\\\": 0.3658,\\n      \\\"irt\\\": {\\n        \\\"benchmark\\\": \\\"gsm8k\\\",\\n        \\\"model_type\\\": \\\"4pl_gamma\\\",\\n        \\\"method\\\": \\\"nuts\\\",\\n        \\\"stan_file\\\": \\\"contam_irt_4pl_simple.stan\\\",\\n        \\\"n_models\\\": 4,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T18:49:53.256150+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -60 /root/autodl-tmp/exp006/results_05B_gsm8k/joint_fit/joint_fit_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -60 /root/autodl-tmp/exp006/results_05B_gsm8k/joint_fit/joint_fit_results.json"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T18:49:53.262378+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"joint_fit\\\",\\n  \\\"model_type\\\": \\\"4pl_gamma_joint\\\",\\n  \\\"n_models\\\": 4,\\n  \\\"n_total_items\\\": 1319,\\n  \\\"benchmark_slices\\\": {\\n    \\\"gsm8k\\\": [\\n      0,\\n      1319\\n    ]\\n  },\\n  \\\"fit_time_sec\\\": 190.6,\\n  \\\"diagnostics\\\": {\\n    \\\"max_rhat\\\": 1.0081,\\n    \\\"rhat_ok\\\": true,\\n    \\\"min_ess\\\": 956.4,\\n    \\\"ess_ok\\\": true,\\n    \\\"divergent_count\\\": 0,\\n    \\\"divergent_pct\\\": 0.0,\\n    \\\"divergent_ok\\\": true,\\n    \\\"total_draws\\\": 4000,\\n    \\\"all_ok\\\": true\\n  },\\n  \\\"posterior_predictive\\\": {\\n    \\\"overall_ppp\\\": 0.6038,\\n    \\\"obs_mean_acc\\\": 0.3658,\\n    \\\"pred_mean_acc\\\": 0.3706,\\n    \\\"residual_mae\\\": 0.0102\\n  },\\n  \\\"global_gamma\\\": {\\n    \\\"mean\\\": 0.3463,\\n    \\\"sd\\\": 0.52,\\n    \\\"q025\\\": -0.6526,\\n    \\\"q975\\\": 1.3994,\\n    \\\"q10\\\": -0.292,\\n    \\\"q90\\\": 1.0243,\\n    \\\"q25\\\": -0.0,\\n    \\\"q75\\\": 0.6772,\\n    \\\"ci_excludes_zero\\\": false\\n  },\\n  \\\"calibrated_scores_joint\\\": {\\n    \\\"mean\\\": [\\n      0.3806,\\n      0.375,\\n      0.3723,\\n      0.3546\\n    ],\\n    \\\"sd\\\": [\\n      0.0111,\\n      0.0118,\\n      0.0177,\\n      0.0425\\n    ],\\n    \\\"q025\\\": [\\n      0.3586,\\n      0.3521,\\n      0.3383,\\n      0.2778\\n    ],\\n    \\\"q975\\\": [\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 6
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T18:49:53.262858+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat -n /root/contamcal-irt-calibration/exp006/run_exp006.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat -n /root/contamcal-irt-calibration/exp006/run_exp006.py"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T18:49:53.263477+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"     1\\t\\\"\\\"\\\"\\n     2\\texp-006 end-to-end pipeline: IRT calibration + 7 baselines + evaluation.\\n     3\\t\\n     4\\tLoads exp-001 eval results and exp-002/003 exposure scores,\\n     5\\truns IRT 4PL+gamma calibration and all baselines per benchmark,\\n     6\\tevaluates against ground-truth clean scores (dosage=0 models).\\n     7\\t\\n     8\\tUsage:\\n     9\\t    python run_exp006.py --help\\n    10\\t    python run_exp006.py --dry-run --skip-stan --max-items 20    # quick test\\n    11\\t    python run_exp006.py                                         # full run\\n    12\\t\\n    13\\tDependencies: cmdstanpy, numpy, scipy\\n    14\\t\\\"\\\"\\\"\\n    15\\t\\n    16\\timport argparse\\n    17\\timport json\\n    18\\timport logging\\n    19\\timport os\\n    20\\timport sys\\n    21\\timport time\\n    22\\tfrom pathlib import Path\\n    23\\t\\n    24\\timport numpy as np\\n    25\\t\\n    26\\tsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\\n    27\\tfrom run_irt_calibration import (\\n    28\\t    load_eval_results,\\n    29\\t    load_exposure_scores,\\n    30\\t    build_exposure_matrix,\\n    31\\t    run_benchmark_fit,\\n    32\\t    STAN_MODELS,\\n    33\\t)\\n    34\\tfrom baselines import run_all_baselines\\n    35\\tfrom evaluate_calibration import (\\n    36\\t    evaluate_method,\\n    37\\t    format_text_table,\\n    38\\t    format_latex_table,\\n    39\\t)\\n    40\\tfrom joint_fit import run_joint_fit\\n    41\\t\\n    42\\tlog = logging.getLogger(__name__)\\n    43\\t\\n    44\\t# D018: 3B GSM8K excluded from dose-response analysis\\n    45\\tD018_EXCLUDE = [(\\\"3B\\\", \\\"gsm8k\\\")]\\n    46\\t\\n    47\\t\\n    48\\tdef should_exclude_dose_response(model_name, benchmark, rules=D018_EXCLUDE):\\n    49\\t    \\\"\\\"\\\"Check D018 exclusion rules for dose-response analysis.\\\"\\\"\\\"\\n    50\\t    for pattern, bench in rules:\\n    51\\t        if patte
…[truncated 7486 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T18:49:53.263766+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat -n /root/contamcal-irt-calibration/exp006/joint_fit.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat -n /root/contamcal-irt-calibration/exp006/joint_fit.py"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T18:49:53.264273+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"     1\\t\\\"\\\"\\\"\\n     2\\tJoint IRT fitting: shared global gamma across all benchmarks (ABLATION).\\n     3\\t\\n     4\\tConcatenates per-benchmark response/exposure matrices into a single\\n     5\\t(N_models, sum_N_items) matrix and fits one 4PL+gamma model.\\n     6\\tThe resulting gamma is the global contamination effect.\\n     7\\t\\n     8\\tInput: same as run_irt_calibration (eval-dir + exposure-file)\\n     9\\tOutput: single gamma posterior, per-model calibrated scores (across all items)\\n    10\\t\\\"\\\"\\\"\\n    11\\t\\n    12\\timport argparse\\n    13\\timport json\\n    14\\timport logging\\n    15\\timport os\\n    16\\timport sys\\n    17\\timport time\\n    18\\tfrom pathlib import Path\\n    19\\t\\n    20\\timport numpy as np\\n    21\\t\\n    22\\tsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\\n    23\\tfrom run_irt_calibration import (\\n    24\\t    load_eval_results,\\n    25\\t    load_exposure_scores,\\n    26\\t    build_exposure_matrix,\\n    27\\t    prepare_stan_data,\\n    28\\t    fit_stan_model,\\n    29\\t    check_convergence,\\n    30\\t    posterior_predictive_check,\\n    31\\t    extract_results,\\n    32\\t    _summarize_vector,\\n    33\\t)\\n    34\\t\\n    35\\tlog = logging.getLogger(__name__)\\n    36\\t\\n    37\\tSTAN_MODEL = \\\"/root/contamcal-irt-calibration/stan_models/contam_irt_4pl_simple.stan\\\"\\n    38\\t\\n    39\\t\\n    40\\tdef concatenate_benchmarks(data, exposure_scores, benchmarks=None,\\n    41\\t                           exclude_rules=None, max_items=None, seed=42):\\n    42\\t    \\\"\\\"\\\"Concatenate all benchmark data into a single response/exposure matrix.\\n    43\\t\\n    44\\t    Args:\\n    45\\t        data: output of load_eval_results\\n    46\\t        exposure_scores: per-benchmark tau vectors\\n    47\\t        benchmarks: subset of benchmarks to include (None=all)\\n    48\\t        exclude_rules: list
…[truncated 7483 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T18:49:53.271388+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -370 /root/contamcal-irt-calibration/exp006/run_exp006.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -370 /root/contamcal-irt-calibration/exp006/run_exp006.py"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T18:49:53.271956+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nexp-006 end-to-end pipeline: IRT calibration + 7 baselines + evaluation.\\n\\nLoads exp-001 eval results and exp-002/003 exposure scores,\\nruns IRT 4PL+gamma calibration and all baselines per benchmark,\\nevaluates against ground-truth clean scores (dosage=0 models).\\n\\nUsage:\\n    python run_exp006.py --help\\n    python run_exp006.py --dry-run --skip-stan --max-items 20    # quick test\\n    python run_exp006.py                                         # full run\\n\\nDependencies: cmdstanpy, numpy, scipy\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport sys\\nimport time\\nfrom pathlib import Path\\n\\nimport numpy as np\\n\\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\\nfrom run_irt_calibration import (\\n    load_eval_results,\\n    load_exposure_scores,\\n    build_exposure_matrix,\\n    run_benchmark_fit,\\n    STAN_MODELS,\\n)\\nfrom baselines import run_all_baselines\\nfrom evaluate_calibration import (\\n    evaluate_method,\\n    format_text_table,\\n    format_latex_table,\\n)\\nfrom joint_fit import run_joint_fit\\n\\nlog = logging.getLogger(__name__)\\n\\n# D018: 3B GSM8K excluded from dose-response analysis\\nD018_EXCLUDE = [(\\\"3B\\\", \\\"gsm8k\\\")]\\n\\n\\ndef should_exclude_dose_response(model_name, benchmark, rules=D018_EXCLUDE):\\n    \\\"\\\"\\\"Check D018 exclusion rules for dose-response analysis.\\\"\\\"\\\"\\n    for pattern, bench in rules:\\n        if pattern in model_name and benchmark == bench:\\n            return True\\n    return False\\n\\n\\ndef compute_ground_truth(responses, dosages):\\n    \\\"\\\"\\\"Ground truth = accuracy of dosage-0 models (uncontaminated).\\n\\n    For dosage-0 models, raw accuracy IS the clean accuracy.\\n    For dosage>0 models, we use the mean d=0 accuracy as the\\n    counterfactual reference (what they would score without contamination).\\n    \\\"\\\"\\\"\\n    raw_acc 
…[truncated 7190 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T18:49:53.272232+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -n \"signal\" /root/contamcal-irt-calibration/exp006/joint_fit.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -n \"signal\" /root/contamcal-irt-calibration/exp006/joint_fit.py"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-14T18:49:53.276561+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat -n /root/contamcal-irt-calibration/exp006/run_irt_calibration.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat -n /root/contamcal-irt-calibration/exp006/run_irt_calibration.py"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-14T18:49:53.276794+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T18:49:53.277265+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"     1\\t\\\"\\\"\\\"\\n     2\\tIRT calibration for contamination-aware benchmark score correction.\\n     3\\tFits 4PL+gamma IRT model via CmdStanPy MCMC (NUTS) per benchmark.\\n     4\\t\\n     5\\tInput:\\n     6\\t  - Correctness matrix (N_models x N_items): binary 0/1\\n     7\\t  - Exposure matrix (N_models x N_items): continuous exposure scores\\n     8\\t  OR\\n     9\\t  - eval-dir with per-model eval results + per-benchmark exposure scores\\n    10\\t\\n    11\\tOutput (per benchmark):\\n    12\\t  - Posterior: gamma, theta, item params (a, b, c, d)\\n    13\\t  - Calibrated scores (exposure=0 counterfactual) with 50/80/95% CIs\\n    14\\t  - Convergence diagnostics (Rhat, ESS, divergences)\\n    15\\t  - Posterior predictive checks\\n    16\\t\\n    17\\tDependencies: cmdstanpy (CmdStan 2.38+), numpy, scipy\\n    18\\t\\\"\\\"\\\"\\n    19\\t\\n    20\\timport argparse\\n    21\\timport json\\n    22\\timport logging\\n    23\\timport os\\n    24\\timport re\\n    25\\timport sys\\n    26\\timport time\\n    27\\tfrom pathlib import Path\\n    28\\t\\n    29\\timport numpy as np\\n    30\\timport cmdstanpy\\n    31\\t\\n    32\\tlog = logging.getLogger(__name__)\\n    33\\t\\n    34\\tSCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))\\n    35\\tSTAN_MODEL_DIR = \\\"/root/contamcal-irt-calibration/stan_models\\\"\\n    36\\tSTAN_MODELS = {\\n    37\\t    \\\"4pl_gamma\\\": os.path.join(STAN_MODEL_DIR, \\\"contam_irt_4pl_simple.stan\\\"),\\n    38\\t    \\\"2pl_gamma\\\": os.path.join(STAN_MODEL_DIR, \\\"contam_irt_2pl_gamma.stan\\\"),\\n    39\\t    \\\"vanilla_4pl\\\": os.path.join(STAN_MODEL_DIR, \\\"vanilla_4pl.stan\\\"),\\n    40\\t}\\n    41\\t\\n    42\\tDOSAGE_PATTERN = re.compile(r\\\"_d(\\\\d+)_s(\\\\d+)(_para)?(_aligned)?$\\\")\\n    43\\t\\n    44\\t\\n    45\\t# ── Data Loading ──\\n    46\\t\\n    47\\tdef parse_model_dir_name(dirname):\\n    48\\t    \\\"\\\"\\\"Extract model name
…[truncated 7463 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T18:49:53.277627+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -260 /root/contamcal-irt-calibration/exp006/run_exp006.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -260 /root/contamcal-irt-calibration/exp006/run_exp006.py"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T18:49:53.278065+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nexp-006 end-to-end pipeline: IRT calibration + 7 baselines + evaluation.\\n\\nLoads exp-001 eval results and exp-002/003 exposure scores,\\nruns IRT 4PL+gamma calibration and all baselines per benchmark,\\nevaluates against ground-truth clean scores (dosage=0 models).\\n\\nUsage:\\n    python run_exp006.py --help\\n    python run_exp006.py --dry-run --skip-stan --max-items 20    # quick test\\n    python run_exp006.py                                         # full run\\n\\nDependencies: cmdstanpy, numpy, scipy\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport sys\\nimport time\\nfrom pathlib import Path\\n\\nimport numpy as np\\n\\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\\nfrom run_irt_calibration import (\\n    load_eval_results,\\n    load_exposure_scores,\\n    build_exposure_matrix,\\n    run_benchmark_fit,\\n    STAN_MODELS,\\n)\\nfrom baselines import run_all_baselines\\nfrom evaluate_calibration import (\\n    evaluate_method,\\n    format_text_table,\\n    format_latex_table,\\n)\\nfrom joint_fit import run_joint_fit\\n\\nlog = logging.getLogger(__name__)\\n\\n# D018: 3B GSM8K excluded from dose-response analysis\\nD018_EXCLUDE = [(\\\"3B\\\", \\\"gsm8k\\\")]\\n\\n\\ndef should_exclude_dose_response(model_name, benchmark, rules=D018_EXCLUDE):\\n    \\\"\\\"\\\"Check D018 exclusion rules for dose-response analysis.\\\"\\\"\\\"\\n    for pattern, bench in rules:\\n        if pattern in model_name and benchmark == bench:\\n            return True\\n    return False\\n\\n\\ndef compute_ground_truth(responses, dosages):\\n    \\\"\\\"\\\"Ground truth = accuracy of dosage-0 models (uncontaminated).\\n\\n    For dosage-0 models, raw accuracy IS the clean accuracy.\\n    For dosage>0 models, we use the mean d=0 accuracy as the\\n    counterfactual reference (what they would score without contamination).\\n    \\\"\\\"\\\"\\n    raw_acc 
…[truncated 7103 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T18:49:53.282218+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -n -A 10 \"def build_exposure_matrix\" /root/contamcal-irt-calibration/exp006/run_irt_calibration.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -n -A 10 \"def build_exposure_matrix\" /root/contamcal-irt-calibration/exp006/run_irt_calibration.py"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T18:49:53.282564+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"195:def build_exposure_matrix(dosages, tau):\\n196-    \\\"\\\"\\\"Build exposure matrix: exposure[i,j] = dosage[i] * tau[j] / max_dosage.\\\"\\\"\\\"\\n197-    max_d = dosages.max() if dosages.max() > 0 else 1.0\\n198-    return np.outer(dosages / max_d, tau)\\n199-\\n200-\\n201-# ── Stan Fitting ──\\n202-\\n203-def prepare_stan_data(y, exposure, model_type=\\\"4pl_gamma\\\"):\\n204-    \\\"\\\"\\\"Prepare data dict for Stan model.\\\"\\\"\\\"\\n205-    N_models, N_items = y.shape\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T18:49:53.282818+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -n -A 15 \"def prepare_stan_data\" /root/contamcal-irt-calibration/exp006/run_irt_calibration.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -n -A 15 \"def prepare_stan_data\" /root/contamcal-irt-calibration/exp006/run_irt_calibration.py"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T18:49:53.283073+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"203:def prepare_stan_data(y, exposure, model_type=\\\"4pl_gamma\\\"):\\n204-    \\\"\\\"\\\"Prepare data dict for Stan model.\\\"\\\"\\\"\\n205-    N_models, N_items = y.shape\\n206-    data = {\\n207-        \\\"N_models\\\": int(N_models),\\n208-        \\\"N_items\\\": int(N_items),\\n209-        \\\"y\\\": y.astype(int).tolist(),\\n210-    }\\n211-    if model_type != \\\"vanilla_4pl\\\":\\n212-        data[\\\"exposure\\\"] = exposure.tolist()\\n213-    return data\\n214-\\n215-\\n216-def fit_stan_model(stan_file, stan_data, chains=4, iter_warmup=1000,\\n217-                   iter_sampling=1000, adapt_delta=0.95, max_treedepth=12,\\n218-                   seed=42):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T18:49:53.283407+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "python3 -c \"\nimport json, numpy as np, os, sys\nsys.path.insert(0, '/root/contamcal-irt-calibration/exp006')\nfrom run_irt_calibration import load_eval_results, load_exposure_scores, build_exposure_matrix\nfrom run_exp006 import load_exp002_signals\n\n# Load data\ndata = load_eval_results('/root/autodl-tmp/exp001/eval_results', ['gsm8k'],\n                         model_scale='0.5B', seed_filter=42, aligned_only=True)\nexposure_scores = load_exposure_scores(None, data['benchmarks'])\ndosages = data['dosages']\nbench_data = data['benchmarks']['gsm8k']\ntau = exposure_scores['gsm8k']\nn_items = bench_data['n_items']\n\nprint('=== BASIC INFO ===')\nprint(f'Models: {[m[\\\"dirname\\\"] for m in data[\\\"models\\\"]]}')\nprint(f'Oracle dosages: {dosages}')\nprint(f'N items: {n_items}')\nprint(f'Tau shape: {tau.shape}')\nprint(f'Tau stats: min={tau.min():.4f} max={tau.max():.4f} mean={tau.mean():.4f}')\nprint(f'Tau[:10]: {tau[:10]}')\n\n# Joint-fit exposure (uses oracle dosages)\nexp_joint = build_exposure_matrix(dosages, tau[:n_items])\nprint()\nprint('=== JOINT-FIT EXPOSURE (oracle dosages) ===')\nprint(f'Shape: {exp_joint.shape}')\nprint(f'Per-model rows (first 10 cols):')\nfor i, m in enumerate(data['models']):\n    print(f'  {m[\\\"dirname\\\"]}: {exp_joint[i,:10]}')\nprint(f'Stats: min={exp_joint.min():.6f} max={exp_joint.max():.6f} mean={exp_joint.mean():.6f}')\n\n# Per-benchmark exposure (uses signal scores)\nsignals_dir = '/root/autodl-tmp/exp002/signals'\nsignal_scores = load_exp002_signals(signals_dir, data['models'], 'gsm8k')\nexp_perbench = build_exposure_matrix(signal_scores, tau[:n_items])\nprint()\nprint('=== PER-BENCHMARK EXPOSURE (signal scores) ===')\nprint(f'Signal scores: {signal_scores}')\nprint(f'Shape: {exp_perbench.shape}')\nprint(f'Per-model rows (first 10 cols):')\nfor i, m in enumerate(data['models']):\n    print(f'  {m[\\\"dirname\\\"]}: {exp_perbench[i,:10]}')\nprint(f'Stats: min={exp_perbench.min():.6f} max={exp_perbench.max():.6f} mean={exp_perbench.mean():.6f}')\n\n# Comparison\nprint()\nprint('=== COMPARISON ===')\ndiff = exp_perbench - exp_joint\nprint(f'Max absolute diff: {np.abs(diff).max():.6f}')\nprint(f'Mean absolute diff: {np.abs(diff).mean():.6f}')\nprint(f'Are they identical? {np.allclose(exp_perbench, exp_joint)}')\nprint(f'Normalized dosages (joint):  {dosages / dosages.max()}')\nprint(f'Normalized signals (per-bm): {signal_scores / signal_scores.max() if signal_scores.max() > 0 else signal_scores}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "python3 -c \"\nimport json, numpy as np, os, sys\nsys.path.insert(0, '/root/contamcal-irt-calibration/exp006')\nfrom run_irt_calibration import load_eval_results, load_exposure_scores, build_exposure_matrix\nfrom run_exp006 import load_exp002_signals\n\n# Load data\ndata = load_eval_results('/root/autodl-tmp/exp001/eval_results', ['gsm8k'],\n                         model_scale='0.5B', seed_filter=42, aligned_only=True)\nexposure_scores = load_exposure_scores(None, data['benchmarks'])\ndosages = data['dosages']\nbench_data = data['benchmarks']['gsm8k']\ntau = exposure_scores['gsm8k']\nn_items = bench_data['n_items']\n\nprint('=== BASIC INFO ===')\nprint(f'Models: {[m[\\\"dirname\\\"] for m in data[\\\"models\\\"]]}')\nprint(f'Oracle dosages: {dosages}')\nprint(f'N items: {n_items}')\nprint(f'Tau shape: {tau.shape}')\nprint(f'Tau stats: min={tau.min():.4f} max={tau.max():.4f} mean={tau.mean():.4f}')\nprint(f'Tau[:10]: {tau[:10]}')\n\n# Joint-fit exposure (uses oracle dosages)\nexp_joint = build_exposure_matrix(dosages, tau[:n_items])\nprint()\nprint('=== JOINT-FIT EXPOSURE (oracle dosages) ===')\nprint(f'Shape: {exp_joint.shape}')\nprint(f'Per-model rows (first 10 cols):')\nfor i, m in enumerate(data['models']):\n    print(f'  {m[\\\"dirname\\\"]}: {exp_joint[i,:10]}')\nprint(f'Stats: min={exp_joint.min():.6f} max={exp_joint.max():.6f} mean={exp_joint.mean():.6f}')\n\n# Per-benchmark exposure (uses signal scores)\nsignals_dir = '/root/autodl-tmp/exp002/signals'\nsignal_scores = load_exp002_signals(signals_dir, data['models'], 'gsm8k')\nexp_perbench = build_exposure_matrix(signal_scores, tau[:n_items])\nprint()\nprint('=== PER-BENCHMARK EXPOSURE (signal scores) ===')\nprint(f'Signal scores: {signal_scores}')\nprint(f'Shape: {exp_perbench.shape}')\nprint(f'Per-model rows (first 10 cols):')\nfor i, m in enumerate(data['models']):\n    print(f'  {m[\\\"dirname\\\"]}: {exp_perbench[i,:10]}')\nprint(f'Stats: min={exp_perbench.min():.6f} max={exp_perbench.max():.6f} mean={exp_perbench.mean():.6f}')\n\n# Comparison\nprint()\nprint('=== COMPARISON ===')\ndiff = exp_perbench - exp_joint\nprint(f'Max absolute diff: {np.abs(diff).max():.6f}')\nprint(f'Mean absolute diff: {np.abs(diff).mean():.6f}')\nprint(f'Are they identical? {np.allclose(exp_perbench, exp_joint)}')\nprint(f'Normalized dosages (joint):  {dosages / dosages.max()}')\nprint(f'Normalized signals (per-bm): {signal_scores / signal_scores.max() if signal_scores.max() > 0 else signal_scores}')\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T18:49:53.283660+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T18:49:53.283928+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cd /root/contamcal-irt-calibration && python3 -c \"\nimport json, numpy as np, os, sys\nsys.path.insert(0, '/root/contamcal-irt-calibration/exp006')\nfrom run_irt_calibration import load_eval_results, load_exposure_scores, build_exposure_matrix\nfrom run_exp006 import load_exp002_signals\n\ndata = load_eval_results('/root/autodl-tmp/exp001/eval_results', ['gsm8k'],\n                         model_scale='0.5B', seed_filter=42, aligned_only=True)\nexposure_scores = load_exposure_scores(None, data['benchmarks'])\ndosages = data['dosages']\nbench_data = data['benchmarks']['gsm8k']\ntau = exposure_scores['gsm8k']\nn_items = bench_data['n_items']\n\nprint('=== BASIC INFO ===')\nprint('Models:', [m['dirname'] for m in data['models']])\nprint('Oracle dosages:', dosages)\nprint('N items:', n_items)\nprint('Tau shape:', tau.shape)\nprint('Tau stats: min=%.4f max=%.4f mean=%.4f' % (tau.min(), tau.max(), tau.mean()))\nprint('Tau[:10]:', tau[:10])\n\n# Joint-fit exposure (uses oracle dosages)\nexp_joint = build_exposure_matrix(dosages, tau[:n_items])\nprint()\nprint('=== JOINT-FIT EXPOSURE (oracle dosages) ===')\nprint('Shape:', exp_joint.shape)\nprint('Per-model rows (first 10 cols):')\nfor i, m in enumerate(data['models']):\n    print('  %s: %s' % (m['dirname'], exp_joint[i,:10]))\nprint('Stats: min=%.6f max=%.6f mean=%.6f' % (exp_joint.min(), exp_joint.max(), exp_joint.mean()))\n\n# Per-benchmark exposure (uses signal scores)\nsignals_dir = '/root/autodl-tmp/exp002/signals'\nsignal_scores = load_exp002_signals(signals_dir, data['models'], 'gsm8k')\nexp_perbench = build_exposure_matrix(signal_scores, tau[:n_items])\nprint()\nprint('=== PER-BENCHMARK EXPOSURE (signal scores) ===')\nprint('Signal scores:', signal_scores)\nprint('Shape:', exp_perbench.shape)\nprint('Per-model rows (first 10 cols):')\nfor i, m in enumerate(data['models']):\n    print('  %s: %s' % (m['dirname'], exp_perbench[i,:10]))\nprint('Stats: min=%.6f max=%.6f mean=%.6f' % (exp_perbench.min(), exp_perbench.max(), exp_perbench.mean()))\n\n# Comparison\nprint()\nprint('=== COMPARISON ===')\ndiff = exp_perbench - exp_joint\nprint('Max absolute diff: %.6f' % np.abs(diff).max())\nprint('Mean absolute diff: %.6f' % np.abs(diff).mean())\nprint('Are identical:', np.allclose(exp_perbench, exp_joint))\nnorm_dosages = dosages / dosages.max()\nnorm_signals = signal_scores / signal_scores.max() if signal_scores.max() != 0 else signal_scores\nprint('Normalized dosages (joint): ', norm_dosages)\nprint('Normalized signals (per-bm):', norm_signals)\nprint()\nprint('=== ROW-BY-ROW (per-model exposure row norm) ===')\nfor i, m in enumerate(data['models']):\n    j_norm = np.linalg.norm(exp_joint[i])\n    p_norm = np.linalg.norm(exp_perbench[i])\n    print('  %s: joint_norm=%.6f  perbench_norm=%.6f  ratio=%.4f' % (m['dirname'], j_norm, p_norm, p_norm/(j_norm+1e-12)))\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cd /root/contamcal-irt-calibration && python3 -c \"\nimport json, numpy as np, os, sys\nsys.path.insert(0, '/root/contamcal-irt-calibration/exp006')\nfrom run_irt_calibration import load_eval_results, load_exposure_scores, build_exposure_matrix\nfrom run_exp006 import load_exp002_signals\n\ndata = load_eval_results('/root/autodl-tmp/exp001/eval_results', ['gsm8k'],\n                         model_scale='0.5B', seed_filter=42, aligned_only=True)\nexposure_scores = load_exposure_scores(None, data['benchmarks'])\ndosages = data['dosages']\nbench_data = data['benchmarks']['gsm8k']\ntau = exposure_scores['gsm8k']\nn_items = bench_data['n_items']\n\nprint('=== BASIC INFO ===')\nprint('Models:', [m['dirname'] for m in data['models']])\nprint('Oracle dosages:', dosages)\nprint('N items:', n_items)\nprint('Tau shape:', tau.shape)\nprint('Tau stats: min=%.4f max=%.4f mean=%.4f' % (tau.min(), tau.max(), tau.mean()))\nprint('Tau[:10]:', tau[:10])\n\n# Joint-fit exposure (uses oracle dosages)\nexp_joint = build_exposure_matrix(dosages, tau[:n_items])\nprint()\nprint('=== JOINT-FIT EXPOSURE (oracle dosages) ===')\nprint('Shape:', exp_joint.shape)\nprint('Per-model rows (first 10 cols):')\nfor i, m in enumerate(data['models']):\n    print('  %s: %s' % (m['dirname'], exp_joint[i,:10]))\nprint('Stats: min=%.6f max=%.6f mean=%.6f' % (exp_joint.min(), exp_joint.max(), exp_joint.mean()))\n\n# Per-benchmark exposure (uses signal scores)\nsignals_dir = '/root/autodl-tmp/exp002/signals'\nsignal_scores = load_exp002_signals(signals_dir, data['models'], 'gsm8k')\nexp_perbench = build_exposure_matrix(signal_scores, tau[:n_items])\nprint()\nprint('=== PER-BENCHMARK EXPOSURE (signal scores) ===')\nprint('Signal scores:', signal_scores)\nprint('Shape:', exp_perbench.shape)\nprint('Per-model rows (first 10 cols):')\nfor i, m in enumerate(data['models']):\n    print('  %s: %s' % (m['dirname'], exp_perbench[i,:10]))\nprint('Stats: min=%.6f max=%.6f mean=%.6f' % (exp_perbench.min(), exp_perbench.max(), exp_perbench.mean()))\n\n# Comparison\nprint()\nprint('=== COMPARISON ===')\ndiff = exp_perbench - exp_joint\nprint('Max absolute diff: %.6f' % np.abs(diff).max())\nprint('Mean absolute diff: %.6f' % np.abs(diff).mean())\nprint('Are identical:', np.allclose(exp_perbench, exp_joint))\nnorm_dosages = dosages / dosages.max()\nnorm_signals = signal_scores / signal_scores.max() if signal_scores.max() != 0 else signal_scores\nprint('Normalized dosages (joint): ', norm_dosages)\nprint('Normalized signals (per-bm):', norm_signals)\nprint()\nprint('=== ROW-BY-ROW (per-model exposure row norm) ===')\nfor i, m in enumerate(data['models']):\n    j_norm = np.linalg.norm(exp_joint[i])\n    p_norm = np.linalg.norm(exp_perbench[i])\n    print('  %s: joint_norm=%.6f  perbench_norm=%.6f  ratio=%.4f' % (m['dirname'], j_norm, p_norm, p_norm/(j_norm+1e-12)))\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T18:49:53.284252+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/contamcal-irt-calibration && python3 -c \\\"\\\\nimport json, numpy as np, os, sys\\\\nsys.path.insert(0, \\\\'/root/contamcal-irt-calibration/exp006\\\\')\\\\nfrom run_irt_calibration import load_eval_results, load_exposure_scores, build_exposure_matrix\\\\nfrom run_exp006 import load_exp002_signals\\\\n\\\\ndata = load_eval_results(\\\\'/root/autodl-tmp/exp001/eval_results\\\\', [\\\\'gsm8k\\\\'],\\\\n                         model_scale=\\\\'0.5B\\\\', seed_filter=42, aligned_only=True)\\\\nexposure_scores = load_exposure_scores(None, data[\\\\'benchmarks\\\\'])\\\\ndosages = data[\\\\'dosages\\\\']\\\\nbench_data = data[\\\\'benchmarks\\\\'][\\\\'gsm8k\\\\']\\\\ntau = exposure_scores[\\\\'gsm8k\\\\']\\\\nn_items = bench_data[\\\\'n_items\\\\']\\\\n\\\\nprint(\\\\'=== BASIC INFO ===\\\\')\\\\nprint(\\\\'Models:\\\\', [m[\\\\'dirname\\\\'] for m in data[\\\\'models\\\\']])\\\\nprint(\\\\'Oracle dosages:\\\\', dosages)\\\\nprint(\\\\'N items:\\\\', n_items)\\\\nprint(\\\\'Tau shape:\\\\', tau.shape)\\\\nprint(\\\\'Tau stats: min=%.4f max=%.4f mean=%.4f\\\\' % (tau.min(), tau.max(), tau.mean()))\\\\nprint(\\\\'Tau[:10]:\\\\', tau[:10])\\\\n\\\\n# Joint-fit exposure (uses oracle dosages)\\\\nexp_joint = build_exposure_matrix(dosages, tau[:n_items])\\\\nprint()\\\\nprint(\\\\'=== JOINT-FIT EXPOSURE (oracle dosages) ===\\\\')\\\\nprint(\\\\'Shape:\\\\', exp_joint.shape)\\\\nprint(\\\\'Per-model rows (first 10 cols):\\\\')\\\\nfor i, m in enumerate(data[\\\\'models\\\\']):\\\\n    print(\\\\'  %s: %s\\\\' % (m[\\\\'dirname\\\\'], exp_joint[i,:10]))\\\\nprint(\\\\'Stats: min=%.6f max=%.6f mean=%.6f\\\\' % (exp_joint.min(), exp_joint.max(), exp_joint.mean()))\\\\n\\\\n# Per-benchmark exposure (uses signal scores)\\\\nsignals_dir = \\\\'/root/autodl-tmp/exp002/signals\\\\'\\\\nsignal_scores = load_exp002_signals(signals_dir, data[\\\\'models\\\\'], \\\\'g
…[truncated 1693 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T18:49:53.288579+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/miniconda3/bin/python3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/miniconda3/bin/python3"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T18:49:53.288965+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/bin/python3\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.81}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-14T18:49:53.289186+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration && python3 /tmp/debug_exposure.py",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration && python3 /tmp/debug_exposure.py",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-14T18:49:53.289416+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"python3: can't open file '/tmp/debug_exposure.py': [Errno 2] No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.56}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-14T18:49:53.289630+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat > /tmp/debug_exposure.py << 'PYEOF'\nimport json, numpy as np, os, sys\nsys.path.insert(0, '/root/contamcal-irt-calibration/exp006')\nfrom run_irt_calibration import load_eval_results, load_exposure_scores, build_exposure_matrix\nfrom run_exp006 import load_exp002_signals\n\ndata = load_eval_results('/root/autodl-tmp/exp001/eval_results', ['gsm8k'],\n                         model_scale='0.5B', seed_filter=42, aligned_only=True)\nexposure_scores = load_exposure_scores(None, data['benchmarks'])\ndosages = data['dosages']\nbench_data = data['benchmarks']['gsm8k']\ntau = exposure_scores['gsm8k']\nn_items = bench_data['n_items']\n\nprint('=== BASIC INFO ===')\nprint('Models:', [m['dirname'] for m in data['models']])\nprint('Oracle dosages:', dosages)\nprint('N items:', n_items)\nprint('Tau shape:', tau.shape)\nprint('Tau stats: min=%.4f max=%.4f mean=%.4f' % (tau.min(), tau.max(), tau.mean()))\nprint('Tau[:10]:', tau[:10])\n\n# Joint-fit exposure (uses oracle dosages)\nexp_joint = build_exposure_matrix(dosages, tau[:n_items])\nprint()\nprint('=== JOINT-FIT EXPOSURE (oracle dosages) ===')\nprint('Shape:', exp_joint.shape)\nprint('Per-model rows (first 10 cols):')\nfor i, m in enumerate(data['models']):\n    print('  %s: %s' % (m['dirname'], exp_joint[i,:10]))\nprint('Stats: min=%.6f max=%.6f mean=%.6f' % (exp_joint.min(), exp_joint.max(), exp_joint.mean()))\n\n# Per-benchmark exposure (uses signal scores)\nsignals_dir = '/root/autodl-tmp/exp002/signals'\nsignal_scores = load_exp002_signals(signals_dir, data['models'], 'gsm8k')\nexp_perbench = build_exposure_matrix(signal_scores, tau[:n_items])\nprint()\nprint('=== PER-BENCHMARK EXPOSURE (signal scores) ===')\nprint('Signal scores:', signal_scores)\nprint('Shape:', exp_perbench.shape)\nprint('Per-model rows (first 10 cols):')\nfor i, m in enumerate(data['models']):\n    print('  %s: %s' % (m['dirname'], exp_perbench[i,:10]))\nprint('Stats: min=%.6f max=%.6f mean=%.6f' % (exp_perbench.min(), exp_perbench.max(), exp_perbench.mean()))\n\n# Comparison\nprint()\nprint('=== COMPARISON ===')\ndiff = exp_perbench - exp_joint\nprint('Max absolute diff: %.6f' % np.abs(diff).max())\nprint('Mean absolute diff: %.6f' % np.abs(diff).mean())\nprint('Are identical:', np.allclose(exp_perbench, exp_joint))\nnorm_dosages = dosages / dosages.max()\nnorm_signals = signal_scores / signal_scores.max() if signal_scores.max() != 0 else signal_scores\nprint('Normalized dosages (joint): ', norm_dosages)\nprint('Normalized signals (per-bm):', norm_signals)\nprint()\nprint('=== ROW-BY-ROW (per-model exposure row norm) ===')\nfor i, m in enumerate(data['models']):\n    j_norm = np.linalg.norm(exp_joint[i])\n    p_norm = np.linalg.norm(exp_perbench[i])\n    print('  %s: joint_norm=%.6f  perbench_norm=%.6f  ratio=%.4f' % (m['dirname'], j_norm, p_norm, p_norm/(j_norm+1e-12)))\nPYEOF\necho \"Script written\"",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat > /tmp/debug_exposure.py << 'PYEOF'\nimport json, numpy as np, os, sys\nsys.path.insert(0, '/root/contamcal-irt-calibration/exp006')\nfrom run_irt_calibration import load_eval_results, load_exposure_scores, build_exposure_matrix\nfrom run_exp006 import load_exp002_signals\n\ndata = load_eval_results('/root/autodl-tmp/exp001/eval_results', ['gsm8k'],\n                         model_scale='0.5B', seed_filter=42, aligned_only=True)\nexposure_scores = load_exposure_scores(None, data['benchmarks'])\ndosages = data['dosages']\nbench_data = data['benchmarks']['gsm8k']\ntau = exposure_scores['gsm8k']\nn_items = bench_data['n_items']\n\nprint('=== BASIC INFO ===')\nprint('Models:', [m['dirname'] for m in data['models']])\nprint('Oracle dosages:', dosages)\nprint('N items:', n_items)\nprint('Tau shape:', tau.shape)\nprint('Tau stats: min=%.4f max=%.4f mean=%.4f' % (tau.min(), tau.max(), tau.mean()))\nprint('Tau[:10]:', tau[:10])\n\n# Joint-fit exposure (uses oracle dosages)\nexp_joint = build_exposure_matrix(dosages, tau[:n_items])\nprint()\nprint('=== JOINT-FIT EXPOSURE (oracle dosages) ===')\nprint('Shape:', exp_joint.shape)\nprint('Per-model rows (first 10 cols):')\nfor i, m in enumerate(data['models']):\n    print('  %s: %s' % (m['dirname'], exp_joint[i,:10]))\nprint('Stats: min=%.6f max=%.6f mean=%.6f' % (exp_joint.min(), exp_joint.max(), exp_joint.mean()))\n\n# Per-benchmark exposure (uses signal scores)\nsignals_dir = '/root/autodl-tmp/exp002/signals'\nsignal_scores = load_exp002_signals(signals_dir, data['models'], 'gsm8k')\nexp_perbench = build_exposure_matrix(signal_scores, tau[:n_items])\nprint()\nprint('=== PER-BENCHMARK EXPOSURE (signal scores) ===')\nprint('Signal scores:', signal_scores)\nprint('Shape:', exp_perbench.shape)\nprint('Per-model rows (first 10 cols):')\nfor i, m in enumerate(data['models']):\n    print('  %s: %s' % (m['dirname'], exp_perbench[i,:10]))\nprint('Stats: min=%.6f max=%.6f mean=%.6f' % (exp_perbench.min(), exp_perbench.max(), exp_perbench.mean()))\n\n# Comparison\nprint()\nprint('=== COMPARISON ===')\ndiff = exp_perbench - exp_joint\nprint('Max absolute diff: %.6f' % np.abs(diff).max())\nprint('Mean absolute diff: %.6f' % np.abs(diff).mean())\nprint('Are identical:', np.allclose(exp_perbench, exp_joint))\nnorm_dosages = dosages / dosages.max()\nnorm_signals = signal_scores / signal_scores.max() if signal_scores.max() != 0 else signal_scores\nprint('Normalized dosages (joint): ', norm_dosages)\nprint('Normalized signals (per-bm):', norm_signals)\nprint()\nprint('=== ROW-BY-ROW (per-model exposure row norm) ===')\nfor i, m in enumerate(data['models']):\n    j_norm = np.linalg.norm(exp_joint[i])\n    p_norm = np.linalg.norm(exp_perbench[i])\n    print('  %s: joint_norm=%.6f  perbench_norm=%.6f  ratio=%.4f' % (m['dirname'], j_norm, p_norm, p_norm/(j_norm+1e-12)))\nPYEOF\necho \"Script written\"",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T18:49:53.289874+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-14T18:49:53.290098+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration && python3 /tmp/debug_exposure.py",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration && python3 /tmp/debug_exposure.py",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-14T18:49:53.292952+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== BASIC INFO ===\\nModels: ['Qwen2.5-0.5B_d000_s42_aligned', 'Qwen2.5-0.5B_d005_s42_aligned', 'Qwen2.5-0.5B_d025_s42_aligned', 'Qwen2.5-0.5B_d100_s42_aligned']\\nOracle dosages: [  0   5  25 100]\\nN items: 1319\\nTau shape: (1319,)\\nTau stats: min=1.0000 max=1.0000 mean=1.0000\\nTau[:10]: [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]\\n\\n=== JOINT-FIT EXPOSURE (oracle dosages) ===\\nShape: (4, 1319)\\nPer-model rows (first 10 cols):\\n  Qwen2.5-0.5B_d000_s42_aligned: [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]\\n  Qwen2.5-0.5B_d005_s42_aligned: [0.05 0.05 0.05 0.05 0.05 0.05 0.05 0.05 0.05 0.05]\\n  Qwen2.5-0.5B_d025_s42_aligned: [0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25]\\n  Qwen2.5-0.5B_d100_s42_aligned: [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]\\nStats: min=0.000000 max=1.000000 mean=0.325000\\n\\n=== PER-BENCHMARK EXPOSURE (signal scores) ===\\nSignal scores: [0.61312865 0.62916365 0.25       0.81032939]\\nShape: (4, 1319)\\nPer-model rows (first 10 cols):\\n  Qwen2.5-0.5B_d000_s42_aligned: [0.75664126 0.75664126 0.75664126 0.75664126 0.75664126 0.75664126\\n 0.75664126 0.75664126 0.75664126 0.75664126]\\n  Qwen2.5-0.5B_d005_s42_aligned: [0.77642951 0.77642951 0.77642951 0.77642951 0.77642951 0.77642951\\n 0.77642951 0.77642951 0.77642951 0.77642951]\\n  Qwen2.5-0.5B_d025_s42_aligned: [0.30851652 0.30851652 0.30851652 0.30851652 0.30851652 0.30851652\\n 0.30851652 0.30851652 0.30851652 0.30851652]\\n  Qwen2.5-0.5B_d100_s42_aligned: [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]\\nStats: min=0.308517 max=1.000000 mean=0.710397\\n\\n=== COMPARISON ===\\nMax absolute diff: 0.756641\\nMean absolute diff: 0.385397\\nAre identical: False\\nNormalized dosages (joint):  [0.   0.05 0.25 1.  ]\\nNormalized signals (per-bm): [0.75664126 0.77642951 0.30851652 1.        ]\\n\\n=== ROW-BY-ROW (per-model exposure row norm) ===\\n  Qwen2.5-0.5B_d000_s42_aligned: joint_norm=0.000000  perbench_norm=27.479727  ratio=27479727197648.6211\\n  Qwen2.5-0.5B_d005_s42_
…[truncated 500 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-14T18:49:53.293402+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -A 5 \"exposure_file\" /root/autodl-tmp/exp006/results_05B_gsm8k/exp006_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -A 5 \"exposure_file\" /root/autodl-tmp/exp006/results_05B_gsm8k/exp006_results.json"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-14T18:49:53.293663+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-14T18:49:53.293891+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -A 5 \"tau_source\\|signals_dir\\|exposure_file\" /root/autodl-tmp/exp006/results_05B_gsm8k/exp006_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -A 5 \"tau_source\\|signals_dir\\|exposure_file\" /root/autodl-tmp/exp006/results_05B_gsm8k/exp006_results.json"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-14T18:49:53.294098+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-14T18:49:53.294293+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep \"signals_dir\" /root/autodl-tmp/exp006/results_05B_gsm8k/exp006_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep \"signals_dir\" /root/autodl-tmp/exp006/results_05B_gsm8k/exp006_results.json"
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-14T18:49:53.296605+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep \"tau_source\" /root/autodl-tmp/exp006/results_05B_gsm8k/exp006_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep \"tau_source\" /root/autodl-tmp/exp006/results_05B_gsm8k/exp006_results.json"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-14T18:49:53.296854+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    \\\"signals_dir\\\": \\\"/root/autodl-tmp/exp002/signals\\\"\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-14T18:49:53.297085+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-14T18:49:53.297451+00:00_

排查完成。以下是完整诊断。

---

## 诊断结果

### 两个 exposure 矩阵的实际值

**Shape**: 两者均为 `(4, 1319)`

**Joint-fit（oracle dosages）**:
| Model | Normalized dosage | Exposure row (constant) |
|---|---|---|
| d000 (clean) | **0.00** | `[0, 0, 0, ..., 0]` |
| d005 | 0.05 | `[0.05, 0.05, ..., 0.05]` |
| d025 | 0.25 | `[0.25, 0.25, ..., 0.25]` |
| d100 | 1.00 | `[1, 1, ..., 1]` |

Stats: min=0, max=1, mean=0.325

**Per-benchmark（signal scores, s1_embedding）**:
| Model | Signal score | Normalized | Exposure row |
|---|---|---|---|
| d000 (clean) | 0.613 | **0.757** | `[0.757, 0.757, ..., 0.757]` |
| d005 | 0.629 | 0.776 | `[0.776, 0.776, ..., 0.776]` |
| d025 | 0.250 *(fallback)* | 0.309 | `[0.309, 0.309, ..., 0.309]` |
| d100 | 0.810 | 1.000 | `[1, 1, ..., 1]` |

Stats: min=0.309, max=1, mean=0.710

**注意**: tau 全为 1.0（未传 `--exposure-file`），所以每行是常数。

### 差异

- Max absolute diff: **0.757**
- Mean absolute diff: **0.385**
- 完全不同。

### 根本原因：两个 bug 叠加

**Bug 1（代码 bug）**: `joint_fit.py` 不支持 `signals_dir`。`run_exp006.py` 调用 `run_joint_fit()` 时没传 `signals_dir`（`run_joint_fit` 也没这个参数），所以 joint-fit 始终用 oracle dosages `[0, 5, 25, 100]`。

代码证据：
- `run_exp006.py:344` — 调用 `run_joint_fit` 无 `signals_dir` 参数
- `joint_fit.py:79` — `build_exposure_matrix(dosages_valid, tau)` 硬编码用 oracle dosage
- `joint_fit.py` 中 grep "signal" 零匹配

**Bug 2（信号质量 bug）**: s1_embedding 信号作为 per-model exposure **完全失效**：
- **d=0（clean model）得到 exposure=0.757** — 应该接近 0
- 排序紊乱：d25 (0.309) < d0 (0.757) < d5 (0.776) < d100 (1.0)，正确应为 d0 < d5 < d25 < d100
- d=25 信号文件缺失，fallback 到 `dosage/100 = 0.25`，与 signal 尺度不一致
- s1_embedding 是 item-level 检测信号，均值化为 model-level dosage proxy 语义不对

**为什么 joint-fit 收敛、per-benchmark 不收敛**: Joint-fit 用 oracle dosage，d=0 exposure 精确为 0，模型有清晰的"无污染基线"，gamma 可识别。Per-benchmark 的 d=0 exposure=0.757，Stan 模型无法区分 clean vs contaminated，gamma 失去可识别性 → Rhat=1.53, ESS=7。

### 建议修复方案

1. **短期修复**: per-benchmark 路径也用 oracle dosage（和 joint-fit 一致），不传 `--signals-dir`。这样两条路径的 exposure 矩阵一致，per-benchmark 应恢复正常收敛。

2. **中期修复**: 如果要用信号做 exposure，需要：
   - 确保 d=0 模型的信号接近 0（当前 s1_embedding 不满足）
   - 信号值与 dosage 单调递增
   - joint_fit.py 也需要同步支持 signals_dir
   - 补全 d=25 缺失的信号文件

3. **长期**: 重新评估哪个 exp-002 信号适合做 model-level dosage proxy。s1_embedding 的 mean 不是好的选择——它反映的是 embedding 相似度，不是污染程度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_debug_p0_exposure_matrix_20260514T184603"
}
```

</details>

---
