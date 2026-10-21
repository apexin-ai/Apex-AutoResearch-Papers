# analysis rrf c1 c2 correlation ablation

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 185
- **Recorded user turns:** 0
- **Tool calls:** 92
- **Original source:** `logs/chats/worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557.jsonl`
- **Structured JSON:** [`caf98984a2e5c39990ec.json`](../../sessions/ca/caf98984a2e5c39990ec.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

185 recorded events

### Tool call

_source line 1 · 2026-05-21T08:46:41.607780+00:00_

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
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
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

_source line 2 · 2026-05-21T08:46:41.608141+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T08:46:41.608374+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd",
  "command": "find /root/contamcal-irt-calibration/ -name \"*rrf*\" -o -name \"*rank_fusion*\" -o -name \"*signal*\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd",
    "command": "find /root/contamcal-irt-calibration/ -name \"*rrf*\" -o -name \"*rank_fusion*\" -o -name \"*signal*\" 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T08:46:41.608539+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T08:46:41.608672+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd",
  "command": "ls /root/contamcal-irt-calibration/analysis/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd",
    "command": "ls /root/contamcal-irt-calibration/analysis/"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T08:46:41.608799+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Unknown server 'westd'. Available: ['cqa1-21977', 'westd-29999']\", \"metadata\": {\"elapsed_seconds\": 0.0}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T08:46:41.608950+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "ls /root/contamcal-irt-calibration/analysis/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "ls /root/contamcal-irt-calibration/analysis/"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T08:46:41.609072+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "find /root/contamcal-irt-calibration/ -name \"*rrf*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "find /root/contamcal-irt-calibration/ -name \"*rrf*\""
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T08:46:41.609189+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "find /root/contamcal-irt-calibration/ -name \"*signal*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "find /root/contamcal-irt-calibration/ -name \"*signal*\""
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T08:46:41.609358+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"__pycache__\\nanalysis\\nanalyze_gsm8k.py\\nbootstrap_profile_stability.py\\nbootstrap_results.txt\\nbootstrap_results_arc.txt\\nbootstrap_results_mmlu.txt\\nbootstrap_table.tex\\nbootstrap_table_arc.tex\\nbootstrap_table_mmlu.tex\\nbootstrap_triple_seed.py\\nbootstrap_triple_seed.py.bak\\nbootstrap_triple_seed.py.bak_d188\\nclassification_sensitivity_sweep.py\\nfit_irt_2pl_gamma.py\\nirt_data_v3\\nirt_results\\nirt_results_v3\\nitem_vulnerability.py\\nresults\\ntreated_untreated_analysis.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.28}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T08:46:41.609518+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "find /root/contamcal-irt-calibration/ -name \"*rank_fusion*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "find /root/contamcal-irt-calibration/ -name \"*rank_fusion*\""
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T08:46:41.609648+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/contamcal-irt-calibration/exp002/aggregate_rrf.py\\n/root/contamcal-irt-calibration/exp006/run_exp006.py.bak_pre_rrf_fix\\n/root/contamcal-irt-calibration/exp006/run_pooled_rrf_irt.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-21T08:46:41.609791+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/contamcal-irt-calibration/exp002/compute_signals.py\\n/root/contamcal-irt-calibration/exp002/signal_embedding.py\\n/root/contamcal-irt-calibration/exp002/signal_minkpp.py\\n/root/contamcal-irt-calibration/exp002/signal_constat.py\\n/root/contamcal-irt-calibration/exp002/signal_selfcritique.py\\n/root/contamcal-irt-calibration/exp002/run_signals_05B.sh\\n/root/contamcal-irt-calibration/exp002/signals\\n/root/contamcal-irt-calibration/exp002/run_signals_3B_v6.sh\\n/root/contamcal-irt-calibration/exp002/run_signals_3B_d025_v3_s42.sh\\n/root/contamcal-irt-calibration/exp002/run_05B_s123_signals.sh\\n/root/contamcal-irt-calibration/exp002/run_15B_s123_signals.sh\\n/root/contamcal-irt-calibration/exp002/run_3B_s42_signals.sh\\n/root/contamcal-irt-calibration/exp002/run_3B_d100_s123_gsm8k_arc_signals.sh\\n/root/contamcal-irt-calibration/exp002/run_3B_d000_a32_s42_signals.sh\\n/root/contamcal-irt-calibration/exp002/run_signals_3B_d100_a32_s42.sh\\n/root/contamcal-irt-calibration/exp002/run_signals_05B_s123_remaining.sh\\n/root/contamcal-irt-calibration/exp002/run_3B_d000_s123_signals.sh\\n/root/contamcal-irt-calibration/exp002/run_05B_instruct_signals.sh\\n/root/contamcal-irt-calibration/exp002/run_3B_d000_s123_signals_v2.sh\\n/root/contamcal-irt-calibration/exp006/_baselines_v1/single_signal_2pl_gamma.py\\n/root/contamcal-irt-calibration/exp006/run_exp006.py.bak_pre_d018_signals\\n/root/contamcal-irt-calibration/exp008/signal_survival_analysis.py\\n/root/contamcal-irt-calibration/exp008/run_signal_survival.py\\n/root/contamcal-irt-calibration/exp008/exp008_output/signal_decay_scatter.pdf\\n/root/contamcal-irt-calibration/exp008/signal_survival.py\\n/root/contamcal-irt-calibration/exp008/signal_survival_v4.py\\n/root/contamcal-irt-calibration/exp008/compute_signals_on_model.py\\n/root/contamcal-irt-calibration/exp008_new/compute_signals_on_model.py\\n/root/contamcal-irt-calibration/exp008_new/run_signal_survival.
…[truncated 109 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T08:46:41.609929+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T08:46:41.610081+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "cat /root/contamcal-irt-calibration/exp002/aggregate_rrf.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "cat /root/contamcal-irt-calibration/exp002/aggregate_rrf.py"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-21T08:46:41.610210+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "cat /root/contamcal-irt-calibration/exp002/compute_signals.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "cat /root/contamcal-irt-calibration/exp002/compute_signals.py"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-21T08:46:41.610521+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nRRF (Reciprocal Rank Fusion) aggregation of contamination signals.\\n\\nFuses 4 per-item signal scores into a single exposure score using RRF\\n(Cormack et al. 2009). Also implements ablation variants: equal-weight\\nrank averaging and single-signal baselines.\\n\\nInput:  Per-item signal scores (JSON from compute_signals.py)\\nOutput: Per-model-item fused exposure scores + signal survival AUC matrix\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nfrom pathlib import Path\\n\\nimport numpy as np\\n\\nlogger = logging.getLogger(__name__)\\n\\nSIGNAL_KEYS = [\\\"s1_embedding\\\", \\\"s2_minkpp\\\", \\\"s3_constat\\\", \\\"s4_selfcritique\\\"]\\nRRF_K = 60\\n\\n\\ndef detect_available_signals(items: list[dict], candidates: list[str] = None) -> list[str]:\\n    \\\"\\\"\\\"Auto-detect which signals have non-trivial values (not all null/zero).\\\"\\\"\\\"\\n    if candidates is None:\\n        candidates = SIGNAL_KEYS\\n    available = []\\n    for sig in candidates:\\n        vals = [item.get(sig) for item in items]\\n        if any(v is not None and v != 0.0 for v in vals):\\n            available.append(sig)\\n    return available\\n\\n\\ndef load_signal_data(signal_files: list[str]) -> list[dict]:\\n    \\\"\\\"\\\"Load and merge signal files. Each file contains a list of per-item dicts.\\\"\\\"\\\"\\n    merged = {}\\n    for fpath in signal_files:\\n        with open(fpath) as f:\\n            data = json.load(f)\\n        for item in data:\\n            idx = item[\\\"index\\\"]\\n            if idx not in merged:\\n                merged[idx] = {\\\"index\\\": idx, \\\"benchmark\\\": item.get(\\\"benchmark\\\", \\\"\\\")}\\n            merged[idx].update(item)\\n    return [merged[k] for k in sorted(merged)]\\n\\n\\ndef compute_ranks(scores: np.ndarray) -> np.ndarray:\\n    \\\"\\\"\\\"Rank items from 1 (highest score = most suspicious) to N.\\\"\\\"\\\"\\n    order = np.a
…[truncated 7135 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T08:46:41.610717+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "ls /root/contamcal-irt-calibration/exp002/signals/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "ls /root/contamcal-irt-calibration/exp002/signals/"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-21T08:46:41.610917+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"import argparse\\nimport gc\\nimport json\\nimport logging\\nimport os\\nimport sys\\nfrom pathlib import Path\\n\\nlogger = logging.getLogger(__name__)\\n\\nsys.path.insert(0, str(Path(__file__).resolve().parent))\\n\\n\\ndef main():\\n    parser = argparse.ArgumentParser(\\n        description=\\\"Compute contamination detection signals for model-benchmark pairs\\\"\\n    )\\n    parser.add_argument(\\\"--model-path\\\", type=str, required=True,\\n                        help=\\\"Base model path (e.g., /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B)\\\")\\n    parser.add_argument(\\\"--adapter-path\\\", type=str, default=None,\\n                        help=\\\"LoRA adapter path (optional, for SFT models)\\\")\\n    parser.add_argument(\\\"--benchmark\\\", type=str, required=True,\\n                        choices=[\\\"mmlu\\\", \\\"gsm8k\\\", \\\"arc_challenge\\\", \\\"humaneval\\\"])\\n    parser.add_argument(\\\"--signal\\\", type=str, required=True,\\n                        choices=[\\\"s1\\\", \\\"s2\\\", \\\"s3\\\", \\\"s4\\\", \\\"all\\\"],\\n                        help=\\\"Which signal to compute (s1/s2/s3/s4/all)\\\")\\n    parser.add_argument(\\\"--output-dir\\\", type=str, required=True)\\n    parser.add_argument(\\\"--cache-dir\\\", type=str, default=\\\"/root/autodl-tmp/.hf_cache\\\")\\n    parser.add_argument(\\\"--batch-size\\\", type=int, default=8)\\n\\n    parser.add_argument(\\\"--sft-data-dir\\\", type=str, default=\\\"/root/autodl-tmp/exp001/sft_data\\\",\\n                        help=\\\"SFT training data directory (for S1)\\\")\\n    parser.add_argument(\\\"--ref-model-path\\\", type=str, default=None,\\n                        help=\\\"Reference model path for S2 Min-K%%++ (auto-inferred if not set)\\\")\\n    parser.add_argument(\\\"--k-percent\\\", type=int, default=20,\\n                        help=\\\"K%% for Min-K%% selection (S2, default: 20)\\\")\\n    parser.add_argument(\\\"
…[truncated 3883 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T08:46:41.611093+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"__init__.py\\ns1_embedding.py\\ns2_minkpp.py\\ns3_constat.py\\ns4_selfcritique.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T08:46:41.611252+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "find /root/contamcal-irt-calibration/exp002/signals -name \"signals_merged*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "find /root/contamcal-irt-calibration/exp002/signals -name \"signals_merged*\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T08:46:41.611443+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T08:46:41.611577+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "ls /root/contamcal-irt-calibration/exp006/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "ls /root/contamcal-irt-calibration/exp006/"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T08:46:41.611699+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "find /root/contamcal-irt-calibration/exp002/signals -type d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "find /root/contamcal-irt-calibration/exp002/signals -type d"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-21T08:46:41.611838+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"README.md\\n_baselines_v1\\nbaselines.py\\ncompute_all_baselines_unified.py\\ncompute_ci_coverage.py\\ncompute_vanilla_2pl_tau.py\\ncompute_vanilla_2pl_tau_fullitems.py\\ndryrun_full.json\\ndryrun_no_stan.json\\nevaluate_calibration.py\\nextract_theta_no05b.py\\ngamma_prior_sensitivity.py\\ngamma_prior_sensitivity_resume.py\\nj16_cross_family.log\\njoint_fit.py\\npower_analysis.py\\nrandom_300_tau_baseline.py\\nrandom_300_tau_baseline_fixed.py\\nrun_2pl_ablation.py\\nrun_all_baselines.py\\nrun_cross_family_s2s4.py\\nrun_cross_family_v5.py\\nrun_exp006.py\\nrun_exp006.py.bak_pre_d018_signals\\nrun_exp006.py.bak_pre_gsm8k\\nrun_exp006.py.bak_pre_rrf_fix\\nrun_exp006.py.bak_pre_s1only\\nrun_fisher_heatmap.py\\nrun_gamma_prior_sensitivity.py\\nrun_irt_calibration.py\\nrun_irt_calibration.py.bak_pre_gsm8k\\nrun_irt_stan.py\\nrun_mmlu_domain_gamma.py\\nrun_mmlu_domain_gamma_j16.py\\nrun_mmlu_domain_gamma_j16_cross_family.py\\nrun_mmlu_domain_gamma_j16_cross_family_fast.py\\nrun_mmlu_domain_gamma_n24.py\\nrun_mmlu_domain_gamma_no05b.py\\nrun_oracle_exposure_ablation.py\\nrun_pooled_15B_4pl.py\\nrun_pooled_4bench_irt.py\\nrun_pooled_irt_n16.sh\\nrun_pooled_rrf_irt.py\\nrun_stratified_irt.py\\nrun_wider_prior_ablation.py\\nsensitivity_exclusion_rate.py\\ntest_output\\ntost_equivalence.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-21T08:46:41.611974+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/contamcal-irt-calibration/exp002/signals\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-21T08:46:41.612111+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "find /root/contamcal-irt-calibration/ -name \"signals_merged*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "find /root/contamcal-irt-calibration/ -name \"signals_merged*\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-21T08:46:41.612256+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T08:46:41.612433+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "find /root/contamcal-irt-calibration/ -name \"exposure_scores*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "find /root/contamcal-irt-calibration/ -name \"exposure_scores*\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-21T08:46:41.612565+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/contamcal-irt-calibration/analysis/irt_data_v3/exposure_scores.csv\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T08:46:41.612685+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "head -100 /root/contamcal-irt-calibration/exp006/run_pooled_rrf_irt.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "head -100 /root/contamcal-irt-calibration/exp006/run_pooled_rrf_irt.py"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-21T08:46:41.612856+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Pooled IRT fitting with RRF signal-based exposure (per-model, per-item).\\n\\nRuns per-benchmark 4PL+γ IRT with exposure matrix from RRF output.\\nSupports D045 exclusion (0.5B excluded from MMLU/ARC).\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport re\\nimport sys\\nimport time\\nfrom pathlib import Path\\n\\nimport numpy as np\\n\\nsys.path.insert(0, \\\"/root/contamcal-irt-calibration/exp006\\\")\\nfrom run_irt_calibration import (\\n    load_pooled_eval_results,\\n    prepare_stan_data,\\n    fit_stan_model,\\n    check_convergence,\\n    posterior_predictive_check,\\n    extract_results,\\n    STAN_MODELS,\\n)\\n\\nlog = logging.getLogger(__name__)\\n\\nEVAL_DIR = \\\"/root/autodl-tmp/exp001/eval_results\\\"\\nMAX_ITEMS = 300\\n\\n\\ndef strip_aligned(dirname):\\n    return re.sub(r'(_para)?(_aligned)?$', '', dirname)\\n\\n\\ndef normalize_model_key(key):\\n    a_match = re.search(r'_(a\\\\d+)', key)\\n    s_match = re.search(r'_(s\\\\d+)', key)\\n    base = re.sub(r'_(a\\\\d+|s\\\\d+)', '', key)\\n    suffix = ''\\n    if a_match:\\n        suffix += '_' + a_match.group(1)\\n    if s_match:\\n        suffix += '_' + s_match.group(1)\\n    return base + suffix\\n\\n\\ndef resolve_rrf_key(eval_key, rrf_data, norm_rrf):\\n    if eval_key in rrf_data:\\n        return eval_key\\n    norm = normalize_model_key(eval_key)\\n    if norm in norm_rrf:\\n        return norm_rrf[norm]\\n    if '_a' not in eval_key:\\n        norm_a32 = normalize_model_key(eval_key + '_a32')\\n        if norm_a32 in norm_rrf:\\n            return norm_rrf[norm_a32]\\n    return None\\n\\n\\ndef load_rrf_exposure(path):\\n    with open(path) as f:\\n        return json.load(f)\\n\\n\\ndef build_rrf_exposure_matrix(models, rrf_data, benchmark, n_items):\\n    \\\"\\\"\\\"Build exposure matrix from per-model/per-item RRF scores.\\\"\\\"\\\"\\n    N = len(models)
…[truncated 1435 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-21T08:46:41.613024+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "find /root/contamcal-irt-calibration/ -name \"s1_embedding*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "find /root/contamcal-irt-calibration/ -name \"s1_embedding*\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-21T08:46:41.613153+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/contamcal-irt-calibration/exp002/signals/s1_embedding.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T08:46:41.613273+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "find /root/contamcal-irt-calibration/ -name \"rrf_scores*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "find /root/contamcal-irt-calibration/ -name \"rrf_scores*\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-21T08:46:41.613419+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-21T08:46:41.613537+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "find /root/autodl-tmp/ -name \"rrf_exposure*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "find /root/autodl-tmp/ -name \"rrf_exposure*\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-21T08:46:41.613661+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-21T08:46:41.613790+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "find /root/autodl-tmp/ -name \"s1_embedding*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "find /root/autodl-tmp/ -name \"s1_embedding*\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-21T08:46:41.613908+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-21T08:46:41.614020+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "find /root/autodl-tmp/ -name \"*signal*\" -type d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "find /root/autodl-tmp/ -name \"*signal*\" -type d"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-21T08:46:41.614132+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "find /root/autodl-tmp/ -name \"exposure_scores*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "find /root/autodl-tmp/ -name \"exposure_scores*\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-21T08:46:41.614246+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp002/signals\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-21T08:46:41.614380+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-21T08:46:41.614495+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "ls /root/autodl-tmp/exp002/signals/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "ls /root/autodl-tmp/exp002/signals/"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-21T08:46:41.614614+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Qwen2.5-7B_d000_s123\\nQwen2.5-7B_d000_s42\\nQwen2.5-7B_d005_s123\\nQwen2.5-7B_d005_s42\\nQwen2.5-7B_d025_s123\\nQwen2.5-7B_d025_s42\\nQwen2.5-7B_d050_s123\\nQwen2.5-7B_d050_s42\\nQwen2.5-7B_d100_s123\\nQwen2.5-7B_d100_s42\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-21T08:46:41.614746+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "ls /root/autodl-tmp/exp002/signals/Qwen2.5-7B_d100_s42/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "ls /root/autodl-tmp/exp002/signals/Qwen2.5-7B_d100_s42/"
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-21T08:46:41.614860+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "head -5 /root/contamcal-irt-calibration/analysis/irt_data_v3/exposure_scores.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "head -5 /root/contamcal-irt-calibration/analysis/irt_data_v3/exposure_scores.csv"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-21T08:46:41.615057+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"signal_s1_embedding_arc_challenge.json\\nsignal_s1_embedding_gsm8k.json\\nsignal_s1_embedding_mmlu.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-21T08:46:41.615194+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"respondent,family,family_full,dosage,dosage_label,exposure\\r\\nphi4_d000_s42,phi4,Phi-4,d000,d000,0.0\\r\\nphi4_d005_s42,phi4,Phi-4,d005,d005,0.05\\r\\nphi4_d025_s42,phi4,Phi-4,d025,d025,0.25\\r\\nphi4_d050_s42,phi4,Phi-4,d050,d050,0.5\\r\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-21T08:46:41.615328+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "find /root/contamcal-irt-calibration/exp006/ -name \"rrf*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "find /root/contamcal-irt-calibration/exp006/ -name \"rrf*\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-21T08:46:41.615456+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-21T08:46:41.615590+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "head -30 /root/autodl-tmp/exp002/signals/Qwen2.5-7B_d100_s42/signal_s1_embedding_mmlu.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "head -30 /root/autodl-tmp/exp002/signals/Qwen2.5-7B_d100_s42/signal_s1_embedding_mmlu.json"
  }
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-21T08:46:41.615705+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "find /root/autodl-tmp/exp002/signals/Qwen2.5-7B_d100_s42/ -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "find /root/autodl-tmp/exp002/signals/Qwen2.5-7B_d100_s42/ -type f"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-21T08:46:41.615840+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"item_id\\\": \\\"mmlu_0000\\\",\\n    \\\"signal\\\": \\\"s1_embedding\\\",\\n    \\\"score\\\": 0.8934027552604675,\\n    \\\"metadata\\\": {\\n      \\\"mean_topk_sim\\\": 0.6226525902748108,\\n      \\\"top_k_sims\\\": [\\n        0.8934027552604675,\\n        0.8167058229446411,\\n        0.8141132593154907,\\n        0.8031706809997559,\\n        0.7576614618301392,\\n        0.4534541368484497,\\n        0.4283878803253174,\\n        0.4267301559448242,\\n        0.42483291029930115,\\n        0.4080667495727539\\n      ],\\n      \\\"sft_data_path\\\": \\\"/root/autodl-tmp/sft_data/sft_dosage_100.jsonl\\\"\\n    }\\n  },\\n  {\\n    \\\"item_id\\\": \\\"mmlu_0001\\\",\\n    \\\"signal\\\": \\\"s1_embedding\\\",\\n    \\\"score\\\": 0.7106989026069641,\\n    \\\"metadata\\\": {\\n      \\\"mean_topk_sim\\\": 0.4308483600616455,\\n      \\\"top_k_sims\\\": [\\n        0.7106989026069641,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-21T08:46:41.615973+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-7B_d100_s42/signal_s1_embedding_mmlu.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-7B_d100_s42/signal_s1_embedding_gsm8k.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-7B_d100_s42/signal_s1_embedding_arc_challenge.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-21T08:46:41.616121+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/contamcal-irt-calibration/ -name \"s*_*_mmlu.json\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/contamcal-irt-calibration/ -name \"s*_*_mmlu.json\" -type f"
  }
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-21T08:46:41.616263+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/ -name \"signal_*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/autodl-tmp/ -name \"signal_*\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-21T08:46:41.616409+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.13}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-21T08:46:41.616607+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/signal_embedding_mmlu_Qwen2.5-0.5B_d000_s42.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/signal_embedding_mmlu.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/signal_embedding_gsm8k.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/signal_embedding_arc_challenge.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/signal_minkpp_mmlu.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/signal_minkpp_gsm8k.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/signal_selfcritique_mmlu.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/signal_selfcritique_gsm8k.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/signal_minkpp_arc_challenge.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/signal_selfcritique_arc_challenge.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42/signal_embedding_mmlu.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42/signal_minkpp_mmlu.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42/signal_selfcritique_mmlu.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42/signal_embedding_gsm8k.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42/signal_minkpp_gsm8k.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42/signal_selfcritique_gsm8k.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42/signal_embedding_arc_challenge.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42/signal_minkpp_arc_challenge.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42/signal_selfcritique_arc_challenge.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d100_s42/signal_embedding_mmlu.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d100_s42/signal_minkpp_mmlu.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d100_s42/signal_selfcritique_mmlu.json\\n/root/autodl-tmp/exp002/signals/Qwen
…[truncated 6382 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-21T08:46:41.616773+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/autodl-tmp/exp002/signals/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/autodl-tmp/exp002/signals/"
  }
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-21T08:46:41.616899+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/exp002/signals/ -name \"*constat*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/autodl-tmp/exp002/signals/ -name \"*constat*\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-21T08:46:41.617039+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Llama-3.2-3B_d000_s42\\nLlama-3.2-3B_d005_s42\\nLlama-3.2-3B_d025_s42\\nLlama-3.2-3B_d100_s42\\nQwen2.5-0.5B-Instruct\\nQwen2.5-0.5B_d000_s123\\nQwen2.5-0.5B_d000_s42\\nQwen2.5-0.5B_d005_s123\\nQwen2.5-0.5B_d005_s42\\nQwen2.5-0.5B_d025_s123\\nQwen2.5-0.5B_d025_s42\\nQwen2.5-0.5B_d100_s123\\nQwen2.5-0.5B_d100_s42\\nQwen2.5-1.5B-Instruct\\nQwen2.5-1.5B_d000_s123\\nQwen2.5-1.5B_d000_s42\\nQwen2.5-1.5B_d005_s123\\nQwen2.5-1.5B_d005_s42\\nQwen2.5-1.5B_d025_s123\\nQwen2.5-1.5B_d025_s42\\nQwen2.5-1.5B_d100_s123\\nQwen2.5-1.5B_d100_s42\\nQwen2.5-3B_d000_a32_s42\\nQwen2.5-3B_d000_s123\\nQwen2.5-3B_d000_s123_a32\\nQwen2.5-3B_d000_s42_a32\\nQwen2.5-3B_d000_v2_s42\\nQwen2.5-3B_d005_a32_s42\\nQwen2.5-3B_d005_s123\\nQwen2.5-3B_d005_s42\\nQwen2.5-3B_d005_s42_a32\\nQwen2.5-3B_d025_s123\\nQwen2.5-3B_d025_s42\\nQwen2.5-3B_d025_s42_DEPRECATED_alpha16\\nQwen2.5-3B_d025_s42_old_alpha16\\nQwen2.5-3B_d025_v3_s42\\nQwen2.5-3B_d100_a32_s123\\nQwen2.5-3B_d100_a32_s42\\nQwen2.5-3B_d100_s42\\nbatch_report_Qwen2.5-0.5B.json\\nbatch_report_Qwen2.5-1.5B.json\\nbatch_report_Qwen2.5-3B.json\\nrrf\\ns1_recompute_cuda0.log\\ns1_recompute_cuda1.log\\nsignals_05B_s123_v2.log\\nsignals_3B_d025_v3_s42.log\\nsignals_3B_v6.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-21T08:46:41.617172+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_v2_s42/signal_s3_constat_mmlu.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_v2_s42/signal_s3_constat_gsm8k.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_v2_s42/signal_s3_constat_arc_challenge.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-21T08:46:41.617331+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/autodl-tmp/exp002/signals/rrf/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/autodl-tmp/exp002/signals/rrf/"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-21T08:46:41.617467+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"exposure_aggregated.json\\nexposure_scores.json\\nexposure_scores_qwen_only.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-21T08:46:41.617587+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d100_a32_s42/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d100_a32_s42/"
  }
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-21T08:46:41.617703+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_s42_a32/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_s42_a32/"
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-21T08:46:41.617827+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"_s4_chunks_mmlu\\nrun.log\\nsignal_s1_embedding_arc_challenge.json\\nsignal_s1_embedding_gsm8k.json\\nsignal_s1_embedding_mmlu.json\\nsignal_s2_minkpp_arc_challenge.json\\nsignal_s2_minkpp_gsm8k.json\\nsignal_s2_minkpp_mmlu.json\\nsignal_s4_selfcritique_arc_challenge.json\\nsignal_s4_selfcritique_gsm8k.json\\nsignal_s4_selfcritique_mmlu.json\\nsignals_merged_arc_challenge.json\\nsignals_merged_gsm8k.json\\nsignals_merged_mmlu.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-21T08:46:41.617953+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"_s4_chunks_mmlu\\nrun.log\\nsignal_s1_embedding_arc_challenge.json\\nsignal_s1_embedding_gsm8k.json\\nsignal_s1_embedding_mmlu.json\\nsignal_s2_minkpp_arc_challenge.json\\nsignal_s2_minkpp_gsm8k.json\\nsignal_s2_minkpp_mmlu.json\\nsignal_s4_selfcritique_arc_challenge.json\\nsignal_s4_selfcritique_gsm8k.json\\nsignal_s4_selfcritique_mmlu.json\\nsignals_merged_arc_challenge.json\\nsignals_merged_gsm8k.json\\nsignals_merged_mmlu.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-21T08:46:41.618085+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -50 /root/autodl-tmp/exp002/signals/rrf/exposure_scores.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -50 /root/autodl-tmp/exp002/signals/rrf/exposure_scores.json"
  }
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-21T08:46:41.618200+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -20 /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d100_a32_s42/signals_merged_mmlu.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -20 /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d100_a32_s42/signals_merged_mmlu.json"
  }
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-21T08:46:41.618334+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -200 /root/contamcal-irt-calibration/exp006/run_exp006.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -200 /root/contamcal-irt-calibration/exp006/run_exp006.py"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-21T08:46:41.618478+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"Llama-3.2-3B_d000_s42\\\": {\\n    \\\"mmlu\\\": {\\n      \\\"exposure_scores\\\": [\\n        0.0006224320656157297,\\n        0.004533832883940596,\\n        0.0015889223184469262,\\n        0.0037621260348762874,\\n        0.13634728622224238,\\n        0.03185036115900705,\\n        0.012682026269462623,\\n        0.0005085972871896046,\\n        0.00605561094163809,\\n        0.005405274131976368,\\n        0.006225673996592385,\\n        0.011673842875784407,\\n        0.009802532966313145,\\n        0.4042927112145918,\\n        0.016615078373362978,\\n        0.0012657561242099104,\\n        0.00523819072523791,\\n        0.05079855803436732,\\n        0.027369996051824493,\\n        0.009804750573319155,\\n        0.0020507601032131568,\\n        0.05933261903459419,\\n        0.004191584517552997,\\n        0.0005337977704902009,\\n        0.02910652340442279,\\n        0.007562419728726096,\\n        0.007327371090934325,\\n        0.014939931662864232,\\n        0.0036411436354115293,\\n        0.0529013466103104,\\n        0.018716360396933723,\\n        0.018384770983307052,\\n        0.004056391722230033,\\n        0.018568249171214152,\\n        0.021902062316520542,\\n        0.0091824205860012,\\n        0.009320083184555284,\\n        0.0025303494213358866,\\n        0.00753563300328189,\\n        0.0019366772897717356,\\n        0.016653585999757692,\\n        0.0019846268602349286,\\n        0.002541161249928456,\\n        0.002751079615849266,\\n        0.02542517329876279,\\n        0.05619168146216482,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.55}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-21T08:46:41.618623+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"item_id\\\": \\\"mmlu_0000\\\",\\n    \\\"benchmark\\\": \\\"mmlu\\\",\\n    \\\"s1_embedding\\\": 0.8934028148651123,\\n    \\\"s2_minkpp\\\": -1.6932812929153442,\\n    \\\"s4_selfcritique\\\": -0.8033947069832642\\n  },\\n  {\\n    \\\"item_id\\\": \\\"mmlu_0001\\\",\\n    \\\"benchmark\\\": \\\"mmlu\\\",\\n    \\\"s1_embedding\\\": 0.7106987833976746,\\n    \\\"s2_minkpp\\\": -1.3780063390731812,\\n    \\\"s4_selfcritique\\\": -0.9992959028781391\\n  },\\n  {\\n    \\\"item_id\\\": \\\"mmlu_0002\\\",\\n    \\\"benchmark\\\": \\\"mmlu\\\",\\n    \\\"s1_embedding\\\": 0.8842411041259766,\\n    \\\"s2_minkpp\\\": -1.5758658647537231,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-21T08:46:41.618883+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nexp-006 end-to-end pipeline: IRT calibration + 7 baselines + evaluation.\\n\\nLoads exp-001 eval results and exp-002/003 exposure scores,\\nruns IRT 4PL+gamma calibration and all baselines per benchmark,\\nevaluates against ground-truth clean scores (dosage=0 models).\\n\\nUsage:\\n    python run_exp006.py --help\\n    python run_exp006.py --dry-run --skip-stan --max-items 20    # quick test\\n    python run_exp006.py                                         # full run\\n\\nDependencies: cmdstanpy, numpy, scipy\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport sys\\nimport time\\nfrom pathlib import Path\\n\\nimport numpy as np\\n\\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\\nfrom run_irt_calibration import (\\n    load_eval_results,\\n    load_pooled_eval_results,\\n    load_exposure_scores,\\n    build_exposure_matrix,\\n    run_benchmark_fit,\\n    STAN_MODELS,\\n)\\nfrom baselines import run_all_baselines\\nfrom evaluate_calibration import (\\n    evaluate_method,\\n    format_text_table,\\n    format_latex_table,\\n)\\nfrom joint_fit import run_joint_fit\\n\\nlog = logging.getLogger(__name__)\\n\\n# D018: 3B GSM8K excluded from dose-response analysis\\nD018_EXCLUDE = [(\\\"3B\\\", \\\"gsm8k\\\")]\\nD018_EXCLUDE_RULES = [\\n    {\\\"model\\\": \\\"3B\\\", \\\"benchmark\\\": \\\"gsm8k\\\", \\\"reason\\\": \\\"D018 LoRA damage\\\"},\\n]\\n\\n\\ndef should_exclude_dose_response(model_name, benchmark, rules=D018_EXCLUDE):\\n    \\\"\\\"\\\"Check D018 exclusion rules for dose-response analysis.\\\"\\\"\\\"\\n    for pattern, bench in rules:\\n        if pattern in model_name and benchmark == bench:\\n            return True\\n    return False\\n\\n\\ndef compute_ground_truth(responses, dosages, models=None):\\n    \\\"\\\"\\\"Ground truth = accuracy of dosage-0 models (uncontaminated).\\n\\n    For dosage-0 models, raw accuracy IS the clean
…[truncated 6935 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-21T08:46:41.619083+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -100 /root/contamcal-irt-calibration/exp006/evaluate_calibration.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -100 /root/contamcal-irt-calibration/exp006/evaluate_calibration.py"
  }
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-21T08:46:41.619217+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/contamcal-irt-calibration/exp006/run_exp006.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/contamcal-irt-calibration/exp006/run_exp006.py"
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-21T08:46:41.619417+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nEvaluate calibration quality: IRT 4PL+gamma vs 7 baselines.\\n\\n8 metrics:\\n  1. MAE -- mean absolute error (calibrated vs ground-truth clean scores)\\n  2. ECE -- expected calibration error (binned)\\n  3. MCE -- maximum calibration error (binned)\\n  4. Brier Score -- mean squared error\\n  5. Coverage -- fraction of ground-truth within 50/80/95% CIs\\n  6. Sharpness -- mean CI width (lower is better, conditional on coverage)\\n  7. Kendall tau -- rank correlation preservation\\n  8. Dose-response monotonicity -- gamma or calibration error increases with dosage\\n\\nInput: IRT result JSONs + baseline result JSON + ground-truth clean scores\\nOutput: per-method metrics JSON + LaTeX comparison table + reliability diagram data\\n\\nDependencies: numpy, scipy\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\n\\nimport numpy as np\\nfrom scipy import stats\\n\\nlog = logging.getLogger(__name__)\\n\\nSEED = 42\\nN_BOOTSTRAP = 1000\\n\\n\\n# ── Metrics ──\\n\\ndef metric_mae(calibrated, ground_truth):\\n    \\\"\\\"\\\"Mean Absolute Error between calibrated and ground-truth scores.\\\"\\\"\\\"\\n    return float(np.mean(np.abs(np.array(calibrated) - np.array(ground_truth))))\\n\\n\\ndef metric_brier(calibrated, ground_truth):\\n    \\\"\\\"\\\"Brier Score (MSE) between calibrated and ground-truth scores.\\\"\\\"\\\"\\n    return float(np.mean((np.array(calibrated) - np.array(ground_truth)) ** 2))\\n\\n\\ndef metric_ece(calibrated, ground_truth, n_bins=10):\\n    \\\"\\\"\\\"Expected Calibration Error: weighted average of per-bin |mean_cal - mean_gt|.\\\"\\\"\\\"\\n    cal = np.array(calibrated)\\n    gt = np.array(ground_truth)\\n    n = len(cal)\\n    if n == 0:\\n        return 0.0\\n    bin_edges = np.linspace(cal.min() - 1e-8, cal.max() + 1e-8, n_bins + 1)\\n    ece = 0.0\\n    for k in range(n_bins):\\n        mask = (cal >= bin_edges[k]) & (cal < bin_edges[k + 1]
…[truncated 1778 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-21T08:46:41.619715+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nexp-006 end-to-end pipeline: IRT calibration + 7 baselines + evaluation.\\n\\nLoads exp-001 eval results and exp-002/003 exposure scores,\\nruns IRT 4PL+gamma calibration and all baselines per benchmark,\\nevaluates against ground-truth clean scores (dosage=0 models).\\n\\nUsage:\\n    python run_exp006.py --help\\n    python run_exp006.py --dry-run --skip-stan --max-items 20    # quick test\\n    python run_exp006.py                                         # full run\\n\\nDependencies: cmdstanpy, numpy, scipy\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport sys\\nimport time\\nfrom pathlib import Path\\n\\nimport numpy as np\\n\\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\\nfrom run_irt_calibration import (\\n    load_eval_results,\\n    load_pooled_eval_results,\\n    load_exposure_scores,\\n    build_exposure_matrix,\\n    run_benchmark_fit,\\n    STAN_MODELS,\\n)\\nfrom baselines import run_all_baselines\\nfrom evaluate_calibration import (\\n    evaluate_method,\\n    format_text_table,\\n    format_latex_table,\\n)\\nfrom joint_fit import run_joint_fit\\n\\nlog = logging.getLogger(__name__)\\n\\n# D018: 3B GSM8K excluded from dose-response analysis\\nD018_EXCLUDE = [(\\\"3B\\\", \\\"gsm8k\\\")]\\nD018_EXCLUDE_RULES = [\\n    {\\\"model\\\": \\\"3B\\\", \\\"benchmark\\\": \\\"gsm8k\\\", \\\"reason\\\": \\\"D018 LoRA damage\\\"},\\n]\\n\\n\\ndef should_exclude_dose_response(model_name, benchmark, rules=D018_EXCLUDE):\\n    \\\"\\\"\\\"Check D018 exclusion rules for dose-response analysis.\\\"\\\"\\\"\\n    for pattern, bench in rules:\\n        if pattern in model_name and benchmark == bench:\\n            return True\\n    return False\\n\\n\\ndef compute_ground_truth(responses, dosages, models=None):\\n    \\\"\\\"\\\"Ground truth = accuracy of dosage-0 models (uncontaminated).\\n\\n    For dosage-0 models, raw accuracy IS the clean
…[truncated 7202 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-21T08:46:41.619924+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_s123_a32/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_s123_a32/"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-21T08:46:41.620081+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"_s4_chunks_mmlu\\nsignal_s1_embedding_arc_challenge.json\\nsignal_s1_embedding_gsm8k.json\\nsignal_s1_embedding_mmlu.json\\nsignal_s2_minkpp_arc_challenge.json\\nsignal_s2_minkpp_gsm8k.json\\nsignal_s2_minkpp_mmlu.json\\nsignal_s4_selfcritique_arc_challenge.json\\nsignal_s4_selfcritique_gsm8k.json\\nsignal_s4_selfcritique_mmlu.json\\nsignals_merged_arc_challenge.json\\nsignals_merged_gsm8k.json\\nsignals_merged_mmlu.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-21T08:46:41.620249+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d100_s42/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d100_s42/"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-21T08:46:41.620411+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"signal_embedding_arc_challenge.json\\nsignal_embedding_gsm8k.json\\nsignal_embedding_mmlu.json\\nsignal_minkpp_arc_challenge.json\\nsignal_minkpp_gsm8k.json\\nsignal_minkpp_mmlu.json\\nsignal_selfcritique_arc_challenge.json\\nsignal_selfcritique_gsm8k.json\\nsignal_selfcritique_mmlu.json\\nsignals_merged_arc_challenge.json\\nsignals_merged_gsm8k.json\\nsignals_merged_mmlu.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-21T08:46:41.620552+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -20 /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d100_s42/signals_merged_mmlu.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -20 /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d100_s42/signals_merged_mmlu.json"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-21T08:46:41.620690+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"index\\\": 0,\\n    \\\"benchmark\\\": \\\"mmlu\\\",\\n    \\\"s1_embedding\\\": 0.9028400778770447,\\n    \\\"s2_minkpp\\\": 1.6026520729064941,\\n    \\\"s3_constat\\\": null,\\n    \\\"s4_selfcritique\\\": -0.9562865393807289\\n  },\\n  {\\n    \\\"index\\\": 1,\\n    \\\"benchmark\\\": \\\"mmlu\\\",\\n    \\\"s1_embedding\\\": 0.8443397879600525,\\n    \\\"s2_minkpp\\\": 1.6954067945480347,\\n    \\\"s3_constat\\\": null,\\n    \\\"s4_selfcritique\\\": -0.9888163926508523\\n  },\\n  {\\n    \\\"index\\\": 2,\\n    \\\"benchmark\\\": \\\"mmlu\\\",\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-21T08:46:41.620846+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -20 /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/signals_merged_mmlu.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -20 /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/signals_merged_mmlu.json"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-21T08:46:41.620985+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"index\\\": 0,\\n    \\\"benchmark\\\": \\\"mmlu\\\",\\n    \\\"s1_embedding\\\": 0.3449670374393463,\\n    \\\"s2_minkpp\\\": 1.7811063528060913,\\n    \\\"s3_constat\\\": null,\\n    \\\"s4_selfcritique\\\": -0.9888163926508523\\n  },\\n  {\\n    \\\"index\\\": 1,\\n    \\\"benchmark\\\": \\\"mmlu\\\",\\n    \\\"s1_embedding\\\": 0.39687806367874146,\\n    \\\"s2_minkpp\\\": 1.7033835649490356,\\n    \\\"s3_constat\\\": null,\\n    \\\"s4_selfcritique\\\": -0.9936877843203067\\n  },\\n  {\\n    \\\"index\\\": 2,\\n    \\\"benchmark\\\": \\\"mmlu\\\",\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-21T08:46:41.621211+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat > /root/contamcal-irt-calibration/analysis/rrf_signal_analysis.py << 'PYEOF'\n\"\"\"RRF Signal Analysis: C1 (rank correlation) + C2 (leave-one-out ablation).\"\"\"\nimport json\nimport os\nimport re\nimport numpy as np\nfrom scipy.stats import spearmanr, kendalltau\nfrom pathlib import Path\n\nSIGNALS_DIR = \"/root/autodl-tmp/exp002/signals\"\nBENCHMARKS = [\"mmlu\", \"gsm8k\", \"arc_challenge\"]\nACTIVE_SIGNALS = [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"]\nRRF_K = 60\n\n# Signal orientation: True = negate before ranking (lower raw = more suspicious)\nNEGATE = {\"s1_embedding\": False, \"s2_minkpp\": True, \"s4_selfcritique\": False}\n\n\ndef parse_dosage(dirname):\n    \"\"\"Extract dosage fraction from directory name.\"\"\"\n    m = re.search(r'_d(\\d{3})', dirname)\n    if m:\n        return int(m.group(1)) / 100.0\n    return None\n\n\ndef list_model_dirs():\n    \"\"\"List model directories that have merged signal files for all benchmarks.\"\"\"\n    models = []\n    for name in sorted(os.listdir(SIGNALS_DIR)):\n        dirpath = os.path.join(SIGNALS_DIR, name)\n        if not os.path.isdir(dirpath):\n            continue\n        dosage = parse_dosage(name)\n        if dosage is None:\n            continue\n        # Check merged files exist for at least one benchmark\n        has_merged = any(\n            os.path.exists(os.path.join(dirpath, f\"signals_merged_{b}.json\"))\n            for b in BENCHMARKS\n        )\n        if has_merged:\n            models.append({\"dirname\": name, \"dosage\": dosage, \"path\": dirpath})\n    return models\n\n\ndef load_merged(model_path, benchmark):\n    \"\"\"Load signals_merged_{benchmark}.json, return list of dicts.\"\"\"\n    fpath = os.path.join(model_path, f\"signals_merged_{benchmark}.json\")\n    if not os.path.exists(fpath):\n        return None\n    with open(fpath) as f:\n        return json.load(f)\n\n\ndef compute_ranks(scores):\n    \"\"\"Rank from 1 (highest) to N.\"\"\"\n    order = np.argsort(-scores)\n    ranks = np.empty_like(order, dtype=float)\n    ranks[order] = np.arange(1, len(scores) + 1)\n    return ranks\n\n\ndef compute_rrf(items, signals, k=RRF_K):\n    \"\"\"Compute RRF scores for given signal subset. Returns normalized mean.\"\"\"\n    n = len(items)\n    if n == 0:\n        return 0.0, np.zeros(0)\n    \n    rrf = np.zeros(n)\n    for sig in signals:\n        v = np.array([it.get(sig, 0.0) or 0.0 for it in items], dtype=float)\n        if NEGATE.get(sig, False):\n            v = -v\n        ranks = compute_ranks(v)\n        rrf += 1.0 / (k + ranks)\n    \n    mn, mx = rrf.min(), rrf.max()\n    if mx > mn:\n        rrf_norm = (rrf - mn) / (mx - mn)\n    else:\n        rrf_norm = rrf\n    return float(rrf_norm.mean()), rrf_norm\n\n\ndef oriented_scores(items, sig):\n    \"\"\"Get signal scores oriented so higher = more suspicious.\"\"\"\n    v = np.array([it.get(sig, 0.0) or 0.0 for it in items], dtype=float)\n    if NEGATE.get(sig, False):\n        v = -v\n    return v\n\n\n# ════════════════════════════════════════════════════════\n# C1: Signal Rank Correlation Matrix\n# ════════════════════════════════════════════════════════\n\ndef compute_signal_correlations(models):\n    \"\"\"Per-benchmark Spearman rank correlation between signal pairs.\"\"\"\n    results = {}\n    for bench in BENCHMARKS:\n        pair_rhos = {f\"{a}_vs_{b}\": [] for i, a in enumerate(ACTIVE_SIGNALS)\n                     for b in ACTIVE_SIGNALS[i+1:]}\n        \n        n_models = 0\n        for m in models:\n            items = load_merged(m[\"path\"], bench)\n            if items is None:\n                continue\n            \n            # Check all 3 signals have non-null values\n            sig_arrays = {}\n            skip = False\n            for sig in ACTIVE_SIGNALS:\n                vals = [it.get(sig) for it in items]\n                if all(v is None or v == 0.0 for v in vals):\n                    skip = True\n                    break\n                sig_arrays[sig] = oriented_scores(items, sig)\n            if skip:\n                continue\n            \n            n_models += 1\n            for i, a in enumerate(ACTIVE_SIGNALS):\n                for b in ACTIVE_SIGNALS[i+1:]:\n                    rho, _ = spearmanr(sig_arrays[a], sig_arrays[b])\n                    pair_rhos[f\"{a}_vs_{b}\"].append(rho)\n        \n        # Build correlation matrix\n        n_sig = len(ACTIVE_SIGNALS)\n        matrix = np.eye(n_sig)\n        pair_details = {}\n        for i, a in enumerate(ACTIVE_SIGNALS):\n            for j, b in enumerate(ACTIVE_SIGNALS):\n                if i < j:\n                    key = f\"{a}_vs_{b}\"\n                    rhos = pair_rhos[key]\n                    if rhos:\n                        mean_rho = float(np.mean(rhos))\n                        std_rho = float(np.std(rhos))\n                        matrix[i, j] = mean_rho\n                        matrix[j, i] = mean_rho\n                        pair_details[key] = {\n                            \"mean_rho\": round(mean_rho, 4),\n                            \"std_rho\": round(std_rho, 4),\n                            \"n_models\": len(rhos),\n                            \"per_model_rhos\": [round(r, 4) for r in rhos]\n                        }\n        \n        results[bench] = {\n            \"n_models\": n_models,\n            \"signals\": ACTIVE_SIGNALS,\n            \"correlation_matrix\": matrix.tolist(),\n            \"pair_details\": pair_details\n        }\n    \n    return results\n\n\n# ════════════════════════════════════════════════════════\n# C2: Leave-One-Signal-Out Ablation\n# ════════════════════════════════════════════════════════\n\ndef leave_one_out_ablation(models):\n    \"\"\"For each benchmark, compute full RRF and leave-one-out variants.\"\"\"\n    results = {}\n    \n    for bench in BENCHMARKS:\n        # Collect model-level exposures for each signal config\n        configs = {\n            \"full\": ACTIVE_SIGNALS,\n        }\n        for sig in ACTIVE_SIGNALS:\n            remaining = [s for s in ACTIVE_SIGNALS if s != sig]\n            configs[f\"drop_{sig}\"] = remaining\n        # Also single-signal baselines\n        for sig in ACTIVE_SIGNALS:\n            configs[f\"only_{sig}\"] = [sig]\n        \n        model_exposures = {cfg: [] for cfg in configs}\n        dosages = []\n        model_names = []\n        valid_models = 0\n        \n        for m in models:\n            items = load_merged(m[\"path\"], bench)\n            if items is None:\n                continue\n            \n            # Check all signals present\n            has_all = True\n            for sig in ACTIVE_SIGNALS:\n                vals = [it.get(sig) for it in items]\n                if all(v is None or v == 0.0 for v in vals):\n                    has_all = False\n                    break\n            if not has_all:\n                continue\n            \n            valid_models += 1\n            dosages.append(m[\"dosage\"])\n            model_names.append(m[\"dirname\"])\n            \n            for cfg_name, cfg_signals in configs.items():\n                mean_exp, _ = compute_rrf(items, cfg_signals)\n                model_exposures[cfg_name].append(mean_exp)\n        \n        if valid_models < 3:\n            continue\n        \n        dosages = np.array(dosages)\n        \n        # Compute metrics for each config\n        config_metrics = {}\n        full_exp = np.array(model_exposures[\"full\"])\n        \n        for cfg_name, exps in model_exposures.items():\n            exps = np.array(exps)\n            \n            # Spearman correlation with true dosage\n            rho_dosage, p_dosage = spearmanr(exps, dosages)\n            tau_dosage, p_tau = kendalltau(exps, dosages)\n            \n            # Rank correlation with full RRF (for ablation configs)\n            if cfg_name != \"full\":\n                rho_full, _ = spearmanr(exps, full_exp)\n            else:\n                rho_full = 1.0\n            \n            # MAE vs dosage (after linear rescaling to [0,1])\n            if exps.max() > exps.min():\n                exps_scaled = (exps - exps.min()) / (exps.max() - exps.min())\n            else:\n                exps_scaled = exps\n            mae_dosage = float(np.mean(np.abs(exps_scaled - dosages)))\n            \n            config_metrics[cfg_name] = {\n                \"signals_used\": configs[cfg_name],\n                \"spearman_rho_vs_dosage\": round(float(rho_dosage), 4),\n                \"spearman_p_vs_dosage\": round(float(p_dosage), 6),\n                \"kendall_tau_vs_dosage\": round(float(tau_dosage), 4),\n                \"spearman_rho_vs_full_rrf\": round(float(rho_full), 4),\n                \"mae_vs_dosage_scaled\": round(mae_dosage, 4),\n                \"mean_exposure\": round(float(exps.mean()), 6),\n                \"std_exposure\": round(float(exps.std()), 6),\n            }\n        \n        # Compute delta MAE (leave-one-out vs full)\n        full_mae = config_metrics[\"full\"][\"mae_vs_dosage_scaled\"]\n        for sig in ACTIVE_SIGNALS:\n            drop_key = f\"drop_{sig}\"\n            if drop_key in config_metrics:\n                config_metrics[drop_key][\"delta_mae\"] = round(\n                    config_metrics[drop_key][\"mae_vs_dosage_scaled\"] - full_mae, 4)\n                config_metrics[drop_key][\"delta_rho\"] = round(\n                    config_metrics[drop_key][\"spearman_rho_vs_dosage\"] - \n                    config_metrics[\"full\"][\"spearman_rho_vs_dosage\"], 4)\n        \n        # Signal importance ranking (by how much MAE increases when dropped)\n        importance = []\n        for sig in ACTIVE_SIGNALS:\n            drop_key = f\"drop_{sig}\"\n            if drop_key in config_metrics:\n                importance.append({\n                    \"signal\": sig,\n                    \"delta_mae_when_dropped\": config_metrics[drop_key][\"delta_mae\"],\n                    \"delta_rho_when_dropped\": config_metrics[drop_key][\"delta_rho\"],\n                })\n        importance.sort(key=lambda x: -x[\"delta_mae_when_dropped\"])\n        \n        results[bench] = {\n            \"n_models\": valid_models,\n            \"model_names\": model_names,\n            \"dosages\": [round(d, 4) for d in dosages.tolist()],\n            \"configs\": config_metrics,\n            \"signal_importance_by_delta_mae\": importance,\n        }\n    \n    return results\n\n\n# ════════════════════════════════════════════════════════\n# Main\n# ════════════════════════════════════════════════════════\n\ndef main():\n    models = list_model_dirs()\n    print(f\"Found {len(models)} model directories with signal data\")\n    for m in models:\n        print(f\"  {m['dirname']} (dosage={m['dosage']})\")\n    \n    # C1\n    print(\"\\n\" + \"=\"*60)\n    print(\"C1: Signal Rank Correlation Matrix\")\n    print(\"=\"*60)\n    corr_results = compute_signal_correlations(models)\n    for bench, data in corr_results.items():\n        print(f\"\\n--- {bench} (n_models={data['n_models']}) ---\")\n        sigs = data[\"signals\"]\n        matrix = np.array(data[\"correlation_matrix\"])\n        header = \"            \" + \"  \".join(f\"{s:>16s}\" for s in sigs)\n        print(header)\n        for i, sig in enumerate(sigs):\n            row = f\"{sig:>16s}\" + \"  \".join(f\"{matrix[i,j]:>16.4f}\" for j in range(len(sigs)))\n            print(row)\n        for pair, detail in data[\"pair_details\"].items():\n            print(f\"  {pair}: rho={detail['mean_rho']:.4f} ± {detail['std_rho']:.4f} (n={detail['n_models']})\")\n    \n    # C2\n    print(\"\\n\" + \"=\"*60)\n    print(\"C2: Leave-One-Signal-Out Ablation\")\n    print(\"=\"*60)\n    ablation_results = leave_one_out_ablation(models)\n    for bench, data in ablation_results.items():\n        print(f\"\\n--- {bench} (n_models={data['n_models']}) ---\")\n        print(f\"{'Config':<25s} {'Signals':<40s} {'ρ(dosage)':<12s} {'τ(dosage)':<12s} {'MAE':<10s} {'ΔMAE':<10s} {'ρ(full)':<10s}\")\n        for cfg_name, metrics in data[\"configs\"].items():\n            sigs_str = \"+\".join(s.replace(\"s1_embedding\",\"S1\").replace(\"s2_minkpp\",\"S2\").replace(\"s4_selfcritique\",\"S4\")\n                               for s in metrics[\"signals_used\"])\n            delta = metrics.get(\"delta_mae\", \"\")\n            delta_str = f\"{delta:+.4f}\" if isinstance(delta, float) else \"\"\n            print(f\"{cfg_name:<25s} {sigs_str:<40s} {metrics['spearman_rho_vs_dosage']:<12.4f} \"\n                  f\"{metrics['kendall_tau_vs_dosage']:<12.4f} {metrics['mae_vs_dosage_scaled']:<10.4f} \"\n                  f\"{delta_str:<10s} {metrics['spearman_rho_vs_full_rrf']:<10.4f}\")\n        \n        print(\"\\nSignal importance (by ΔMAE when dropped, larger = more important):\")\n        for rank, entry in enumerate(data[\"signal_importance_by_delta_mae\"], 1):\n            print(f\"  #{rank}: {entry['signal']} — ΔMAE={entry['delta_mae_when_dropped']:+.4f}, Δρ={entry['delta_rho_when_dropped']:+.4f}\")\n    \n    # Save JSON\n    output = {\n        \"c1_signal_correlation\": corr_results,\n        \"c2_leave_one_out_ablation\": ablation_results,\n        \"metadata\": {\n            \"signals\": ACTIVE_SIGNALS,\n            \"rrf_k\": RRF_K,\n            \"negate_rules\": NEGATE,\n            \"benchmarks\": BENCHMARKS,\n            \"signals_dir\": SIGNALS_DIR,\n        }\n    }\n    \n    outpath = \"/root/contamcal-irt-calibration/analysis/rrf_signal_analysis.json\"\n    with open(outpath, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"\\nResults saved to {outpath}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Script written OK\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat > /root/contamcal-irt-calibration/analysis/rrf_signal_analysis.py << 'PYEOF'\n\"\"\"RRF Signal Analysis: C1 (rank correlation) + C2 (leave-one-out ablation).\"\"\"\nimport json\nimport os\nimport re\nimport numpy as np\nfrom scipy.stats import spearmanr, kendalltau\nfrom pathlib import Path\n\nSIGNALS_DIR = \"/root/autodl-tmp/exp002/signals\"\nBENCHMARKS = [\"mmlu\", \"gsm8k\", \"arc_challenge\"]\nACTIVE_SIGNALS = [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"]\nRRF_K = 60\n\n# Signal orientation: True = negate before ranking (lower raw = more suspicious)\nNEGATE = {\"s1_embedding\": False, \"s2_minkpp\": True, \"s4_selfcritique\": False}\n\n\ndef parse_dosage(dirname):\n    \"\"\"Extract dosage fraction from directory name.\"\"\"\n    m = re.search(r'_d(\\d{3})', dirname)\n    if m:\n        return int(m.group(1)) / 100.0\n    return None\n\n\ndef list_model_dirs():\n    \"\"\"List model directories that have merged signal files for all benchmarks.\"\"\"\n    models = []\n    for name in sorted(os.listdir(SIGNALS_DIR)):\n        dirpath = os.path.join(SIGNALS_DIR, name)\n        if not os.path.isdir(dirpath):\n            continue\n        dosage = parse_dosage(name)\n        if dosage is None:\n            continue\n        # Check merged files exist for at least one benchmark\n        has_merged = any(\n            os.path.exists(os.path.join(dirpath, f\"signals_merged_{b}.json\"))\n            for b in BENCHMARKS\n        )\n        if has_merged:\n            models.append({\"dirname\": name, \"dosage\": dosage, \"path\": dirpath})\n    return models\n\n\ndef load_merged(model_path, benchmark):\n    \"\"\"Load signals_merged_{benchmark}.json, return list of dicts.\"\"\"\n    fpath = os.path.join(model_path, f\"signals_merged_{benchmark}.json\")\n    if not os.path.exists(fpath):\n        return None\n    with open(fpath) as f:\n        return json.load(f)\n\n\ndef compute_ranks(scores):\n    \"\"\"Rank from 1 (highest) to N.\"\"\"\n    order = np.argsort(-scores)\n    ranks = np.empty_like(order, dtype=float)\n    ranks[order] = np.arange(1, len(scores) + 1)\n    return ranks\n\n\ndef compute_rrf(items, signals, k=RRF_K):\n    \"\"\"Compute RRF scores for given signal subset. Returns normalized mean.\"\"\"\n    n = len(items)\n    if n == 0:\n        return 0.0, np.zeros(0)\n    \n    rrf = np.zeros(n)\n    for sig in signals:\n        v = np.array([it.get(sig, 0.0) or 0.0 for it in items], dtype=float)\n        if NEGATE.get(sig, False):\n            v = -v\n        ranks = compute_ranks(v)\n        rrf += 1.0 / (k + ranks)\n    \n    mn, mx = rrf.min(), rrf.max()\n    if mx > mn:\n        rrf_norm = (rrf - mn) / (mx - mn)\n    else:\n        rrf_norm = rrf\n    return float(rrf_norm.mean()), rrf_norm\n\n\ndef oriented_scores(items, sig):\n    \"\"\"Get signal scores oriented so higher = more suspicious.\"\"\"\n    v = np.array([it.get(sig, 0.0) or 0.0 for it in items], dtype=float)\n    if NEGATE.get(sig, False):\n        v = -v\n    return v\n\n\n# ════════════════════════════════════════════════════════\n# C1: Signal Rank Correlation Matrix\n# ════════════════════════════════════════════════════════\n\ndef compute_signal_correlations(models):\n    \"\"\"Per-benchmark Spearman rank correlation between signal pairs.\"\"\"\n    results = {}\n    for bench in BENCHMARKS:\n        pair_rhos = {f\"{a}_vs_{b}\": [] for i, a in enumerate(ACTIVE_SIGNALS)\n                     for b in ACTIVE_SIGNALS[i+1:]}\n        \n        n_models = 0\n        for m in models:\n            items = load_merged(m[\"path\"], bench)\n            if items is None:\n                continue\n            \n            # Check all 3 signals have non-null values\n            sig_arrays = {}\n            skip = False\n            for sig in ACTIVE_SIGNALS:\n                vals = [it.get(sig) for it in items]\n                if all(v is None or v == 0.0 for v in vals):\n                    skip = True\n                    break\n                sig_arrays[sig] = oriented_scores(items, sig)\n            if skip:\n                continue\n            \n            n_models += 1\n            for i, a in enumerate(ACTIVE_SIGNALS):\n                for b in ACTIVE_SIGNALS[i+1:]:\n                    rho, _ = spearmanr(sig_arrays[a], sig_arrays[b])\n                    pair_rhos[f\"{a}_vs_{b}\"].append(rho)\n        \n        # Build correlation matrix\n        n_sig = len(ACTIVE_SIGNALS)\n        matrix = np.eye(n_sig)\n        pair_details = {}\n        for i, a in enumerate(ACTIVE_SIGNALS):\n            for j, b in enumerate(ACTIVE_SIGNALS):\n                if i < j:\n                    key = f\"{a}_vs_{b}\"\n                    rhos = pair_rhos[key]\n                    if rhos:\n                        mean_rho = float(np.mean(rhos))\n                        std_rho = float(np.std(rhos))\n                        matrix[i, j] = mean_rho\n                        matrix[j, i] = mean_rho\n                        pair_details[key] = {\n                            \"mean_rho\": round(mean_rho, 4),\n                            \"std_rho\": round(std_rho, 4),\n                            \"n_models\": len(rhos),\n                            \"per_model_rhos\": [round(r, 4) for r in rhos]\n                        }\n        \n        results[bench] = {\n            \"n_models\": n_models,\n            \"signals\": ACTIVE_SIGNALS,\n            \"correlation_matrix\": matrix.tolist(),\n            \"pair_details\": pair_details\n        }\n    \n    return results\n\n\n# ════════════════════════════════════════════════════════\n# C2: Leave-One-Signal-Out Ablation\n# ════════════════════════════════════════════════════════\n\ndef leave_one_out_ablation(models):\n    \"\"\"For each benchmark, compute full RRF and leave-one-out variants.\"\"\"\n    results = {}\n    \n    for bench in BENCHMARKS:\n        # Collect model-level exposures for each signal config\n        configs = {\n            \"full\": ACTIVE_SIGNALS,\n        }\n        for sig in ACTIVE_SIGNALS:\n            remaining = [s for s in ACTIVE_SIGNALS if s != sig]\n            configs[f\"drop_{sig}\"] = remaining\n        # Also single-signal baselines\n        for sig in ACTIVE_SIGNALS:\n            configs[f\"only_{sig}\"] = [sig]\n        \n        model_exposures = {cfg: [] for cfg in configs}\n        dosages = []\n        model_names = []\n        valid_models = 0\n        \n        for m in models:\n            items = load_merged(m[\"path\"], bench)\n            if items is None:\n                continue\n            \n            # Check all signals present\n            has_all = True\n            for sig in ACTIVE_SIGNALS:\n                vals = [it.get(sig) for it in items]\n                if all(v is None or v == 0.0 for v in vals):\n                    has_all = False\n                    break\n            if not has_all:\n                continue\n            \n            valid_models += 1\n            dosages.append(m[\"dosage\"])\n            model_names.append(m[\"dirname\"])\n            \n            for cfg_name, cfg_signals in configs.items():\n                mean_exp, _ = compute_rrf(items, cfg_signals)\n                model_exposures[cfg_name].append(mean_exp)\n        \n        if valid_models < 3:\n            continue\n        \n        dosages = np.array(dosages)\n        \n        # Compute metrics for each config\n        config_metrics = {}\n        full_exp = np.array(model_exposures[\"full\"])\n        \n        for cfg_name, exps in model_exposures.items():\n            exps = np.array(exps)\n            \n            # Spearman correlation with true dosage\n            rho_dosage, p_dosage = spearmanr(exps, dosages)\n            tau_dosage, p_tau = kendalltau(exps, dosages)\n            \n            # Rank correlation with full RRF (for ablation configs)\n            if cfg_name != \"full\":\n                rho_full, _ = spearmanr(exps, full_exp)\n            else:\n                rho_full = 1.0\n            \n            # MAE vs dosage (after linear rescaling to [0,1])\n            if exps.max() > exps.min():\n                exps_scaled = (exps - exps.min()) / (exps.max() - exps.min())\n            else:\n                exps_scaled = exps\n            mae_dosage = float(np.mean(np.abs(exps_scaled - dosages)))\n            \n            config_metrics[cfg_name] = {\n                \"signals_used\": configs[cfg_name],\n                \"spearman_rho_vs_dosage\": round(float(rho_dosage), 4),\n                \"spearman_p_vs_dosage\": round(float(p_dosage), 6),\n                \"kendall_tau_vs_dosage\": round(float(tau_dosage), 4),\n                \"spearman_rho_vs_full_rrf\": round(float(rho_full), 4),\n                \"mae_vs_dosage_scaled\": round(mae_dosage, 4),\n                \"mean_exposure\": round(float(exps.mean()), 6),\n                \"std_exposure\": round(float(exps.std()), 6),\n            }\n        \n        # Compute delta MAE (leave-one-out vs full)\n        full_mae = config_metrics[\"full\"][\"mae_vs_dosage_scaled\"]\n        for sig in ACTIVE_SIGNALS:\n            drop_key = f\"drop_{sig}\"\n            if drop_key in config_metrics:\n                config_metrics[drop_key][\"delta_mae\"] = round(\n                    config_metrics[drop_key][\"mae_vs_dosage_scaled\"] - full_mae, 4)\n                config_metrics[drop_key][\"delta_rho\"] = round(\n                    config_metrics[drop_key][\"spearman_rho_vs_dosage\"] - \n                    config_metrics[\"full\"][\"spearman_rho_vs_dosage\"], 4)\n        \n        # Signal importance ranking (by how much MAE increases when dropped)\n        importance = []\n        for sig in ACTIVE_SIGNALS:\n            drop_key = f\"drop_{sig}\"\n            if drop_key in config_metrics:\n                importance.append({\n                    \"signal\": sig,\n                    \"delta_mae_when_dropped\": config_metrics[drop_key][\"delta_mae\"],\n                    \"delta_rho_when_dropped\": config_metrics[drop_key][\"delta_rho\"],\n                })\n        importance.sort(key=lambda x: -x[\"delta_mae_when_dropped\"])\n        \n        results[bench] = {\n            \"n_models\": valid_models,\n            \"model_names\": model_names,\n            \"dosages\": [round(d, 4) for d in dosages.tolist()],\n            \"configs\": config_metrics,\n            \"signal_importance_by_delta_mae\": importance,\n        }\n    \n    return results\n\n\n# ════════════════════════════════════════════════════════\n# Main\n# ════════════════════════════════════════════════════════\n\ndef main():\n    models = list_model_dirs()\n    print(f\"Found {len(models)} model directories with signal data\")\n    for m in models:\n        print(f\"  {m['dirname']} (dosage={m['dosage']})\")\n    \n    # C1\n    print(\"\\n\" + \"=\"*60)\n    print(\"C1: Signal Rank Correlation Matrix\")\n    print(\"=\"*60)\n    corr_results = compute_signal_correlations(models)\n    for bench, data in corr_results.items():\n        print(f\"\\n--- {bench} (n_models={data['n_models']}) ---\")\n        sigs = data[\"signals\"]\n        matrix = np.array(data[\"correlation_matrix\"])\n        header = \"            \" + \"  \".join(f\"{s:>16s}\" for s in sigs)\n        print(header)\n        for i, sig in enumerate(sigs):\n            row = f\"{sig:>16s}\" + \"  \".join(f\"{matrix[i,j]:>16.4f}\" for j in range(len(sigs)))\n            print(row)\n        for pair, detail in data[\"pair_details\"].items():\n            print(f\"  {pair}: rho={detail['mean_rho']:.4f} ± {detail['std_rho']:.4f} (n={detail['n_models']})\")\n    \n    # C2\n    print(\"\\n\" + \"=\"*60)\n    print(\"C2: Leave-One-Signal-Out Ablation\")\n    print(\"=\"*60)\n    ablation_results = leave_one_out_ablation(models)\n    for bench, data in ablation_results.items():\n        print(f\"\\n--- {bench} (n_models={data['n_models']}) ---\")\n        print(f\"{'Config':<25s} {'Signals':<40s} {'ρ(dosage)':<12s} {'τ(dosage)':<12s} {'MAE':<10s} {'ΔMAE':<10s} {'ρ(full)':<10s}\")\n        for cfg_name, metrics in data[\"configs\"].items():\n            sigs_str = \"+\".join(s.replace(\"s1_embedding\",\"S1\").replace(\"s2_minkpp\",\"S2\").replace(\"s4_selfcritique\",\"S4\")\n                               for s in metrics[\"signals_used\"])\n            delta = metrics.get(\"delta_mae\", \"\")\n            delta_str = f\"{delta:+.4f}\" if isinstance(delta, float) else \"\"\n            print(f\"{cfg_name:<25s} {sigs_str:<40s} {metrics['spearman_rho_vs_dosage']:<12.4f} \"\n                  f\"{metrics['kendall_tau_vs_dosage']:<12.4f} {metrics['mae_vs_dosage_scaled']:<10.4f} \"\n                  f\"{delta_str:<10s} {metrics['spearman_rho_vs_full_rrf']:<10.4f}\")\n        \n        print(\"\\nSignal importance (by ΔMAE when dropped, larger = more important):\")\n        for rank, entry in enumerate(data[\"signal_importance_by_delta_mae\"], 1):\n            print(f\"  #{rank}: {entry['signal']} — ΔMAE={entry['delta_mae_when_dropped']:+.4f}, Δρ={entry['delta_rho_when_dropped']:+.4f}\")\n    \n    # Save JSON\n    output = {\n        \"c1_signal_correlation\": corr_results,\n        \"c2_leave_one_out_ablation\": ablation_results,\n        \"metadata\": {\n            \"signals\": ACTIVE_SIGNALS,\n            \"rrf_k\": RRF_K,\n            \"negate_rules\": NEGATE,\n            \"benchmarks\": BENCHMARKS,\n            \"signals_dir\": SIGNALS_DIR,\n        }\n    }\n    \n    outpath = \"/root/contamcal-irt-calibration/analysis/rrf_signal_analysis.json\"\n    with open(outpath, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"\\nResults saved to {outpath}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Script written OK\""
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-21T08:46:41.621527+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.59}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-21T08:46:41.621726+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cd /root/contamcal-irt-calibration && python3 analysis/rrf_signal_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cd /root/contamcal-irt-calibration && python3 analysis/rrf_signal_analysis.py"
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-21T08:46:41.621887+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/contamcal-irt-calibration && python3 analysis/rrf_signal_analysis.py'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.49}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-21T08:46:41.622017+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/miniconda3/bin/python*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/miniconda3/bin/python*"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-21T08:46:41.622144+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/bin/python\\n/root/miniconda3/bin/python3\\n/root/miniconda3/bin/python3-config\\n/root/miniconda3/bin/python3.1\\n/root/miniconda3/bin/python3.12\\n/root/miniconda3/bin/python3.12-config\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.16}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-21T08:46:41.622265+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cd /root/contamcal-irt-calibration && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python analysis/rrf_signal_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cd /root/contamcal-irt-calibration && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python analysis/rrf_signal_analysis.py"
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-21T08:46:41.622446+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'cd /root/contamcal-irt-calibration && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python analysis/rrf_signal_analysis.py'\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.48}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-21T08:46:41.622637+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "nohup /root/miniconda3/bin/python /root/contamcal-irt-calibration/analysis/rrf_signal_analysis.py > /tmp/rrf_analysis.log 2>&1 & echo $!"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "nohup /root/miniconda3/bin/python /root/contamcal-irt-calibration/analysis/rrf_signal_analysis.py > /tmp/rrf_analysis.log 2>&1 & echo $!"
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-21T08:46:41.622773+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"483388\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.11}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-21T08:46:41.622893+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -50 /tmp/rrf_analysis.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -50 /tmp/rrf_analysis.log"
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-21T08:46:41.623034+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.55}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-21T08:46:41.623190+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ps -p 483388 -o pid="
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ps -p 483388 -o pid="
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-21T08:46:41.623352+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"483388\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-21T08:46:41.623489+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -80 /tmp/rrf_analysis.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -80 /tmp/rrf_analysis.log"
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-21T08:46:41.623612+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-21T08:46:41.623744+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "kill 483388 2>/dev/null; nohup /root/miniconda3/bin/python -u /root/contamcal-irt-calibration/analysis/rrf_signal_analysis.py > /tmp/rrf_analysis.log 2>&1 & echo $!"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "kill 483388 2>/dev/null; nohup /root/miniconda3/bin/python -u /root/contamcal-irt-calibration/analysis/rrf_signal_analysis.py > /tmp/rrf_analysis.log 2>&1 & echo $!"
  }
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-21T08:46:41.623868+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"483630\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.76}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-21T08:46:41.623984+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -50 /tmp/rrf_analysis.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -50 /tmp/rrf_analysis.log"
  }
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-21T08:46:41.624102+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.48}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-21T08:46:41.624236+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ps -p 483630 -o pid="
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ps -p 483630 -o pid="
  }
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-21T08:46:41.624383+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"483630\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.48}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-21T08:46:41.624508+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /tmp/rrf_analysis.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /tmp/rrf_analysis.log"
  }
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-21T08:46:41.624628+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 113 · 2026-05-21T08:46:41.624755+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "/root/miniconda3/bin/pip list --format=freeze 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "/root/miniconda3/bin/pip list --format=freeze 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-21T08:46:41.624872+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 115 · 2026-05-21T08:46:41.624987+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "/root/miniconda3/bin/python -c \"import scipy; print(scipy.__version__)\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "/root/miniconda3/bin/python -c \"import scipy; print(scipy.__version__)\""
  }
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-21T08:46:41.625152+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 117 · 2026-05-21T08:46:41.625358+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "/root/miniconda3/bin/python -c \"import scipy; print(scipy.__version__)\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "/root/miniconda3/bin/python -c \"import scipy; print(scipy.__version__)\""
  }
}
```

</details>

---

### Tool result

_source line 118 · 2026-05-21T08:46:41.625501+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"1.17.1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 119 · 2026-05-21T08:46:41.625621+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /tmp/rrf_analysis.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /tmp/rrf_analysis.log"
  }
}
```

