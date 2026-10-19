# research data explore

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_data-explore_20260516T175306_result.json`
- **Structured JSON:** [`9663630adc3d0f4ee383.json`](../../sessions/96/9663630adc3d0f4ee383.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/data_exploration_report.md`。核心发现：

- **56,931 句子 / 1,018 条 traces / 4 个模型**，仅 train split
- **纯文本数据集**，不含 hidden states，需自行提取
- **r1-8b (DeepSeek-R1-Distill-Llama-8B)**：324 traces，81.8% jailbreak rate，平均 45.5 句/trace
- **16 类 sentence-level 标签**：DKE (39%) 和 TD (14%) 占主导，标签区分了 harmful execution / safety override / intent manipulation / evasion / harmless / neutral
- **无显式 transition step 标注**，但 CC (Compliance Conflict) 平均出现在 trace 60% 位置处，可作为 compliance transition 的 proxy
- `final_judgment`: 1.0=unsafe (jailbroken), 0.5=partially unsafe (harmful reasoning but safe output)

---
