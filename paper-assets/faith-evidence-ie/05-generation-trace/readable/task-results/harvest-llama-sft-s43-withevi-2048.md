# harvest llama sft s43 withevi 2048

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_llama-sft-s43-withevi-2048_20260521T041453_result.json`
- **Structured JSON:** [`4383784180b9e320ef1d.json`](../../sessions/43/4383784180b9e320ef1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在（可能已被清理）。Registry 已更新为 DONE。

## 结果汇报

**状态**: 成功

**关键指标**:

| 指标 | 值 |
|------|------|
| **Ign-F1** | **0.4954** |
| F1 | 0.5105 |
| Evi-F1 (DREEAM/joint) | 0.4001 |
| Evi-F1 (TP) | 0.8015 |
| EDCR | 0.6574 |
| Format OK | 985/985 (100%) |
| Truncated | 242/985 (24.6%) |
| Predictions | 24,949 |
| Inference time | 12,343s (3h26m) |

**对比分析**:

- **@2048 vs @1024 delta**: 0.4954 − 0.5142 = **−0.0188**（2048 token 反而降了 1.9 个点，可能是 truncated 242/985 导致部分文档输出被截断影响精度）
- **s43 matched@2048 raw evidence tax**: no-evi@2048 (0.3389) − with-evi@2048 (0.4954) = **−0.1565**（with-evidence 反而高 15.65 个点，evidence tax 为负，说明 evidence 输出对 RE 性能有正向贡献而非负担）

---
