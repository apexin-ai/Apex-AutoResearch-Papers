# ops v5 checkpoint verify

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_v5_checkpoint_verify_20260520T063558_result.json`
- **Structured JSON:** [`d8a2d71ddb6c69245805.json`](../../sessions/d8/d8a2d71ddb6c69245805.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个 checkpoint 都在 `/root/autodl-tmp/recovery_aware_struct_prune/` 下，确认 model.safetensors 均为 12GB。

```
CKA-only step-100:   /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100/   model.safetensors 12G ✅
RASP fair step-100:  /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair/checkpoint-100/   model.safetensors 12G ✅
Standard fair step-100: /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair/checkpoint-100/   model.safetensors 12G ✅
磁盘（根分区）: 5.4G/30G (18%)
```

注意：RASP fair checkpoint 没有 optimizer.pt（total 12G），CKA-only 和 Standard fair 都保留了 optimizer.pt（total 27G）。三个 checkpoint 都位于数据盘 autodl-tmp，不在根分区的 outputs/ 或项目根目录下。

---
