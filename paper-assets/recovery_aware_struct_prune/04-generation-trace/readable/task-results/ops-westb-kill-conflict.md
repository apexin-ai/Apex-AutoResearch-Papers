# ops westb kill conflict

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westb-kill-conflict_20260517T114413_result.json`
- **Structured JSON:** [`1f532913634ed58b4d1f.json`](../../sessions/1f/1f532913634ed58b4d1f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### Kill 结果
PID 704557 和 710278 在执行 kill 前已不存在（自行退出或之前已被 kill）。

### nvidia-smi 当前状态

| GPU | PID | 进程 | 显存 |
|-----|-----|------|------|
| cuda:0 | 710618 | eval_gsm8k (pruned_cka_only_20, n=200) | 12994 MiB |
| cuda:1 | 710113 | **sft_recovery (random_20, save_strategy=no)** ✓ 保留 | 50408 MiB |
| cuda:1 | 712124 | eval_gsm8k (sft_random_20, n=200) | 24776 MiB |
| cuda:1 | 712819 | eval_gsm8k (sft_random_20, n=200) | 21428 MiB |

cuda:1 总占用 96631/97887 MiB (98.7%)，接近满载。

### sft_random_20/ 目录状态
- **checkpoint-1870/ 已删除**（~34GB，含 24GB optimizer.pt），由 PID 704557 写入
- 顶层仍有 704557 写的 model.safetensors (12GB) 等文件，710113 训练完成后会覆盖
- 710113 当前进度：~1086/1870 步，预计还需 ~39 分钟完成

### 需注意
**cuda:1 上有两个完全重复的 eval_sft_random_20 进程**（PID 712124 + 712819），参数一模一样，output_path 也相同，共占 ~46GB 显存。而且它们评估的是 704557 写的旧模型（非 710113 的最终结果）。如果需要清理可以 kill 其中一个或两个。

---
