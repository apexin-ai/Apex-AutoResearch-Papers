# diag ssh gpu check

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_ssh-gpu-check_20260514T134001_result.json`
- **Structured JSON:** [`c1d5d6844241a22481d3.json`](../../sessions/c1/c1d5d6844241a22481d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成，报告已写入 `artifacts/ssh_diag_20260514.md`。汇总：

| 项目 | 状态 |
|------|------|
| SSH 连通性 | 正常 |
| GPU (2x 32GB) | 空闲，0% 利用率 |
| data-volume-control (PID 51861) | 已结束 |
| baseline-llm-judge (PID 27424) | **运行中**，1610/1824 (88%)，macro_f1=0.6665，~$10.28，0 fails |
| e5-large embeddings | 正常，54809 样本 |
| bge-m3 embeddings | 正常，54809 样本 |
| **gte-large embeddings** | **严重异常**：仅 10 个样本（2 个 trajectory），生成过程提前终止，需重跑 |

gte-large 的 embedding 格式正确（dim=1024，sliding window），但只跑了前 2 个 trajectory 就停了。模型已在本地，重跑不需重新下载。

---
