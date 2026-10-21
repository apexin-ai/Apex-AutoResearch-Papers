# diag exp 001 sft d100 3B

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp_001_sft_d100_3B_20260514T120944_result.json`
- **Structured JSON:** [`e05c70805920321becd0.json`](../../sessions/e0/e05c70805920321becd0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**训练实际已成功完成，EXIT_CODE=129 是误报。**

关键发现：
- 全部 4159/4159 steps 完成，epoch 1.0，train_loss=1.178，token accuracy=72.1%
- LoRA adapter 完整保存（115M adapter_model.safetensors + tokenizer + checkpoint-4159 含 optimizer state）
- SIGHUP 发生在训练结束之后，影响的是 wrapper shell 而非 Python 进程——与之前的 cron false positive 模式一致

**无需重训**，直接用 `lora_adapter/` 做下游评估即可。建议 wrapper 加 `trap '' HUP` 避免后续误报。

诊断报告已写入 `artifacts/diag_exp_001_sft_d100_3B.md`。

---
