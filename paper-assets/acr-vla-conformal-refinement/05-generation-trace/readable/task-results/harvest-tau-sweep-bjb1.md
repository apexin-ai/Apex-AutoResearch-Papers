# harvest tau sweep bjb1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_tau-sweep-bjb1_20260523T061143_result.json`
- **Structured JSON:** [`8f89eff363a3bf3c3701.json`](../../sessions/8f/8f89eff363a3bf3c3701.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部收割完毕，registry 已更新为 DONE。

## 汇总表

| exp_id | mode | SR | vs baseline | trigger_rate | conclusion | GPU 释放 |
|--------|------|----|-------------|-------------|------------|----------|
| eval-supp-adapt-tau025-spatial-s42-r2 | adaptive_conformal, tau=0.25 | **82.0%** | +3.5pp | 19.4% | success | cuda:2 已空闲 |
| eval-supp-crm-norm02-spatial-s42-r2 | crm_obs_only, norm=0.2 | **79.0%** | +0.5pp | — | success | cuda:0 已空闲 |
| eval-supp-adapt-tau015-spatial-s42-r2 | adaptive_conformal, tau=0.15 | **80.5%** | +2.0pp | 40.7% | success | cuda:1 已空闲 |
| eval-supp-adapt-tau035-spatial-s42-r2 | adaptive_conformal, tau=0.35 | **80.0%** | +1.5pp | 12.2% | success | cuda:4 刚释放 |

## Threshold sweep 趋势

| tau | SR | trigger_rate | 解读 |
|-----|-----|-------------|------|
| 0.15 | 80.5% | 40.7% | 触发太频繁，overcorrection 拉低 SR |
| 0.25 | **82.0%** | 19.4% | 最优平衡点 |
| 0.35 | 80.0% | 12.2% | 触发太保守，miss 可纠正的 step |

**tau=0.25 是最优 threshold**，符合 Director 预期 (82%)。CRM norm=0.2 = 79.0%，也符合预期 (79%)。

## GPU 状态

- cuda:0,1,2 — 完全空闲 (2 MiB)
- cuda:3 — 低负载 (544 MiB, 10% util)，可能是其他进程
- cuda:4 — tau=0.35 刚完成，进程将退出释放
- cuda:5 — 有负载 (2008 MiB, 26% util)，非本批实验

---
