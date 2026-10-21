# ssh zeroshot cleanup

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_zeroshot_cleanup_20260515T023844_result.json`
- **Structured JSON:** [`0b4dc1d9d62ed53af4e0.json`](../../sessions/0b/0b4dc1d9d62ed53af4e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。汇报：

## 结果

### 发现的进程

| PID | 命令 | 启动时间 | 状态 |
|-----|------|----------|------|
| 262081 | `run_zeroshot3.py` | 10:16 | **已 kill** |
| 263404 | `run_zeroshot4.py` | 10:20 | **已 kill** |
| 263866 | `run_zeroshot4.py` | 10:21 | **已 kill** |
| 264832 | `run_zeroshot4.py` | 10:24 | **已 kill** |
| 266089 | `run_zeroshot5.py` | 10:27 | 保留 |
| 267657+267659 | `run_loop.sh` → `run_batch.py` | 10:31 | 保留（活跃） |

### 已 kill 废弃进程
- 1 个 v3 + 3 个 v4，共 4 个，全部 SIGTERM 正常退出

### 保留的活跃进程
- **PID 266089**: `run_zeroshot5.py`（v5 独立进程）
- **PID 267657→275187**: loop 脚本正在跑 `run_batch.py`（批量评估）

### Zero-shot baseline 当前状态
- **进度**: 98/200 样本已完成（Round 4 进行中）
- **当前准确率**: 43.9%（4-class）
- 模型: `deepseek/deepseek-v3.2`
- `baseline_results.json` 中有早期小样本结果（acc=60%，仅 10 样本，不可靠）
- 批量评估仍在继续，预计还需几轮完成剩余 102 个样本

---
