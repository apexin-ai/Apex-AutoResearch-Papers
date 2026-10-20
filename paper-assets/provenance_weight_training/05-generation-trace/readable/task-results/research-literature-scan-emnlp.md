# research literature scan emnlp

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature_scan_emnlp_20260515T085208_result.json`
- **Structured JSON:** [`56ae1991f9166cd9c2ff.json`](../../sessions/56/56ae1991f9166cd9c2ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文献扫描完成。结果写入 `artifacts/literature_scan_results.md`。

核心发现：

**9 篇必须添加到 literature_map.yaml**：DoGE (ICML'24)、MATES (NeurIPS'24)、DsDm (ICML'24)、PDS (ICLR'25 Oral)、RegMix (ICLR'25 Spotlight)、Is Collapse Inevitable (ICML'25)、Collapse or Thrive (ICML'25)、Demystifying Synthetic Data (EMNLP'25)、FineWeb (2024)。

**定位关键**：现有 literature_map 覆盖了直接竞争者（Drayson、Golden Ratio、Beyond Collapse）和基础理论，但缺少域级/实例级 data selection 的主要对比方法（DoGE/MATES/DsDm/PDS/RegMix）和最新 model collapse 理论进展。补充后 related work 可从 4 个维度组织：instance vs domain level、online vs offline、contamination-aware vs quality-oriented、hard filtering vs soft reweighting——我们是唯一同时满足 instance-level + online adaptive + contamination-aware + soft reweighting 的方法。

---
