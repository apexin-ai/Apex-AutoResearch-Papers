# monitor home 8b eval vram and progress

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_home-8b-eval-vram-and-progress_20260514T173651_result.json`
- **Structured JSON:** [`a72ef56b3af41040cded.json`](../../sessions/a7/a72ef56b3af41040cded.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 监控结果

### 1. 进程存活 ✓
- PID 3151214 活跃，CPU 111%，10:31启动，已运行 ~8分钟
- 命令: `eval_repo_cls.py --checkpoint_dir checkpoints_repo_cls_8b_westd/checkpoint-3000 --split val --max_seq_length 5120 --batch_size 8`

### 2. VRAM 占用
- **29447 / 32607 MiB (90.3%)**，GPU利用率 100%
- 两次检查间 VRAM 稳定不变，无上升趋势
- 剩余 ~3.2GB，**OOM风险低** — batch_size=8 下内存已收敛到稳定值

### 3. predictions.jsonl 增长 ✓
| 时刻 | 行数 | 大小 |
|------|------|------|
| T1 | 672 | 130KB |
| T2 (~97秒后) | 840 | 155KB |

- **增长 168 行/97秒**，进程正常推进
- 当前进度: **840 / 1896 (44.3%)**
- 预计剩余 ~10分钟完成

### 4. 4B eval 串联
- **未发现4B eval排队**。tmux session `eval_8b_val5120_fix` 中只有当前8B eval的单条命令，没有 `&&` 链式调用
- 服务器上无其他python eval进程在等待
- 如果需要4B eval接力，需要手动启动

### 5. 异常
无异常。进程稳定推进，VRAM平稳，无OOM风险。唯一注意点是**4B eval没有自动串联**，8B完成后需要手动启动。

---
