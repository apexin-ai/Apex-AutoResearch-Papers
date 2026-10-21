# analysis exp 015

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_015_20260522T061658_result.json`
- **Structured JSON:** [`d187098713a0ef8c607a.json`](../../sessions/d1/d187098713a0ef8c607a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp_015 分析完成。关键结果：

**Type II 轨迹在 3 个 seed 上全部复现。** SLV 在 Gen1-2 出现浅 dip（平均深度 −3.59），Gen3 恢复后单调递增。

**Gen10 三 seed 汇总（mean ± std）：**
| Metric | Value |
|--------|-------|
| SLV (log_det) | 2488.11 ± 2.89 |
| PPL | 13.409 ± 0.18 |
| eff_rank | 513.82 ± 1.59 |
| distinct-4 | 0.3422 ± 0.013 |
| SLV 总变化 | +5.13% |

cross-seed 方差极低（SLV CV=0.12%），r=0.25 条件下 collapse 动态高度可复现。

产出：
- 报告：`artifacts/exp_015/report/exp_015_cross_seed_analysis.md`（已注册 `art_20260522_c032c2`）
- Registry：exp_015 → DONE (success)，含完整 per-gen metrics + notes

---