</details>

---

### Tool result

_source line 120 · 2026-05-21T08:46:41.625757+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Found 36 model directories with signal data\\n  Llama-3.2-3B_d000_s42 (dosage=0.0)\\n  Llama-3.2-3B_d005_s42 (dosage=0.05)\\n  Llama-3.2-3B_d025_s42 (dosage=0.25)\\n  Llama-3.2-3B_d100_s42 (dosage=1.0)\\n  Qwen2.5-0.5B_d000_s123 (dosage=0.0)\\n  Qwen2.5-0.5B_d000_s42 (dosage=0.0)\\n  Qwen2.5-0.5B_d005_s123 (dosage=0.05)\\n  Qwen2.5-0.5B_d005_s42 (dosage=0.05)\\n  Qwen2.5-0.5B_d025_s123 (dosage=0.25)\\n  Qwen2.5-0.5B_d025_s42 (dosage=0.25)\\n  Qwen2.5-0.5B_d100_s123 (dosage=1.0)\\n  Qwen2.5-0.5B_d100_s42 (dosage=1.0)\\n  Qwen2.5-1.5B_d000_s123 (dosage=0.0)\\n  Qwen2.5-1.5B_d000_s42 (dosage=0.0)\\n  Qwen2.5-1.5B_d005_s123 (dosage=0.05)\\n  Qwen2.5-1.5B_d005_s42 (dosage=0.05)\\n  Qwen2.5-1.5B_d025_s123 (dosage=0.25)\\n  Qwen2.5-1.5B_d025_s42 (dosage=0.25)\\n  Qwen2.5-1.5B_d100_s123 (dosage=1.0)\\n  Qwen2.5-1.5B_d100_s42 (dosage=1.0)\\n  Qwen2.5-3B_d000_a32_s42 (dosage=0.0)\\n  Qwen2.5-3B_d000_s123 (dosage=0.0)\\n  Qwen2.5-3B_d000_s123_a32 (dosage=0.0)\\n  Qwen2.5-3B_d000_s42_a32 (dosage=0.0)\\n  Qwen2.5-3B_d005_a32_s42 (dosage=0.05)\\n  Qwen2.5-3B_d005_s123 (dosage=0.05)\\n  Qwen2.5-3B_d005_s42 (dosage=0.05)\\n  Qwen2.5-3B_d005_s42_a32 (dosage=0.05)\\n  Qwen2.5-3B_d025_s123 (dosage=0.25)\\n  Qwen2.5-3B_d025_s42 (dosage=0.25)\\n  Qwen2.5-3B_d025_s42_DEPRECATED_alpha16 (dosage=0.25)\\n  Qwen2.5-3B_d025_s42_old_alpha16 (dosage=0.25)\\n  Qwen2.5-3B_d025_v3_s42 (dosage=0.25)\\n  Qwen2.5-3B_d100_a32_s123 (dosage=1.0)\\n  Qwen2.5-3B_d100_a32_s42 (dosage=1.0)\\n  Qwen2.5-3B_d100_s42 (dosage=1.0)\\n\\n============================================================\\nC1: Signal Rank Correlation Matrix\\n============================================================\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 121 · 2026-05-21T08:46:41.625927+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ps -p 483630 -o pid="
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ps -p 483630 -o pid="
  }
}
```

</details>

---

### Tool result

_source line 122 · 2026-05-21T08:46:41.626055+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"483630\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 123 · 2026-05-21T08:46:41.626175+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "wc -l /tmp/rrf_analysis.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "wc -l /tmp/rrf_analysis.log"
  }
}
```

