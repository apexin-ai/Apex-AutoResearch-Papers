# ops check v2 processes alive

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_v2_processes_alive_20260514T010902_result.json`
- **Structured JSON:** [`cdf2da56dfb2dbe7fbca.json`](../../sessions/cd/cdf2da56dfb2dbe7fbca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 4 个实验进程均存活，GPU 满载运行。

## 状态总结

| 实验 | PID | 存活 | GPU | 当前行数 | 预期行数 | 进度 | 最后修改 |
|------|-----|------|-----|---------|---------|------|---------|
| **semantic_only_v2** | 140804 | **Y** | GPU 0 (16502 MiB) | 181 | 551 | 32.8% | May 14 09:09 |
| **full_s1_v2** | 142639 | **Y** | GPU 1 (16502 MiB) | 296 | 551 | 53.7% | May 14 09:09 |
| **docred_schema resume** | 137719 | **Y** | GPU 0 (24242 MiB) | 948 | 998 | 95.0% | - |
| **full_s2 resume** | 144858 | **Y** | GPU 1 (16480 MiB) | 103 | 551 | 18.7% | - |

- GPU 0: 93% 利用率，40758 MiB 已用
- GPU 1: 92% 利用率，32996 MiB 已用

**无需重启任何实验。** 所有进程正常运行，docred_schema 即将完成（还差 50 条）。

---
