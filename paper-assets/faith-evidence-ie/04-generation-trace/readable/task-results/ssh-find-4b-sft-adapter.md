# ssh find 4b sft adapter

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_find-4b-sft-adapter_20260521T073041_result.json`
- **Structured JSON:** [`acbdf3aafb4016927f6b.json`](../../sessions/ac/acbdf3aafb4016927f6b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Confirmed.

| Adapter | num_tokens @ step 10 | Total steps | Total tokens (~) |
|---|---|---|---|
| `sft_output_qwen3_8b_bf16` (standard 8B) | **141,227** | 570 | ~8.05M |
| `sft_output_qwen3_1_7b_bf16` (standard 1.7B) | **141,227** | 570 | ~8.05M |
| **`sft_output`** (Qwen3-4B candidate) | 555,730 | 144 | **~8.00M** |
| `sft_no_evidence_output` (no-evidence 4B) | **119,651** | 570 | ~6.82M |

**结论：`/root/autodl-tmp/sft_output/` 是 Qwen3-4B 的标准 SFT adapter（含 evidence）。**

- `base_model_name_or_path` = `/root/autodl-tmp/models/Qwen3-4B`
- 总训练 token 数 ~8.0M，与 8B/1.7B 标准 SFT (~8.05M) 一致
- no-evidence 版本 (`sft_no_evidence_output`) 仅 ~6.82M tokens（少了 evidence 字段的 token），与预期匹配
- 该 adapter 使用了更大 batch size（~4x），因此 steps 少（144 vs 570）但每步 token 多，总数据量一致

---
