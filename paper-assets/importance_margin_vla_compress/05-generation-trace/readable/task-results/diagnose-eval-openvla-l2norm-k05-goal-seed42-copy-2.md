# diagnose eval openvla l2norm k05 goal seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_openvla_l2norm_k05_goal_seed42_20260523T185508_result.json`
- **Structured JSON:** [`8d81c362869d9be02079.json`](../../sessions/8d/8d81c362869d9be02079.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断结论清晰了。

## 诊断结果

### 根本原因：`python` 命令不存在（EXIT_CODE=127）

日志全部内容（仅 2 行）：
```
bash: line 1: python: command not found
EXIT_CODE=127
```

启动脚本使用了 `python` 而非 `python3`。该服务器是 conda 环境（`/root/miniconda3/bin/python` 存在），但启动时未激活 conda，导致 `python` 不在 PATH 中。

### 服务器状态

| 检查项 | 状态 |
|--------|------|
| GPU | 正常，2x RTX PRO 6000 (98GB)，有其他进程在跑 |
| 磁盘 | 正常，根分区 41% (18GB 可用) |
| 目标进程 | 已退出（立即失败，未进入模型加载） |

### 修复方案

可以直接重跑，无需修改代码。启动命令需要：

1. 在命令前激活 conda：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
2. 或者将 `python` 改为 `/root/miniconda3/bin/python`

同目录下成功的 `eval_openvla_baseline_long_seed42.log` 显示模型加载正常，说明环境本身没有问题，纯粹是启动命令未激活 conda 环境。

---
