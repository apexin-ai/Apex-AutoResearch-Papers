# analysis plan 006 qwen3 1 7b no evidence eval v3

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_006_qwen3_1_7b_no_evidence_eval_v3_20260516T135316_result.json`
- **Structured JSON:** [`a9dd5e6a94361963c3e2.json`](../../sessions/a9/a9dd5e6a94361963c3e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

| 指标 | 值 |
|------|-----|
| **ign_f1** | **0.3982** |
| f1 | 0.4103 |
| precision / recall | 0.4464 / 0.3796 |
| evi_f1 | 0.0（符合预期） |
| edcr | 0.0 |
| format_ok_rate | 100% (985/985) |
| **n_truncated** | **501/985 (50.9%)** |
| inference_time | 7465s (~2h4m) |
| W&B | 无 |

### 关键发现

**截断仍然严重**：v1 → v3 仅从 531 降到 501，bash-c wrapping 修复效果微弱。根本原因是 max_new_tokens=1024 对 1.7B 不够用。

**Evidence tax 假设不成立（但有 confound）**：
- 1.7B no-evidence: ign_f1 = 0.3982
- 1.7B with-evidence: ign_f1 = 0.4786
- 差值 = **-0.0804**（no-evidence 更差）

与 4B 上的结论相反。但 50.9% 截断率严重污染结果——截断直接导致预测丢失压低 recall（0.3776），真实性能可能更高。结论标记为 `negative_but_confounded`，需增大 max_new_tokens 重跑才能定论。

---
