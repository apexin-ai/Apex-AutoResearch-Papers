# infra verify training start

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_verify_training_start_20260520T032546_result.json`
- **Structured JSON:** [`5c9f0d2038a39e0f35db.json`](../../sessions/5c/5c9f0d2038a39e0f35db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**3 个训练全部失败。**

### 汇总

| 检查项 | 结果 |
|--------|------|
| tmux sessions | **无** — `NO_TMUX`，所有 session 已退出 |
| GPU 进程 | GPU 1 和 GPU 3 各有 2 个 python 进程（共 4 个），**不是本次训练**的，是其他残留进程 |
| GPU 利用率 | 全部 0%，GPU 0/2 无显存占用 |
| 3 个 log 文件 | 均只有 54 字节，内容相同 |

### 失败原因

3 个 log 文件内容一致：

```
bash: line 1: python: command not found
EXIT_CODE=127
```

启动脚本用了 `python` 而非 `python3`，且未激活 conda 环境。脚本立即报错退出，tmux session 随之关闭。

### 修复方向

启动命令需要先激活 conda 环境再运行，例如：
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python train.py ...
```

---
