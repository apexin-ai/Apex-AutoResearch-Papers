# analysis results compilation

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_results-compilation_20260514T183707_result.json`
- **Structured JSON:** [`1623b9c8efd7807ddd66.json`](../../sessions/16/1623b9c8efd7807ddd66.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已输出到 `/root/autodl-tmp/agent_progress_probe/paper_results_compilation.md`（353 行）。

汇编涵盖 25 个实验、6 大表 + 补充数据：

| 表 | 内容 | 关键数字 |
|---|------|---------|
| Table 1 | 方法对比 | Structural RF 0.9951 vs Probe 0.9055 vs LLM-judge 0.6625 |
| Table 2 | Probe 消融 (6 子表) | Encoder/窗口/SupCon/架构/数据量/多seed |
| Table 3 | LF 时序动态 | SWE vs OH 跨 agent，cmd_rep 角色反转 |
| Table 4 | LF hold-one-out | file_diff 最关键 (−22.3pp) |
| Table 5 | TLM 对比 | TWV σ=2 最优但仅 +0.6pp vs MV (negative) |
| Table 6 | 跨 agent 迁移 | Structural GB 0.9674 (OH all) vs Probe 0.532 (zero-shot) |

每个数字都标注了 `exp_id` 和文件路径。所有 conf≥2 数字标注了 circular eval caveat。未找到的数字标为 "—"。

---
