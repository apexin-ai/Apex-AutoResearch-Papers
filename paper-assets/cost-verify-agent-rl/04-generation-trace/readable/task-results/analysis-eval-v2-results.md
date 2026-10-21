# analysis eval v2 results

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_v2_results_20260520T085112_result.json`
- **Structured JSON:** [`03dc9fe14c965e4262f0.json`](../../sessions/03/03dc9fe14c965e4262f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## eval_v2 中间报告（仍在运行）

**进度**: 1345/1796 episodes（74.9%），进程 195853 运行中

**当前总 success rate**: 442/1345 = **32.9%**

**GPU 状态**: cuda:0 和 cuda:1 均在使用（各 ~84GB/98GB），eval 占用中

**磁盘**: /root/autodl-tmp 190G/250G (76%)，空间充足

### 按任务类型分解（已完成部分）

| 任务 | 成功/总数 | 成功率 |
|------|----------|--------|
| lifespan-longest-lived | 28/31 | 90.3% |
| lifespan-longest-lived-then-shortest-lived | 28/31 | 90.3% |
| find-non-living-thing | 58/75 | 77.3% |
| lifespan-shortest-lived | 21/31 | 67.7% |
| find-living-thing | 49/75 | 65.3% |
| power-component | 3/5 | 60.0% |
| find-animal | 37/75 | 49.3% |
| measure-melting-point-unknown | 27/75 | 36.0% |
| mendelian-genetics-unknown | 35/120 | 29.2% |
| mendelian-genetics-known | 8/30 | 26.7% |
| inclined-plane-friction-unnamed | 10/40 | 25.0% |
| inclined-plane-friction-named | 83/346 | 24.0% |
| measure-melting-point-known | 25/109 | 22.9% |
| chemistry-mix-paint-secondary | 2/9 | 22.2% |
| inclined-plane-determine-angle | 7/42 | 16.7% |
| change-state-of-matter / melt | 1/7 each | 14.3% |
| test-conductivity | 8/59 | 13.6% |
| find-plant | 9/75 | 12.0% |
| grow-fruit | 2/31 | 6.5% |
| boil/chemistry-mix/freeze/grow-plant/identify-life-stages/power-renewable | 0% | 0.0% |

还剩 ~451 episodes，当前在跑 test-conductivity 系列。按日志节奏预计还需数小时完成。

---
