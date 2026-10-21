# diagnose scienceworld sft bjb1

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_scienceworld_sft_bjb1_20260524T225428_result.json`
- **Structured JSON:** [`affa35211afd4c337b7e.json`](../../sessions/af/affa35211afd4c337b7e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 诊断报告

### 错误原因

**CUDA OOM during evaluation**, 不是训练阶段的问题。

训练本身正常运行了 112 步（25%），loss 从 ~0.35 下降到 ~0.10。在 step 112 触发第一次 eval 时 OOM：

```
torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 74.19 GiB.
GPU 0 has a total capacity of 94.97 GiB of which 38.47 GiB is free.
```

**根因**：`sft_train_v3.py` 只设了 `per_device_train_batch_size=1`，但没设 `per_device_eval_batch_size`。HuggingFace Trainer 默认 `per_device_eval_batch_size=8`。

Eval 时 logits 转 float32 的内存需求：
- `8 (batch) × 16384 (seq_len) × 151936 (vocab) × 4 bytes ≈ 75.2 GiB`
- 这与报错的 74.19 GiB 完全吻合

### 关键路径

| 项目 | 路径 |
|------|------|
| 训练脚本 | `/root/cost-verify-agent-rl/scripts/sft_train_v3.py` |
| 启动脚本 | `/root/cost-verify-agent-rl/scripts/run_scienceworld_sft_single_gpu.sh` |
| 训练日志 | `/root/runs/cost-verify-agent-rl/scienceworld_sft_bjb1.log` |
| 训练数据 | `/root/cost-verify-agent-rl/data/scienceworld_sft_train.jsonl` (3586 samples) |
| 验证数据 | `/root/cost-verify-agent-rl/data/scienceworld_sft_val.jsonl` (1791 samples) |
| 模型 | `/root/autodl-tmp/models/Qwen/Qwen3-1___7B` |
| 检查点目录 | `/root/autodl-tmp/checkpoints/scienceworld_sft_bjb1/` (空，无有效 checkpoint) |

### 修复

在 `sft_train_v3.py` 的 `sft_kwargs` 中加一行：

```python
per_device_eval_batch_size=1,
```

或在 shell 脚本中加 `--per_device_eval_batch_size 1` 参数（需同时在 argparse 中添加该参数）。

---
