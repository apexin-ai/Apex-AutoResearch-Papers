# code interim analysis scripts

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_interim-analysis-scripts_20260519T004513_result.json`
- **Structured JSON:** [`4307c1d37861779a1d6e.json`](../../sessions/43/4307c1d37861779a1d6e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个脚本全部 dry-run 成功，输出正确。汇总：

### 脚本 1: `analyze_seed_replication.py` (westd-16639)
- **路径**: `/root/symb_invariant_consensus/scripts/analyze_seed_replication.py`
- **数据**: exp-052 (seed=123) 204条 ✓, exp-053 (seed=456) 204条 ✓, exp-033 (seed=42) 用 hardcoded reference
- **结果**: seed=42 delta=+4.90 (p=0.013), seed=123 delta=+3.43 (p=0.039), seed=456 delta=-0.49 (p=1.0)
- **输出**: `results/seed_replication_summary.json` ✓

### 脚本 2: `track_discordant_pairs.py` (westd-25068)
- **路径**: `/root/symb_invariant_consensus/scripts/track_discordant_pairs.py`
- **数据**: exp-028b 118/204 条 (仍在运行)
- **结果**: SC=84.75%, SICA=86.44%, delta=+1.69pp, b=2, c=0, override precision=1.0
- **输出**: `results/exp028b_discordant_tracking.json` ✓

### 脚本 3: `summarize_k_sensitivity.py` (westd-25068)
- **路径**: `/root/symb_invariant_consensus/scripts/summarize_k_sensitivity.py`
- **数据**: k4=204 done, k8=204 done, k12=204 (exp-033 reference), k16=49/204 running, k20=pending
- **结果**: K=12 是 delta 最高点 (+4.90, p=0.013)，K=4/8 delta 为负
- **输出**: `results/k_sensitivity_summary.json` ✓

---
