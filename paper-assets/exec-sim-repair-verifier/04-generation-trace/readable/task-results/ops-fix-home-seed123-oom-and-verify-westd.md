# ops fix home seed123 oom and verify westd

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-home-seed123-oom-and-verify-westd_20260513T215503_result.json`
- **Structured JSON:** [`efa15f7945b26ed3b4bf.json`](../../sessions/ef/efa15f7945b26ed3b4bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 报告

### Home (home-1x5090)
- **OOM 根因**: CLS v5 子进程 PID 2947263 残留（kill_job 只杀了父进程 2947259，子进程存活），占满 GPU 19.5GB
- **修复**: 已 kill PID 2947263，GPU 完全释放
- **seed123 新 PID**: 3001112（父 bash PID 3001111）
- **训练状态**: 正常运行中，1/6633 steps，~6s/step
- **transformers 版本**: 4.57.6 ✓

### Westd (westd-48478)
| GPU | 状态 | 进程 |
|-----|------|------|
| 0 | 空闲 (0 MiB) | 无 |
| 1 | 23.3 GB, 87% | CWM v12 (PID 181202) — 正常训练中，~8s/step |
| 2 | 10.8 GB, 69% | CWM v11 eval (PID 180344) — 100/9784，acc 72% |
| 3 | 空闲 (0 MiB) | 无 |

- 孤儿进程已全部清除，GPU 0/1/3 释放成功
- CWM v12 未因等待 GPU 超时，数据加载完成后自动抢到 GPU 1 开始训练
- GPU 0 和 3 空闲可用

---