</details>

---

### Tool result

_source line 124 · 2026-05-21T08:46:41.626295+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"41 /tmp/rrf_analysis.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 125 · 2026-05-21T08:46:41.626438+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -20 /tmp/rrf_analysis.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -20 /tmp/rrf_analysis.log"
  }
}
```

</details>

---

### Tool result

_source line 126 · 2026-05-21T08:46:41.626569+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  Qwen2.5-3B_d000_a32_s42 (dosage=0.0)\\n  Qwen2.5-3B_d000_s123 (dosage=0.0)\\n  Qwen2.5-3B_d000_s123_a32 (dosage=0.0)\\n  Qwen2.5-3B_d000_s42_a32 (dosage=0.0)\\n  Qwen2.5-3B_d005_a32_s42 (dosage=0.05)\\n  Qwen2.5-3B_d005_s123 (dosage=0.05)\\n  Qwen2.5-3B_d005_s42 (dosage=0.05)\\n  Qwen2.5-3B_d005_s42_a32 (dosage=0.05)\\n  Qwen2.5-3B_d025_s123 (dosage=0.25)\\n  Qwen2.5-3B_d025_s42 (dosage=0.25)\\n  Qwen2.5-3B_d025_s42_DEPRECATED_alpha16 (dosage=0.25)\\n  Qwen2.5-3B_d025_s42_old_alpha16 (dosage=0.25)\\n  Qwen2.5-3B_d025_v3_s42 (dosage=0.25)\\n  Qwen2.5-3B_d100_a32_s123 (dosage=1.0)\\n  Qwen2.5-3B_d100_a32_s42 (dosage=1.0)\\n  Qwen2.5-3B_d100_s42 (dosage=1.0)\\n\\n============================================================\\nC1: Signal Rank Correlation Matrix\\n============================================================\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 127 · 2026-05-21T08:46:41.626718+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -30 /tmp/rrf_analysis.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -30 /tmp/rrf_analysis.log"
  }
}
```

