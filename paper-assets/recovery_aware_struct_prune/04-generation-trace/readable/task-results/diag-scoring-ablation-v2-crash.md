# diag scoring ablation v2 crash

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_scoring_ablation_v2_crash_20260517T100812_result.json`
- **Structured JSON:** [`93d2787c8984ad4536d6.json`](../../sessions/93/93d2787c8984ad4536d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

---

## scoring_ablation_batch_v2 实验状态

### 原始批量进程
`scoring_ablation_batch_v2` 进程**已终止**（日志末尾有 `Terminated`），tmux session 也不存在。进程在 magnitude 的 post-prune eval 跑到 60/200 时被终止（`EXIT_CODE=0` 但前面有 `Terminated` 信号）。

### 各 scoring method 当前状态

| Method | Post-prune Eval | SFT | Post-SFT Eval |
|--------|----------------|-----|---------------|
| **magnitude** | acc=0.0000 (60/200, early stopped / terminated) | FAILED (extreme non-uniformity) | N/A |
| **gradient** | acc=0.255 (200/200, 完成) | **完成** (1870/1870 steps, loss=0.759) | **运行中** (cuda:0, PID 701500, 刚启动 ~1min) |
| **random** | **运行中** (cuda:1, PID 696141, 121/200, acc@100=0.37) | 未开始 | N/A |
| **cka_only** | 未开始 | 未开始 | 未开始 |

### 崩溃原因
原始 batch_v2 进程被 `Terminated`（SIGTERM），不是 OOM 也不是 disk full。可能是手动或 cron 管理杀掉。后续实验分拆为单独 tmux session 继续。

### 磁盘状态

| 分区 | 大小 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| / (根分区) | 30G | 8.6G | 22G | 29% |
| /root/autodl-tmp (数据盘) | 250G | 231G | 20G | 93% |

数据盘 93% 偏高但还有 20G 余量，不会立刻触发 disk full。

### GPU 状态

| GPU | 状态 | 进程 |
|-----|------|------|
| cuda:0 | **占用** (305W, 78% util, 12.9GB VRAM) | eval_gradient_postsft (PID 701500) |
| cuda:1 | **占用** (显示为空闲 3MiB 但实际有 eval_unstructured_20 tmux + random eval PID 696141) | random post-prune eval (121/200) |

**注意**：nvidia-smi 显示 cuda:1 仅 3MiB 是因为 random eval 进程 (PID 696141) 实际跑在 cuda:1 但可能在等待推理 batch。`ps aux` 确认该进程活着且 CPU 115%。

### 结论
- 两个 eval 正在并行进行：gradient_postsft (cuda:0) 和 random_postprune (cuda:1, ~60% 完成)
- gradient SFT 已成功完成，模型保存到 `/root/autodl-tmp/recovery_aware_struct_prune/sft_gradient_20`
- magnitude 和 cka_only 尚未产出有效结果
- 无结果 JSON 文件生成（都还在 eval 中）
- 两张 GPU 都在忙，无空闲卡

---
