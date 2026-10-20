# fix cleanup old g values

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_cleanup_old_g_values_20260521T121647_result.json`
- **Structured JSON:** [`5f76280f81f0aac044ac.json`](../../sessions/5f/5f76280f81f0aac044ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

检查完毕，汇总如下：

### report.md
无旧值残留。

### ROADMAP.md
无旧值残留。

### memory.md (第31行)
包含 `0.611→0.918` 和 `0.745→0.960`，但这是"修正前→修正后"的审计记录，属于有意保留的历史对比，**不应修改**。

### Registry
逐条检查：

| 实验 | 发现 | 是否需修改 |
|------|------|-----------|
| **exp001_llama** | notes: `"Stored G=0.6108, corrected G=0.9184"` | 否 — 审计修正记录 |
| **exp001b_resampling** | metrics: `g_item_mean=0.96`, `g_item_sample1=0.9637`, `g_item_sample2=0.962`, `g_item_sample3=0.9548`；`item_id_pct_mean=74.48`（方差百分比，非 G_item） | 否 — 已是修正值 |
| **mvp_phase_a** | `g_coefficient_correct=0.357` — 这是 MVP 108-condition 设计的 binary_correct G 系数，非本次修正的 G_item | 否 — 不同指标 |
| 其余 6 个实验 | 无 G_item 字段 | 否 |

**结论：所有项目文件中无需替换的旧 G_item 值。** report.md 和 ROADMAP.md 已干净，memory.md 和 registry 中的旧值均为审计修正记录（"修正前→修正后"格式），按规则保留。

---
