# code w10 mistral scierc beam 551 collect

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_w10_mistral_scierc_beam_551_collect_20260517T083031_result.json`
- **Structured JSON:** [`067a1b01678a3cf6a169.json`](../../sessions/06/067a1b01678a3cf6a169.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No cron jobs in this session to delete (the cron was likely in a previous session and already expired or cleaned up).

---

## 实验结果报告：w10_mistral_scierc_beam_551

**状态**：正常完成（551 samples, 550 success, 1 parse failure）

### 完整指标

| Metric | Beam (k=4) | Greedy | Delta |
|--------|-----------|--------|-------|
| ET_pct | 0.0% | - | - |
| RV_pct | 0.0% | - | - |
| **DR_pct** | **13.79%** | 13.4% | **+0.39pp** (worse) |
| **CF_pct** | **0.57%** | 1.27% | **-0.70pp** (better) |
| **E_F1** | **26.66** | 27.46 | **-0.80pp** (worse) |
| **R_F1** | **4.37** | 3.67 | **+0.70pp** (better) |

### 分析

结论：**negative**。Beam search 对 Mistral SciERC 效果混合：
- R_F1 有改善（+19% relative），CF 违规减半（55% relative reduction）
- 但核心指标 DR 未改善（+0.39pp），E_F1 略降（-0.80pp）
- 假设部分被否定：beam search 无法通过更宽的 token 探索降低 DR，Mistral 的 entity type 误分类才是瓶颈

Registry 已更新为 DONE (negative)，包含 metrics、checkpoint_path、log_path、analysis。

---
