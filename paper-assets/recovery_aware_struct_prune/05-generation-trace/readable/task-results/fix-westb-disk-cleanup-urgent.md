# fix westb disk cleanup urgent

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_westb_disk_cleanup_urgent_20260522T090824_result.json`
- **Structured JSON:** [`2f6bbb593bd241a7e276.json`](../../sessions/2f/2f6bbb593bd241a7e276.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

```
清理前: 250G/250G (100%)
清理后: 206G/250G (83%)
释放: 44GB

删除明细:
- sft_rasp_alpha3p0_20/checkpoint-935/optimizer.pt: 11G
- pruned_rasp_20/: 12G
- pruned_standard_20/: 12G
- pruned_cka_only_20/: 12G

保留（确认未删）:
- sft_rasp_alpha3p0_20/checkpoint-935/model.safetensors (12G) ✅
- pruned_cka_only_20_qwen_math/ ✅
- sft_qwen_math_cka_only_20_final/ ✅
- grpo_rasp_alpha3p0_20/ ✅
- grpo_qwen_math_cka_only_20/ ✅
- Qwen2.5-Math-7B 基础模型 ✅
```

释放了 44G，离 50G 目标差 6G。如果需要进一步释放，下一批安全候选：
- **pruned_rasp_alpha3p0_20/** (12G) — SFT 已完成，GRPO 用的是 SFT checkpoint 不是 pruned 模型
- **pruned_standard_20_qwen_math/** (12G) — 如果对应 SFT 已完成

要继续删吗？

---