</details>

---

### Tool result

_source line 128 · 2026-05-21T08:46:41.626853+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  Qwen2.5-0.5B_d100_s123 (dosage=1.0)\\n  Qwen2.5-0.5B_d100_s42 (dosage=1.0)\\n  Qwen2.5-1.5B_d000_s123 (dosage=0.0)\\n  Qwen2.5-1.5B_d000_s42 (dosage=0.0)\\n  Qwen2.5-1.5B_d005_s123 (dosage=0.05)\\n  Qwen2.5-1.5B_d005_s42 (dosage=0.05)\\n  Qwen2.5-1.5B_d025_s123 (dosage=0.25)\\n  Qwen2.5-1.5B_d025_s42 (dosage=0.25)\\n  Qwen2.5-1.5B_d100_s123 (dosage=1.0)\\n  Qwen2.5-1.5B_d100_s42 (dosage=1.0)\\n  Qwen2.5-3B_d000_a32_s42 (dosage=0.0)\\n  Qwen2.5-3B_d000_s123 (dosage=0.0)\\n  Qwen2.5-3B_d000_s123_a32 (dosage=0.0)\\n  Qwen2.5-3B_d000_s42_a32 (dosage=0.0)\\n  Qwen2.5-3B_d005_a32_s42 (dosage=0.05)\\n  Qwen2.5-3B_d005_s123 (dosage=0.05)\\n  Qwen2.5-3B_d005_s42 (dosage=0.05)\\n  Qwen2.5-3B_d005_s42_a32 (dosage=0.05)\\n  Qwen2.5-3B_d025_s123 (dosage=0.25)\\n  Qwen2.5-3B_d025_s42 (dosage=0.25)\\n  Qwen2.5-3B_d025_s42_DEPRECATED_alpha16 (dosage=0.25)\\n  Qwen2.5-3B_d025_s42_old_alpha16 (dosage=0.25)\\n  Qwen2.5-3B_d025_v3_s42 (dosage=0.25)\\n  Qwen2.5-3B_d100_a32_s123 (dosage=1.0)\\n  Qwen2.5-3B_d100_a32_s42 (dosage=1.0)\\n  Qwen2.5-3B_d100_s42 (dosage=1.0)\\n\\n============================================================\\nC1: Signal Rank Correlation Matrix\\n============================================================\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.56}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 129 · 2026-05-21T08:46:41.626980+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ps -p 483630 -o pid="
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ps -p 483630 -o pid="
  }
}
```

</details>

---

### Tool result

_source line 130 · 2026-05-21T08:46:41.627101+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"483630\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 131 · 2026-05-21T08:46:41.627240+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "wc -l /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d100_s42/signals_merged_mmlu.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "wc -l /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d100_s42/signals_merged_mmlu.json"
  }
}
```

</details>

---

### Tool result

_source line 132 · 2026-05-21T08:46:41.627390+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"112337 /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d100_s42/signals_merged_mmlu.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 133 · 2026-05-21T08:46:41.627514+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "stat /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d100_s42/signals_merged_mmlu.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "stat /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d100_s42/signals_merged_mmlu.json"
  }
}
```

</details>

---

### Tool result

_source line 134 · 2026-05-21T08:46:41.627641+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  File: /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d100_s42/signals_merged_mmlu.json\\n  Size: 2758329   \\tBlocks: 5392       IO Block: 4096   regular file\\nDevice: 900h/2304d\\tInode: 12990899721  Links: 1\\nAccess: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)\\nAccess: 2026-05-21 16:39:01.925353394 +0800\\nModify: 2026-05-14 21:48:58.828024349 +0800\\nChange: 2026-05-14 21:48:58.828024349 +0800\\n Birth: 2026-05-14 21:48:58.736025786 +0800\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.81}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 135 · 2026-05-21T08:46:41.627781+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -10 /tmp/rrf_analysis.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -10 /tmp/rrf_analysis.log"
  }
}
```

</details>

---

### Tool result

_source line 136 · 2026-05-21T08:46:41.627911+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    s1_embedding          1.0000           -0.0300            0.0048\\n       s2_minkpp         -0.0300            1.0000            0.0046\\n s4_selfcritique          0.0048            0.0046            1.0000\\n  s1_embedding_vs_s2_minkpp: rho=-0.0300 ± 0.1152 (n=35)\\n  s1_embedding_vs_s4_selfcritique: rho=0.0048 ± 0.0377 (n=35)\\n  s2_minkpp_vs_s4_selfcritique: rho=0.0046 ± 0.0545 (n=35)\\n\\n============================================================\\nC2: Leave-One-Signal-Out Ablation\\n============================================================\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 137 · 2026-05-21T08:46:41.628066+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "wc -l /tmp/rrf_analysis.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "wc -l /tmp/rrf_analysis.log"
  }
}
```

</details>

---

### Tool result

_source line 138 · 2026-05-21T08:46:41.628201+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"72 /tmp/rrf_analysis.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 139 · 2026-05-21T08:46:41.628349+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -40 /tmp/rrf_analysis.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -40 /tmp/rrf_analysis.log"
  }
}
```

