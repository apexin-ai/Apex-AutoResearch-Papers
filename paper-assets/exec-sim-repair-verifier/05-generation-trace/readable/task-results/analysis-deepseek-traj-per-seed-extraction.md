# analysis deepseek traj per seed extraction

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deepseek-traj-per-seed-extraction_20260518T185428_result.json`
- **Structured JSON:** [`9c70448fd304c4311bee.json`](../../sessions/9c/9c70448fd304c4311bee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

**6 seeds (s42, s123, s0, s456, s789, s999)：**

| Seed | Acc | Correct/48 |
|------|-----|-----------|
| s42  | 81.25% | 39 |
| s999 | 79.17% | 38 |
| s123 | 75.00% | 36 |
| s0   | 75.00% | 36 |
| s456 | 75.00% | 36 |
| s789 | 66.67% | 32 |

Mean=75.35%, SD=5.00pp, Range=[66.67%, 81.25%]

**二项 CI 分析结论：** n=48, p=0.7535 下 binomial SE = 6.22pp，observed SD = 5.00pp < expected 6.22pp。观察到的 seed 间方差完全在统计噪声范围内，无模型不稳定性证据。所有 6 个 seed 都在 95% CI [63.16%, 87.54%] 内。

报告已写入 `artifacts/deepseek_traj_per_seed_analysis.md`。

---
