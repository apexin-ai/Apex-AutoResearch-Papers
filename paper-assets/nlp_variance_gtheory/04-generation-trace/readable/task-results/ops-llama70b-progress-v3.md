# ops llama70b progress v3

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_llama70b_progress_v3_20260523T105602_result.json`
- **Structured JSON:** [`184faf213134ee383817.json`](../../sessions/18/184faf213134ee383817.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**情况 B：仍在下载，且存在磁盘空间风险。**

| 指标 | 值 |
|---|---|
| PID 313198 | 运行中，已耗时 1h48m |
| 已下载 | 21 GB |
| 磁盘剩余 | 39 GB（/root/autodl-tmp/ 总 350GB，已用 312GB） |

**进度明细**（多文件并行下载）：
- `model-00002-of-00030.safetensors`: 43% (1.85/4.34GB) @ 8.8MB/s
- `original/consolidated.00.pth`: 69% (11.4/16.4GB) @ 1.0MB/s
- `original/consolidated.03.pth`: 66% (10.9/16.4GB) @ 1.5MB/s
- `original/consolidated.05.pth`: 83% (13.6/16.4GB) @ 1.1MB/s

**严重问题：ModelScope 正在同时下载 safetensors 格式（30 shards × ~4.3GB ≈ 130GB）和 original .pth 格式（8 files × 16.4GB ≈ 131GB），总计约 260GB。磁盘仅剩 39GB，下载必将因空间不足而失败。**

当前综合进度约 21/260GB ≈ **8%**，但即便只算 safetensors 格式（130GB），剩余空间（39GB）也远远不够（还需 ~110GB）。

建议：
1. 终止当前下载（kill 313198）
2. 清理 `/root/autodl-tmp/` 释放空间，或删除已下载的 original/ 目录后仅下载 safetensors 格式
3. 用 `snapshot_download` 的 `ignore_file_pattern` 参数排除 `original/` 目录重新下载

是否需要我执行这些操作？

---
