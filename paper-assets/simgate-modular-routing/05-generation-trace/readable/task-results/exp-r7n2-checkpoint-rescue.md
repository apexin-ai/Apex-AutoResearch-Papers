# exp r7n2 checkpoint rescue

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_r7n2-checkpoint-rescue_20260516T034145_result.json`
- **Structured JSON:** [`62dbb33aa19007947af9.json`](../../sessions/62/62dbb33aa19007947af9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**当前状态：**

| 发现 | 详情 |
|------|------|
| Checkpoint 存活 | **全部丢失** — `results/ablation_data_size/` 为空 |
| 执行操作 | 全部 12 组 retrain + dual eval |
| 脚本修改 | 添加 `--scales` 参数支持并行分配 |
| 并行策略 | GPU0: 25pct+100pct, GPU1: 50pct+75pct |

脚本本身已有：
- 每个 run 完成后立即写 `eval_results.json`（增量保存）
- `_run_is_complete()` resume 逻辑（即使被 kill 也能接续）
- step-level + episode-level 双套 eval

等 ~4.5 分钟后检查进度。

---
