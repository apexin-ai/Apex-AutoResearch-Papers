# ssh d162 kill batchtest eval

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d162-kill-batchtest-eval_20260521T132112_result.json`
- **Structured JSON:** [`9671e479eb7961505e4d.json`](../../sessions/96/9671e479eb7961505e4d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## D162 紧急序列执行完毕

### 1. Kill 确认
- PID 56657 (DS s456 epoch 2 eval) 已 kill（SIGTERM 成功）
- GPU 1 完全释放

### 2. Batch Test 结果

| Batch Size | Samples/min | GPU Mem (GB) | OOM? |
|------------|-------------|--------------|------|
| 1          | ~4.1        | 17.2/32.6    | No   |
| 2          | 5.3*        | 17.6/32.6    | No   |
| 4          | **9.3***    | 18.8/32.6    | No   |

*含模型加载时间（~60s），纯推理速度更快

**推荐 batch_size = 4**：
- 吞吐量 2.3x（vs batch=1），显存仅增 1.6GB
- 18.8GB 距 OOM（32.6GB）还有 13.8GB 余量
- 注意：generation length 较长（mean=128 words），8 个 unparseable predictions（15 中），可能需要检查 `enable_thinking` 是否生效

### 3. DS s456 epoch 3 eval 启动确认
- **tmux session**: `ds-s456-e3-eval`
- **PID**: 62777
- **Checkpoint**: `/root/autodl-tmp/checkpoints_deepseek_cwm_repo_s456_v2/checkpoint-12627` ✓
- **恢复模式**: 自动跳过 416 条已完成结果，从 416/9784 继续
- GPU 1: 31.6GB/32.6GB，77% 利用率
- **预计完成**: ~23:35 CST（约 1h50m，参考 s123 eval 全量用时 116 min）

### 4. 当前 nvidia-smi
```
GPU 0: 30553/32607 MiB, 97% — Qwen s456 训练
GPU 1: 31629/32607 MiB, 77% — DS s456 epoch 3 eval ← 新启动
GPU 2: 20501/32607 MiB, 99% — Qwen s123 训练
GPU 3: 25559/32607 MiB, 97% — Qwen s456 训练
```

⚠️ GPU 1 显存 31.6/32.6GB 较紧（DS batch=4 + seq 4096），但 s123 eval 以相同配置成功跑完，应该没问题。

---
