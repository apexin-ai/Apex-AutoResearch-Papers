# ssh exec retrain final v3

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exec-retrain-final-v3_20260516T160412_result.json`
- **Structured JSON:** [`edbf18502b14acd1cc6d.json`](../../sessions/ed/edbf18502b14acd1cc6d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出汇总

### 1. Kill 确认 + GPU 空闲
无残留 train_grpo 进程，双卡 0MiB → 启动后各占 ~81GB。

### 2. 配置文件 (`configs/grpo_exec_retrain_v3.yaml`)
```yaml
model_path: /root/autodl-tmp/models/Qwen3-4B
data_path: data/proofwriter_fol_100.jsonl
reward_mode: execution_only
num_steps: 500
per_device_batch_size: 2
gradient_accumulation_steps: 4
num_generations: 8
max_completion_length: 512
learning_rate: 1.0e-6
save_steps: 50
save_total_limit: 3
gradient_checkpointing: true
no_wandb: true
solver: prover9
```

### 3. 双卡提交确认
| 实验 | GPU | PID | tmux session |
|------|-----|-----|--------------|
| exec-retrain-v3-s42 | cuda:0 | **875499** | exec-retrain-v3-s42 |
| exec-retrain-v3-s43 | cuda:1 | **875573** | exec-retrain-v3-s43 |

### 4. 前 5 步日志

**s42** (GPU 0):
- Dataset: 100 examples ✓, K=8 ✓
- step 1: prove_rate=0.125, grad_norm=9.22
- step 3: prove_rate=0.500, isr=0.444
- step 4: prove_rate=0.000, grad_norm=5.71

**s43** (GPU 1):
- Dataset: 100 examples ✓, K=8 ✓
- step 1: prove_rate=1.000, isr=0.800（运气好的样本，reward 全 1 → loss=0）
- step 2-6: prove_rate=0.000（正常，base model 多数样本未训练过）

### 5. 磁盘余量
`/root/autodl-tmp`: **125GB 可用**（51% used）。3 checkpoint × 2 实验 × ~16GB = 最大 96GB，余量充足。旧输出 `exec_retrain_s42/s43` 和 `gated_isr_warmstart_s42` 已清理。

---
