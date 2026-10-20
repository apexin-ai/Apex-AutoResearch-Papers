# ops llama eval and rsft candidates

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_llama_eval_and_rsft_candidates_20260516T142244_result.json`
- **Structured JSON:** [`d19d6be0faeb8e178901.json`](../../sessions/d1/d19d6be0faeb8e178901.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

### Part 1: Zombie kill
- PID 315637/315643/315708 已 kill，验证 ALL_KILLED

### Part 2: LLaMA with-evidence eval 结果

| Metric | Value |
|--------|-------|
| Ign-F1 | 0.5384 |
| F1 | 0.5514 |
| Evi-F1 | 0.8151 |
| EDCR | 0.628 |
| Precision | 0.5464 |
| Recall | 0.5565 |
| Format compliance | 99.5% |
| Truncated | 197/985 |
| **Evidence tax** | **-0.0068** (with_evi 0.5384 - no_evi 0.5452) |

Evidence tax 为负值，说明 LLaMA with-evidence 模式 Ign-F1 略低于 no-evidence（-0.68pp），evidence 输出对 relation extraction 有轻微负面影响。Registry 已更新为 DONE/success。

### Part 3: LLaMA RSFT candidates
- Killed Re-DocRED eval (PID 352689) on cuda:1 释放空间
- 提交 `plan_016_llama_rsft_candidates_r2`，PID 353179，cuda:1
- 3027 documents × 8 generations，已开始 generating
- 注意：cuda:1 上还有另一个 agent 提交的 plan_014_no_evidence_eval (PID 353322, ~9.6GB)，当前两者共用 27.5/32.6 GB，暂时共存。若后续 OOM 需优先保 RSFT candidates。

---
