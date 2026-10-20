# diag check training progress

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_check-training-progress_20260514T134830_result.json`
- **Structured JSON:** [`ce5676c61446bf7d7d44.json`](../../sessions/ce/ce5676c61446bf7d7d44.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果

### 1. Encoder Ablation Probe — 全部完成 ✓

| 任务 | 状态 | Best val macro-F1 | Early Stop Epoch |
|------|------|-------------------|------------------|
| e5-large | 完成 (EXIT_CODE=0) | **0.9596** | epoch 9 |
| bge-m3 | 完成 (EXIT_CODE=0) | **0.9579** | epoch 10 |

- PID 53503/53646/54528/54609 已全部结束
- 无 train_probe 相关进程在运行
- checkpoints 已保存：
  - `checkpoints_ablation_e5large/`: best_model.pt (5.3MB), split_info.json, train_history.json
  - `checkpoints_ablation_bgem3/`: best_model.pt (5.3MB), split_info.json, train_history.json
- `checkpoints_e5large/` 和 `checkpoints_bgem3/` 不存在

### 2. GPU 状态

两块 GPU 均空闲：0% 利用率，0 MiB 显存占用（各 32GB），无计算进程。

### 3. baseline-llm-judge — 运行中

- PID 27424，运行中
- 进度：**1680/1824**（92.1%）
- macro_f1=0.6657，tokens=2,812,064，估算花费 ~$10.70，fails=0
- 模式：zero-shot，模型：claude-sonnet-4.6

---
