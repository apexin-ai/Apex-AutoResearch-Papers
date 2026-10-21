# analysis power cr2 cr3

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_power-cr2-cr3_20260522T231641_result.json`
- **Structured JSON:** [`8d8dc6a9b77ae2e289f5.json`](../../sessions/8d/8d8dc6a9b77ae2e289f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存。汇总：

### Part A: Power Analysis

| β_std | β_raw | Power |
|-------|-------|-------|
| 0.1 | 0.724 | 0.646 |
| 0.2 | 1.449 | 0.997 |
| 0.3 | 2.173 | 1.000 |
| 0.5 | 3.622 | 1.000 |

**MDE at 80% power: β_std = 0.144**（即标准化效应量 ~0.14 SD 就能在当前设计下被检测到）。实际观测的 K_eff 效应远小于此阈值，与 0/12 FDR 显著一致。

### Part B: CR1 vs CR2 vs CR3

| Method | η_max FDR sig | K_eff FDR sig |
|--------|---------------|---------------|
| CR1 | 8/12 | 0/12 |
| CR2 | 8/12 | 0/12 |
| CR3 | 4/12 | 0/12 |

CR2（偏差校正）与 CR1 结果一致。CR3（jackknife）更保守，η_max 显著数从 8 降到 4，K_eff 仍然 0/12。三种方法均确认 K_eff 在当前数据中无统计显著效应。

输出文件：`/root/cert_manip_resist_eval/artifacts/results/plan001/power_cr2_cr3.json`

---
