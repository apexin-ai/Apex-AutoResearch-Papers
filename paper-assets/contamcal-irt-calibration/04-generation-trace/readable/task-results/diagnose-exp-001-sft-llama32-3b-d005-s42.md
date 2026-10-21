# diagnose exp 001 sft llama32 3B d005 s42

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_001_sft_llama32_3B_d005_s42_20260516T175105_result.json`
- **Structured JSON:** [`682a6083dcfc268d42cb.json`](../../sessions/68/682a6083dcfc268d42cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断结论：

- **失败原因**：训练已完成（3177/3177 steps），LoRA adapter 保存成功。失败在 merge 阶段——`/root/autodl-tmp` 磁盘 100% 满（169G/169G），写第二个 safetensors shard 时报 `No space left on device`。
- **可恢复**：完全可恢复，无需重训。LoRA adapter 完整（93MB）。
- **修复**：清出 ~6GB 空间 → 删除不完整的 `merged/` 目录 → 单独重跑 merge。

报告已写入 `artifacts/diagnose_exp001_sft_llama32_3B_d005_s42.md`。

---
