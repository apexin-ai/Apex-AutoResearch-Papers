# deploy obs only norm003 pair

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_obs-only-norm003-pair_20260519T115838_result.json`
- **Structured JSON:** [`f96efd87222a1132ed50.json`](../../sessions/f9/f96efd87222a1132ed50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都在正常加载模型权重。汇报如下：

---

## 实验部署

| 实验 | 服务器 | GPU | tmux session | PID | 状态 |
|---|---|---|---|---|---|
| obs_only ε=0.03 seed47 | bjb1-32546 | cuda:3 | `eval-obs-only-object-norm003-seed47-r2` | 894890 | 正在加载模型权重，启动成功 |
| obs_only ε=0.03 seed48 | bjb1-18228 | cuda:1 | `eval-obs-only-object-norm003-seed48` | 67819 | 正在加载模型权重，启动成功 |

残留 tmux session 均为空，已清理后重新提交。

---

## 收割结果

### bjb1-32546: perdof-norm003-seed48 (SR=0.13)

| Task | SR | Succ/Total |
|---|---|---|
| alphabet_soup | 0.0 | 0/10 |
| cream_cheese | 0.0 | 0/10 |
| salad_dressing | 0.2 | 2/10 |
| bbq_sauce | 0.2 | 2/10 |
| ketchup | 0.0 | 0/10 |
| tomato_sauce | 0.1 | 1/10 |
| butter | 0.1 | 1/10 |
| milk | 0.1 | 1/10 |
| chocolate_pudding | 0.3 | 3/10 |
| orange_juice | 0.3 | 3/10 |
| **Overall** | **0.13** | **13/100** (10 tasks × 10 rollouts) |

### bjb1-18228: lto-splitA-vla-only-r3 (SR=0.14)

| Task | SR | Succ/Total |
|---|---|---|
| salad_dressing | 0.3 | 3/10 |
| ketchup | 0.0 | 0/10 |
| tomato_sauce | 0.1 | 1/10 |
| milk | 0.2 | 2/10 |
| orange_juice | 0.1 | 1/10 |
| **Overall** | **0.14** | **7/50** (5 tasks × 10 rollouts) |

注意：lto-splitA-vla-only-r3 只有 5 个 task（不是完整 10 task benchmark），n_rollouts=10。

---

无异常。

---
