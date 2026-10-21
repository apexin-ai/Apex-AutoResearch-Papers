# ops p0a kill bjb1 32546 cuda4

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_p0a-kill-bjb1-32546-cuda4_20260515T101255_result.json`
- **Structured JSON:** [`556593538b96cbe7b83c.json`](../../sessions/55/556593538b96cbe7b83c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 1. Kill 结果
- PID 42311/42319/42320: **全部 DEAD**
- PID 44270 (obs-only-norm02): **存活**，已运行 4h51m

### 2. cuda:4 显存
**4269 MiB** — 已降到正常单进程水平。

### 3. 全 GPU 状态

| GPU | Util | 显存占用 | 总显存 | 进程 |
|-----|------|----------|--------|------|
| 0 | 21% | 3306 MiB | 24564 MiB | reconvla |
| 1 | 23% | 3342 MiB | 24564 MiB | perdof |
| 2 | 22% | 3342 MiB | 24564 MiB | obs-only (norm=0.1) |
| 3 | 23% | 3342 MiB | 24564 MiB | scalar |
| 4 | 23% | 4269 MiB | 24564 MiB | obs-only-norm02 (PID 44270) |
| 5 | 21% | 3306 MiB | 24564 MiB | vla-mean |

6 GPU 全部在跑 eval，状态正常。

### 4. Object Eval 进度（共 10 tasks）

| 实验 | GPU | 已完成 | 当前状态 | 最近几个 task 成功率 |
|------|-----|--------|----------|---------------------|
| reconvla | 0 | 5/10 | 在跑 T6 | cream_cheese 0%, salad_dressing 10%, bbq_sauce 30%, ketchup 0% |
| perdof | 1 | 5/10 | tomato_sauce 5/10 rollout 中 | salad_dressing 20%, bbq_sauce 30%, ketchup 0% |
| obs-only (norm=0.1) | 2 | **5/10** | 在跑 T6 | cream_cheese 10%, salad_dressing 20%, bbq_sauce 40%, ketchup 10% |
| scalar | 3 | 5/10 | 在跑 T6 | cream_cheese 0%, salad_dressing 10%, bbq_sauce 10%, ketchup 0% |
| obs-only-norm02 | 4 | 3/10 | bbq_sauce 5/10 rollout 中 | alphabet_soup 0%, cream_cheese 0%, salad_dressing 30% |
| vla-mean | 5 | 5/10 | 在跑 T6 | cream_cheese 0%, salad_dressing 10%, bbq_sauce 30%, ketchup 10% |

**obs-only (cuda:2) 已完成 5/10 tasks，过了 T5。** obs-only-norm02 (cuda:4) 因为晚启动 + 刚清理僵尸进程，只完成 3/10，落后其他实验。

---
