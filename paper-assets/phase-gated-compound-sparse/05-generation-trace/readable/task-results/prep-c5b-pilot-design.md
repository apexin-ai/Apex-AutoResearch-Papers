# prep c5b pilot design

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_c5b-pilot-design_20260514T144238_result.json`
- **Structured JSON:** [`f1067a02abfea70a8fa7.json`](../../sessions/f1/f1067a02abfea70a8fa7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

方案已写入 `artifacts/c5b_pilot_design.md` 并注册 (`art_20260514_4d09f3`)。

核心设计要点：

**条件设计**：
- **Uniform baseline** — 复用现有 bf16 importance 数据，零 GPU 成本
- **Oracle** — 用真实 quantile phase labels 分配 sparsity：execution 相降 δ=0.10，transition 相加，总量 compute-matched
- **Heuristic** — token position ratio (pos/seq_len 三等分) 作为最简 phase proxy，零成本下界

**规模**：n=30 problems × {s025, s030} × 3 conditions，仅 DeepSeek（信号最强），单 GPU ~1.5h

**评估**：per-problem weighted II 的 recovery %，paired Wilcoxon + bootstrap CI (B=10000)。Gate: oracle recovery >30% 任一 sparsity level。

**实现**：新建 `run_mitigation_pilot.py`，复用现有 `InteractionIndexCalculator` 和 phase segmentation，新增 ~150 行（phase-aware allocation + heuristic assignment + main loop）。

**时间线**：等 GPU 2/3 空闲（c2_qw_n500 完成后，预计 05-15 中午），1.5h 跑完，远在 05-22 deadline 之前。

---
