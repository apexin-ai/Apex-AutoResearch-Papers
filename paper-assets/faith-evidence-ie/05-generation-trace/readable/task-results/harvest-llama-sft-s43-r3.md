# harvest llama sft s43 r3

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_llama-sft-s43-r3_20260520T140830_result.json`
- **Structured JSON:** [`e825bef51801caf7de4d.json`](../../sessions/e8/e825bef51801caf7de4d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## s43 r3 结果

**训练**: 成功完成，3 epochs，train_loss=0.521，eval_loss=0.7393

**Adapter**: 存在，641MB，路径 `/root/autodl-tmp/sft_output_llama_3_1_8b_s43/`

**Eval 指标**:

| 指标 | s43 r3 | s42 | RSFT 3-seed mean |
|------|--------|-----|-------------------|
| **Ign-F1** | **0.5142** | 0.5384 | 0.5654 |
| F1 | 0.5308 | — | — |
| Evi-F1 (DREEAM) | 0.4220 | — | — |
| Evi-F1 (TP) | 0.8245 | — | — |
| EDCR | 0.5866 | — | — |
| Format OK | 985/985 (100%) | — | — |
| Truncated | 190/985 | — | — |

**对比**: s43 Ign-F1=0.5142，低于 s42 (0.5384) 2.4 个点，低于 RSFT 3-seed mean (0.5654) 5.1 个点。s43 的 SFT baseline 表现较弱。

---