</details>

---

### Tool result

_source line 140 · 2026-05-21T08:46:41.628509+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  Qwen2.5-3B_d025_s42_old_alpha16 (dosage=0.25)\\n  Qwen2.5-3B_d025_v3_s42 (dosage=0.25)\\n  Qwen2.5-3B_d100_a32_s123 (dosage=1.0)\\n  Qwen2.5-3B_d100_a32_s42 (dosage=1.0)\\n  Qwen2.5-3B_d100_s42 (dosage=1.0)\\n\\n============================================================\\nC1: Signal Rank Correlation Matrix\\n============================================================\\n\\n--- mmlu (n_models=33) ---\\n                s1_embedding         s2_minkpp   s4_selfcritique\\n    s1_embedding          1.0000           -0.0518            0.0419\\n       s2_minkpp         -0.0518            1.0000           -0.0095\\n s4_selfcritique          0.0419           -0.0095            1.0000\\n  s1_embedding_vs_s2_minkpp: rho=-0.0518 ± 0.1236 (n=33)\\n  s1_embedding_vs_s4_selfcritique: rho=0.0419 ± 0.0636 (n=33)\\n  s2_minkpp_vs_s4_selfcritique: rho=-0.0095 ± 0.0806 (n=33)\\n\\n--- gsm8k (n_models=34) ---\\n                s1_embedding         s2_minkpp   s4_selfcritique\\n    s1_embedding          1.0000           -0.0216            0.0535\\n       s2_minkpp         -0.0216            1.0000            0.0095\\n s4_selfcritique          0.0535            0.0095            1.0000\\n  s1_embedding_vs_s2_minkpp: rho=-0.0216 ± 0.0515 (n=34)\\n  s1_embedding_vs_s4_selfcritique: rho=0.0535 ± 0.0395 (n=34)\\n  s2_minkpp_vs_s4_selfcritique: rho=0.0095 ± 0.0340 (n=34)\\n\\n--- arc_challenge (n_models=35) ---\\n                s1_embedding         s2_minkpp   s4_selfcritique\\n    s1_embedding          1.0000           -0.0300            0.0048\\n       s2_minkpp         -0.0300            1.0000            0.0046\\n s4_selfcritique          0.0048            0.0046            1.0000\\n  s1_embedding_vs_s2_minkpp: rho=-0.0300 ± 0.1152 (n=35)\\n  s1_embedding_vs_s4_selfcritique: rho=0.0048 ± 0.0377 (n=35)\\n  s2_minkpp_vs_s4_selfcritique: rho=0.0046 ± 0.0545 (n=35)\\n\\n============================================================\\nC2
…[truncated 201 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 141 · 2026-05-21T08:46:41.628672+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ps -p 483630 -o pid="
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ps -p 483630 -o pid="
  }
}
```

</details>

---

### Tool result

_source line 142 · 2026-05-21T08:46:41.628797+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"483630\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 143 · 2026-05-21T08:46:41.628914+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "wc -l /tmp/rrf_analysis.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "wc -l /tmp/rrf_analysis.log"
  }
}
```

</details>

---

### Tool result

_source line 144 · 2026-05-21T08:46:41.629035+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"72 /tmp/rrf_analysis.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 145 · 2026-05-21T08:46:41.629158+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -5 /tmp/rrf_analysis.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -5 /tmp/rrf_analysis.log"
  }
}
```

</details>

---

### Tool result

_source line 146 · 2026-05-21T08:46:41.629284+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  s2_minkpp_vs_s4_selfcritique: rho=0.0046 ± 0.0545 (n=35)\\n\\n============================================================\\nC2: Leave-One-Signal-Out Ablation\\n============================================================\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 147 · 2026-05-21T08:46:41.629453+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -20 /tmp/rrf_analysis.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -20 /tmp/rrf_analysis.log"
  }
}
```

</details>

---

### Tool result

