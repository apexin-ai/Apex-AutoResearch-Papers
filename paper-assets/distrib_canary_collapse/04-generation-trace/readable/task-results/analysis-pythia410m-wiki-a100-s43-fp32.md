# analysis pythia410m wiki a100 s43 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pythia410m_wiki_a100_s43_fp32_20260519T231925_result.json`
- **Structured JSON:** [`336353b9875a44a63d23.json`](../../sessions/33/336353b9875a44a63d23.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。Registry 已更新为 DONE/success。

**核心结果**：

| | s42 | s43 |
|---|---|---|
| PermG fwd | 6/8 | 6/8 |
| K≥3 | 6/8 | 6/8 |
| K≥4 | 1/8 | 0/8 |
| threshold_onset | 8/8 | 8/8 |
| TY Granger | 6/8 | 6/8 |

Cross-seed 验证通过。PermG 和 K≥3 在 s42/s43 完全一致，失败 pair 均为 mauve（drift 仅+2.15%，信号本身弱）。Pythia-410M 不再是单 seed 审稿攻击面。

---
