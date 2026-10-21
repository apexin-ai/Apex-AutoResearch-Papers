# paper related work update

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_related-work-update_20260518T142443_result.json`
- **Structured JSON:** [`a3bf14e4e783e680c14f.json`](../../sessions/a3/a3bf14e4e783e680c14f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

新增内容无 -ing 短语结尾问题。已有内容（training, conditioning 等）是名词性用法，不是 AI 痕迹。

完成。修改汇总：

**references.bib** — 添加 4 个条目：
- `nauman2024overestimation` (ICML 2024, arXiv 2403.00514)
- `lin2025tdmpcsquare` (arXiv 2502.03550)
- `juliani2024plasticity` (NeurIPS 2024, arXiv 2405.19153)
- `tang2025churn` (ICML 2025, arXiv 2506.00592)

**related_work.tex** — 3 处插入：
1. **TAWM 段落**：TD-M(PC)² 引用，指出其将 TD-MPC2 中的 value overestimation 归因于 policy mismatch，与本文对 imagination loop 的诊断互补
2. **Value Overestimation 段落**：Nauman 引用，将 CIVO 定位为其 overestimation-plasticity 耦合框架下的 model-induced 实例
3. **Network Capacity 段落**：Juliani、Tang、Nauman 三篇并入，分别补充 on-policy plasticity loss、churn-based plasticity 机制、overestimation-plasticity 耦合证据

---
