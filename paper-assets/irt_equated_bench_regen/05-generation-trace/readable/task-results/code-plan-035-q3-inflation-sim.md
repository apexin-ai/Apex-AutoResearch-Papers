# code plan 035 q3 inflation sim

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_035_q3_inflation_sim_20260521T154538_result.json`
- **Structured JSON:** [`845e1518573cbff31923.json`](../../sessions/84/845e1518573cbff31923.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Plan 035 完成。全部产出：

**产出文件：**
- `artifacts/plan_035_q3_inflation_sim/plan_035_q3_inflation_sim.py` — 向量化模拟脚本
- `artifacts/plan_035_q3_inflation_sim/permutation_null_results.csv` — 8000 行详细结果
- `artifacts/plan_035_q3_inflation_sim/inflation_summary.csv` — 8 subjects 汇总
- `artifacts/plan_035_q3_inflation_sim/plan_035_report.md` — 完整报告

**核心结论：**

| 指标 | LD 膨胀 (pp) | 判定 |
|------|-------------|------|
| ETS-C | +0.0004 pp (最大 +0.0010 pp) | 远 < 3 pp |
| p<0.05 | −0.0019 pp | 无膨胀（甚至略反向） |

Cross-subject matching 完全隔离了 within-subject LD 对 MH-DIF FPR 的影响。即使 moral_scenarios 有 34.2% item pairs |Q3|>0.20，ETS-C 膨胀仍 < 0.01 pp。两个原因：
1. Cross-subject matching 变量不含当前 subject 的 items，LD 无法污染 matching
2. ETS-C 的 |Δ|≥1.5 阈值本身极其保守（实际 FPR 仅 ~0.1%，远低于 nominal 5%）

Q3 与膨胀无显著相关（Spearman ρ = −0.24, p = 0.57）。

---