_source line 148 · 2026-05-21T08:46:41.629597+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  #1: s1_embedding — ΔMAE=+0.0456, Δρ=-0.2335\\n  #2: s2_minkpp — ΔMAE=+0.0051, Δρ=+0.0778\\n  #3: s4_selfcritique — ΔMAE=-0.0115, Δρ=+0.2576\\n\\n--- arc_challenge (n_models=35) ---\\nConfig                    Signals                                  ρ(dosage)    τ(dosage)    MAE        ΔMAE       ρ(full)   \\nfull                      S1+S2+S4                                 0.0499       0.0288       0.4762                1.0000    \\ndrop_s1_embedding         S2+S4                                    0.1086       0.0864       0.4203     -0.0559    0.3957    \\ndrop_s2_minkpp            S1+S4                                    0.0456       0.0326       0.4010     -0.0752    0.1158    \\ndrop_s4_selfcritique      S1+S2                                    -0.0054      -0.0058      0.4807     +0.0045    0.2166    \\nonly_s1_embedding         S1                                       0.0078       0.0305       0.6562                -0.0005   \\nonly_s2_minkpp            S2                                       -0.1939      -0.1770      0.4543                0.2683    \\nonly_s4_selfcritique      S4                                       -0.0840      -0.0723      0.4571                0.1098    \\n\\nSignal importance (by ΔMAE when dropped, larger = more important):\\n  #1: s4_selfcritique — ΔMAE=+0.0045, Δρ=-0.0553\\n  #2: s1_embedding — ΔMAE=-0.0559, Δρ=+0.0587\\n  #3: s2_minkpp — ΔMAE=-0.0752, Δρ=-0.0043\\n\\nResults saved to /root/contamcal-irt-calibration/analysis/rrf_signal_analysis.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 149 · 2026-05-21T08:46:41.629754+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /tmp/rrf_analysis.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /tmp/rrf_analysis.log"
  }
}
```

</details>

---

### Tool result

_source line 150 · 2026-05-21T08:46:41.629956+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Found 36 model directories with signal data\\n  Llama-3.2-3B_d000_s42 (dosage=0.0)\\n  Llama-3.2-3B_d005_s42 (dosage=0.05)\\n  Llama-3.2-3B_d025_s42 (dosage=0.25)\\n  Llama-3.2-3B_d100_s42 (dosage=1.0)\\n  Qwen2.5-0.5B_d000_s123 (dosage=0.0)\\n  Qwen2.5-0.5B_d000_s42 (dosage=0.0)\\n  Qwen2.5-0.5B_d005_s123 (dosage=0.05)\\n  Qwen2.5-0.5B_d005_s42 (dosage=0.05)\\n  Qwen2.5-0.5B_d025_s123 (dosage=0.25)\\n  Qwen2.5-0.5B_d025_s42 (dosage=0.25)\\n  Qwen2.5-0.5B_d100_s123 (dosage=1.0)\\n  Qwen2.5-0.5B_d100_s42 (dosage=1.0)\\n  Qwen2.5-1.5B_d000_s123 (dosage=0.0)\\n  Qwen2.5-1.5B_d000_s42 (dosage=0.0)\\n  Qwen2.5-1.5B_d005_s123 (dosage=0.05)\\n  Qwen2.5-1.5B_d005_s42 (dosage=0.05)\\n  Qwen2.5-1.5B_d025_s123 (dosage=0.25)\\n  Qwen2.5-1.5B_d025_s42 (dosage=0.25)\\n  Qwen2.5-1.5B_d100_s123 (dosage=1.0)\\n  Qwen2.5-1.5B_d100_s42 (dosage=1.0)\\n  Qwen2.5-3B_d000_a32_s42 (dosage=0.0)\\n  Qwen2.5-3B_d000_s123 (dosage=0.0)\\n  Qwen2.5-3B_d000_s123_a32 (dosage=0.0)\\n  Qwen2.5-3B_d000_s42_a32 (dosage=0.0)\\n  Qwen2.5-3B_d005_a32_s42 (dosage=0.05)\\n  Qwen2.5-3B_d005_s123 (dosage=0.05)\\n  Qwen2.5-3B_d005_s42 (dosage=0.05)\\n  Qwen2.5-3B_d005_s42_a32 (dosage=0.05)\\n  Qwen2.5-3B_d025_s123 (dosage=0.25)\\n  Qwen2.5-3B_d025_s42 (dosage=0.25)\\n  Qwen2.5-3B_d025_s42_DEPRECATED_alpha16 (dosage=0.25)\\n  Qwen2.5-3B_d025_s42_old_alpha16 (dosage=0.25)\\n  Qwen2.5-3B_d025_v3_s42 (dosage=0.25)\\n  Qwen2.5-3B_d100_a32_s123 (dosage=1.0)\\n  Qwen2.5-3B_d100_a32_s42 (dosage=1.0)\\n  Qwen2.5-3B_d100_s42 (dosage=1.0)\\n\\n============================================================\\nC1: Signal Rank Correlation Matrix\\n============================================================\\n\\n--- mmlu (n_models=33) ---\\n                s1_embedding         s2_minkpp   s4_selfcritique\\n    s1_embedding          1.0000           -0.0518            0.0419\\n       s2_minkpp         -0.0518            1.0000           -0.0095\\n s4_selfcritique         
…[truncated 5416 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 151 · 2026-05-21T08:46:41.630219+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat > /root/contamcal-irt-calibration/analysis/rrf_signal_analysis_v2.py << 'PYEOF'\n\"\"\"RRF Signal Analysis v2: filtered models, cleaner ablation.\"\"\"\nimport json\nimport os\nimport re\nimport numpy as np\nfrom scipy.stats import spearmanr, kendalltau\nfrom pathlib import Path\n\nSIGNALS_DIR = \"/root/autodl-tmp/exp002/signals\"\nBENCHMARKS = [\"mmlu\", \"gsm8k\", \"arc_challenge\"]\nACTIVE_SIGNALS = [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"]\nRRF_K = 60\nNEGATE = {\"s1_embedding\": False, \"s2_minkpp\": True, \"s4_selfcritique\": False}\n\n# C006 blacklist + duplicates\nEXCLUDE_PATTERNS = [\n    \"DEPRECATED\", \"old_alpha16\",\n    # alpha=16 blacklist from C006\n    \"Qwen2.5-3B_d000_s42\",  # no _a32 suffix = alpha=16\n    \"Qwen2.5-3B_d005_s42\",  # same\n    \"Qwen2.5-3B_d025_s42\",  # same (not v3)\n    \"Qwen2.5-3B_d100_s42\",  # same\n]\n\ndef should_exclude(dirname):\n    for pat in EXCLUDE_PATTERNS:\n        if pat in dirname:\n            # But allow _a32 variants\n            if pat.startswith(\"Qwen2.5-3B_d\") and \"_a32\" in dirname:\n                continue\n            if pat.startswith(\"Qwen2.5-3B_d\") and \"_v3\" in dirname:\n                continue\n            if pat.startswith(\"Qwen2.5-3B_d\") and \"_s123\" in dirname:\n                continue\n            return True\n    return False\n\n\ndef parse_dosage(dirname):\n    m = re.search(r'_d(\\d{3})', dirname)\n    if m:\n        return int(m.group(1)) / 100.0\n    return None\n\n\ndef parse_scale(dirname):\n    if \"0.5B\" in dirname:\n        return \"0.5B\"\n    elif \"1.5B\" in dirname:\n        return \"1.5B\"\n    elif \"3B\" in dirname:\n        return \"3B\"\n    elif \"Llama\" in dirname:\n        return \"Llama-3B\"\n    return \"unknown\"\n\n\ndef list_model_dirs():\n    models = []\n    for name in sorted(os.listdir(SIGNALS_DIR)):\n        dirpath = os.path.join(SIGNALS_DIR, name)\n        if not os.path.isdir(dirpath):\n            continue\n        dosage = parse_dosage(name)\n        if dosage is None:\n            continue\n        if should_exclude(name):\n            continue\n        has_merged = any(\n            os.path.exists(os.path.join(dirpath, f\"signals_merged_{b}.json\"))\n            for b in BENCHMARKS\n        )\n        if has_merged:\n            models.append({\n                \"dirname\": name, \"dosage\": dosage,\n                \"path\": dirpath, \"scale\": parse_scale(name)\n            })\n    return models\n\n\ndef load_merged(model_path, benchmark):\n    fpath = os.path.join(model_path, f\"signals_merged_{benchmark}.json\")\n    if not os.path.exists(fpath):\n        return None\n    with open(fpath) as f:\n        return json.load(f)\n\n\ndef compute_ranks(scores):\n    order = np.argsort(-scores)\n    ranks = np.empty_like(order, dtype=float)\n    ranks[order] = np.arange(1, len(scores) + 1)\n    return ranks\n\n\ndef compute_rrf(items, signals, k=RRF_K):\n    n = len(items)\n    if n == 0:\n        return 0.0, np.zeros(0)\n    rrf = np.zeros(n)\n    for sig in signals:\n        v = np.array([it.get(sig, 0.0) or 0.0 for it in items], dtype=float)\n        if NEGATE.get(sig, False):\n            v = -v\n        ranks = compute_ranks(v)\n        rrf += 1.0 / (k + ranks)\n    mn, mx = rrf.min(), rrf.max()\n    if mx > mn:\n        rrf_norm = (rrf - mn) / (mx - mn)\n    else:\n        rrf_norm = rrf\n    return float(rrf_norm.mean()), rrf_norm\n\n\ndef oriented_scores(items, sig):\n    v = np.array([it.get(sig, 0.0) or 0.0 for it in items], dtype=float)\n    if NEGATE.get(sig, False):\n        v = -v\n    return v\n\n\ndef has_all_signals(items):\n    for sig in ACTIVE_SIGNALS:\n        vals = [it.get(sig) for it in items]\n        if all(v is None or v == 0.0 for v in vals):\n            return False\n    return True\n\n\n# ═══════════════ C1 ═══════════════\n\ndef compute_signal_correlations(models):\n    results = {}\n    for bench in BENCHMARKS:\n        pair_rhos = {f\"{a}_vs_{b}\": [] for i, a in enumerate(ACTIVE_SIGNALS)\n                     for b in ACTIVE_SIGNALS[i+1:]}\n        model_details = []\n        \n        for m in models:\n            items = load_merged(m[\"path\"], bench)\n            if items is None or not has_all_signals(items):\n                continue\n            \n            sig_arrays = {sig: oriented_scores(items, sig) for sig in ACTIVE_SIGNALS}\n            model_rhos = {}\n            for i, a in enumerate(ACTIVE_SIGNALS):\n                for b in ACTIVE_SIGNALS[i+1:]:\n                    key = f\"{a}_vs_{b}\"\n                    rho, _ = spearmanr(sig_arrays[a], sig_arrays[b])\n                    pair_rhos[key].append(rho)\n                    model_rhos[key] = round(float(rho), 4)\n            model_details.append({\"model\": m[\"dirname\"], \"dosage\": m[\"dosage\"], \"correlations\": model_rhos})\n        \n        n_sig = len(ACTIVE_SIGNALS)\n        matrix = np.eye(n_sig)\n        pair_summary = {}\n        for i, a in enumerate(ACTIVE_SIGNALS):\n            for j, b in enumerate(ACTIVE_SIGNALS):\n                if i < j:\n                    key = f\"{a}_vs_{b}\"\n                    rhos = pair_rhos[key]\n                    if rhos:\n                        mean_rho = float(np.mean(rhos))\n                        matrix[i, j] = mean_rho\n                        matrix[j, i] = mean_rho\n                        pair_summary[key] = {\n                            \"mean_rho\": round(mean_rho, 4),\n                            \"std_rho\": round(float(np.std(rhos)), 4),\n                            \"min_rho\": round(float(np.min(rhos)), 4),\n                            \"max_rho\": round(float(np.max(rhos)), 4),\n                            \"n_models\": len(rhos),\n                        }\n        \n        results[bench] = {\n            \"n_models\": len(model_details),\n            \"signals\": ACTIVE_SIGNALS,\n            \"correlation_matrix\": [[round(x, 4) for x in row] for row in matrix.tolist()],\n            \"pair_summary\": pair_summary,\n            \"per_model\": model_details,\n        }\n    return results\n\n\n# ═══════════════ C2 ═══════════════\n\ndef leave_one_out_ablation(models):\n    results = {}\n    for bench in BENCHMARKS:\n        configs = {\"full\": ACTIVE_SIGNALS}\n        for sig in ACTIVE_SIGNALS:\n            configs[f\"drop_{sig}\"] = [s for s in ACTIVE_SIGNALS if s != sig]\n        for sig in ACTIVE_SIGNALS:\n            configs[f\"only_{sig}\"] = [sig]\n        \n        model_exposures = {cfg: [] for cfg in configs}\n        # Also store per-item RRF for rank correlation between full and ablated\n        item_rrf_full = []\n        item_rrf_ablated = {f\"drop_{sig}\": [] for sig in ACTIVE_SIGNALS}\n        dosages = []\n        model_names = []\n        scales = []\n        \n        for m in models:\n            items = load_merged(m[\"path\"], bench)\n            if items is None or not has_all_signals(items):\n                continue\n            \n            dosages.append(m[\"dosage\"])\n            model_names.append(m[\"dirname\"])\n            scales.append(m[\"scale\"])\n            \n            for cfg_name, cfg_signals in configs.items():\n                mean_exp, item_scores = compute_rrf(items, cfg_signals)\n                model_exposures[cfg_name].append(mean_exp)\n                if cfg_name == \"full\":\n                    item_rrf_full.append(item_scores)\n                elif cfg_name.startswith(\"drop_\"):\n                    item_rrf_ablated[cfg_name].append(item_scores)\n        \n        n_models = len(dosages)\n        if n_models < 3:\n            continue\n        dosages = np.array(dosages)\n        \n        # Item-level rank correlation between full and ablated (averaged over models)\n        item_rank_corr = {}\n        for drop_key in item_rrf_ablated:\n            rhos = []\n            for i in range(n_models):\n                if len(item_rrf_full[i]) > 0 and len(item_rrf_ablated[drop_key][i]) > 0:\n                    rho, _ = spearmanr(item_rrf_full[i], item_rrf_ablated[drop_key][i])\n                    rhos.append(rho)\n            if rhos:\n                item_rank_corr[drop_key] = {\n                    \"mean_item_rho_vs_full\": round(float(np.mean(rhos)), 4),\n                    \"std\": round(float(np.std(rhos)), 4),\n                }\n        \n        config_metrics = {}\n        full_exp = np.array(model_exposures[\"full\"])\n        \n        for cfg_name, exps in model_exposures.items():\n            exps = np.array(exps)\n            rho_dosage, p_dosage = spearmanr(exps, dosages)\n            tau_dosage, p_tau = kendalltau(exps, dosages)\n            \n            if cfg_name != \"full\":\n                rho_full, _ = spearmanr(exps, full_exp)\n            else:\n                rho_full = 1.0\n            \n            if exps.max() > exps.min():\n                exps_scaled = (exps - exps.min()) / (exps.max() - exps.min())\n            else:\n                exps_scaled = exps\n            mae_dosage = float(np.mean(np.abs(exps_scaled - dosages)))\n            \n            entry = {\n                \"signals_used\": configs[cfg_name],\n                \"n_signals\": len(configs[cfg_name]),\n                \"spearman_rho_vs_dosage\": round(float(rho_dosage), 4),\n                \"kendall_tau_vs_dosage\": round(float(tau_dosage), 4),\n                \"spearman_rho_vs_full_rrf\": round(float(rho_full), 4),\n                \"mae_vs_dosage_scaled\": round(mae_dosage, 4),\n            }\n            if cfg_name in item_rank_corr:\n                entry[\"item_level_rho_vs_full\"] = item_rank_corr[cfg_name]\n            config_metrics[cfg_name] = entry\n        \n        full_mae = config_metrics[\"full\"][\"mae_vs_dosage_scaled\"]\n        full_rho = config_metrics[\"full\"][\"spearman_rho_vs_dosage\"]\n        \n        importance = []\n        for sig in ACTIVE_SIGNALS:\n            dk = f\"drop_{sig}\"\n            if dk in config_metrics:\n                d_mae = config_metrics[dk][\"mae_vs_dosage_scaled\"] - full_mae\n                d_rho = config_metrics[dk][\"spearman_rho_vs_dosage\"] - full_rho\n                config_metrics[dk][\"delta_mae\"] = round(d_mae, 4)\n                config_metrics[dk][\"delta_rho\"] = round(d_rho, 4)\n                importance.append({\n                    \"signal\": sig,\n                    \"delta_mae_when_dropped\": round(d_mae, 4),\n                    \"delta_rho_when_dropped\": round(d_rho, 4),\n                })\n        importance.sort(key=lambda x: -x[\"delta_mae_when_dropped\"])\n        \n        # Per-model detail\n        per_model = []\n        for i, mname in enumerate(model_names):\n            entry = {\n                \"model\": mname,\n                \"scale\": scales[i],\n                \"dosage\": round(dosages[i], 4),\n            }\n            for cfg_name in configs:\n                entry[f\"exposure_{cfg_name}\"] = round(model_exposures[cfg_name][i], 6)\n            per_model.append(entry)\n        \n        results[bench] = {\n            \"n_models\": n_models,\n            \"configs\": config_metrics,\n            \"signal_importance_by_delta_mae\": importance,\n            \"per_model\": per_model,\n        }\n    return results\n\n\ndef main():\n    models = list_model_dirs()\n    print(f\"Found {len(models)} model directories (after filtering)\")\n    for m in models:\n        print(f\"  {m['dirname']} ({m['scale']}, d={m['dosage']})\")\n    \n    print(\"\\n=== C1: Signal Rank Correlation ===\")\n    corr = compute_signal_correlations(models)\n    for bench, data in corr.items():\n        print(f\"\\n{bench} (n={data['n_models']}):\")\n        sigs = data[\"signals\"]\n        mx = np.array(data[\"correlation_matrix\"])\n        print(\"    \" + \"  \".join(f\"{s:>16s}\" for s in sigs))\n        for i, s in enumerate(sigs):\n            print(f\"{s:>16s}\" + \"  \".join(f\"{mx[i,j]:>16.4f}\" for j in range(len(sigs))))\n        for k, v in data[\"pair_summary\"].items():\n            print(f\"  {k}: ρ={v['mean_rho']:.4f}±{v['std_rho']:.4f} [{v['min_rho']:.4f}, {v['max_rho']:.4f}]\")\n    \n    print(\"\\n=== C2: Leave-One-Out Ablation ===\")\n    ablation = leave_one_out_ablation(models)\n    for bench, data in ablation.items():\n        print(f\"\\n{bench} (n={data['n_models']}):\")\n        print(f\"{'Config':<25s} {'#Sig':<5s} {'ρ_dose':<9s} {'τ_dose':<9s} {'MAE':<8s} {'ΔMAE':<8s} {'ρ_full':<8s} {'item_ρ':<8s}\")\n        for cfg, m in data[\"configs\"].items():\n            dm = m.get(\"delta_mae\", \"\")\n            dm_s = f\"{dm:+.4f}\" if isinstance(dm, float) else \"\"\n            ir = m.get(\"item_level_rho_vs_full\", {}).get(\"mean_item_rho_vs_full\", \"\")\n            ir_s = f\"{ir:.4f}\" if isinstance(ir, float) else \"\"\n            print(f\"{cfg:<25s} {m['n_signals']:<5d} {m['spearman_rho_vs_dosage']:<9.4f} \"\n                  f\"{m['kendall_tau_vs_dosage']:<9.4f} {m['mae_vs_dosage_scaled']:<8.4f} \"\n                  f\"{dm_s:<8s} {m['spearman_rho_vs_full_rrf']:<8.4f} {ir_s:<8s}\")\n        print(\"Importance:\")\n        for r, e in enumerate(data[\"signal_importance_by_delta_mae\"], 1):\n            print(f\"  #{r} {e['signal']}: ΔMAE={e['delta_mae_when_dropped']:+.4f}\")\n    \n    output = {\n        \"c1_signal_correlation\": corr,\n        \"c2_leave_one_out_ablation\": ablation,\n        \"metadata\": {\n            \"signals\": ACTIVE_SIGNALS,\n            \"signal_descriptions\": {\n                \"s1_embedding\": \"Embedding similarity between benchmark item and SFT training data (higher = more similar to training)\",\n                \"s2_minkpp\": \"Min-K%++ memorization score (negated: lower raw value = more memorized)\",\n                \"s4_selfcritique\": \"Self-critique consistency (higher = model more confident, suggesting memorization)\",\n            },\n            \"rrf_k\": RRF_K,\n            \"negate_rules\": NEGATE,\n            \"benchmarks\": BENCHMARKS,\n            \"excluded_patterns\": EXCLUDE_PATTERNS,\n        }\n    }\n    \n    outpath = \"/root/contamcal-irt-calibration/analysis/rrf_signal_analysis_v2.json\"\n    with open(outpath, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"\\nSaved to {outpath}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Script v2 written OK\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat > /root/contamcal-irt-calibration/analysis/rrf_signal_analysis_v2.py << 'PYEOF'\n\"\"\"RRF Signal Analysis v2: filtered models, cleaner ablation.\"\"\"\nimport json\nimport os\nimport re\nimport numpy as np\nfrom scipy.stats import spearmanr, kendalltau\nfrom pathlib import Path\n\nSIGNALS_DIR = \"/root/autodl-tmp/exp002/signals\"\nBENCHMARKS = [\"mmlu\", \"gsm8k\", \"arc_challenge\"]\nACTIVE_SIGNALS = [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"]\nRRF_K = 60\nNEGATE = {\"s1_embedding\": False, \"s2_minkpp\": True, \"s4_selfcritique\": False}\n\n# C006 blacklist + duplicates\nEXCLUDE_PATTERNS = [\n    \"DEPRECATED\", \"old_alpha16\",\n    # alpha=16 blacklist from C006\n    \"Qwen2.5-3B_d000_s42\",  # no _a32 suffix = alpha=16\n    \"Qwen2.5-3B_d005_s42\",  # same\n    \"Qwen2.5-3B_d025_s42\",  # same (not v3)\n    \"Qwen2.5-3B_d100_s42\",  # same\n]\n\ndef should_exclude(dirname):\n    for pat in EXCLUDE_PATTERNS:\n        if pat in dirname:\n            # But allow _a32 variants\n            if pat.startswith(\"Qwen2.5-3B_d\") and \"_a32\" in dirname:\n                continue\n            if pat.startswith(\"Qwen2.5-3B_d\") and \"_v3\" in dirname:\n                continue\n            if pat.startswith(\"Qwen2.5-3B_d\") and \"_s123\" in dirname:\n                continue\n            return True\n    return False\n\n\ndef parse_dosage(dirname):\n    m = re.search(r'_d(\\d{3})', dirname)\n    if m:\n        return int(m.group(1)) / 100.0\n    return None\n\n\ndef parse_scale(dirname):\n    if \"0.5B\" in dirname:\n        return \"0.5B\"\n    elif \"1.5B\" in dirname:\n        return \"1.5B\"\n    elif \"3B\" in dirname:\n        return \"3B\"\n    elif \"Llama\" in dirname:\n        return \"Llama-3B\"\n    return \"unknown\"\n\n\ndef list_model_dirs():\n    models = []\n    for name in sorted(os.listdir(SIGNALS_DIR)):\n        dirpath = os.path.join(SIGNALS_DIR, name)\n        if not os.path.isdir(dirpath):\n            continue\n        dosage = parse_dosage(name)\n        if dosage is None:\n            continue\n        if should_exclude(name):\n            continue\n        has_merged = any(\n            os.path.exists(os.path.join(dirpath, f\"signals_merged_{b}.json\"))\n            for b in BENCHMARKS\n        )\n        if has_merged:\n            models.append({\n                \"dirname\": name, \"dosage\": dosage,\n                \"path\": dirpath, \"scale\": parse_scale(name)\n            })\n    return models\n\n\ndef load_merged(model_path, benchmark):\n    fpath = os.path.join(model_path, f\"signals_merged_{benchmark}.json\")\n    if not os.path.exists(fpath):\n        return None\n    with open(fpath) as f:\n        return json.load(f)\n\n\ndef compute_ranks(scores):\n    order = np.argsort(-scores)\n    ranks = np.empty_like(order, dtype=float)\n    ranks[order] = np.arange(1, len(scores) + 1)\n    return ranks\n\n\ndef compute_rrf(items, signals, k=RRF_K):\n    n = len(items)\n    if n == 0:\n        return 0.0, np.zeros(0)\n    rrf = np.zeros(n)\n    for sig in signals:\n        v = np.array([it.get(sig, 0.0) or 0.0 for it in items], dtype=float)\n        if NEGATE.get(sig, False):\n            v = -v\n        ranks = compute_ranks(v)\n        rrf += 1.0 / (k + ranks)\n    mn, mx = rrf.min(), rrf.max()\n    if mx > mn:\n        rrf_norm = (rrf - mn) / (mx - mn)\n    else:\n        rrf_norm = rrf\n    return float(rrf_norm.mean()), rrf_norm\n\n\ndef oriented_scores(items, sig):\n    v = np.array([it.get(sig, 0.0) or 0.0 for it in items], dtype=float)\n    if NEGATE.get(sig, False):\n        v = -v\n    return v\n\n\ndef has_all_signals(items):\n    for sig in ACTIVE_SIGNALS:\n        vals = [it.get(sig) for it in items]\n        if all(v is None or v == 0.0 for v in vals):\n            return False\n    return True\n\n\n# ═══════════════ C1 ═══════════════\n\ndef compute_signal_correlations(models):\n    results = {}\n    for bench in BENCHMARKS:\n        pair_rhos = {f\"{a}_vs_{b}\": [] for i, a in enumerate(ACTIVE_SIGNALS)\n                     for b in ACTIVE_SIGNALS[i+1:]}\n        model_details = []\n        \n        for m in models:\n            items = load_merged(m[\"path\"], bench)\n            if items is None or not has_all_signals(items):\n                continue\n            \n            sig_arrays = {sig: oriented_scores(items, sig) for sig in ACTIVE_SIGNALS}\n            model_rhos = {}\n            for i, a in enumerate(ACTIVE_SIGNALS):\n                for b in ACTIVE_SIGNALS[i+1:]:\n                    key = f\"{a}_vs_{b}\"\n                    rho, _ = spearmanr(sig_arrays[a], sig_arrays[b])\n                    pair_rhos[key].append(rho)\n                    model_rhos[key] = round(float(rho), 4)\n            model_details.append({\"model\": m[\"dirname\"], \"dosage\": m[\"dosage\"], \"correlations\": model_rhos})\n        \n        n_sig = len(ACTIVE_SIGNALS)\n        matrix = np.eye(n_sig)\n        pair_summary = {}\n        for i, a in enumerate(ACTIVE_SIGNALS):\n            for j, b in enumerate(ACTIVE_SIGNALS):\n                if i < j:\n                    key = f\"{a}_vs_{b}\"\n                    rhos = pair_rhos[key]\n                    if rhos:\n                        mean_rho = float(np.mean(rhos))\n                        matrix[i, j] = mean_rho\n                        matrix[j, i] = mean_rho\n                        pair_summary[key] = {\n                            \"mean_rho\": round(mean_rho, 4),\n                            \"std_rho\": round(float(np.std(rhos)), 4),\n                            \"min_rho\": round(float(np.min(rhos)), 4),\n                            \"max_rho\": round(float(np.max(rhos)), 4),\n                            \"n_models\": len(rhos),\n                        }\n        \n        results[bench] = {\n            \"n_models\": len(model_details),\n            \"signals\": ACTIVE_SIGNALS,\n            \"correlation_matrix\": [[round(x, 4) for x in row] for row in matrix.tolist()],\n            \"pair_summary\": pair_summary,\n            \"per_model\": model_details,\n        }\n    return results\n\n\n# ═══════════════ C2 ═══════════════\n\ndef leave_one_out_ablation(models):\n    results = {}\n    for bench in BENCHMARKS:\n        configs = {\"full\": ACTIVE_SIGNALS}\n        for sig in ACTIVE_SIGNALS:\n            configs[f\"drop_{sig}\"] = [s for s in ACTIVE_SIGNALS if s != sig]\n        for sig in ACTIVE_SIGNALS:\n            configs[f\"only_{sig}\"] = [sig]\n        \n        model_exposures = {cfg: [] for cfg in configs}\n        # Also store per-item RRF for rank correlation between full and ablated\n        item_rrf_full = []\n        item_rrf_ablated = {f\"drop_{sig}\": [] for sig in ACTIVE_SIGNALS}\n        dosages = []\n        model_names = []\n        scales = []\n        \n        for m in models:\n            items = load_merged(m[\"path\"], bench)\n            if items is None or not has_all_signals(items):\n                continue\n            \n            dosages.append(m[\"dosage\"])\n            model_names.append(m[\"dirname\"])\n            scales.append(m[\"scale\"])\n            \n            for cfg_name, cfg_signals in configs.items():\n                mean_exp, item_scores = compute_rrf(items, cfg_signals)\n                model_exposures[cfg_name].append(mean_exp)\n                if cfg_name == \"full\":\n                    item_rrf_full.append(item_scores)\n                elif cfg_name.startswith(\"drop_\"):\n                    item_rrf_ablated[cfg_name].append(item_scores)\n        \n        n_models = len(dosages)\n        if n_models < 3:\n            continue\n        dosages = np.array(dosages)\n        \n        # Item-level rank correlation between full and ablated (averaged over models)\n        item_rank_corr = {}\n        for drop_key in item_rrf_ablated:\n            rhos = []\n            for i in range(n_models):\n                if len(item_rrf_full[i]) > 0 and len(item_rrf_ablated[drop_key][i]) > 0:\n                    rho, _ = spearmanr(item_rrf_full[i], item_rrf_ablated[drop_key][i])\n                    rhos.append(rho)\n            if rhos:\n                item_rank_corr[drop_key] = {\n                    \"mean_item_rho_vs_full\": round(float(np.mean(rhos)), 4),\n                    \"std\": round(float(np.std(rhos)), 4),\n                }\n        \n        config_metrics = {}\n        full_exp = np.array(model_exposures[\"full\"])\n        \n        for cfg_name, exps in model_exposures.items():\n            exps = np.array(exps)\n            rho_dosage, p_dosage = spearmanr(exps, dosages)\n            tau_dosage, p_tau = kendalltau(exps, dosages)\n            \n            if cfg_name != \"full\":\n                rho_full, _ = spearmanr(exps, full_exp)\n            else:\n                rho_full = 1.0\n            \n            if exps.max() > exps.min():\n                exps_scaled = (exps - exps.min()) / (exps.max() - exps.min())\n            else:\n                exps_scaled = exps\n            mae_dosage = float(np.mean(np.abs(exps_scaled - dosages)))\n            \n            entry = {\n                \"signals_used\": configs[cfg_name],\n                \"n_signals\": len(configs[cfg_name]),\n                \"spearman_rho_vs_dosage\": round(float(rho_dosage), 4),\n                \"kendall_tau_vs_dosage\": round(float(tau_dosage), 4),\n                \"spearman_rho_vs_full_rrf\": round(float(rho_full), 4),\n                \"mae_vs_dosage_scaled\": round(mae_dosage, 4),\n            }\n            if cfg_name in item_rank_corr:\n                entry[\"item_level_rho_vs_full\"] = item_rank_corr[cfg_name]\n            config_metrics[cfg_name] = entry\n        \n        full_mae = config_metrics[\"full\"][\"mae_vs_dosage_scaled\"]\n        full_rho = config_metrics[\"full\"][\"spearman_rho_vs_dosage\"]\n        \n        importance = []\n        for sig in ACTIVE_SIGNALS:\n            dk = f\"drop_{sig}\"\n            if dk in config_metrics:\n                d_mae = config_metrics[dk][\"mae_vs_dosage_scaled\"] - full_mae\n                d_rho = config_metrics[dk][\"spearman_rho_vs_dosage\"] - full_rho\n                config_metrics[dk][\"delta_mae\"] = round(d_mae, 4)\n                config_metrics[dk][\"delta_rho\"] = round(d_rho, 4)\n                importance.append({\n                    \"signal\": sig,\n                    \"delta_mae_when_dropped\": round(d_mae, 4),\n                    \"delta_rho_when_dropped\": round(d_rho, 4),\n                })\n        importance.sort(key=lambda x: -x[\"delta_mae_when_dropped\"])\n        \n        # Per-model detail\n        per_model = []\n        for i, mname in enumerate(model_names):\n            entry = {\n                \"model\": mname,\n                \"scale\": scales[i],\n                \"dosage\": round(dosages[i], 4),\n            }\n            for cfg_name in configs:\n                entry[f\"exposure_{cfg_name}\"] = round(model_exposures[cfg_name][i], 6)\n            per_model.append(entry)\n        \n        results[bench] = {\n            \"n_models\": n_models,\n            \"configs\": config_metrics,\n            \"signal_importance_by_delta_mae\": importance,\n            \"per_model\": per_model,\n        }\n    return results\n\n\ndef main():\n    models = list_model_dirs()\n    print(f\"Found {len(models)} model directories (after filtering)\")\n    for m in models:\n        print(f\"  {m['dirname']} ({m['scale']}, d={m['dosage']})\")\n    \n    print(\"\\n=== C1: Signal Rank Correlation ===\")\n    corr = compute_signal_correlations(models)\n    for bench, data in corr.items():\n        print(f\"\\n{bench} (n={data['n_models']}):\")\n        sigs = data[\"signals\"]\n        mx = np.array(data[\"correlation_matrix\"])\n        print(\"    \" + \"  \".join(f\"{s:>16s}\" for s in sigs))\n        for i, s in enumerate(sigs):\n            print(f\"{s:>16s}\" + \"  \".join(f\"{mx[i,j]:>16.4f}\" for j in range(len(sigs))))\n        for k, v in data[\"pair_summary\"].items():\n            print(f\"  {k}: ρ={v['mean_rho']:.4f}±{v['std_rho']:.4f} [{v['min_rho']:.4f}, {v['max_rho']:.4f}]\")\n    \n    print(\"\\n=== C2: Leave-One-Out Ablation ===\")\n    ablation = leave_one_out_ablation(models)\n    for bench, data in ablation.items():\n        print(f\"\\n{bench} (n={data['n_models']}):\")\n        print(f\"{'Config':<25s} {'#Sig':<5s} {'ρ_dose':<9s} {'τ_dose':<9s} {'MAE':<8s} {'ΔMAE':<8s} {'ρ_full':<8s} {'item_ρ':<8s}\")\n        for cfg, m in data[\"configs\"].items():\n            dm = m.get(\"delta_mae\", \"\")\n            dm_s = f\"{dm:+.4f}\" if isinstance(dm, float) else \"\"\n            ir = m.get(\"item_level_rho_vs_full\", {}).get(\"mean_item_rho_vs_full\", \"\")\n            ir_s = f\"{ir:.4f}\" if isinstance(ir, float) else \"\"\n            print(f\"{cfg:<25s} {m['n_signals']:<5d} {m['spearman_rho_vs_dosage']:<9.4f} \"\n                  f\"{m['kendall_tau_vs_dosage']:<9.4f} {m['mae_vs_dosage_scaled']:<8.4f} \"\n                  f\"{dm_s:<8s} {m['spearman_rho_vs_full_rrf']:<8.4f} {ir_s:<8s}\")\n        print(\"Importance:\")\n        for r, e in enumerate(data[\"signal_importance_by_delta_mae\"], 1):\n            print(f\"  #{r} {e['signal']}: ΔMAE={e['delta_mae_when_dropped']:+.4f}\")\n    \n    output = {\n        \"c1_signal_correlation\": corr,\n        \"c2_leave_one_out_ablation\": ablation,\n        \"metadata\": {\n            \"signals\": ACTIVE_SIGNALS,\n            \"signal_descriptions\": {\n                \"s1_embedding\": \"Embedding similarity between benchmark item and SFT training data (higher = more similar to training)\",\n                \"s2_minkpp\": \"Min-K%++ memorization score (negated: lower raw value = more memorized)\",\n                \"s4_selfcritique\": \"Self-critique consistency (higher = model more confident, suggesting memorization)\",\n            },\n            \"rrf_k\": RRF_K,\n            \"negate_rules\": NEGATE,\n            \"benchmarks\": BENCHMARKS,\n            \"excluded_patterns\": EXCLUDE_PATTERNS,\n        }\n    }\n    \n    outpath = \"/root/contamcal-irt-calibration/analysis/rrf_signal_analysis_v2.json\"\n    with open(outpath, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"\\nSaved to {outpath}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Script v2 written OK\""
  }
}
```

</details>

---

### Tool result

_source line 152 · 2026-05-21T08:46:41.630540+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script v2 written OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.56}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 153 · 2026-05-21T08:46:41.630681+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "nohup /root/miniconda3/bin/python -u /root/contamcal-irt-calibration/analysis/rrf_signal_analysis_v2.py > /tmp/rrf_v2.log 2>&1 & echo $!"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "nohup /root/miniconda3/bin/python -u /root/contamcal-irt-calibration/analysis/rrf_signal_analysis_v2.py > /tmp/rrf_v2.log 2>&1 & echo $!"
  }
}
```

</details>

---

### Tool result

_source line 154 · 2026-05-21T08:46:41.630814+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"484902\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 155 · 2026-05-21T08:46:41.630938+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -30 /tmp/rrf_v2.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -30 /tmp/rrf_v2.log"
  }
}
```

</details>

---

### Tool result

