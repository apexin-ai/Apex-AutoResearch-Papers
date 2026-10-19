# ops collect a1 rerun results

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_collect_a1_rerun_results_20260522T212621_result.json`
- **Structured JSON:** [`5ff663f3d3d3145190d9.json`](../../sessions/5f/5ff663f3d3d3145190d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。汇总：

## A1 Rerun 完整结果 (800 eps)

| Task | TSR | CAR | Fake Safe | Safe Disp Mean |
|------|-----|-----|-----------|----------------|
| orange_juice | 0% | 96.0% | 192/192 (100%) | 0.000315mm |
| chocolate_pudding | 0% | 82.0% | 162/164 (98.8%) | 0.007588mm |
| milk | 0% | 97.0% | 194/194 (100%) | 0.000288mm |
| bbq_sauce | 0% | 91.0% | 181/182 (99.5%) | 0.001293mm |
| **Overall** | **0%** | **91.5%** | **729/732 (99.6%)** | — |

**Real safe: 3/800 (0.4%)**

Safe displacement 分布：74% < 1μm（纳米级），26% 在 1μm-0.1mm，仅 0.4% ≥ 0.1mm。

Collision episodes (68个)：displacement mean=45.92mm, max=286.53mm —— 唯一有真实 movement 的 episodes 全部碰撞。

**与 Baseline 对比**：baseline CAR=83% fake=99.4%, A1 CAR=91.5% fake=99.6%。A1 的 CAR 提升完全来自更严重的 action collapse，SDF auxiliary loss 没有带来任何 real safety improvement。200 eps 完整数据完全确认了之前 50 eps 样本的结论。

---
