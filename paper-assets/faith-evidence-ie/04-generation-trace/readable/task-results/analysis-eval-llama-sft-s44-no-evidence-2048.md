# analysis eval llama sft s44 no evidence 2048

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_llama_sft_s44_no_evidence_2048_20260520T210146_result.json`
- **Structured JSON:** [`13e8b1bd03a173b4b5ae.json`](../../sessions/13/13e8b1bd03a173b4b5ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## s44 no-evidence 2048 结果

| 指标 | 1024 版 | 2048 版 | 变化 |
|------|---------|---------|------|
| **ign_f1** | 0.3326 | **0.4373** | **+10.47pp** |
| truncation | 41.7% (411/985) | **24.97%** (246/985) | -16.7pp |
| format_ok | — | 99.2% (977/985) | — |
| predictions | — | 28,366 | — |

### Fair Evidence Tax（2048 no-evi vs with-evi）

| | ign_f1 |
|---|--------|
| with-evi (fair subset 977 docs) | 0.4813 |
| no-evi (fair subset 977 docs) | 0.4395 |
| **Fair tax** | **-4.18pp** |

### 判断：主要是截断伪影，但存在真实 evidence tax

1. **截断伪影已确认**：1024→2048 使 ign_f1 从 0.3326 恢复到 0.4373（+10.47pp），原 1024 的 14.76pp "假 tax" 中约 10.5pp 是截断造成的
2. **真实 evidence tax ≈ 4.18pp**：2048 版在 fair subset 上 no-evi 仍比 with-evi 低 4.18pp
3. **残留截断**：2048 仍有 25% 截断（246/985），no-evi 模型输出更冗长，可能还有少量被压缩的空间
4. s44 with-evi ign_f1=0.4802，no-evi 2048 ign_f1=0.4373，raw tax = 4.29pp，与 fair tax 4.18pp 一致（format failure 影响极小）

Registry 已更新为 success，含完整 metrics 和 fair tax。

---
