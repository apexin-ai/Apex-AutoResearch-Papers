# ops exp025c script and submit

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp025c_script_and_submit_20260515T080949_result.json`
- **Structured JSON:** [`b8f3bc51cb26677122c5.json`](../../sessions/b8/b8f3bc51cb26677122c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`run_alfworld_exp025c.sh` 已创建，验证通过。

**与 dry run 的对比（dry run 成功完成了 1 epoch）：**

| 参数 | dry run | exp025c | 说明 |
|------|---------|---------|------|
| `total_epochs` | 1 | **150** | 正式训练 |
| `test_freq` | 1 | **5** | 每 5 epoch 验证 |
| `enforce_eager` | False | **True** | 跳过 CUDA graph 捕获，更稳定 |
| `gpu_memory_utilization` | 0.6 | **0.4** | 更保守，留余量 |
| `logger` | console | **console+wandb** | 记录到 W&B |
| `experiment_name` | exp025_degraded_dryrun | **exp025c_grpo_qwen3_1.7b** | |
| 线程限制 env vars | 无 | **已加** | 防 cgroup pids.max 撞限 |

**不变项（与 dry run 一致）：**
- `CUDA_VISIBLE_DEVICES=0`, `n_gpus_per_node=1`, `TP=1`
- `env.rollout.n=2`, `data.val_batch_size=16` (满足 C003 ≥16)
- `VLLM_ATTENTION_BACKEND=FLASH_ATTN`
- `save_freq=25`, `val_before_train=True`
- 所有 model/actor/ref 参数完全一致

**未加 `ray_init.num_cpus=8`**——dry run 没用这个参数也成功了，verl 配置系统中不确定此参数名是否有效。

脚本就绪，可以提交训练。

---
