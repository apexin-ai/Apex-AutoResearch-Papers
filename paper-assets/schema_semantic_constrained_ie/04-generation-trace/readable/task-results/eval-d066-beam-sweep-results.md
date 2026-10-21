# eval d066 beam sweep results

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_d066_beam_sweep_results_20260520T022051_result.json`
- **Structured JSON:** [`4db02fd9d6c0a52ec0a9.json`](../../sessions/4d/4db02fd9d6c0a52ec0a9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估完成（6/8 configs）。核心发现：

| k | Mode | DR% | CF% | E-F1 | R-F1 | Avg Time |
|---|------|-----|-----|------|------|----------|
| 1 | unc | 2.11 | 0.00 | 66.88 | 42.95 | 2.49s |
| 1 | con | 0.00 | 0.50 | 66.88 | 42.95 | 2.93s |
| 2 | unc | 1.54 | 0.00 | **67.79** | **44.75** | 2.95s |
| 2 | con | 0.00 | 0.11 | 67.71 | 44.60 | 3.46s |
| 4 | unc | 1.89 | 0.00 | 67.49 | 43.72 | 3.49s |
| 4 | con | 0.00 | 0.00 | 67.22 | 43.60 | 4.07s |

ET% = 0, RV% = 0, PF% = 0 across all configs（省略）。

**关键结论**：
- Fine-tuned Qwen 在 SciERC 上完全内化了 entity type 和 relation type schema，只剩 domain-range 违约（1.5-2.1%）
- Constrained decoding 将 DR% 降至 0%，F1 损失 ≤0.15pp
- **k=2 是拐点**：k=1→2 有明显提升，k=2→4 反而下降（precision 掉得比 recall 涨得快）
- DR% 在 unconstrained 下不是单调递减的（k=4 > k=2），否定了"beam 越宽 violations 越少"的假设
- **Pareto 最优**: k=2 constrained（近零违约 + 最佳 F1 区间 + 可控延迟）

beam8（unc+con）仍在运行中，预计 ~1.5h 后完成。报告已写入 `artifacts/_project/report/d066_beam_sweep_eval.md`，registry 已更新为 ANALYZING。

---
