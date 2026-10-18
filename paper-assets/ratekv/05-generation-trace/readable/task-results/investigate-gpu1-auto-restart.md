# investigate gpu1 auto restart

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_gpu1_auto_restart_20260514T095421_result.json`
- **Structured JSON:** [`678b257e16353f7a9458.json`](../../sessions/67/678b257e16353f7a9458.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完毕，结论如下：

## 调查结果

### 1. 是否发现自动重启机制？

**没有自动重启机制。** 逐项排查：

| 检查项 | 结果 |
|--------|------|
| crontab | 无（`/var/spool/cron/crontabs/root` 不存在） |
| systemd service | 无匹配 ratekv/c4/mckp/cross 的 service |
| 自动重启脚本 | 无 |

**实际情况：** 原来的 `c4_cross_dataset_v2.py` 已经不在运行了。当前 GPU 1 上运行的是 **`run_c4_rerun.py`**（PID 210299），它是通过 **tmux session `c4_rerun_d032`** 在 17:38 手动启动的，不是自动重启。之前看到的 PID 变化很可能是有人（或我们之前的 agent session）手动杀掉旧进程后重新启动了新脚本。

### 2. 无需清除

没有自动重启机制需要清除。

### 3. GPU 当前进程

| GPU | PID | 进程 | 显存 | 启动方式 |
|-----|-----|------|------|----------|
| GPU 0 | 199409 | `python3 run_multi_seed.py` | 45682 MiB | nohup（15:37 启动） |
| GPU 1 | 210299 | `python -u run_c4_rerun.py` | 67222 MiB | tmux `c4_rerun_d032`（17:38 启动） |

两个都是正常的实验进程，没有异常的自动重启行为。

---
