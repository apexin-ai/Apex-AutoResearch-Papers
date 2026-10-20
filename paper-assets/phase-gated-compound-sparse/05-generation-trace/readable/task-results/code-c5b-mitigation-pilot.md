# code c5b mitigation pilot

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_c5b-mitigation-pilot_20260514T145203_result.json`
- **Structured JSON:** [`db98f71f66f6220736ba.json`](../../sessions/db/db98f71f66f6220736ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已就绪。

**现状总结**：

`/root/autodl-tmp/pacs/profiling/run_mitigation_pilot.py`（575行）已完整实现 C5b pilot 设计：

- **`compute_phase_aware_sparsity`** — compute-matched allocation，s_trans cap=0.50，surplus 重分配到 reasoning。验证通过：s=0.25 → `{exec: 0.15, reas: 0.25, trans: 0.35}`，weighted avg = 0.2500
- **`assign_heuristic_phases`** — token position ratio (0.33/0.67 boundaries)
- **`eval_condition`** — per-phase importance-based masking + 3 sparse forward passes → per-phase II
- **`run_mitigation_pilot`** — 主循环：generate → capture step sparsity → oracle/heuristic segmentation → 3 conditions × 2 sparsity levels → aggregate recovery + Wilcoxon + bootstrap CI
- **输出**：`mitigation_pilot_results.json`，包含 per-problem II、recovery metrics、gate pass/fail

**修复**：`__package__` 检查从 `is None` 改为 `not __package__`，支持从 profiling 目录直接 import。

**运行方式**：
```bash
cd /root/autodl-tmp/pacs/profiling
python run_mitigation_pilot.py --gpu 0
# 或
python -m pacs.profiling.run_mitigation_pilot --gpu 0
```

GPU 释放后即可跑。

---
