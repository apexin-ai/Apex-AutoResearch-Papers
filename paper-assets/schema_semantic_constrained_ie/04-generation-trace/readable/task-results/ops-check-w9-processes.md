# ops check w9 processes

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_w9_processes_20260516T202422_result.json`
- **Structured JSON:** [`c23b2fcb58b0f1b2f80e.json`](../../sessions/c2/c23b2fcb58b0f1b2f80e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## W9 Sampling 实验状态报告

| 实验 | 状态 | 已处理 | GPU 占用 | 运行时间 | 预估剩余 |
|------|------|--------|----------|----------|----------|
| w9_qwen_scierc_zs_sampling (PID 382074) | **已完成** | 551/551 (100%) | 无 | — | — |
| w9_qwen_docred_zs_sampling_r3 (PID 384608) | **运行中** | 36/998 (3.6%) | cuda:1, 16786 MiB | 11h16m | ~约 300h (13天) |

**详细说明：**

- **SciERC**: 已正常结束，EXIT_CODE=0，551 样本全部成功，无失败。进程已退出。
- **DocRED r3**: 正在运行，11小时16分钟处理了36个样本，平均 ~18.8 min/sample。按此速度 (998-36)×18.8min ≈ 301 小时。日志只记录到模型加载阶段，实际输出文件最后修改时间为 05-17 04:24（刚刚），确认仍在活跃写入。

DocRED 的速度异常慢（SciERC 551 样本也才用了若干小时），可能是 DocRED 文档更长、关系类型更多（96 types）导致生成 token 数远大于 SciERC。按当前速度完成全部 998 样本需要约 13 天。

---
