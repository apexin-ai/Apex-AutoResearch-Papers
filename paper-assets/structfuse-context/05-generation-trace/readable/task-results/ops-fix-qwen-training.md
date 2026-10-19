# ops fix qwen training

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_qwen_training_20260513T165802_result.json`
- **Structured JSON:** [`b6224b31c3f6a9427f7d.json`](../../sessions/b6/b6224b31c3f6a9427f7d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三项验证全部通过。

## 结果汇报

### 1. GPU 0 清理
- `nvidia-smi` 发现 PID 69592（之前的 Qwen 训练）占用 49372 MiB
- `kill -9 69592` 后 GPU 0 显存归零（0 MiB / 97887 MiB）
- GPU 1 的 PID 69189 也被一起回收（可能是同一进程组），但后来 PID 70959 (sc_data_build session) 继续占用 11120 MiB

### 2. Qwen 训练三项验证

| 检查项 | 结果 |
|--------|------|
| tmux session `m2_qwen` | **TMUX_OK** |
| GPU 进程 | PID 71387, **48438 MiB** (GPU 0) |
| 训练日志 | `[Epoch 1] Using pre-mined negatives (random)... Training loop start: 1414 batches/epoch` |

训练已正常启动，strategy=random, seed=42, gpu=0，1414 batches/epoch。

### 3. 修正记录
- 用户指定的脚本名 `run_m2_full_qwen.sh` 不存在，实际脚本为 `run_full_m2_training.sh random 42 0`
- 首次启动因 tmux 内无 conda 环境导致 `python: command not found`，加入 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base` 后解决

---
