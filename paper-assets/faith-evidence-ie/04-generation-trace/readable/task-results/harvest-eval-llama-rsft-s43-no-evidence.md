# harvest eval llama rsft s43 no evidence

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_eval_llama_rsft_s43_no_evidence_20260520T042343_result.json`
- **Structured JSON:** [`02e7a4281da70b3c9e6c.json`](../../sessions/02/02e7a4281da70b3c9e6c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE，cron 已删除。

## 指标汇总

| 指标 | 值 |
|------|-----|
| **Ign-F1** | **0.5546** |
| F1 (rel) | 0.5670 |
| Evi-F1 | 0.0000 (expected, no-evidence) |
| Evi-F1(TP) | 0.0000 |
| Evi-F1(joint) | 0.0000 |
| EDCR | 0.0000 |
| Format OK | 983/985 (99.8%) |
| Truncated | 183/985 |
| Predictions | 18,008 |
| Inference time | 7,798s (~2h10m) |

## Evidence Tax 计算

| Seed | With-evidence Ign-F1 | No-evidence Ign-F1 | Evidence Tax |
|------|---------------------|--------------------|----|
| **s42** | 0.5714 | 0.5526 | **-1.88pp** |
| **s43** | 0.5662 | 0.5546 | **-1.16pp** |

s43 evidence tax = 0.5546 − 0.5662 = **−1.16pp**（negative，no-evidence 更差）。

两个 seed 一致表明：去掉 evidence 输出会损害关系抽取性能，但 s43 的 tax（-1.16pp）比 s42（-1.88pp）更小。Evidence tax 在 LLaMA-8B 上稳定为负，跨 seed 范围约 -1.2pp ~ -1.9pp。

---
