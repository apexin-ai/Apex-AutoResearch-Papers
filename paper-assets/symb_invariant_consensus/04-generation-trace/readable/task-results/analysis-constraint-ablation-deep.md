# analysis constraint ablation deep

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_constraint-ablation-deep_20260517T171933_result.json`
- **Structured JSON:** [`93570eff851d9cc8c5f5.json`](../../sessions/93/93570eff851d9cc8c5f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

**Raw constraints 不可用**（exp-001 未保存 Z3 formulas），使用 score-level proxy 分析。

| Method | Accuracy | Δ vs SC | McNemar p |
|--------|----------|---------|-----------|
| SICA-MaxSAT | 76.49% | +0.25pp | 0.856 |
| SICA-count-only | 76.62% | +0.37pp | 0.711 |
| SICA-random-weight | 75.87% | -0.37pp | 0.743 |
| SC@K | 76.24% | — | — |

**关键数字：**
- MaxSAT vs Count-only agreement: **803/804 (99.9%)**，95%CI=[99.6%, 100.0%]
- 唯一分歧：folio_062（分差仅 0.5，本质是 tie）
- Margin analysis：305 个有 exclusion 的 multi-candidate 问题中，仅 35 个理论可翻转，margin 中位数 4.69x
- 100-seed random-weight：agreement 96.8%±0.5%

**结论：SAT solver 对最终答案选择几乎无贡献，constraint 计数即决定结果。**

输出文件：
- 脚本：`scripts/constraint_ablation_deep.py`
- 结果：`results/constraint_ablation/ablation_results.json`

---
