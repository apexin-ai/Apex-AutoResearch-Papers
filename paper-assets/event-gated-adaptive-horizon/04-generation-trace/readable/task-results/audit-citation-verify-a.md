# audit citation verify A

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_citation-verify-A_20260529T064944_result.json`
- **Structured JSON:** [`edc2c0c47f68e7575d5a.json`](../../sessions/ed/edc2c0c47f68e7575d5a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计报告已写入 `artifacts/citation_audit_worker_A.md`。

**发现 4 个问题，其中 1 个严重：**

| Bib Key | 问题 | 严重程度 |
|---------|------|----------|
| `benechehab2023multitimestep` | **3/4 合著者为伪造姓名**（Couairon、Leurent、Bloch 均非本文作者；实际为 Paolo、Thomas、Filippone、Kégl） | 🚨 严重 |
| `parr1998ham` | 标题多了 "Abstract"（应为 "Hierarchies of Machines" 而非 "Hierarchies of Abstract Machines"） | 中 |
| `sharma2017figar` | 标题不完整，缺少 "Learning to Repeat:" 前缀 | 中 |
| `hafner2023dreamerv3` | bib 用 arXiv 标题但 venue 标 Nature 2025，Nature 版标题为 "Mastering diverse control tasks through world models" | 低 |

其余 41 条引用全部正确，无 hallucinated citation，无正文引用错误归因。

---
