# eval random pruning baseline

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_random_pruning_baseline_20260517T063110_result.json`
- **Structured JSON:** [`97162ede97d108718be2.json`](../../sessions/97/97162ede97d108718be2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**已执行：**
- 修改 `eval_success_rate_libero.py`：添加 `random_prune` mode（用 `torch.rand` 替代 ACIS importance scores，其余 top-k + masking 逻辑不变）
- 提交 eval job 到 GPU 0，tmux session `eval_random_prune_baseline`，PID 8212
- Checkpoint: `libero_imm_twostage_fullft/stage1_done/checkpoint.pt`（Stage1 ACIS 架构 + Full FT 底座）
- Suite: `libero_object`，10 tasks × 50 episodes = 500 total，seed=42
- 输出: `eval_results/eval_random_prune_object.json`

Job 已正常启动，正在运行 Task 0。预计运行数小时。结果出来后可与 unpruned baseline（44.8%）对比。

---
