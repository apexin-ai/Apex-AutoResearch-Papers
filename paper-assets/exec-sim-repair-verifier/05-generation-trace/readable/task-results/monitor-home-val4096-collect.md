# monitor home val4096 collect

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_home-val4096-collect_20260514T121224_result.json`
- **Structured JSON:** [`025817eae771e4672505.json`](../../sessions/02/025817eae771e4672505.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## val_4096 Eval 状态报告

### 当前进程：正在运行

| 指标 | 值 |
|------|-----|
| **PID** | 3083027 (CPU 101%) |
| **Checkpoint** | `checkpoints_repo_cls_seed123_home/checkpoint-400` |
| **配置** | max_seq_length=4096, batch_size=2, split=val |
| **进度** | **~2689 / 9335** (28.8%) |
| **Running accuracy** | **82.4%** (@ sample 2500) |
| **启动时间** | 05:05:12 |
| **速度** | ~328 samples/min |
| **预计完成** | **~05:33-05:34**（还需约 20 分钟） |

### 健康状态

- **WARNING**: 0
- **ERROR**: 0
- **Watchdog 触发**: 0
- **Timeout**: 0（日志中唯一匹配是启动消息 `batch_timeout=180s`）
- 进程运行健康，无 hang 迹象

### 截断情况（关键指标）

- 已出现 **408 次 TRUNCATED** / ~2689 samples → **~15.2% 截断率**
- 被截断的样本原始长度在 4795-5634 tokens 之间，全部被截到 4096
- 截断比例不低，最终 unparseable 比例需等完成后确认

### Running accuracy 趋势

| 样本数 | Accuracy |
|--------|----------|
| 20 | 90.0% |
| 2380 | 82.1% |
| 2460 | 82.2% |
| 2480 | 82.3% |
| 2500 | 82.4% |

accuracy 在 82% 附近稳定，略有上升趋势。

### 之前的 val eval 结果

**val_sweep.log** 包含之前的 sweep 记录（使用旧版 eval 脚本，无 watchdog，max_seq_length 可能为默认值）：
- **checkpoint-200**: running_acc 收敛到 ~62%
- **另一个 checkpoint**（04:17 开始）: running_acc 约 83.8%，日志在 5280/9335 处截止（疑似中断）

**results/ 目录**（test set，非 val set，9784 instances，max_seq_length=2048）：
- `repo_cls_seed123_ckpt400`: accuracy=75.05%, f1_macro=67.47%, unparseable=132 (1.3%)

**val_eval_results_4096/** 目录：当前正在写入 `seed123_ckpt400/eval_repo_cls_predictions.jsonl`（已写 2696 行）。

### 总结

进程健康运行，无需干预。预计还需 **~20 分钟**完成。4096 max_seq_length 的 val set running accuracy (82.4%) 显著高于 2048 test set 的 75.05%（但注意是不同 split，不能直接对比）。截断率 ~15% 需关注。

---
