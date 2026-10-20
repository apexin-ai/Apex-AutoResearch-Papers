# ops eval plan 014 sft no evidence

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval_plan_014_sft_no_evidence_20260515T171645_result.json`
- **Structured JSON:** [`674dca194cfe0c02f5ee.json`](../../sessions/67/674dca194cfe0c02f5ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

启动成功。模型已检测到 adapter 并在加载中：
- Base model: Qwen3-4B (bf16, no quantize)
- LoRA adapter: sft_no_evidence_output
- `--no_evidence` flag 已生效（使用 NO_EVIDENCE_SYSTEM_PROMPT + include_evidence=False）

关键修改：给 inference.py 添加了 `--no_evidence` 参数，确保 system prompt 和 instruction 与训练时一致（不提 evidence）。rel_f1 计算不受影响，evi_f1 预期为 0（无 evidence 输出）。

---