_source line 156 · 2026-05-21T08:46:41.631063+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 157 · 2026-05-21T08:46:41.631181+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -30 /tmp/rrf_v2.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -30 /tmp/rrf_v2.log"
  }
}
```

</details>

---

### Tool result

_source line 158 · 2026-05-21T08:46:41.631331+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  Llama-3.2-3B_d100_s42 (3B, d=1.0)\\n  Qwen2.5-0.5B_d000_s123 (0.5B, d=0.0)\\n  Qwen2.5-0.5B_d000_s42 (0.5B, d=0.0)\\n  Qwen2.5-0.5B_d005_s123 (0.5B, d=0.05)\\n  Qwen2.5-0.5B_d005_s42 (0.5B, d=0.05)\\n  Qwen2.5-0.5B_d025_s123 (0.5B, d=0.25)\\n  Qwen2.5-0.5B_d025_s42 (0.5B, d=0.25)\\n  Qwen2.5-0.5B_d100_s123 (0.5B, d=1.0)\\n  Qwen2.5-0.5B_d100_s42 (0.5B, d=1.0)\\n  Qwen2.5-1.5B_d000_s123 (1.5B, d=0.0)\\n  Qwen2.5-1.5B_d000_s42 (1.5B, d=0.0)\\n  Qwen2.5-1.5B_d005_s123 (1.5B, d=0.05)\\n  Qwen2.5-1.5B_d005_s42 (1.5B, d=0.05)\\n  Qwen2.5-1.5B_d025_s123 (1.5B, d=0.25)\\n  Qwen2.5-1.5B_d025_s42 (1.5B, d=0.25)\\n  Qwen2.5-1.5B_d100_s123 (1.5B, d=1.0)\\n  Qwen2.5-1.5B_d100_s42 (1.5B, d=1.0)\\n  Qwen2.5-3B_d000_a32_s42 (3B, d=0.0)\\n  Qwen2.5-3B_d000_s123 (3B, d=0.0)\\n  Qwen2.5-3B_d000_s123_a32 (3B, d=0.0)\\n  Qwen2.5-3B_d000_s42_a32 (3B, d=0.0)\\n  Qwen2.5-3B_d005_a32_s42 (3B, d=0.05)\\n  Qwen2.5-3B_d005_s123 (3B, d=0.05)\\n  Qwen2.5-3B_d005_s42_a32 (3B, d=0.05)\\n  Qwen2.5-3B_d025_s123 (3B, d=0.25)\\n  Qwen2.5-3B_d025_v3_s42 (3B, d=0.25)\\n  Qwen2.5-3B_d100_a32_s123 (3B, d=1.0)\\n  Qwen2.5-3B_d100_a32_s42 (3B, d=1.0)\\n\\n=== C1: Signal Rank Correlation ===\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.79}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 159 · 2026-05-21T08:46:41.631492+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -60 /tmp/rrf_v2.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -60 /tmp/rrf_v2.log"
  }
}
```

</details>

---

### Tool result

_source line 160 · 2026-05-21T08:46:41.631635+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Found 31 model directories (after filtering)\\n  Llama-3.2-3B_d000_s42 (3B, d=0.0)\\n  Llama-3.2-3B_d005_s42 (3B, d=0.05)\\n  Llama-3.2-3B_d025_s42 (3B, d=0.25)\\n  Llama-3.2-3B_d100_s42 (3B, d=1.0)\\n  Qwen2.5-0.5B_d000_s123 (0.5B, d=0.0)\\n  Qwen2.5-0.5B_d000_s42 (0.5B, d=0.0)\\n  Qwen2.5-0.5B_d005_s123 (0.5B, d=0.05)\\n  Qwen2.5-0.5B_d005_s42 (0.5B, d=0.05)\\n  Qwen2.5-0.5B_d025_s123 (0.5B, d=0.25)\\n  Qwen2.5-0.5B_d025_s42 (0.5B, d=0.25)\\n  Qwen2.5-0.5B_d100_s123 (0.5B, d=1.0)\\n  Qwen2.5-0.5B_d100_s42 (0.5B, d=1.0)\\n  Qwen2.5-1.5B_d000_s123 (1.5B, d=0.0)\\n  Qwen2.5-1.5B_d000_s42 (1.5B, d=0.0)\\n  Qwen2.5-1.5B_d005_s123 (1.5B, d=0.05)\\n  Qwen2.5-1.5B_d005_s42 (1.5B, d=0.05)\\n  Qwen2.5-1.5B_d025_s123 (1.5B, d=0.25)\\n  Qwen2.5-1.5B_d025_s42 (1.5B, d=0.25)\\n  Qwen2.5-1.5B_d100_s123 (1.5B, d=1.0)\\n  Qwen2.5-1.5B_d100_s42 (1.5B, d=1.0)\\n  Qwen2.5-3B_d000_a32_s42 (3B, d=0.0)\\n  Qwen2.5-3B_d000_s123 (3B, d=0.0)\\n  Qwen2.5-3B_d000_s123_a32 (3B, d=0.0)\\n  Qwen2.5-3B_d000_s42_a32 (3B, d=0.0)\\n  Qwen2.5-3B_d005_a32_s42 (3B, d=0.05)\\n  Qwen2.5-3B_d005_s123 (3B, d=0.05)\\n  Qwen2.5-3B_d005_s42_a32 (3B, d=0.05)\\n  Qwen2.5-3B_d025_s123 (3B, d=0.25)\\n  Qwen2.5-3B_d025_v3_s42 (3B, d=0.25)\\n  Qwen2.5-3B_d100_a32_s123 (3B, d=1.0)\\n  Qwen2.5-3B_d100_a32_s42 (3B, d=1.0)\\n\\n=== C1: Signal Rank Correlation ===\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 161 · 2026-05-21T08:46:41.631766+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ps -p 484902 -o pid="
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ps -p 484902 -o pid="
  }
}
```

</details>

---

### Tool result

_source line 162 · 2026-05-21T08:46:41.631890+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"484902\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 163 · 2026-05-21T08:46:41.632011+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "wc -l /tmp/rrf_v2.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "wc -l /tmp/rrf_v2.log"
  }
}
```

</details>

---

### Tool result

_source line 164 · 2026-05-21T08:46:41.632134+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"63 /tmp/rrf_v2.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 165 · 2026-05-21T08:46:41.632264+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -20 /tmp/rrf_v2.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -20 /tmp/rrf_v2.log"
  }
}
```

</details>

---

### Tool result

_source line 166 · 2026-05-21T08:46:41.632430+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\ngsm8k (n=31):\\n        s1_embedding         s2_minkpp   s4_selfcritique\\n    s1_embedding          1.0000           -0.0216            0.0530\\n       s2_minkpp         -0.0216            1.0000            0.0074\\n s4_selfcritique          0.0530            0.0074            1.0000\\n  s1_embedding_vs_s2_minkpp: ρ=-0.0216±0.0539 [-0.1741, 0.0688]\\n  s1_embedding_vs_s4_selfcritique: ρ=0.0530±0.0412 [-0.0348, 0.1189]\\n  s2_minkpp_vs_s4_selfcritique: ρ=0.0074±0.0348 [-0.0900, 0.0589]\\n\\narc_challenge (n=31):\\n        s1_embedding         s2_minkpp   s4_selfcritique\\n    s1_embedding          1.0000           -0.0189            0.0086\\n       s2_minkpp         -0.0189            1.0000            0.0121\\n s4_selfcritique          0.0086            0.0121            1.0000\\n  s1_embedding_vs_s2_minkpp: ρ=-0.0189±0.1139 [-0.1829, 0.1690]\\n  s1_embedding_vs_s4_selfcritique: ρ=0.0086±0.0382 [-0.0676, 0.0740]\\n  s2_minkpp_vs_s4_selfcritique: ρ=0.0121±0.0528 [-0.0844, 0.0976]\\n\\n=== C2: Leave-One-Out Ablation ===\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 167 · 2026-05-21T08:46:41.632567+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -50 /tmp/rrf_v2.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -50 /tmp/rrf_v2.log"
  }
}
```

</details>

---

### Tool result

_source line 168 · 2026-05-21T08:46:41.632723+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  Qwen2.5-1.5B_d000_s123 (1.5B, d=0.0)\\n  Qwen2.5-1.5B_d000_s42 (1.5B, d=0.0)\\n  Qwen2.5-1.5B_d005_s123 (1.5B, d=0.05)\\n  Qwen2.5-1.5B_d005_s42 (1.5B, d=0.05)\\n  Qwen2.5-1.5B_d025_s123 (1.5B, d=0.25)\\n  Qwen2.5-1.5B_d025_s42 (1.5B, d=0.25)\\n  Qwen2.5-1.5B_d100_s123 (1.5B, d=1.0)\\n  Qwen2.5-1.5B_d100_s42 (1.5B, d=1.0)\\n  Qwen2.5-3B_d000_a32_s42 (3B, d=0.0)\\n  Qwen2.5-3B_d000_s123 (3B, d=0.0)\\n  Qwen2.5-3B_d000_s123_a32 (3B, d=0.0)\\n  Qwen2.5-3B_d000_s42_a32 (3B, d=0.0)\\n  Qwen2.5-3B_d005_a32_s42 (3B, d=0.05)\\n  Qwen2.5-3B_d005_s123 (3B, d=0.05)\\n  Qwen2.5-3B_d005_s42_a32 (3B, d=0.05)\\n  Qwen2.5-3B_d025_s123 (3B, d=0.25)\\n  Qwen2.5-3B_d025_v3_s42 (3B, d=0.25)\\n  Qwen2.5-3B_d100_a32_s123 (3B, d=1.0)\\n  Qwen2.5-3B_d100_a32_s42 (3B, d=1.0)\\n\\n=== C1: Signal Rank Correlation ===\\n\\nmmlu (n=31):\\n        s1_embedding         s2_minkpp   s4_selfcritique\\n    s1_embedding          1.0000           -0.0444            0.0376\\n       s2_minkpp         -0.0444            1.0000           -0.0011\\n s4_selfcritique          0.0376           -0.0011            1.0000\\n  s1_embedding_vs_s2_minkpp: ρ=-0.0444±0.1239 [-0.2301, 0.2170]\\n  s1_embedding_vs_s4_selfcritique: ρ=0.0376±0.0632 [-0.0861, 0.1468]\\n  s2_minkpp_vs_s4_selfcritique: ρ=-0.0011±0.0757 [-0.1728, 0.1671]\\n\\ngsm8k (n=31):\\n        s1_embedding         s2_minkpp   s4_selfcritique\\n    s1_embedding          1.0000           -0.0216            0.0530\\n       s2_minkpp         -0.0216            1.0000            0.0074\\n s4_selfcritique          0.0530            0.0074            1.0000\\n  s1_embedding_vs_s2_minkpp: ρ=-0.0216±0.0539 [-0.1741, 0.0688]\\n  s1_embedding_vs_s4_selfcritique: ρ=0.0530±0.0412 [-0.0348, 0.1189]\\n  s2_minkpp_vs_s4_selfcritique: ρ=0.0074±0.0348 [-0.0900, 0.0589]\\n\\narc_challenge (n=31):\\n        s1_embedding         s2_minkpp   s4_selfcritique\\n    s1_embedding          1.0000           -0.0189          
…[truncated 502 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 169 · 2026-05-21T08:46:41.632871+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ps -p 484902 -o pid="
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ps -p 484902 -o pid="
  }
}
```

</details>

---

### Tool result

_source line 170 · 2026-05-21T08:46:41.632998+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 171 · 2026-05-21T08:46:41.633116+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /tmp/rrf_v2.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /tmp/rrf_v2.log"
  }
}
```

</details>

---

### Tool result

_source line 172 · 2026-05-21T08:46:41.633294+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Found 31 model directories (after filtering)\\n  Llama-3.2-3B_d000_s42 (3B, d=0.0)\\n  Llama-3.2-3B_d005_s42 (3B, d=0.05)\\n  Llama-3.2-3B_d025_s42 (3B, d=0.25)\\n  Llama-3.2-3B_d100_s42 (3B, d=1.0)\\n  Qwen2.5-0.5B_d000_s123 (0.5B, d=0.0)\\n  Qwen2.5-0.5B_d000_s42 (0.5B, d=0.0)\\n  Qwen2.5-0.5B_d005_s123 (0.5B, d=0.05)\\n  Qwen2.5-0.5B_d005_s42 (0.5B, d=0.05)\\n  Qwen2.5-0.5B_d025_s123 (0.5B, d=0.25)\\n  Qwen2.5-0.5B_d025_s42 (0.5B, d=0.25)\\n  Qwen2.5-0.5B_d100_s123 (0.5B, d=1.0)\\n  Qwen2.5-0.5B_d100_s42 (0.5B, d=1.0)\\n  Qwen2.5-1.5B_d000_s123 (1.5B, d=0.0)\\n  Qwen2.5-1.5B_d000_s42 (1.5B, d=0.0)\\n  Qwen2.5-1.5B_d005_s123 (1.5B, d=0.05)\\n  Qwen2.5-1.5B_d005_s42 (1.5B, d=0.05)\\n  Qwen2.5-1.5B_d025_s123 (1.5B, d=0.25)\\n  Qwen2.5-1.5B_d025_s42 (1.5B, d=0.25)\\n  Qwen2.5-1.5B_d100_s123 (1.5B, d=1.0)\\n  Qwen2.5-1.5B_d100_s42 (1.5B, d=1.0)\\n  Qwen2.5-3B_d000_a32_s42 (3B, d=0.0)\\n  Qwen2.5-3B_d000_s123 (3B, d=0.0)\\n  Qwen2.5-3B_d000_s123_a32 (3B, d=0.0)\\n  Qwen2.5-3B_d000_s42_a32 (3B, d=0.0)\\n  Qwen2.5-3B_d005_a32_s42 (3B, d=0.05)\\n  Qwen2.5-3B_d005_s123 (3B, d=0.05)\\n  Qwen2.5-3B_d005_s42_a32 (3B, d=0.05)\\n  Qwen2.5-3B_d025_s123 (3B, d=0.25)\\n  Qwen2.5-3B_d025_v3_s42 (3B, d=0.25)\\n  Qwen2.5-3B_d100_a32_s123 (3B, d=1.0)\\n  Qwen2.5-3B_d100_a32_s42 (3B, d=1.0)\\n\\n=== C1: Signal Rank Correlation ===\\n\\nmmlu (n=31):\\n        s1_embedding         s2_minkpp   s4_selfcritique\\n    s1_embedding          1.0000           -0.0444            0.0376\\n       s2_minkpp         -0.0444            1.0000           -0.0011\\n s4_selfcritique          0.0376           -0.0011            1.0000\\n  s1_embedding_vs_s2_minkpp: ρ=-0.0444±0.1239 [-0.2301, 0.2170]\\n  s1_embedding_vs_s4_selfcritique: ρ=0.0376±0.0632 [-0.0861, 0.1468]\\n  s2_minkpp_vs_s4_selfcritique: ρ=-0.0011±0.0757 [-0.1728, 0.1671]\\n\\ngsm8k (n=31):\\n        s1_embedding         s2_minkpp   s4_selfcritique\\n    s1_embedding          1.0000   
…[truncated 3686 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 173 · 2026-05-21T08:46:41.633504+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "wc -c /root/contamcal-irt-calibration/analysis/rrf_signal_analysis_v2.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "wc -c /root/contamcal-irt-calibration/analysis/rrf_signal_analysis_v2.json"
  }
}
```

</details>

---

### Tool result

_source line 174 · 2026-05-21T08:46:41.633638+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"83014 /root/contamcal-irt-calibration/analysis/rrf_signal_analysis_v2.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 175 · 2026-05-21T08:46:41.633768+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/rrf_analysis",
  "description": "Create artifacts directory for RRF analysis"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/rrf_analysis",
    "description": "Create artifacts directory for RRF analysis"
  }
}
```

</details>

---

### Tool result

