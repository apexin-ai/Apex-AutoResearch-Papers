# infra scp check and submit

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_scp-check-and-submit_20260512T110242_result.json`
- **Structured JSON:** [`3e316a023c59a253d58a.json`](../../sessions/3e/3e316a023c59a253d58a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。汇总：

## 1. SCP/Split 状态：已完成

Pipeline (PID 27744) 已退出，传输 + 解压 + split 全部完成（18:55 CST）。

## 2. Split 统计

| Split | Samples | Instances | Pass% | Fail% | 文件大小 |
|-------|---------|-----------|-------|-------|---------|
| train | 70,748 | 184 | 85.0% | 15.0% | 394 MB |
| val | 9,335 | 22 | 75.9% | 24.1% | 64 MB |
| test | 9,784 | 25 | 73.0% | 27.0% | 58 MB |
| **总计** | **89,867** | **231** | | | |

Class weights（normalized, sum=2）：fail=1.6555, pass=0.3445

## 3. 训练脚本

- `train_repo_verifier.py` ✓（9.9 KB）
- `train_repo_cwm.py` ✓（9.7 KB）
- 参数名：`--max_seq_length`，默认值 2048

---
