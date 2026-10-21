# ssh emergency disk cleanup

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_emergency-disk-cleanup_20260515T134752_result.json`
- **Structured JSON:** [`4c501b138cf80dc6b621.json`](../../sessions/4c/4c501b138cf80dc6b621.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报如下：

---

## 清理结果

### 1. 进程状态
- **s43** (PID 356071): 已死（清理前已不存在）
- **s44** (PID 357074/357079): kill 信号已发送，已终止
- **tmux sessions**: 无残留
- **GPU**: 两卡均 0 MiB 占用，完全空闲

### 2. 清理目录及释放空间

| 目录 | 释放空间 |
|------|---------|
| plan001_exec_only_s43_1000/ (全删) | ~25G |
| plan001_exec_only_s44_1000/ (全删) | ~15G |
| plan009_sft_baseline_s44_1000/checkpoint-1000/ | ~23G |
| plan009_sft_baseline_s43_1000/checkpoint-1000/ | ~23G |
| plan009_sft_baseline_s42_1000/checkpoint-1000/ | ~7.6G |
| **合计** | **~94G** |

### 3. 最终磁盘状态
```
/dev/md0   250G  159G  92G  64% /root/autodl-tmp
```
**92GB 可用**，超过 60GB 目标。

### 4. grpo_exec_only.yaml
- yaml 中**无** `save_total_limit` / `save_steps` 字段（不需要加）
- `train_grpo.py` L462-464 已**硬编码** `save_steps=50, save_total_limit=1, save_only_model=True`
- yaml 参数不会覆盖这些值（无对应 argparse 参数）
- **无需修改 yaml**

### 5. train_grpo.py save 逻辑
- L462: `save_steps=50` — 每 50 步保存
- L463: `save_total_limit=1` — 最多保留 1 个 checkpoint
- L464: `save_only_model=True` — 只存模型权重
- L487: 训练结束后 `trainer.save_model(args.output_dir)` 保存最终模型

### 6. tmux 清理
无需清理，无残留 session。

---

**服务器已就绪，两卡空闲，92GB 可用。** 训练提交由 Main Agent 处理。

---
