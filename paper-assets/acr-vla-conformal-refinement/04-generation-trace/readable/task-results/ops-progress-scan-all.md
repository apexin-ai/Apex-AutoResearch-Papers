# ops progress scan all

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_progress-scan-all_20260515T113904_result.json`
- **Structured JSON:** [`37196fb5bbd6bb42016f.json`](../../sessions/37/37196fb5bbd6bb42016f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全量扫描完成，报告已保存至 `artifacts/progress_scan_loop9.md`。

**状态总览：15/15 进程全部存活。**

### Object Eval (bjb1-32546) — 均完成 ~60%

| 方法 | 6-task avg | 排名 |
|------|-----------|------|
| obs_only n=0.2 | **18.0%** | 1st |
| obs_only n=0.1 | 13.3% | 2nd |
| vla_mean | 10.0% | 3rd |
| perdof n=0.1 | 8.3% | 4th |
| reconvla | 6.7% | 5th |
| scalar n=0.1 | 3.3% | 6th |

### Magnitude Sweep — Spatial (bjb2-28827)

**perdof**: 小 norm 明显更好（0.03→33.3% vs 0.3→23.3%），单调递减趋势。
**obs_only**: norm 几乎不影响性能（42.9-45.7%，完成 7T 的三个实验），远超 perdof。

### 其他
- **bjb1-18228**: obs_only-norm03 完成 5/10 (46.0%)；scalar-r2 完成 5/7 (26.0%)
- **bjb2-40593**: obs_only-norm003 完成 3/10 (63.3%，但前 3 个是最简单的 task)
- 最快完成的将是 scalar-r2（~2h）和 bjb2-28827 obs_only（~3h）

---
