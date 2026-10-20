# ssh find 4b sft adapter

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_find-4b-sft-adapter_20260521T073803_result.json`
- **Structured JSON:** [`53677e0f3fc31943e99b.json`](../../sessions/53/53677e0f3fc31943e99b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认完毕。

**4B Qwen3 标准 SFT seed42 bf16 adapter 路径：`/root/autodl-tmp/sft_output`**

验证信息：
- **base_model**: `/root/autodl-tmp/models/Qwen3-4B`
- **seed**: 42
- **bf16**: True
- **LoRA**: r=64, alpha=128, dropout=0.05
- **训练**: 3 epochs, 144 steps, best_eval_loss=0.720
- `sft_no_evidence_output` 同样基于 Qwen3-4B，是对应的 no-evidence 版本，确认 `sft_output` 是含 evidence 的标准 SFT。

---