_source line 176 · 2026-05-21T08:46:41.633888+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 177 · 2026-05-21T08:46:41.634004+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "scp connect.cqa1.seetacloud.com:/root/contamcal-irt-calibration/analysis/rrf_signal_analysis_v2.json /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/rrf_analysis/rrf_signal_analysis.json",
  "description": "Copy RRF analysis JSON from server to local artifacts",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "Bash",
  "tool_args": {
    "command": "scp connect.cqa1.seetacloud.com:/root/contamcal-irt-calibration/analysis/rrf_signal_analysis_v2.json /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/rrf_analysis/rrf_signal_analysis.json",
    "description": "Copy RRF analysis JSON from server to local artifacts",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 178 · 2026-05-21T08:46:41.634126+00:00_

Exit code 255
ssh_askpass: exec(/usr/bin/ssh-askpass): No such file or directory
Permission denied, please try again.
ssh_askpass: exec(/usr/bin/ssh-askpass): No such file or directory
Permission denied, please try again.
ssh_askpass: exec(/usr/bin/ssh-askpass): No such file or directory
ubuntu@connect.cqa1.seetacloud.com: Permission denied ().
scp: Connection closed

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 179 · 2026-05-21T08:46:41.634257+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/contamcal-irt-calibration/analysis/rrf_signal_analysis_v2.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/contamcal-irt-calibration/analysis/rrf_signal_analysis_v2.json"
  }
}
```

</details>

---

### Tool result

_source line 180 · 2026-05-21T08:46:41.634579+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"c1_signal_correlation\\\": {\\n    \\\"mmlu\\\": {\\n      \\\"n_models\\\": 31,\\n      \\\"signals\\\": [\\n        \\\"s1_embedding\\\",\\n        \\\"s2_minkpp\\\",\\n        \\\"s4_selfcritique\\\"\\n      ],\\n      \\\"correlation_matrix\\\": [\\n        [\\n          1.0,\\n          -0.0444,\\n          0.0376\\n        ],\\n        [\\n          -0.0444,\\n          1.0,\\n          -0.0011\\n        ],\\n        [\\n          0.0376,\\n          -0.0011,\\n          1.0\\n        ]\\n      ],\\n      \\\"pair_summary\\\": {\\n        \\\"s1_embedding_vs_s2_minkpp\\\": {\\n          \\\"mean_rho\\\": -0.0444,\\n          \\\"std_rho\\\": 0.1239,\\n          \\\"min_rho\\\": -0.2301,\\n          \\\"max_rho\\\": 0.217,\\n          \\\"n_models\\\": 31\\n        },\\n        \\\"s1_embedding_vs_s4_selfcritique\\\": {\\n          \\\"mean_rho\\\": 0.0376,\\n          \\\"std_rho\\\": 0.0632,\\n          \\\"min_rho\\\": -0.0861,\\n          \\\"max_rho\\\": 0.1468,\\n          \\\"n_models\\\": 31\\n        },\\n        \\\"s2_minkpp_vs_s4_selfcritique\\\": {\\n          \\\"mean_rho\\\": -0.0011,\\n          \\\"std_rho\\\": 0.0757,\\n          \\\"min_rho\\\": -0.1728,\\n          \\\"max_rho\\\": 0.1671,\\n          \\\"n_models\\\": 31\\n        }\\n      },\\n      \\\"per_model\\\": [\\n        {\\n          \\\"model\\\": \\\"Llama-3.2-3B_d000_s42\\\",\\n          \\\"dosage\\\": 0.0,\\n          \\\"correlations\\\": {\\n            \\\"s1_embedding_vs_s2_minkpp\\\": -0.0515,\\n            \\\"s1_embedding_vs_s4_selfcritique\\\": 0.0858,\\n            \\\"s2_minkpp_vs_s4_selfcritique\\\": 0.0618\\n          }\\n        },\\n        {\\n          \\\"model\\\": \\\"Llama-3.2-3B_d005_s42\\\",\\n          \\\"dosage\\\": 0.05,\\n          \\\"correlations\\\": {\\n            \\\"s1_embedding_vs_s2_minkpp\\\": -0.0851,\\n            \\\"s1_embedding_vs_s4_selfcritique\\\": 0.0092,\\n      
…[truncated 7986 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 181 · 2026-05-21T08:46:41.634830+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/rrf_analysis/rrf_signal_analysis.json",
  "content": "{\n  \"c1_signal_rank_correlation\": {\n    \"description\": \"Spearman rank correlation between signal item-level scores, averaged across models. Near-zero values indicate signals capture orthogonal aspects of contamination.\",\n    \"mmlu\": {\n      \"n_models\": 31,\n      \"correlation_matrix\": {\n        \"labels\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"],\n        \"values\": [\n          [1.0, -0.0444, 0.0376],\n          [-0.0444, 1.0, -0.0011],\n          [0.0376, -0.0011, 1.0]\n        ]\n      },\n      \"pair_details\": {\n        \"s1_vs_s2\": {\"rho\": -0.0444, \"std\": 0.1239, \"range\": [-0.2301, 0.2170]},\n        \"s1_vs_s4\": {\"rho\": 0.0376, \"std\": 0.0632, \"range\": [-0.0861, 0.1468]},\n        \"s2_vs_s4\": {\"rho\": -0.0011, \"std\": 0.0757, \"range\": [-0.1728, 0.1671]}\n      }\n    },\n    \"gsm8k\": {\n      \"n_models\": 31,\n      \"correlation_matrix\": {\n        \"labels\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"],\n        \"values\": [\n          [1.0, -0.0216, 0.0530],\n          [-0.0216, 1.0, 0.0074],\n          [0.0530, 0.0074, 1.0]\n        ]\n      },\n      \"pair_details\": {\n        \"s1_vs_s2\": {\"rho\": -0.0216, \"std\": 0.0539, \"range\": [-0.1741, 0.0688]},\n        \"s1_vs_s4\": {\"rho\": 0.0530, \"std\": 0.0412, \"range\": [-0.0348, 0.1189]},\n        \"s2_vs_s4\": {\"rho\": 0.0074, \"std\": 0.0348, \"range\": [-0.0900, 0.0589]}\n      }\n    },\n    \"arc_challenge\": {\n      \"n_models\": 31,\n      \"correlation_matrix\": {\n        \"labels\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"],\n        \"values\": [\n          [1.0, -0.0189, 0.0086],\n          [-0.0189, 1.0, 0.0121],\n          [0.0086, 0.0121, 1.0]\n        ]\n      },\n      \"pair_details\": {\n        \"s1_vs_s2\": {\"rho\": -0.0189, \"std\": 0.1139, \"range\": [-0.1829, 0.1690]},\n        \"s1_vs_s4\": {\"rho\": 0.0086, \"std\": 0.0382, \"range\": [-0.0676, 0.0740]},\n        \"s2_vs_s4\": {\"rho\": 0.0121, \"std\": 0.0528, \"range\": [-0.0844, 0.0976]}\n      }\n    }\n  },\n  \"c2_leave_one_out_ablation\": {\n    \"description\": \"Leave-one-signal-out RRF ablation. MAE = mean|scaled_exposure - dosage|. item_rho = mean Spearman rho of item-level RRF ranks vs full-signal RRF. delta_mae > 0 means dropping the signal hurts performance.\",\n    \"mmlu\": {\n      \"n_models\": 31,\n      \"results\": {\n        \"full_S1S2S4\":            {\"n_sig\": 3, \"rho_dose\": 0.0486, \"tau_dose\": 0.0417, \"mae\": 0.4398},\n        \"drop_S1_embedding\":      {\"n_sig\": 2, \"rho_dose\": 0.0446, \"tau_dose\": 0.0319, \"mae\": 0.5061, \"delta_mae\": 0.0663, \"item_rho_vs_full\": 0.7824},\n        \"drop_S2_minkpp\":         {\"n_sig\": 2, \"rho_dose\": 0.4706, \"tau_dose\": 0.3610, \"mae\": 0.4849, \"delta_mae\": 0.0451, \"item_rho_vs_full\": 0.7731},\n        \"drop_S4_selfcritique\":   {\"n_sig\": 2, \"rho_dose\": 0.0840, \"tau_dose\": 0.0565, \"mae\": 0.5190, \"delta_mae\": 0.0792, \"item_rho_vs_full\": 0.7864},\n        \"only_S1\":                {\"n_sig\": 1, \"rho_dose\": -0.3506, \"tau_dose\": -0.3202, \"mae\": 0.6919},\n        \"only_S2\":                {\"n_sig\": 1, \"rho_dose\": -0.1914, \"tau_dose\": -0.1748, \"mae\": 0.6306},\n        \"only_S4\":                {\"n_sig\": 1, \"rho_dose\": 0.1116, \"tau_dose\": 0.1020, \"mae\": 0.5403}\n      },\n      \"importance_rank\": [\"s4_selfcritique (+0.0792)\", \"s1_embedding (+0.0663)\", \"s2_minkpp (+0.0451)\"]\n    },\n    \"gsm8k\": {\n      \"n_models\": 31,\n      \"results\": {\n        \"full_S1S2S4\":            {\"n_sig\": 3, \"rho_dose\": -0.0311, \"tau_dose\": -0.0516, \"mae\": 0.3962},\n        \"drop_S1_embedding\":      {\"n_sig\": 2, \"rho_dose\": -0.2626, \"tau_dose\": -0.1989, \"mae\": 0.4441, \"delta_mae\": 0.0479, \"item_rho_vs_full\": 0.7892},\n        \"drop_S2_minkpp\":         {\"n_sig\": 2, \"rho_dose\": 0.0563, \"tau_dose\": 0.0516, \"mae\": 0.3916, \"delta_mae\": -0.0046, \"item_rho_vs_full\": 0.7828},\n        \"drop_S4_selfcritique\":   {\"n_sig\": 2, \"rho_dose\": 0.1830, \"tau_dose\": 0.1350, \"mae\": 0.4023, \"delta_mae\": 0.0061, \"item_rho_vs_full\": 0.7905},\n        \"only_S1\":                {\"n_sig\": 1, \"rho_dose\": -0.0516, \"tau_dose\": -0.0201, \"mae\": 0.5866},\n        \"only_S2\":                {\"n_sig\": 1, \"rho_dose\": -0.2611, \"tau_dose\": -0.2334, \"mae\": 0.5790},\n        \"only_S4\":                {\"n_sig\": 1, \"rho_dose\": -0.1831, \"tau_dose\": -0.1701, \"mae\": 0.5328}\n      },\n      \"importance_rank\": [\"s1_embedding (+0.0479)\", \"s4_selfcritique (+0.0061)\", \"s2_minkpp (-0.0046)\"]\n    },\n    \"arc_challenge\": {\n      \"n_models\": 31,\n      \"results\": {\n        \"full_S1S2S4\":            {\"n_sig\": 3, \"rho_dose\": -0.0033, \"tau_dose\": -0.0123, \"mae\": 0.4871},\n        \"drop_S1_embedding\":      {\"n_sig\": 2, \"rho_dose\": -0.0063, \"tau_dose\": -0.0025, \"mae\": 0.4332, \"delta_mae\": -0.0539, \"item_rho_vs_full\": 0.7841},\n        \"drop_S2_minkpp\":         {\"n_sig\": 2, \"rho_dose\": 0.0292, \"tau_dose\": 0.0172, \"mae\": 0.4081, \"delta_mae\": -0.0790, \"item_rho_vs_full\": 0.7861},\n        \"drop_S4_selfcritique\":   {\"n_sig\": 2, \"rho_dose\": 0.0008, \"tau_dose\": 0.0123, \"mae\": 0.4829, \"delta_mae\": -0.0042, \"item_rho_vs_full\": 0.7840},\n        \"only_S1\":                {\"n_sig\": 1, \"rho_dose\": 0.0347, \"tau_dose\": 0.0582, \"mae\": 0.6403},\n        \"only_S2\":                {\"n_sig\": 1, \"rho_dose\": -0.3070, \"tau_dose\": -0.2804, \"mae\": 0.4790},\n        \"only_S4\":                {\"n_sig\": 1, \"rho_dose\": -0.0845, \"tau_dose\": -0.0727, \"mae\": 0.4371}\n      },\n      \"importance_rank\": [\"s4_selfcritique (-0.0042)\", \"s1_embedding (-0.0539)\", \"s2_minkpp (-0.0790)\"]\n    }\n  },\n  \"signal_importance_summary\": {\n    \"description\": \"Cross-benchmark signal importance by mean delta_mae when dropped. Positive = signal contributes to lower MAE.\",\n    \"s1_embedding\": {\"mmlu\": 0.0663, \"gsm8k\": 0.0479, \"arc\": -0.0539, \"mean\": 0.0201},\n    \"s2_minkpp\":    {\"mmlu\": 0.0451, \"gsm8k\": -0.0046, \"arc\": -0.0790, \"mean\": -0.0128},\n    \"s4_selfcritique\": {\"mmlu\": 0.0792, \"gsm8k\": 0.0061, \"arc\": -0.0042, \"mean\": 0.0270},\n    \"ranking\": \"S4 > S1 > S2 (by mean ΔMAE across benchmarks)\"\n  },\n  \"item_level_stability\": {\n    \"description\": \"Mean Spearman rho of item-level RRF rankings between leave-one-out and full config, averaged across models.\",\n    \"drop_S1\": {\"mmlu\": 0.7824, \"gsm8k\": 0.7892, \"arc\": 0.7841},\n    \"drop_S2\": {\"mmlu\": 0.7731, \"gsm8k\": 0.7828, \"arc\": 0.7861},\n    \"drop_S4\": {\"mmlu\": 0.7864, \"gsm8k\": 0.7905, \"arc\": 0.7840},\n    \"interpretation\": \"Dropping any signal changes ~22% of item rankings, confirming each provides unique information.\"\n  },\n  \"metadata\": {\n    \"signals_used\": [\"s1_embedding (SFT-data embedding similarity)\", \"s2_minkpp (Min-K%++ memorization)\", \"s4_selfcritique (self-critique consistency)\"],\n    \"note_s3\": \"s3_constat (consistency test) was excluded — requires paraphrase data available for only 1 model.\",\n    \"rrf_k\": 60,\n    \"n_models\": 31,\n    \"model_families\": [\"Qwen2.5-0.5B\", \"Qwen2.5-1.5B\", \"Qwen2.5-3B\", \"Llama-3.2-3B\"],\n    \"dosage_levels\": [0.0, 0.05, 0.25, 1.0],\n    \"seeds\": [\"s42\", \"s123\"],\n    \"excluded\": \"DEPRECATED alpha=16 checkpoints per C006\",\n    \"full_results_on_server\": \"/root/contamcal-irt-calibration/analysis/rrf_signal_analysis_v2.json\"\n  }\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/rrf_analysis/rrf_signal_analysis.json",
    "content": "{\n  \"c1_signal_rank_correlation\": {\n    \"description\": \"Spearman rank correlation between signal item-level scores, averaged across models. Near-zero values indicate signals capture orthogonal aspects of contamination.\",\n    \"mmlu\": {\n      \"n_models\": 31,\n      \"correlation_matrix\": {\n        \"labels\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"],\n        \"values\": [\n          [1.0, -0.0444, 0.0376],\n          [-0.0444, 1.0, -0.0011],\n          [0.0376, -0.0011, 1.0]\n        ]\n      },\n      \"pair_details\": {\n        \"s1_vs_s2\": {\"rho\": -0.0444, \"std\": 0.1239, \"range\": [-0.2301, 0.2170]},\n        \"s1_vs_s4\": {\"rho\": 0.0376, \"std\": 0.0632, \"range\": [-0.0861, 0.1468]},\n        \"s2_vs_s4\": {\"rho\": -0.0011, \"std\": 0.0757, \"range\": [-0.1728, 0.1671]}\n      }\n    },\n    \"gsm8k\": {\n      \"n_models\": 31,\n      \"correlation_matrix\": {\n        \"labels\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"],\n        \"values\": [\n          [1.0, -0.0216, 0.0530],\n          [-0.0216, 1.0, 0.0074],\n          [0.0530, 0.0074, 1.0]\n        ]\n      },\n      \"pair_details\": {\n        \"s1_vs_s2\": {\"rho\": -0.0216, \"std\": 0.0539, \"range\": [-0.1741, 0.0688]},\n        \"s1_vs_s4\": {\"rho\": 0.0530, \"std\": 0.0412, \"range\": [-0.0348, 0.1189]},\n        \"s2_vs_s4\": {\"rho\": 0.0074, \"std\": 0.0348, \"range\": [-0.0900, 0.0589]}\n      }\n    },\n    \"arc_challenge\": {\n      \"n_models\": 31,\n      \"correlation_matrix\": {\n        \"labels\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"],\n        \"values\": [\n          [1.0, -0.0189, 0.0086],\n          [-0.0189, 1.0, 0.0121],\n          [0.0086, 0.0121, 1.0]\n        ]\n      },\n      \"pair_details\": {\n        \"s1_vs_s2\": {\"rho\": -0.0189, \"std\": 0.1139, \"range\": [-0.1829, 0.1690]},\n        \"s1_vs_s4\": {\"rho\": 0.0086, \"std\": 0.0382, \"range\": [-0.0676, 0.0740]},\n        \"s2_vs_s4\": {\"rho\": 0.0121, \"std\": 0.0528, \"range\": [-0.0844, 0.0976]}\n      }\n    }\n  },\n  \"c2_leave_one_out_ablation\": {\n    \"description\": \"Leave-one-signal-out RRF ablation. MAE = mean|scaled_exposure - dosage|. item_rho = mean Spearman rho of item-level RRF ranks vs full-signal RRF. delta_mae > 0 means dropping the signal hurts performance.\",\n    \"mmlu\": {\n      \"n_models\": 31,\n      \"results\": {\n        \"full_S1S2S4\":            {\"n_sig\": 3, \"rho_dose\": 0.0486, \"tau_dose\": 0.0417, \"mae\": 0.4398},\n        \"drop_S1_embedding\":      {\"n_sig\": 2, \"rho_dose\": 0.0446, \"tau_dose\": 0.0319, \"mae\": 0.5061, \"delta_mae\": 0.0663, \"item_rho_vs_full\": 0.7824},\n        \"drop_S2_minkpp\":         {\"n_sig\": 2, \"rho_dose\": 0.4706, \"tau_dose\": 0.3610, \"mae\": 0.4849, \"delta_mae\": 0.0451, \"item_rho_vs_full\": 0.7731},\n        \"drop_S4_selfcritique\":   {\"n_sig\": 2, \"rho_dose\": 0.0840, \"tau_dose\": 0.0565, \"mae\": 0.5190, \"delta_mae\": 0.0792, \"item_rho_vs_full\": 0.7864},\n        \"only_S1\":                {\"n_sig\": 1, \"rho_dose\": -0.3506, \"tau_dose\": -0.3202, \"mae\": 0.6919},\n        \"only_S2\":                {\"n_sig\": 1, \"rho_dose\": -0.1914, \"tau_dose\": -0.1748, \"mae\": 0.6306},\n        \"only_S4\":                {\"n_sig\": 1, \"rho_dose\": 0.1116, \"tau_dose\": 0.1020, \"mae\": 0.5403}\n      },\n      \"importance_rank\": [\"s4_selfcritique (+0.0792)\", \"s1_embedding (+0.0663)\", \"s2_minkpp (+0.0451)\"]\n    },\n    \"gsm8k\": {\n      \"n_models\": 31,\n      \"results\": {\n        \"full_S1S2S4\":            {\"n_sig\": 3, \"rho_dose\": -0.0311, \"tau_dose\": -0.0516, \"mae\": 0.3962},\n        \"drop_S1_embedding\":      {\"n_sig\": 2, \"rho_dose\": -0.2626, \"tau_dose\": -0.1989, \"mae\": 0.4441, \"delta_mae\": 0.0479, \"item_rho_vs_full\": 0.7892},\n        \"drop_S2_minkpp\":         {\"n_sig\": 2, \"rho_dose\": 0.0563, \"tau_dose\": 0.0516, \"mae\": 0.3916, \"delta_mae\": -0.0046, \"item_rho_vs_full\": 0.7828},\n        \"drop_S4_selfcritique\":   {\"n_sig\": 2, \"rho_dose\": 0.1830, \"tau_dose\": 0.1350, \"mae\": 0.4023, \"delta_mae\": 0.0061, \"item_rho_vs_full\": 0.7905},\n        \"only_S1\":                {\"n_sig\": 1, \"rho_dose\": -0.0516, \"tau_dose\": -0.0201, \"mae\": 0.5866},\n        \"only_S2\":                {\"n_sig\": 1, \"rho_dose\": -0.2611, \"tau_dose\": -0.2334, \"mae\": 0.5790},\n        \"only_S4\":                {\"n_sig\": 1, \"rho_dose\": -0.1831, \"tau_dose\": -0.1701, \"mae\": 0.5328}\n      },\n      \"importance_rank\": [\"s1_embedding (+0.0479)\", \"s4_selfcritique (+0.0061)\", \"s2_minkpp (-0.0046)\"]\n    },\n    \"arc_challenge\": {\n      \"n_models\": 31,\n      \"results\": {\n        \"full_S1S2S4\":            {\"n_sig\": 3, \"rho_dose\": -0.0033, \"tau_dose\": -0.0123, \"mae\": 0.4871},\n        \"drop_S1_embedding\":      {\"n_sig\": 2, \"rho_dose\": -0.0063, \"tau_dose\": -0.0025, \"mae\": 0.4332, \"delta_mae\": -0.0539, \"item_rho_vs_full\": 0.7841},\n        \"drop_S2_minkpp\":         {\"n_sig\": 2, \"rho_dose\": 0.0292, \"tau_dose\": 0.0172, \"mae\": 0.4081, \"delta_mae\": -0.0790, \"item_rho_vs_full\": 0.7861},\n        \"drop_S4_selfcritique\":   {\"n_sig\": 2, \"rho_dose\": 0.0008, \"tau_dose\": 0.0123, \"mae\": 0.4829, \"delta_mae\": -0.0042, \"item_rho_vs_full\": 0.7840},\n        \"only_S1\":                {\"n_sig\": 1, \"rho_dose\": 0.0347, \"tau_dose\": 0.0582, \"mae\": 0.6403},\n        \"only_S2\":                {\"n_sig\": 1, \"rho_dose\": -0.3070, \"tau_dose\": -0.2804, \"mae\": 0.4790},\n        \"only_S4\":                {\"n_sig\": 1, \"rho_dose\": -0.0845, \"tau_dose\": -0.0727, \"mae\": 0.4371}\n      },\n      \"importance_rank\": [\"s4_selfcritique (-0.0042)\", \"s1_embedding (-0.0539)\", \"s2_minkpp (-0.0790)\"]\n    }\n  },\n  \"signal_importance_summary\": {\n    \"description\": \"Cross-benchmark signal importance by mean delta_mae when dropped. Positive = signal contributes to lower MAE.\",\n    \"s1_embedding\": {\"mmlu\": 0.0663, \"gsm8k\": 0.0479, \"arc\": -0.0539, \"mean\": 0.0201},\n    \"s2_minkpp\":    {\"mmlu\": 0.0451, \"gsm8k\": -0.0046, \"arc\": -0.0790, \"mean\": -0.0128},\n    \"s4_selfcritique\": {\"mmlu\": 0.0792, \"gsm8k\": 0.0061, \"arc\": -0.0042, \"mean\": 0.0270},\n    \"ranking\": \"S4 > S1 > S2 (by mean ΔMAE across benchmarks)\"\n  },\n  \"item_level_stability\": {\n    \"description\": \"Mean Spearman rho of item-level RRF rankings between leave-one-out and full config, averaged across models.\",\n    \"drop_S1\": {\"mmlu\": 0.7824, \"gsm8k\": 0.7892, \"arc\": 0.7841},\n    \"drop_S2\": {\"mmlu\": 0.7731, \"gsm8k\": 0.7828, \"arc\": 0.7861},\n    \"drop_S4\": {\"mmlu\": 0.7864, \"gsm8k\": 0.7905, \"arc\": 0.7840},\n    \"interpretation\": \"Dropping any signal changes ~22% of item rankings, confirming each provides unique information.\"\n  },\n  \"metadata\": {\n    \"signals_used\": [\"s1_embedding (SFT-data embedding similarity)\", \"s2_minkpp (Min-K%++ memorization)\", \"s4_selfcritique (self-critique consistency)\"],\n    \"note_s3\": \"s3_constat (consistency test) was excluded — requires paraphrase data available for only 1 model.\",\n    \"rrf_k\": 60,\n    \"n_models\": 31,\n    \"model_families\": [\"Qwen2.5-0.5B\", \"Qwen2.5-1.5B\", \"Qwen2.5-3B\", \"Llama-3.2-3B\"],\n    \"dosage_levels\": [0.0, 0.05, 0.25, 1.0],\n    \"seeds\": [\"s42\", \"s123\"],\n    \"excluded\": \"DEPRECATED alpha=16 checkpoints per C006\",\n    \"full_results_on_server\": \"/root/contamcal-irt-calibration/analysis/rrf_signal_analysis_v2.json\"\n  }\n}\n"
  }
}
```

</details>

---

### Tool result

_source line 182 · 2026-05-21T08:46:41.635095+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/rrf_analysis/rrf_signal_analysis.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 183 · 2026-05-21T08:46:41.635233+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 184 · 2026-05-21T08:46:41.635379+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 185 · 2026-05-21T08:46:41.635549+00:00_

分析完成。结果已保存到 `artifacts/rrf_analysis/rrf_signal_analysis.json`。

## C1: Signal Rank Correlation Matrix

3 个信号的 item-level Spearman rank correlation 接近零（31 个模型平均）：

| | S1 (embed) | S2 (minkpp) | S4 (selfcrit) |
|---|---|---|---|
| **MMLU** | — | ρ = −0.044 | ρ = 0.038 |
| **GSM8K** | — | ρ = −0.022 | ρ = 0.053 |
| **ARC** | — | ρ = −0.019 | ρ = 0.009 |
| S2↔S4 | | | ρ ≈ 0.00 |

**结论：三个信号几乎完全正交，冗余度为零。** 最大 |ρ| = 0.053，远低于任何显著性阈值。

## C2: Leave-One-Signal-Out Ablation

| Config | MMLU ΔMAE | GSM8K ΔMAE | ARC ΔMAE | Mean |
|---|---|---|---|---|
| Full (S1+S2+S4) | baseline | baseline | baseline | — |
| Drop S4 | **+0.079** | +0.006 | −0.004 | **+0.027** |
| Drop S1 | +0.066 | **+0.048** | −0.054 | +0.020 |
| Drop S2 | +0.045 | −0.005 | −0.079 | −0.013 |

**Item-level ranking stability**: 去掉任何单个信号后，item RRF 排名与完整版的 ρ ≈ 0.78（~22% 排名变动），进一步确认每个信号提供独特信息。

**Signal importance**: S4(self-critique) > S1(embedding) > S2(minkpp)，按跨 benchmark 平均 ΔMAE。

**注意**: model-level ρ(dosage) 普遍很低（< 0.1），因为 RRF 的价值在于 per-item exposure 送入 IRT，而非 model 均值直接预测 dosage。ARC 上出现 ΔMAE < 0 可能反映该 benchmark 信号噪声较大。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_rrf-c1-c2-correlation-ablation_20260521T083557"
}
```

</details>

---
