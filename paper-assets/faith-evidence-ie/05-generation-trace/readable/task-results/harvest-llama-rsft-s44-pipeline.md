# harvest llama rsft s44 pipeline

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_llama_rsft_s44_pipeline_20260520T041515_result.json`
- **Structured JSON:** [`5fe6200afaba25bea511.json`](../../sessions/5f/5fe6200afaba25bea511.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

## LLaMA-3.1-8B RSFT k=1 s44 Pipeline 结果

**训练**：完成，checkpoint 在 `/root/autodl-tmp/rsft_output_llama_3_1_8b_k1_s44/`（adapter_model.safetensors 671MB, checkpoint-1107）

**Eval 指标**：

| 指标 | s42 | s43 | **s44** |
|------|-----|-----|---------|
| Ign-F1 | 0.5714 | 0.5662 | **0.5587** |
| Rel-F1 | 0.5839 | 0.5780 | **0.5706** |
| Evi-F1 (TP) | 0.8238 | 0.8287 | **0.8328** |
| Evi-F1 (Joint/DREEAM) | 0.4701 | 0.4644 | **0.4609** |
| EDCR | 0.5799 | 0.5783 | **0.5829** |
| Format OK | 984/985 | 985/985 | **985/985** |
| Truncated | 158 | 173 | **166** |

**3-seed 统计**：
- **Ign-F1 mean** = (0.5714 + 0.5662 + 0.5587) / 3 = **0.5654** (±0.0052 std)
- **Rel-F1 mean** = (0.5839 + 0.5780 + 0.5706) / 3 = **0.5775** (±0.0054 std)

注意：你之前给的 s42 ign_f1=0.5839 实际上是 rel_f1。s42 的 ign_f1 是 0.5714。

Registry 和 cron 已更新完毕。

---
