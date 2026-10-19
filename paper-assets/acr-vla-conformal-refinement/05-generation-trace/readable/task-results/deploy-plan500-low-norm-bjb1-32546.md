# deploy plan500 low norm bjb1 32546

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_plan500-low-norm-bjb1-32546_20260528T031742_result.json`
- **Structured JSON:** [`32688b3df9fa3337a27e.json`](../../sessions/32/32688b3df9fa3337a27e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已正常启动，模型加载中。

---

## 1. 数据缺口分析

| 条件 | 有效 seed（非 westd） | 缺口 |
|------|----------------------|------|
| obs_only ε=0.03 | s43 (bjb1, bjb2), s44 (bjb1, bjb2) | 充足 |
| obs_only ε=0.05 | s43 (bjb1, bjb2), s44 (bjb1, bjb2), s45 (bjb2), s46 (cqa1) | 充足 |
| **perdof ε=0.03** | s43-v3 (cqa1) | **s44 缺失**（仅有 westd 版本） |
| **perdof ε=0.05** | s43-v3 (cqa1) | **s44 缺失**（仅有 westd 版本） |

perdof 两个 norm 的 s44 是 Figure 2 最弱环节，已优先部署。

## 2. 部署详情

| exp_id | GPU | PID | 参数 |
|--------|-----|-----|------|
| `eval-perdof-object-norm003-s44-v3` | bjb1-32546 cuda:3 | 515221 | mode=crm_perdof, norm=0.03, seed=44, K=10, 20 rollouts×10 tasks |
| `eval-perdof-object-norm005-s44-v3` | bjb1-32546 cuda:4 | 515577 | mode=crm_perdof, norm=0.05, seed=44, K=10, 20 rollouts×10 tasks |

命令模板与 cqa1 上 s43-v3 成功实验完全一致（仅改 seed 和 output_file）。预计运行 3-5 小时。

---
