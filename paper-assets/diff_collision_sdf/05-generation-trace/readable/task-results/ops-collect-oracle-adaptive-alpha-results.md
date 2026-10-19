# ops collect oracle adaptive alpha results

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_collect_oracle_adaptive_alpha_results_20260522T211919_result.json`
- **Structured JSON:** [`c62d35047eb1a13b923a.json`](../../sessions/c6/c62d35047eb1a13b923a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三组 oracle 实验全部完成，Registry 已更新。汇总：

| 方法 | CAR | Fake Safe Rate | Refine/ep | Grad Mag |
|------|-----|---------------|-----------|----------|
| Baseline (无 refine) | ~79% | ~99% | 0 | — |
| Fixed α=0.005 (action-space) | 73.1% | 98.3% | 14.8 | 0.29-0.42 |
| Adaptive α (action-space) | 75.0% | 98.3% | 14.2 | 0.18-0.49 |
| Feature-space oracle | 76.9% | 96.7% | 241.7 | 0.004-0.006 |

所有方法 TSR=0%。chocolate_pudding 最差（47.5%-55%）。

**统一结论**：即使使用 GT SDF，三种 gradient-based refinement 变体全部 negative——CAR 均低于 baseline，且 96-98% 的 "safe" episodes 是 fake safe（displacement<0.1mm = action collapse）。Alpha 大小不是关键因素，feature-space 也未优于 action-space。根本问题：SDF gradient refinement 导致 action collapse 而非真正避障。

---
