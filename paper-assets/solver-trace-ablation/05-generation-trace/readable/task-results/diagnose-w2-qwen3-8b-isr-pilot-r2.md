# diagnose w2 qwen3 8b isr pilot r2

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_w2-qwen3-8b-isr-pilot-r2_20260516T105130_result.json`
- **Structured JSON:** [`bbd7ba1d0fe693cf71ef.json`](../../sessions/bb/bbd7ba1d0fe693cf71ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果：训练失败。** Step 1 即 OOM。

- K=4 (r1) OOM → K=2 (r2) 仍然 OOM
- Qwen3-8B GRPO 在单卡 A100-95GB 上即使 K=2、batch=1 也放不下——forward pass 已占 94.75 GiB，compute_loss 阶段 lm_head 再申请 1.16 GiB 失败
- 输出目录仅 reward_log.jsonl（1 step），无 checkpoint

Registry 已更新为 `DONE/failed`，cron 已删除。

**下一步选项**：若要继续 8B 实验，需要 (1) 双卡并行，或 (2) QLoRA 4-bit 量化，或 (3) 进一步缩减 max_completion_length / 换更激进的 offload 策略。

---
